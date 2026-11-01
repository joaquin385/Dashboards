"""Arma la nota en el orden de la pirámide.

El asistente escribe la primera oración, el límite y la otra historia.
Un hueco `{hoja|campo|...}` se llena con el número de esa ficha. Si el número
no está en una hoja completa, la nota no sale.
"""

import re
from dataclasses import dataclass

from contrato.encargo import Encargo
from contrato.hojas import HOJAS_POR_ID
from contrato.paquetes import PAQUETES
from pipeline.correr import Resultado

_HUECO = re.compile(r"\{([^{}]+)\}")
_IDIOMAS = ("es", "en")

_FIRMAR = {
    "es": "no alcanza para firmar",
    "en": "does not suffice to sign",
}

_SEPARA = {
    "es": "no separa",
    "en": "does not separate",
}

_QUE_DECIDE = {
    "es": (
        "hay que",
        "conviene",
        "dejá",
        "deja de",
        "el mes que viene",
        "la causa es",
        "cayó porque",
        "cayo porque",
    ),
    "en": (
        "we should",
        "you should",
        "it is worth",
        "next month",
        "the cause is",
        "fell because",
        "drop it",
    ),
}

_ROTULOS = {
    "es": {
        "destinatario": "Destinatario",
        "primera": "Primera oración",
        "evidencia": "Evidencia",
        "limite": "Límite",
        "otra": "Otra historia",
        "cierres": "Cierres",
        "descriptivo": "Descriptivo",
        "causal": "Causal",
        "decision": "Decisión",
    },
    "en": {
        "destinatario": "Addressee",
        "primera": "First sentence",
        "evidencia": "Evidence",
        "limite": "Limit",
        "otra": "Other story",
        "cierres": "Closings",
        "descriptivo": "Descriptive",
        "causal": "Causal",
        "decision": "Decision",
    },
}


@dataclass(frozen=True)
class Cierre:
    tipo: str
    texto: str


@dataclass(frozen=True)
class HuecoVacio:
    hoja_id: str
    dato_que_falta: str
    frase_que_frena: str
    sigue_en_pie: str = ""


@dataclass(frozen=True)
class Nota:
    destinatario: str
    primera_oracion: str
    evidencia: tuple[tuple[str, str], ...]
    limite: str
    otra_historia: str | None
    cierres: tuple[Cierre, ...]
    huecos_vacios: tuple[HuecoVacio, ...] = ()


@dataclass(frozen=True)
class NotaLista:
    orden: tuple[str, ...]
    texto: str


def revisar(nota: Nota, resultado: Resultado, encargo: Encargo) -> NotaLista:
    if resultado.detenido:
        raise ValueError(resultado.detenido)
    if encargo.idioma not in _IDIOMAS:
        raise ValueError(f"El idioma {encargo.idioma} no está en la entrega.")
    rotulos = _ROTULOS[encargo.idioma]
    profundidad = PAQUETES[encargo.paquete]["profundidad_nota"]
    completas = {ficha.hoja_id for ficha in resultado.fichas if ficha.estado == "completa"}
    vacias = {ficha.hoja_id: ficha for ficha in resultado.fichas if ficha.estado == "vacia"}
    dichas = {hueco.hoja_id for hueco in nota.huecos_vacios}
    if dichas != set(vacias):
        raise ValueError("Cada hoja vacía se nombra en la nota, con el dato que falta.")
    if {hoja_id for hoja_id, _ in nota.evidencia} != completas:
        raise ValueError("La evidencia recorre las hojas que se completaron, y ninguna vacía.")

    tipos = [cierre.tipo for cierre in nota.cierres]
    if "descriptivo" not in tipos or "causal" not in tipos:
        raise ValueError("La nota cierra en descriptivo y en causal.")
    if encargo.decision:
        if "decision" not in tipos or encargo.decision not in nota.primera_oracion:
            raise ValueError("La decisión nombrada abre la nota y tiene su cierre.")
    elif "decision" in tipos:
        raise ValueError("Sin una decisión nombrada, el cierre de decisión no se escribe.")

    if profundidad == "piramide_con_otra_historia" and not nota.otra_historia:
        raise ValueError("Premium incluye la otra historia.")
    if profundidad != "piramide_con_otra_historia" and nota.otra_historia:
        raise ValueError("Ese paquete no entrega el párrafo de la otra historia.")
    if encargo.decision is None:
        if (
            _FIRMAR[encargo.idioma] not in nota.primera_oracion
            and _FIRMAR[encargo.idioma] not in nota.limite
        ):
            raise ValueError("Sin decisión nombrada, la nota dice qué no alcanza a firmar.")

    for cierre in nota.cierres:
        if cierre.tipo == "causal" and _SEPARA[encargo.idioma] not in cierre.texto.casefold():
            raise ValueError("El cierre causal dice que la tabla no separa la causa.")
        if cierre.tipo == "descriptivo" and "{" not in cierre.texto:
            raise ValueError("El cierre descriptivo cita un peso de una hoja.")

    orden = ["destinatario", "primera oración", "evidencia", "límite"]
    if profundidad == "piramide_con_otra_historia":
        orden.append("otra historia")
    orden.append("cierres")

    partes = [
        f"{rotulos['destinatario']}\n{_llenar(nota.destinatario, resultado, encargo.idioma)}",
        f"{rotulos['primera']}\n{_llenar(nota.primera_oracion, resultado, encargo.idioma)}",
        rotulos["evidencia"] + "\n" + "\n\n".join(
            _evidencia(hoja_id, texto, resultado, encargo.idioma) for hoja_id, texto in nota.evidencia
        ),
        rotulos["limite"] + "\n" + _llenar(nota.limite, resultado, encargo.idioma) + _vacios(nota, encargo.idioma),
    ]
    if profundidad == "piramide_con_otra_historia":
        partes.append(f"{rotulos['otra']}\n{_llenar(nota.otra_historia or '', resultado, encargo.idioma)}")
    partes.append(
        rotulos["cierres"] + "\n" + "\n\n".join(
            _cierre(cierre, resultado, rotulos, encargo.idioma) for cierre in nota.cierres
        )
    )
    texto = "\n\n".join(partes)
    if encargo.decision is None:
        _sin_decision_de_mas(texto, encargo.idioma)
    return NotaLista(tuple(orden), texto)


