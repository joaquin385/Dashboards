"""Lee un número o una fecha con la regla que el asistente escribió.

No prueba el otro formato si el declarado no entra. 03/04 es marzo o abril
según esa regla, y el punto es miles o decimal según esa regla.
"""

import re
from datetime import date, datetime
from decimal import Decimal, InvalidOperation

from contrato.encargo import Encargo

_ENTERO = re.compile(r"^-?\d+$")


def numero(valor: str, encargo: Encargo, *, dinero: bool = True) -> int:
    texto = (valor or "").strip()
    if not texto:
        raise ValueError("Quedó un número vacío.")
    if encargo.separador_miles and encargo.separador_miles == encargo.separador_decimal:
        raise ValueError("El separador de miles y el decimal no pueden ser el mismo.")
    if not dinero or encargo.decimales == 0:
        if encargo.separador_miles:
            texto = texto.replace(encargo.separador_miles, "")
        if not _ENTERO.fullmatch(texto):
            raise ValueError(f"Quedó un número sin convertir: {valor!r}.")
        return int(texto)
    if not encargo.separador_decimal:
        raise ValueError("El asistente no escribió el separador decimal.")
    if encargo.separador_miles:
        texto = texto.replace(encargo.separador_miles, "")
    if encargo.separador_decimal != ".":
        texto = texto.replace(encargo.separador_decimal, ".")
    try:
        cuantia = Decimal(texto)
    except InvalidOperation:
        raise ValueError(f"Quedó un número sin convertir: {valor!r}.") from None
    menor = cuantia * (Decimal(10) ** encargo.decimales)
    if menor != menor.to_integral_value():
        raise ValueError(f"Quedó un número sin convertir: {valor!r}.")
    return int(menor)


def leer_numero(valor: str, encargo: Encargo, *, dinero: bool = True) -> int | None:
    """Lo que no entra en la regla queda afuera. La marca siguiente lo anota."""

    if not (valor or "").strip():
        return None
    try:
        return numero(valor, encargo, dinero=dinero)
    except ValueError:
        return None


def fecha_leida(valor: object, encargo: Encargo) -> date:
    if isinstance(valor, datetime):
        return valor.date()
    if isinstance(valor, date):
        return valor
    texto = str(valor).strip()
    try:
        return datetime.strptime(texto, encargo.formato_fecha).date()
    except ValueError:
        raise ValueError(
            f"La fecha {valor!r} no entra en el formato {encargo.formato_fecha}."
        ) from None


def dividir(numerador: int, denominador: int) -> tuple[int, bool]:
    """Parte en enteros. El segundo valor dice si hubo que redondear."""

    if denominador == 0:
        raise ValueError("La división no tiene base.")
    if numerador % denominador == 0:
        return numerador // denominador, False
    signo = 1 if (numerador > 0) == (denominador > 0) else -1
    cociente = (abs(numerador) + abs(denominador) // 2) // abs(denominador)
    return signo * cociente, True
