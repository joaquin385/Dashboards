"""La corrida que el asistente escribe al lado del match."""

from dataclasses import dataclass
from datetime import date, timedelta


_GRANOS = ("mes", "semana", "trimestre", "fechas")


@dataclass(frozen=True)
class Periodo:
    """Un recorte ya escrito. El pipeline no elige el mes por su cuenta."""

    grano: str
    inicio: date
    fin: date

    def __post_init__(self) -> None:
        if self.grano not in _GRANOS:
            raise ValueError(f"El grano del período no está en la lista: {self.grano}.")
        if self.inicio > self.fin:
            raise ValueError("El período empieza después de terminar.")

    @staticmethod
    def mes(anio: int, numero: int) -> "Periodo":
        inicio = date(anio, numero, 1)
        if numero == 12:
            fin = date(anio, 12, 31)
        else:
            fin = date(anio, numero + 1, 1) - timedelta(days=1)
        return Periodo("mes", inicio, fin)

    @staticmethod
    def trimestre(anio: int, numero: int) -> "Periodo":
        primer_mes = (numero - 1) * 3 + 1
        inicio = date(anio, primer_mes, 1)
        fin = Periodo.mes(anio, primer_mes + 2).fin
        return Periodo("trimestre", inicio, fin)

    @staticmethod
    def entre(grano: str, inicio: date, fin: date) -> "Periodo":
        return Periodo(grano, inicio, fin)

    def clave(self) -> tuple:
        if self.grano == "mes":
            return (self.inicio.year, self.inicio.month)
        return (self.grano, self.inicio, self.fin)

    def etiqueta(self) -> str:
        if self.grano == "mes":
            return f"{self.inicio.year}-{self.inicio.month:02d}"
        return f"{self.inicio.isoformat()} a {self.fin.isoformat()}"


@dataclass(frozen=True)
class Calendario:
    """Qué día abre, escrito antes de contar las filas."""

    abre: tuple[int, ...]
    feriados: tuple[date, ...]
    texto: str

    def dias(self, periodo: Periodo) -> tuple[date, ...]:
        feriados = set(self.feriados)
        abre = set(self.abre)
        salida = []
        dia = periodo.inicio
        while dia <= periodo.fin:
            if dia.weekday() in abre and dia not in feriados:
                salida.append(dia)
            dia += timedelta(days=1)
        return tuple(salida)


@dataclass(frozen=True)
class ReglaMedicion:
    """Cómo se fabricó el importe. Bruta, neta, y si el impuesto queda afuera."""

    venta: str
    impuesto_afuera: bool = False
    salto: str | None = None

    def __post_init__(self) -> None:
        if self.venta not in {"bruta", "neta"}:
            raise ValueError("La regla de venta es bruta o neta.")

    def texto(self) -> str:
        partes = [f"venta {self.venta}"]
        if self.impuesto_afuera:
            partes.append("el impuesto queda afuera del precio")
        return "; ".join(partes)


@dataclass(frozen=True)
class Marca:
    """Una suciedad, con lo que hay que hacerle.

    numero_con_punto_de_miles convierte 2.000 en 2000.
    comprobante_repetido deja la primera fila de cada ticket.
    no_sumar saca los tickets que el asistente nombró.
    esperar anota la suciedad que no cambia la suma.
    Si hoja está escrita y esa hoja no se encendió, la marca se anota
    y las filas no se tocan.
    """

    accion: str
    columnas: tuple[str, ...] = ()
    tickets: tuple[str, ...] = ()
    detalle: str = ""
    hoja: str | None = None


@dataclass(frozen=True)
class Instruccion:
    periodo: Periodo
    periodo_anterior: Periodo
    anio_pasado: Periodo
    camino: tuple[str, ...]
    que_dia: str
    costo_es_por_unidad: bool
    calendario: Calendario | None = None
    medicion: ReglaMedicion | None = None
    indice: dict[tuple[int, int], int] | None = None
    mes_del_indice: tuple[int, int] | None = None
    mes_escrito: str | None = None
    fuente_indice: str | None = None
