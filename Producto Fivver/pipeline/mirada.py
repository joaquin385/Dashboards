"""Lo que el asistente mira antes de escribir el match.

Lee los nombres y las filas que le pasen. No asigna papeles. Si un papel
queda ambiguo, pregunta. Si ve una persona, pide otro corte y el pipeline
no corre. No mira qué columna deja el período más llamativo.
"""

import re
import unicodedata
from dataclasses import dataclass

FRASE_DE_PERSONAS = (
    "El archivo trae personas identificables. Se pide un corte por día, "
    "producto, local o proyecto antes de seguir."
)

# Un encabezado entra acá solo cuando nombra a una persona, no a un grupo.
_PERSONAS = {
    "nombre",
    "name",
    "apellido",
    "surname",
    "telefono",
    "phone",
    "celular",
    "mobile",
    "whatsapp",
    "mail",
    "email",
    "correo",
    "e_mail",
    "dni",
    "documento",
    "customer_id",
    "cliente_id",
    "user_id",
    "id_cliente",
    "id_usuario",
}

# Sinónimos del encabezado. Dos columnas del mismo papel se preguntan.
# Una sola no se asigna: el match lo escribe el asistente.
_SINONIMOS = {
    "importe": {
        "importe",
        "amount",
        "total",
        "revenue",
        "sales",
        "facturacion",
        "monto",
        "gross",
    },
    "fecha": {"fecha", "date", "day", "dia"},
    "unidades": {"unidades", "units", "qty", "quantity", "cantidad"},
    "precio": {"precio", "price", "unit_price"},
    "costo": {"costo", "cost", "unit_cost"},
    "grupo": {"grupo", "product", "producto", "item", "category", "categoria"},
}

_EMAIL = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
_FECHA = re.compile(r"^\d{4}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class Mirada:
    preguntas: tuple[str, ...]
    personas: tuple[str, ...]
    se_puede_correr: bool


def parece_persona(texto: str) -> bool:
    """Un mail, un teléfono o un encabezado que señala a una persona."""

    limpio = (texto or "").strip()
    if not limpio:
        return False
    if _EMAIL.fullmatch(limpio) or _es_telefono(limpio):
        return True
    return _clave(limpio) in _PERSONAS


def mirar(nombres: list[str], filas: list[dict[str, str]]) -> Mirada:
    personas = _personas(nombres, filas)
    preguntas = []
    if personas:
        preguntas.append(FRASE_DE_PERSONAS)
    preguntas.extend(_ambiguedades(nombres))
    return Mirada(
        preguntas=tuple(preguntas),
        personas=tuple(personas),
        se_puede_correr=not personas,
    )


def _personas(nombres: list[str], filas: list[dict[str, str]]) -> list[str]:
    halladas = []
    for nombre in nombres:
        if _clave(nombre) in _PERSONAS or _celdas_de_persona(nombre, filas):
            halladas.append(nombre)
    return halladas


def _celdas_de_persona(nombre: str, filas: list[dict[str, str]]) -> bool:
    for fila in filas:
        texto = (fila.get(nombre) or "").strip()
        if not texto:
            continue
        if _EMAIL.fullmatch(texto) or _es_telefono(texto):
            return True
    return False


def _es_telefono(texto: str) -> bool:
    if _FECHA.fullmatch(texto):
        return False
    digitos = re.sub(r"\D", "", texto)
    if len(digitos) < 8:
        return False
    return any(signo in texto for signo in "+-() ")


def _ambiguedades(nombres: list[str]) -> list[str]:
    preguntas = []
    for papel, sinonimos in _SINONIMOS.items():
        columnas = [nombre for nombre in nombres if _clave(nombre) in sinonimos]
        if len(columnas) < 2:
            continue
        lista = ", ".join(columnas)
        preguntas.append(
            f"Hay más de una columna que puede ser el {papel}: {lista}. "
            "El asistente pregunta cuál es. "
            "No se elige la que deja el período más llamativo."
        )
    return preguntas


def _clave(nombre: str) -> str:
    texto = unicodedata.normalize("NFKD", nombre.strip().lower())
    texto = "".join(letra for letra in texto if not unicodedata.combining(letra))
    return texto.replace(" ", "_").replace("-", "_")
