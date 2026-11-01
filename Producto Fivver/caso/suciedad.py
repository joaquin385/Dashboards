"""La suciedad que la fase 3 le agrega a Loma.

El CSV limpio no se toca: esa es la cuenta. Este archivo es el que entra al
pipeline. El asistente ya marcó qué suciedad cambia la suma.
"""

import csv
from pathlib import Path

from caso.archivos import filas_ventas

CARPETA = Path(__file__).resolve().parent
SUCIO = CARPETA / "loma-ventas-sucio.csv"
COLUMNAS = ["fecha", "producto", "unidades", "precio", "costo", "importe", "ticket", "nota"]

# La fila de Cordel del 1 de septiembre trae el precio y el importe con punto de miles.
# La suma de la columna no los lee hasta convertirlos.
FILA_EN_TEXTO = ("2026-09-01", "Cordel")

# La primera Maroma de agosto está exportada dos veces, con el mismo ticket.
FILA_REPETIDA = ("2026-08-01", "Maroma")
TICKET_REPETIDO = "T-MAROMA-01"

# El total de Cordel de agosto, sentado otra vez al final del mes.
TICKET_QUE_NO_SE_SUMA = "T-TOTAL"
NOTA_DEL_TOTAL = "total de Cordel de agosto, ya incluido"

# La mayúscula y el comentario viven en la nota. No cambian el producto ni el importe.
NOTA_QUE_ESPERA = "REVISAR"


def filas_sucias() -> list[dict[str, str]]:
    filas = []
    repetida = None
    for numero, origen in enumerate(filas_ventas(), start=1):
        unidades = int(origen["unidades"])
        precio = int(origen["precio"])
        fila = {
            "fecha": origen["fecha"],
            "producto": origen["producto"],
            "unidades": origen["unidades"],
            "precio": origen["precio"],
            "costo": origen["costo"],
            "importe": str(unidades * precio),
            "ticket": f"T{numero:04d}",
            "nota": "",
        }
        if (fila["fecha"], fila["producto"]) == FILA_EN_TEXTO:
            fila["precio"] = "2.000"
            fila["costo"] = "1.000"
            fila["importe"] = "12.000"
            fila["nota"] = NOTA_QUE_ESPERA
        if (fila["fecha"], fila["producto"]) == FILA_REPETIDA:
            fila["ticket"] = TICKET_REPETIDO
            repetida = dict(fila)
        filas.append(fila)

    filas.append(dict(repetida))
    filas.append(
        {
            "fecha": "2026-08-31",
            "producto": "Cordel",
            "unidades": "100",
            "precio": "2000",
            "costo": "1000",
            "importe": "200000",
            "ticket": TICKET_QUE_NO_SE_SUMA,
            "nota": NOTA_DEL_TOTAL,
        }
    )
    filas.append({columna: "" for columna in COLUMNAS})
    return filas


def escribir() -> None:
    with SUCIO.open("w", encoding="utf-8", newline="") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=COLUMNAS)
        escritor.writeheader()
        escritor.writerows(filas_sucias())
