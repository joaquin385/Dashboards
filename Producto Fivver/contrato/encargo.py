"""Lo que el asistente deja escrito antes de que el pipeline calcule."""

from dataclasses import dataclass, field

from contrato.papeles import PAPELES


@dataclass(frozen=True)
class Encargo:
    """Un archivo ya mirado, con el match y las marcas del asistente.

    columnas: papel del contrato -> nombre de la columna en el archivo.
    Un papel ausente es una columna que este archivo no tiene.
    """

    columnas: dict[str, str]
    fechas_cubren_el_anio_pasado: bool
    el_calendario_cambio: bool
    moneda: str
    pais: str
    pais_publica_indice: bool
    fuente_indice: str | None
    mes_del_indice: str | None
    corte_elegido: str | None
    hay_personas: bool
    grano: str
    grano_coincide: bool
    decision: str | None
    paquete: str
    hojas_pedidas: tuple[str, ...]
    importe_sale_de_unidades_por_precio: bool = False
    filas: int | None = None
    separador_decimal: str = ""
    separador_miles: str = ""
    formato_fecha: str = "%Y-%m-%d"
    decimales: int = 0
    idioma: str = "es"
    unidad_del_papel: dict[str, str] = field(default_factory=dict)
    hoja_del_archivo: str | None = None
    abre: str | None = None
    origen: str = ""

    def columna(self, papel: str) -> str | None:
        return self.columnas.get(papel)

    def tiene_importe(self) -> bool:
        if self.columna("importe") is not None:
            return True
        return (
            self.importe_sale_de_unidades_por_precio
            and self.columna("unidades") is not None
            and self.columna("precio") is not None
        )

    def papeles_desconocidos(self) -> tuple[str, ...]:
        return tuple(papel for papel in self.columnas if papel not in PAPELES)
