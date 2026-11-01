"""Esqueleto de la nota. El asistente escribe los huecos de criterio. El pipeline deja los pesos."""

from dataclasses import dataclass

from contrato.encargo import Encargo


ORACIONES_PROHIBIDAS_EN_LA_NOTA = (
    "Una causa que las columnas no separan.",
    "Un pronóstico.",
    "Un efecto medido.",
    "Una decisión que el comprador no nombró.",
    "Un número de una hoja que no se completó.",
)

REGLA_OTRA_HISTORIA = (
    "Si la otra historia le cambia la decisión, el cambio va en la primera oración, "
    "en cualquier paquete. El párrafo de la otra historia se entrega en Premium."
)


@dataclass(frozen=True)
class EsqueletoNota:
    profundidad: str
    orden: tuple[str, ...]
    destinatario: str
    primera_oracion: str
    evidencia: str
    limite: str
    otra_historia: str | None
    regla_otra_historia: str
    oraciones_prohibidas: tuple[str, ...]


def esqueleto(encargo: Encargo, profundidad: str) -> EsqueletoNota:
    if encargo.decision:
        primera = (
            f"La primera oración es esta decisión, y no llega más lejos que el límite: "
            f"{encargo.decision}"
        )
    else:
        primera = (
            "La primera oración es la comparación. "
            "La nota dice qué decisión este archivo no alcanza a firmar."
        )

    orden = ["destinatario", "primera oración", "evidencia", "límite"]
    otra = None
    if profundidad == "piramide_con_otra_historia":
        orden.append("otra historia")
        otra = (
            "La otra historia que también cabe en estos pesos. "
            "Si le cambia la decisión, ya está en la primera oración."
        )
    if profundidad == "frase":
        orden = ["primera oración", "límite de la comparación"]

    return EsqueletoNota(
        profundidad=profundidad,
        orden=tuple(orden),
        destinatario=(
            "Quién podría firmar la frase. "
            "Si el comprador no lo dijo, el hueco queda para el asistente."
        ),
        primera_oracion=primera,
        evidencia="Los pesos de las hojas que se completaron, cada uno en su hoja.",
        limite="Hasta dónde no llegan esas hojas, y qué frase frena cada hoja vacía.",
        otra_historia=otra,
        regla_otra_historia=REGLA_OTRA_HISTORIA,
        oraciones_prohibidas=ORACIONES_PROHIBIDAS_EN_LA_NOTA,
    )
