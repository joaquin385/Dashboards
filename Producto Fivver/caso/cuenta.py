"""Los números de Loma, escritos antes de leer el archivo.

La prosa está en cuenta.md. Acá quedan las mismas cifras para que la prueba
pueda comprobar el CSV sin volver a inventar la cuenta.
"""

from datetime import date

NEGOCIO = "Loma"
GRANO = "un producto en un día de apertura"
CORTE = "producto"
MONEDA = "pesos"
PAIS = "Argentina"

# Loma abre de lunes a sábado. El sábado pesa como un día de semana.
# Cierra el domingo y el feriado que cae de lunes a sábado.
FERIADO = date(2026, 8, 17)

PRECIOS = {
    (2025, 9): {"Cordel": 1_000, "Soga": 2_500, "Maroma": 10_000},
    (2026, 8): {"Cordel": 2_000, "Soga": 5_000, "Maroma": 20_000},
    (2026, 9): {"Cordel": 2_000, "Soga": 5_000, "Maroma": 20_000},
}

COSTOS = {
    (2025, 9): {"Cordel": 500, "Soga": 1_000, "Maroma": 6_000},
    (2026, 8): {"Cordel": 1_000, "Soga": 2_000, "Maroma": 12_000},
    (2026, 9): {"Cordel": 1_000, "Soga": 2_000, "Maroma": 12_000},
}

# Unidades por día de apertura. Septiembre 2026 no tiene Maroma: no hubo fila.
UNIDADES_POR_DIA = {
    (2025, 9): {"Cordel": 4, "Soga": 2, "Maroma": 1},
    (2026, 8): {"Cordel": 4, "Soga": 2, "Maroma": 2},
    (2026, 9): {"Cordel": 6, "Soga": 2},
}

DIAS_DE_APERTURA = {
    (2025, 9): 26,
    (2026, 8): 25,
    (2026, 9): 26,
}

# Facturación de cada mes, armada en cuenta.md.
FACTURACION = {
    (2025, 9): 494_000,
    (2026, 8): 1_450_000,
    (2026, 9): 572_000,
}

COSTO_DEL_MES = {
    (2025, 9): 260_000,
    (2026, 8): 800_000,
    (2026, 9): 260_000,
}

QUEDA = {
    (2025, 9): 234_000,
    (2026, 8): 650_000,
    (2026, 9): 312_000,
}

# Agosto a septiembre de 2026. Camino: cantidad, mezcla, precio.
PIEZA_CANTIDAD = 58_000
PIEZA_MEZCLA = -936_000
PIEZA_PRECIO = 0
NETO_CONTRA_AGOSTO = -878_000

# El mismo neto, abierto por producto. No es el camino de las piezas.
POR_PRODUCTO = {"Cordel": 112_000, "Soga": 10_000, "Maroma": -1_000_000}

# Lo que queda, agosto a septiembre, por producto.
QUEDA_POR_PRODUCTO = {"Cordel": 56_000, "Soga": 6_000, "Maroma": -400_000}
NETO_QUEDA = -338_000

NETO_CONTRA_EL_ANIO_PASADO = 78_000
MARCA_DE_CALENDARIO = 58_000

# Copia sin unidades. Índice de práctica, no el IPC publicado.
MES_DEL_INDICE = "septiembre 2025"
INDICE = {
    (2025, 9): 100,
    (2026, 8): 200,
    (2026, 9): 220,
}
FUENTE_INDICE = (
    "Índice de práctica del caso Loma, con septiembre 2025 en 100. "
    "No es el IPC del INDEC. En un encargo real se copia el IPC nacional, "
    "nivel general, y se escribe la publicación."
)
FACTURACION_EN_PESOS_DE_SEPTIEMBRE_2025 = {
    (2025, 9): 494_000,
    (2026, 8): 725_000,
    (2026, 9): 260_000,
}

HOJAS_DE_LOMA = (
    "monitoreo",
    "anio_pasado",
    "piezas",
    "lo_que_queda",
    "calendario",
    "el_que_se_aparta",
)

HOJAS_DE_LA_COPIA = (
    "monitoreo",
    "anio_pasado",
    "calendario",
    "pesos_de_un_mes",
)
