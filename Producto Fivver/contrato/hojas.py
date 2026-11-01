"""Catálogo de hojas. Cada hoja dice qué la enciende, qué cuenta y qué no puede escribir."""

from dataclasses import dataclass

from contrato.encargo import Encargo


@dataclass(frozen=True)
class Hueco:
    nombre: str
    lo_llena: str
    que_entra: str


@dataclass(frozen=True)
class Grafico:
    tipo: str
    serie: str
    base_escrita: str
    eje: str = "arranca en cero"
    recorte_debe_decirse: bool = True


@dataclass(frozen=True)
class Hoja:
    id: str
    nombre: str
    modulos: tuple[str, ...]
    pregunta: str
    cuenta: str
    grafico: Grafico
    huecos: tuple[Hueco, ...]
    limite_obligatorio: str
    oraciones_prohibidas: tuple[str, ...]

    def motivo_si_no_enciende(self, encargo: Encargo) -> str | None:
        return _MOTIVO[self.id](encargo)


def _monitoreo(encargo: Encargo) -> str | None:
    if not encargo.tiene_importe():
        return "Falta el importe. La hoja no se completa."
    if encargo.columna("fecha") is None and encargo.columna("periodo") is None:
        return "Falta la fecha o el período. La hoja no se completa."
    return None


def _anio_pasado(encargo: Encargo) -> str | None:
    if not encargo.tiene_importe():
        return "Falta el importe. La hoja no se completa."
    if encargo.columna("fecha") is None and encargo.columna("periodo") is None:
        return "Falta la fecha o el período. La hoja no se completa."
    if not encargo.fechas_cubren_el_anio_pasado:
        return (
            "Las fechas no cubren el mismo período del año pasado. "
            "La hoja no se completa."
        )
    return None


def _piezas(encargo: Encargo) -> str | None:
    if encargo.columna("unidades") is None:
        return "Faltan las unidades. La hoja no se completa."
    tiene_precio = encargo.columna("precio") is not None
    if not tiene_precio and not encargo.tiene_importe():
        return "Faltan el precio y el importe. La hoja no se completa."
    return None


def _lo_que_queda(encargo: Encargo) -> str | None:
    if not encargo.tiene_importe():
        return "Falta el importe. La hoja no se completa."
    if encargo.columna("costo") is None:
        return (
            "Falta el costo que aparece con la venta. "
            "El margen no está. La hoja no inventa el margen."
        )
    return None


def _calendario(encargo: Encargo) -> str | None:
    if not encargo.tiene_importe():
        return "Falta el importe. La hoja no se completa."
    if encargo.columna("fecha") is None:
        return "Falta la fecha del día. Un período cerrado no alcanza para marcar el calendario."
    if not encargo.el_calendario_cambio:
        return (
            "No quedó marcado un cambio de días hábiles o de feriados. "
            "La hoja no inventa el feriado."
        )
    return None


def _el_que_se_aparta(encargo: Encargo) -> str | None:
    if not encargo.tiene_importe():
        return "Falta el importe. La hoja no se completa."
    if encargo.columna("grupo") is None:
        return "Falta el grupo. La hoja no se completa."
    if not encargo.corte_elegido:
        return (
            "Falta el corte elegido antes de mirar. "
            "La hoja no prueba grupos hasta que uno parezca especial."
        )
    return None


def _pesos(encargo: Encargo) -> str | None:
    if not encargo.tiene_importe():
        return "Falta el importe. La hoja no se completa."
    if encargo.columna("unidades") is not None:
        return "Hay unidades. Esta hoja es para una serie sin unidades y no se completa."
    if encargo.moneda.strip().lower() not in {"peso", "pesos", "ars"}:
        return "La moneda no es pesos. La hoja no se completa."
    if not encargo.pais_publica_indice:
        return "El país no tiene un índice público marcado. La hoja no se completa."
    if not encargo.fuente_indice or not encargo.mes_del_indice:
        return "Faltan la fuente del índice y el mes elegido. La hoja no se completa."
    return None


_MOTIVO = {
    "monitoreo": _monitoreo,
    "anio_pasado": _anio_pasado,
    "piezas": _piezas,
    "lo_que_queda": _lo_que_queda,
    "calendario": _calendario,
    "el_que_se_aparta": _el_que_se_aparta,
    "pesos_de_un_mes": _pesos,
}


