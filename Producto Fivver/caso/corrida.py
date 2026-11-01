"""Lo que el asistente deja escrito para correr Loma. El pipeline no elige columnas."""

from caso.cuenta import (
    FERIADO,
    FUENTE_INDICE,
    GRANO,
    HOJAS_DE_LA_COPIA,
    HOJAS_DE_LOMA,
    INDICE,
    MES_DEL_INDICE,
)
from caso.suciedad import NOTA_QUE_ESPERA, TICKET_QUE_NO_SE_SUMA
from contrato.encargo import Encargo
from pipeline.instruccion import Calendario, Instruccion, Marca, Periodo


def encargo_loma(filas: int) -> Encargo:
    return Encargo(
        columnas={
            "fecha": "fecha",
            "grupo": "producto",
            "unidades": "unidades",
            "precio": "precio",
            "costo": "costo",
            "comprobante": "ticket",
        },
        importe_sale_de_unidades_por_precio=True,
        fechas_cubren_el_anio_pasado=True,
        el_calendario_cambio=True,
        moneda="pesos",
        pais="Argentina",
        pais_publica_indice=True,
        fuente_indice=None,
        mes_del_indice=None,
        corte_elegido="producto",
        hay_personas=False,
        grano=GRANO,
        grano_coincide=True,
        decision=None,
        paquete="premium",
        hojas_pedidas=HOJAS_DE_LOMA,
        filas=filas,
        origen="el archivo de ventas del local",
    )


def encargo_copia(filas: int) -> Encargo:
    return Encargo(
        columnas={"fecha": "fecha", "importe": "importe"},
        fechas_cubren_el_anio_pasado=True,
        el_calendario_cambio=True,
        moneda="pesos",
        pais="Argentina",
        pais_publica_indice=True,
        fuente_indice=FUENTE_INDICE,
        mes_del_indice=MES_DEL_INDICE,
        corte_elegido=None,
        hay_personas=False,
        grano="un día de apertura",
        grano_coincide=True,
        decision=None,
        paquete="premium",
        hojas_pedidas=HOJAS_DE_LA_COPIA + ("lo_que_queda",),
        filas=filas,
        origen="el archivo de ventas del local",
    )


def calendario_loma() -> Calendario:
    return Calendario(
        abre=(0, 1, 2, 3, 4, 5),
        feriados=(FERIADO,),
        texto=(
            "Día de apertura es lunes a sábado, el sábado pesa como un día de semana, "
            "el domingo cierra, y el feriado del 17 de agosto sacó un lunes."
        ),
    )


def instruccion_loma() -> Instruccion:
    return Instruccion(
        periodo=Periodo.mes(2026, 9),
        periodo_anterior=Periodo.mes(2026, 8),
        anio_pasado=Periodo.mes(2025, 9),
        camino=("cantidad", "mezcla", "precio"),
        que_dia="17 de agosto de 2026, feriado, sin fila",
        costo_es_por_unidad=True,
        calendario=calendario_loma(),
        indice=None,
        mes_del_indice=None,
        fuente_indice=None,
    )


def instruccion_copia() -> Instruccion:
    return Instruccion(
        periodo=Periodo.mes(2026, 9),
        periodo_anterior=Periodo.mes(2026, 8),
        anio_pasado=Periodo.mes(2025, 9),
        camino=("cantidad", "mezcla", "precio"),
        que_dia="17 de agosto de 2026, feriado, sin fila",
        costo_es_por_unidad=False,
        calendario=calendario_loma(),
        indice=INDICE,
        mes_del_indice=(2025, 9),
        mes_escrito=MES_DEL_INDICE,
        fuente_indice=FUENTE_INDICE,
    )


def marcas_loma() -> tuple[Marca, ...]:
    return (
        Marca(
            "numero_con_punto_de_miles",
            columnas=("precio", "costo", "importe"),
            detalle="El importe de una fila de Cordel está escrito con punto de miles.",
        ),
        Marca(
            "comprobante_repetido",
            detalle="La Maroma del 1 de agosto está dos veces, con el mismo ticket.",
        ),
        Marca(
            "no_sumar",
            tickets=(TICKET_QUE_NO_SE_SUMA,),
            detalle="El total de Cordel de agosto ya está en las filas del mes.",
        ),
        Marca(
            "esperar",
            detalle=(
                f"La fila en blanco no suma. La nota {NOTA_QUE_ESPERA} "
                "es mayúscula y comentario al margen."
            ),
        ),
    )
