"""Aplica las marcas del asistente y anota el total de antes y el de después."""

import re
from dataclasses import dataclass

from contrato.encargo import Encargo
from pipeline.instruccion import Marca
from pipeline.numeros import leer_numero

_PUNTO_DE_MILES = re.compile(r"^\d{1,3}(\.\d{3})+$")
_ENTERO = re.compile(r"^-?\d+$")


@dataclass(frozen=True)
class Anotacion:
    accion: str
    detalle: str
    antes: int
    despues: int


def limpiar(
    filas: list[dict[str, str]],
    marcas: tuple[Marca, ...],
    encargo: Encargo,
    hojas_encendidas: tuple[str, ...] | None = None,
) -> tuple[list[dict[str, str]], tuple[Anotacion, ...]]:
    encendidas = None if hojas_encendidas is None else set(hojas_encendidas)
    anotaciones = []
    actual = filas
    for marca in marcas:
        antes = total_leido(actual, encargo)
        if _queda_anotada(marca, encendidas):
            anotaciones.append(Anotacion(marca.accion, marca.detalle, antes, antes))
            continue
        actual = _aplicar(marca, actual, encargo)
        despues = total_leido(actual, encargo)
        if marca.accion == "esperar" and antes != despues:
            raise ValueError(
                "La marca que podía esperar movió el total. "
                f"Antes {antes}, después {despues}."
            )
        anotaciones.append(Anotacion(marca.accion, marca.detalle, antes, despues))
    return actual, tuple(anotaciones)


def total_leido(filas: list[dict[str, str]], encargo: Encargo | None = None) -> int:
    """Suma lo que ya se puede leer, por el papel del match.

    Sin encargo, lee la columna que se llama importe. Lo que no entra en la
    regla queda afuera: el texto con punto de miles no suma hasta que una
    marca lo convierte.
    """

    if encargo is None:
        return _total_de_la_columna(filas, "importe", None)
    if encargo.importe_sale_de_unidades_por_precio:
        return _total_unidades_por_precio(filas, encargo)
    columna = encargo.columna("importe")
    if columna is None:
        return 0
    return _total_de_la_columna(filas, columna, encargo)


def _total_de_la_columna(
    filas: list[dict[str, str]],
    columna: str,
    encargo: Encargo | None,
) -> int:
    total = 0
    for fila in filas:
        texto = fila.get(columna, "")
        if encargo is None:
            if _ENTERO.fullmatch(texto or ""):
                total += int(texto)
            continue
        valor = leer_numero(texto, encargo, dinero=True)
        if valor is not None:
            total += valor
    return total


def _total_unidades_por_precio(filas: list[dict[str, str]], encargo: Encargo) -> int:
    unidades = encargo.columna("unidades")
    precio = encargo.columna("precio")
    if unidades is None or precio is None:
        return 0
    total = 0
    for fila in filas:
        cantidad = leer_numero(fila.get(unidades, ""), encargo, dinero=False)
        valor = leer_numero(fila.get(precio, ""), encargo, dinero=True)
        if cantidad is None or valor is None:
            continue
        total += cantidad * valor
    return total


def _queda_anotada(marca: Marca, encendidas: set[str] | None) -> bool:
    return (
        encendidas is not None
        and marca.hoja is not None
        and marca.hoja not in encendidas
    )


def _aplicar(marca: Marca, filas: list[dict[str, str]], encargo: Encargo) -> list[dict[str, str]]:
    if marca.accion == "numero_con_punto_de_miles":
        return [_convertir(fila, marca.columnas) for fila in filas]
    if marca.accion == "comprobante_repetido":
        columna = encargo.columna("comprobante")
        if columna is None:
            raise ValueError("La marca pide el comprobante y el match no lo nombra.")
        return _sin_repetidos(filas, columna)
    if marca.accion == "no_sumar":
        columna = encargo.columna("comprobante")
        if columna is None:
            raise ValueError("La marca pide el comprobante y el match no lo nombra.")
        return [fila for fila in filas if fila.get(columna, "") not in marca.tickets]
    if marca.accion == "esperar":
        return list(filas)
    raise ValueError(f"La marca {marca.accion} no está en la lista del asistente.")


def _convertir(fila: dict[str, str], columnas: tuple[str, ...]) -> dict[str, str]:
    nueva = dict(fila)
    for columna in columnas:
        valor = nueva.get(columna, "")
        if valor and _PUNTO_DE_MILES.fullmatch(valor):
            nueva[columna] = valor.replace(".", "")
    return nueva


def _sin_repetidos(filas: list[dict[str, str]], columna: str) -> list[dict[str, str]]:
    vistos = set()
    limpias = []
    for fila in filas:
        ticket = fila.get(columna, "")
        if ticket and ticket in vistos:
            continue
        if ticket:
            vistos.add(ticket)
        limpias.append(fila)
    return limpias
