"""Los tres paquetes son tres profundidades del mismo catálogo.

La nota no cuenta entre las seis hojas. Es la pirámide armada con las hojas
que sí se completaron.
"""

PAQUETES = {
    "basic": {
        "nombre": "Basic. El mes.",
        "max_filas": 5_000,
        "hojas_fijas": ("monitoreo",),
        "hojas_elegibles": (),
        "max_elegibles": 0,
        "profundidad_nota": "frase",
    },
    "standard": {
        "nombre": "Standard. La historia.",
        "max_filas": 20_000,
        "hojas_fijas": ("monitoreo",),
        "hojas_elegibles": ("anio_pasado", "piezas", "lo_que_queda"),
        "max_elegibles": 2,
        "profundidad_nota": "piramide",
    },
    "premium": {
        "nombre": "Premium. La lectura completa.",
        "max_filas": 50_000,
        "hojas_fijas": (),
        "hojas_elegibles": (
            "monitoreo",
            "anio_pasado",
            "piezas",
            "lo_que_queda",
            "calendario",
            "el_que_se_aparta",
            "pesos_de_un_mes",
        ),
        "max_elegibles": 6,
        "profundidad_nota": "piramide_con_otra_historia",
    },
}