def _evidencia(hoja_id: str, texto: str, resultado: Resultado, idioma: str) -> str:
    nombre = HOJAS_POR_ID[hoja_id].nombre
    return f"{nombre}. {_llenar(texto, resultado, idioma)}"


def _vacios(nota: Nota, idioma: str) -> str:
    if not nota.huecos_vacios:
        return ""
    lineas = []
    for hueco in nota.huecos_vacios:
        nombre = HOJAS_POR_ID[hueco.hoja_id].nombre
        if idioma == "en":
            linea = (
                f"{nombre} is not completed: missing {hueco.dato_que_falta}. "
                f"This stops {hueco.frase_que_frena}."
            )
        else:
            linea = (
                f"{nombre} no se completa: falta {hueco.dato_que_falta}. "
                f"Eso frena {hueco.frase_que_frena}."
            )
        if hueco.sigue_en_pie:
            linea += f" {hueco.sigue_en_pie}"
        lineas.append(linea)
    return "\n" + "\n".join(lineas)


def _cierre(cierre: Cierre, resultado: Resultado, rotulos: dict[str, str], idioma: str) -> str:
    return f"{rotulos[cierre.tipo]}. {_llenar(cierre.texto, resultado, idioma)}"


def _llenar(texto: str, resultado: Resultado, idioma: str) -> str:
    def cambiar(hallado: re.Match) -> str:
        return _valor(hallado.group(1), resultado, idioma)

    return _HUECO.sub(cambiar, texto)


def _valor(token: str, resultado: Resultado, idioma: str) -> str:
    partes = token.split("|")
    hoja_id, hueco, *resto = partes
    formato = "pesos"
    if resto and resto[-1] == "resta":
        formato = "resta"
        resto = resto[:-1]
    ficha = resultado.ficha(hoja_id)
    if ficha.estado != "completa":
        raise ValueError(f"{hoja_id} no tiene número para citar.")
    valor = ficha.huecos[hueco]
    for paso in resto:
        valor = valor[paso]
    if formato == "resta":
        return _resta(valor, idioma)
    if isinstance(valor, int):
        return _pesos(valor)
    return str(valor)


def _resta(valor: int, idioma: str) -> str:
    if idioma == "en":
        if valor < 0:
            return f"{_pesos(abs(valor))} down"
        if valor > 0:
            return f"{_pesos(valor)} up"
        return "the same number"
    if valor < 0:
        return f"{_pesos(abs(valor))} abajo"
    if valor > 0:
        return f"{_pesos(valor)} arriba"
    return "en el mismo número"


def _pesos(valor: int) -> str:
    return f"{valor:,}".replace(",", ".")


def _sin_decision_de_mas(texto: str, idioma: str) -> None:
    bajo = texto.casefold()
    for frase in _QUE_DECIDE[idioma]:
        if frase in bajo:
            raise ValueError(f"La nota decide de más: {frase}.")
