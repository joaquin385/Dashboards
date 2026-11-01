"""Papeles que una columna puede ocupar.

El asistente escribe el match. Este módulo solo nombra los papeles que el
contrato reconoce. Un papel que no está acá no enciende una hoja.
"""

# Entran en la cuenta de alguna hoja del catálogo.
PAPELES_DE_HOJA = (
    "fecha",
    "periodo",
    "importe",
    "unidades",
    "precio",
    "costo",
    "grupo",
)

# Entran en la limpieza, cuando el asistente los marque. No encienden hojas.
PAPELES_DE_LIMPIEZA = (
    "comprobante",
    "estado",
)

# Entran en la regla de medición, cuando el archivo los trae. No encienden hojas.
PAPELES_DE_MEDICION = (
    "devolucion",
    "impuesto",
)

PAPELES = PAPELES_DE_HOJA + PAPELES_DE_LIMPIEZA + PAPELES_DE_MEDICION