HOJAS: tuple[Hoja, ...] = (
    Hoja(
        id="monitoreo",
        nombre="Monitoreo",
        modulos=("B1", "C1"),
        pregunta="El período contra el anterior: el total y lo que más pesa.",
        cuenta=(
            "Total del período menos total del período anterior. "
            "Si hay grupo, la frase nombra el que más pesa en ese total. "
            "Eso no abre la hoja del corte."
        ),
        grafico=Grafico(
            tipo="barras de dos períodos",
            serie="importe",
            base_escrita="el período anterior",
        ),
        huecos=(
            Hueco("total", "pipeline", "importe del período"),
            Hueco("total_base", "pipeline", "importe del período anterior"),
            Hueco("diferencia", "pipeline", "la resta de los dos totales"),
            Hueco("lo_que_mas_pesa", "pipeline", "el grupo de mayor importe, si hay grupo"),
            Hueco("limite", "asistente", "qué esta comparación no dice"),
        ),
        limite_obligatorio=(
            "La base es el período anterior. Esta comparación no dice el mismo "
            "período del año pasado, ni la causa, ni si el período de al lado fue un pico."
        ),
        oraciones_prohibidas=(
            "Cayó porque…",
            "El mes que viene va a…",
            "Hay que actuar por esta comparación sola.",
        ),
    ),
    Hoja(
        id="anio_pasado",
        nombre="El año pasado",
        modulos=("B1",),
        pregunta="El mismo recorte, un año atrás.",
        cuenta="Total del período menos total del mismo período del año pasado.",
        grafico=Grafico(
            tipo="barras de dos períodos",
            serie="importe",
            base_escrita="el mismo período del año pasado",
        ),
        huecos=(
            Hueco("total", "pipeline", "importe del período"),
            Hueco("total_base", "pipeline", "importe del mismo período del año pasado"),
            Hueco("diferencia", "pipeline", "la resta de los dos totales"),
            Hueco("limite", "asistente", "que las dos bases se leen juntas"),
        ),
        limite_obligatorio=(
            "Esta hoja se lee junto con el período anterior. Una baja contra el "
            "mes de al lado puede convivir con una suba contra el año pasado."
        ),
        oraciones_prohibidas=(
            "El período fue malo, dicho con una sola de las dos bases.",
            "Como está arriba del año pasado, el mes de al lado no importa.",
        ),
    ),
    Hoja(
        id="piezas",
        nombre="Piezas",
        modulos=("A6", "C4"),
        pregunta="Cuánto del neto se lleva la cantidad, cuánto el precio y cuánto la mezcla.",
        cuenta=(
            "El total se arma con las piezas que el archivo tiene. "
            "Con unidades y precio, es unidades por precio. "
            "Con unidades e importe y sin precio, el precio es el importe dividido "
            "las unidades, y esa definición queda escrita. "
            "Si hay grupo, la mezcla es una pieza más: el total es la suma, por grupo, "
            "de unidades por precio. Se mueve una pieza por vez y el camino queda escrito. "
            "El neto es la resta de los dos períodos. Cada pieza responde por su tramo."
        ),
        grafico=Grafico(
            tipo="barras de lo que se lleva cada pieza",
            serie="pesos de cada pieza, con signo",
            base_escrita="el período anterior, en el camino escrito",
        ),
        huecos=(
            Hueco("neto", "pipeline", "la resta de los dos períodos"),
            Hueco("tramo_de_cada_pieza", "pipeline", "los pesos del camino escrito"),
            Hueco("camino", "asistente", "qué pieza se movió primero"),
            Hueco("limite", "asistente", "que una pieza no es una causa"),
        ),
        limite_obligatorio=(
            "El neto es la resta. Cada pieza responde por su tramo. Una pieza no es una causa."
        ),
        oraciones_prohibidas=(
            "Cayó por el ticket.",
            "El problema es el precio.",
            "La pieza es la causa.",
        ),
    ),
    Hoja(
        id="lo_que_queda",
        nombre="Lo que queda",
        modulos=("A6", "F6"),
        pregunta="Qué queda después del costo que aparece con la venta.",
        cuenta=(
            "Por período, el importe menos el costo que viene en la fila. "
            "Si ese costo no está, la hoja se anuncia vacía."
        ),
        grafico=Grafico(
            tipo="barras de lo que queda",
            serie="importe menos costo",
            base_escrita="el período anterior",
        ),
        huecos=(
            Hueco("importe", "pipeline", "el importe del período"),
            Hueco("costo", "pipeline", "el costo que viaja con la venta"),
            Hueco("queda", "pipeline", "la resta"),
            Hueco("limite", "asistente", "qué costos no están en el archivo"),
        ),
        limite_obligatorio=(
            "Lo que queda resta solo el costo que está en el archivo. "
            "No es el margen del negocio si faltan costos que no viajan con la venta."
        ),
        oraciones_prohibidas=(
            "El margen del negocio es esta resta.",
            "Conviene bajar el precio.",
        ),
    ),
    Hoja(
        id="calendario",
        nombre="Calendario",
        modulos=("B2",),
        pregunta="Qué parte del total es el calendario.",
        cuenta=(
            "Se marca la parte del importe que cae en el día que el otro período "
            "no tiene: un día hábil de más o un feriado. Se muestra al lado del total."
        ),
        grafico=Grafico(
            tipo="barras del total partido en días comparables y días de calendario",
            serie="importe",
            base_escrita="el período anterior, con los días nombrados",
        ),
        huecos=(
            Hueco("importe_en_dias_de_calendario", "pipeline", "la parte marcada"),
            Hueco("importe_en_dias_comparables", "pipeline", "el resto del total"),
            Hueco("que_dia", "asistente", "el feriado o el día hábil de más"),
            Hueco("limite", "asistente", "que la marca no es la causa"),
        ),
        limite_obligatorio="El día de más o el feriado está marcado. No es la causa del mes.",
        oraciones_prohibidas=(
            "Cayó por el feriado.",
            "El feriado explica el mes.",
        ),
    ),
    Hoja(
        id="el_que_se_aparta",
        nombre="El que se aparta",
        modulos=("C1", "C5", "G5"),
        pregunta="Qué grupo se come el total o el agujero, y cuánto explica.",
        cuenta=(
            "Con el corte que el asistente nombró antes, se mide cuánto de ese grupo "
            "explica el total o el agujero del período. El resto queda junto. "
            "No se abre un segundo corte en la misma hoja."
        ),
        grafico=Grafico(
            tipo="barras del corte elegido",
            serie="importe del grupo elegido y del resto",
            base_escrita="el corte nombrado antes de mirar",
        ),
        huecos=(
            Hueco("corte", "asistente", "el grupo elegido antes"),
            Hueco("importe_del_grupo", "pipeline", "cuánto explica ese grupo"),
            Hueco("importe_del_resto", "pipeline", "el resto, junto"),
            Hueco("limite", "asistente", "que este corte no se eligió después de probar varios"),
        ),
        limite_obligatorio=(
            "El corte es el que quedó elegido antes de mirar. "
            "Un corte aparecido después de probar varios no entra en esta hoja."
        ),
        oraciones_prohibidas=(
            "Este grupo es la causa.",
            "Un segundo corte en la misma hoja.",
            "Un corte que apareció después de probar varios.",
        ),
    ),
    Hoja(
        id="pesos_de_un_mes",
        nombre="Pesos de un mes elegido",
        modulos=("B3",),
        pregunta="La serie pasada a pesos de un mes, con la fuente escrita.",
        cuenta=(
            "Cada importe se multiplica por el índice del mes elegido y se divide "
            "por el índice del mes del importe. La fuente queda escrita en la hoja."
        ),
        grafico=Grafico(
            tipo="barras de pesos corrientes y pesos del mes elegido",
            serie="importe",
            base_escrita="el mes elegido del índice, con la fuente",
        ),
        huecos=(
            Hueco("corrientes", "pipeline", "el importe en pesos del mes"),
            Hueco("constantes", "pipeline", "el importe en pesos del mes elegido"),
            Hueco("fuente", "asistente", "la publicación del índice"),
            Hueco("mes", "asistente", "el mes elegido"),
            Hueco("limite", "asistente", "que el índice no es la canasta de la empresa"),
        ),
        limite_obligatorio=(
            "La serie está en pesos del mes elegido, con la fuente escrita. "
            "El índice no es la canasta de esta empresa y no cuenta unidades."
        ),
        oraciones_prohibidas=(
            "El índice mide la canasta de esta empresa.",
            "En pesos de ese mes se vendieron menos unidades.",
        ),
    ),
)

HOJAS_POR_ID = {hoja.id: hoja for hoja in HOJAS}

# Preguntas del curso que este catálogo no responde. Pedirlas es otro encargo.
OTRO_ENCARGO = {
    "stock_y_flujo": "A5. Hace falta un saldo y los movimientos que lo arman.",
    "embudo": "A7. Hacen falta los pasos, cada uno con su cuenta.",
    "cohortes": "B4. Hace falta el grupo que entra junto, agregado, sin lista de personas.",
    "linea_de_base": "B5. Hace falta la meta, la línea de base o la promesa ya escrita. No se calcula un pronóstico para llenar el hueco.",
    "contrafactual": "F1. Hace falta una decisión nombrada y el antes. El supuesto se escribe. El efecto no se da por medido.",
    "escenarios": "F7. Hace falta una decisión nombrada. Se escriben dos o tres futuros y qué tendría que ser cierto. No es un pronóstico.",
}
