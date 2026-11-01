"""Faro: trece meses, ocho productos y tres locales.

El corte de esta corrida es el producto. El local viaja en el archivo
y esta pantalla no lo abre. Los precios no se mueven. Septiembre de 2026
casi empata con agosto; la mezcla no.
"""

import csv
from dataclasses import replace
from datetime import date
from pathlib import Path

from caso.corrida import encargo_loma
from caso.cuenta import HOJAS_DE_LOMA
from dashboard.html import escribir, guardar
from informe.nota import Cierre, Nota, revisar
from pipeline.correr import correr
from pipeline.instruccion import Calendario, Instruccion, Periodo

CARPETA = Path(__file__).resolve().parent
VENTAS = CARPETA / "faro-ventas.csv"
HTML = CARPETA / "faro.html"

LOCALES = ("Centro", "Norte", "Taller")
PRODUCTOS = ("Lámpara", "Cable", "Tecla", "Zócalo", "Tubo", "Plafón", "Farol", "Foco")
PRECIOS = {
    "Lámpara": 500,
    "Cable": 1_200,
    "Tecla": 2_000,
    "Zócalo": 3_000,
    "Tubo": 4_000,
    "Plafón": 6_000,
    "Farol": 20_000,
    "Foco": 30_000,
}
COSTOS = {producto: precio // 2 for producto, precio in PRECIOS.items()}

# Unidades por local en un día de apertura. Cero no escribe fila.
_NORMAL = {
    "Lámpara": (2, 2, 2),
    "Cable": (2, 2, 2),
    "Tecla": (1, 1, 1),
    "Zócalo": (1, 1, 1),
    "Tubo": (1, 1, 1),
    "Plafón": (1, 1, 1),
    "Farol": (1, 1, 1),
    "Foco": (1, 1, 1),
}


def _unidades(anio: int, mes: int) -> dict[str, tuple[int, int, int]]:
    unidades = dict(_NORMAL)
    if (anio, mes) in ((2025, 12), (2026, 1)):
        unidades["Foco"] = (2, 1, 1)
    elif (anio, mes) == (2025, 11):
        unidades["Tecla"] = (2, 1, 1)
    elif (anio, mes) == (2026, 4):
        unidades["Cable"] = (3, 2, 2)
    elif (anio, mes) == (2026, 9):
        unidades["Lámpara"] = (28, 28, 28)
        unidades["Farol"] = (1, 0, 0)
    return unidades


def dias_de_apertura(anio: int, mes: int) -> list[date]:
    dias = []
    for numero in range(1, 32):
        try:
            fecha = date(anio, mes, numero)
        except ValueError:
            break
        if fecha.weekday() == 6:
            continue
        dias.append(fecha)
    return dias


def filas() -> list[dict[str, str]]:
    salida = []
    for anio, mes in (
        (2025, 9),
        (2025, 10),
        (2025, 11),
        (2025, 12),
        (2026, 1),
        (2026, 2),
        (2026, 3),
        (2026, 4),
        (2026, 5),
        (2026, 6),
        (2026, 7),
        (2026, 8),
        (2026, 9),
    ):
        unidades = _unidades(anio, mes)
        for fecha in dias_de_apertura(anio, mes):
            for producto in PRODUCTOS:
                for local, cantidad in zip(LOCALES, unidades[producto]):
                    if cantidad == 0:
                        continue
                    salida.append(
                        {
                            "fecha": fecha.isoformat(),
                            "local": local,
                            "producto": producto,
                            "unidades": str(cantidad),
                            "precio": str(PRECIOS[producto]),
                            "costo": str(COSTOS[producto]),
                        }
                    )
    return salida


def escribir_archivo() -> None:
    columnas = ["fecha", "local", "producto", "unidades", "precio", "costo"]
    with VENTAS.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(filas())


def instruccion() -> Instruccion:
    return Instruccion(
        periodo=Periodo.mes(2026, 9),
        periodo_anterior=Periodo.mes(2026, 8),
        anio_pasado=Periodo.mes(2025, 9),
        camino=("cantidad", "mezcla", "precio"),
        que_dia="ninguno",
        costo_es_por_unidad=True,
        calendario=Calendario(
            abre=(0, 1, 2, 3, 4, 5),
            feriados=(),
            texto=(
                "Día de apertura es lunes a sábado. El domingo cierra. "
                "No hay feriado marcado."
            ),
        ),
        indice=None,
        mes_del_indice=None,
        fuente_indice=None,
    )


def nota(resultado) -> Nota:
    return Nota(
        destinatario=(
            "Quien podría firmar en Faro no está nombrado. La nota queda en la comparación."
        ),
        primera_oracion=(
            "Septiembre de 2026 está {monitoreo|diferencia|resta} de agosto "
            "y {anio_pasado|diferencia|resta} de septiembre de 2025. "
            "Este archivo no alcanza para firmar una compra."
        ),
        evidencia=(
            (
                "monitoreo",
                "La base es agosto de 2026. Septiembre facturó {monitoreo|total} "
                "contra {monitoreo|total_base}. Lo que más pesa en septiembre es "
                "{monitoreo|lo_que_mas_pesa|grupo}, con {monitoreo|lo_que_mas_pesa|importe}.",
            ),
            (
                "anio_pasado",
                "La otra base es septiembre de 2025, con {anio_pasado|total_base}. "
                "Septiembre de 2026 facturó {anio_pasado|total}.",
            ),
            (
                "piezas",
                "El camino escrito es {piezas|camino}. La cantidad se lleva "
                "{piezas|tramo_de_cada_pieza|cantidad|resta}, la mezcla "
                "{piezas|tramo_de_cada_pieza|mezcla|resta} y el precio queda "
                "{piezas|tramo_de_cada_pieza|precio|resta}. El neto es {piezas|neto|resta}.",
            ),
            (
                "lo_que_queda",
                "Después del costo que viaja con la venta, septiembre deja "
                "{lo_que_queda|queda} y agosto deja {lo_que_queda|queda_base}.",
            ),
            (
                "calendario",
                "La marca es {calendario|importe_en_dias_de_calendario}. "
                "Agosto y septiembre tienen los mismos días de apertura. "
                "El día marcado: {calendario|que_dia}.",
            ),
            (
                "el_que_se_aparta",
                "El corte, elegido antes, es {el_que_se_aparta|corte}. "
                "{el_que_se_aparta|importe_del_grupo|grupo} se lleva "
                "{el_que_se_aparta|importe_del_grupo|importe|resta}. "
                "El resto se lleva {el_que_se_aparta|importe_del_resto|resta}.",
            ),
        ),
        limite=(
            "Las dos bases se leen juntas. Una pieza no es una causa, y otro camino "
            "les cambiaría el tamaño. Lo que queda resta solo el costo de la fila. "
            "El local está en el archivo y este corte no lo abre. "
            "Hay unidades, así que esta nota no pasa la serie a pesos de otro mes."
        ),
        otra_historia=(
            "La otra historia es la mezcla. El neto del mes es {piezas|neto|resta} "
            "y la mezcla se lleva {piezas|tramo_de_cada_pieza|mezcla|resta}. "
            "La primera oración sigue con las dos bases."
        ),
        cierres=(
            Cierre(
                "descriptivo",
                "Septiembre facturó {monitoreo|total} contra {monitoreo|total_base} de agosto, "
                "y {anio_pasado|total} contra {anio_pasado|total_base} de septiembre de 2025.",
            ),
            Cierre(
                "causal",
                "La tabla no separa la causa. Describe el mes contra agosto y contra el año pasado.",
            ),
        ),
    )


def armar() -> None:
    escribir_archivo()
    pedido = instruccion()
    base = encargo_loma(len(filas()))
    encargo = replace(
        base,
        columnas={papel: columna for papel, columna in base.columnas.items() if papel != "comprobante"},
        grano="un producto en un local, en un día de apertura",
        origen="el archivo de ventas de Faro",
        hojas_pedidas=HOJAS_DE_LOMA,
    )
    resultado = correr(encargo, VENTAS, pedido)
    if resultado.detenido:
        raise ValueError(resultado.detenido)
    lista = revisar(nota(resultado), resultado, encargo)
    guardar(HTML, escribir(resultado, lista, pedido, "Faro", encargo))


if __name__ == "__main__":
    armar()
