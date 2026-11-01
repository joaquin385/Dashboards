"""Arma las filas de Loma y las escribe al lado de la cuenta."""

import csv
from datetime import date
from pathlib import Path

from caso.cuenta import (
    COSTOS,
    FERIADO,
    PRECIOS,
    UNIDADES_POR_DIA,
)

CARPETA = Path(__file__).resolve().parent
VENTAS = CARPETA / "loma-ventas.csv"
PESOS = CARPETA / "loma-pesos.csv"
INDICE = CARPETA / "loma-indice.csv"
ORDEN = ("Cordel", "Soga", "Maroma")


def dias_de_apertura(anio: int, mes: int) -> list[date]:
    dias = []
    for dia in range(1, 32):
        try:
            fecha = date(anio, mes, dia)
        except ValueError:
            break
        if fecha.weekday() == 6 or fecha == FERIADO:
            continue
        dias.append(fecha)
    return dias


def filas_ventas() -> list[dict[str, str]]:
    filas = []
    for (anio, mes), unidades in UNIDADES_POR_DIA.items():
        for fecha in dias_de_apertura(anio, mes):
            for producto in ORDEN:
                if producto not in unidades:
                    continue
                filas.append(
                    {
                        "fecha": fecha.isoformat(),
                        "producto": producto,
                        "unidades": str(unidades[producto]),
                        "precio": str(PRECIOS[(anio, mes)][producto]),
                        "costo": str(COSTOS[(anio, mes)][producto]),
                    }
                )
    return filas


def filas_pesos() -> list[dict[str, str]]:
    """Un día, un importe. Sin producto, sin unidades, sin precio y sin costo."""

    por_dia: dict[date, int] = {}
    for fila in filas_ventas():
        fecha = date.fromisoformat(fila["fecha"])
        importe = int(fila["unidades"]) * int(fila["precio"])
        por_dia[fecha] = por_dia.get(fecha, 0) + importe
    return [
        {"fecha": fecha.isoformat(), "importe": str(por_dia[fecha])}
        for fecha in sorted(por_dia)
    ]


def escribir() -> None:
    _csv(VENTAS, filas_ventas(), ["fecha", "producto", "unidades", "precio", "costo"])
    _csv(PESOS, filas_pesos(), ["fecha", "importe"])
    _csv(
        INDICE,
        [
            {"mes": "2025-09", "indice": "100"},
            {"mes": "2026-08", "indice": "200"},
            {"mes": "2026-09", "indice": "220"},
        ],
        ["mes", "indice"],
    )


def _csv(camino: Path, filas: list[dict[str, str]], columnas: list[str]) -> None:
    with camino.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=columnas)
        escritor.writeheader()
        escritor.writerows(filas)
