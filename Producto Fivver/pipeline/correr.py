"""Lee el archivo con el match escrito y llena la ficha de cada hoja."""

import csv
from dataclasses import dataclass
from datetime import date
from pathlib import Path

from contrato.encargo import Encargo
from contrato.evaluar import evaluar
from pipeline.excel import leer as leer_excel
from pipeline.instruccion import Instruccion, Marca, Periodo
from pipeline.limpieza import Anotacion, limpiar
from pipeline.mirada import FRASE_DE_PERSONAS, mirar
from pipeline.numeros import dividir, fecha_leida, numero

_CAMINO = ("cantidad", "mezcla", "precio")
_REDONDEO = "La cuenta está redondeada a la unidad."


@dataclass(frozen=True)
class Fila:
    fecha: date
    importe: int
    unidades: int | None
    precio: int | None
    costo: int | None
    grupo: str | None


@dataclass(frozen=True)
class Ficha:
    hoja_id: str
    estado: str
    motivo: str | None
    pregunta: str
    base: str
    grafico: str
    huecos: dict
    pasos: tuple[str, ...]
    comprobacion: str


@dataclass(frozen=True)
class Resultado:
    archivo: str
    grano: str
    personas: str
    filas: int
    total_pelado: int
    limpieza: tuple[Anotacion, ...]
    fichas: tuple[Ficha, ...]
    unidad: str = ""
    detenido: str | None = None

    def ficha(self, hoja_id: str) -> Ficha:
        for ficha in self.fichas:
            if ficha.hoja_id == hoja_id:
                return ficha
        raise KeyError(hoja_id)


def correr(
    encargo: Encargo,
    archivo: Path,
    instruccion: Instruccion,
    marcas: tuple[Marca, ...] = (),
) -> Resultado:
    _exigir_periodo(instruccion)
    unidad = encargo.unidad_del_papel.get("importe", encargo.moneda)
    if encargo.hay_personas:
        return _sin_correr(encargo, archivo, unidad)
    nombres, crudas = _leer(archivo, encargo)
    if not mirar(nombres, crudas).se_puede_correr:
        return _sin_correr(encargo, archivo, unidad)
    recorrido = evaluar(encargo)
    encendidas = tuple(hoja.id for hoja in recorrido.se_completan)
    limpias, anotaciones = limpiar(crudas, marcas, encargo, encendidas)
    filas = tuple(_filas(limpias, encargo, instruccion))
    if recorrido.detenido:
        return Resultado(
            archivo=str(archivo),
            grano=encargo.grano,
            personas=_personas(encargo),
            filas=len(filas),
            total_pelado=_suma(filas),
            limpieza=anotaciones,
            fichas=(),
            unidad=unidad,
            detenido=recorrido.detenido,
        )
    if any(hoja.id == "calendario" for hoja in recorrido.se_completan) and instruccion.calendario is None:
        raise ValueError("El asistente no declaró los días de apertura.")
    if (encargo.columna("devolucion") or encargo.columna("impuesto")) and instruccion.medicion is None:
        raise ValueError(
            "El archivo trae devolución o impuesto. "
            "El asistente escribe la regla antes de correr."
        )
    if instruccion.camino != _CAMINO:
        return Resultado(
            archivo=str(archivo),
            grano=encargo.grano,
            personas=_personas(encargo),
            filas=len(filas),
            total_pelado=_suma(filas),
            limpieza=anotaciones,
            fichas=(),
            unidad=unidad,
            detenido=(
                "Este pipeline recorre cantidad, mezcla y precio, en ese orden. "
                "Otro camino es otra cuenta."
            ),
        )

    fichas = []
    for hoja in recorrido.se_completan:
        fichas.append(_con_medicion(_CALCULO[hoja.id](hoja, filas, encargo, instruccion), instruccion))
    for vacia in recorrido.se_anuncian_vacias:
        fichas.append(
            Ficha(
                hoja_id=vacia.hoja.id,
                estado="vacia",
                motivo=vacia.motivo,
                pregunta=vacia.hoja.pregunta,
                base=vacia.hoja.grafico.base_escrita,
                grafico=vacia.hoja.grafico.tipo,
                huecos={},
                pasos=(vacia.motivo,),
                comprobacion="La hoja no se completa.",
            )
        )
    return Resultado(
        archivo=str(archivo),
        grano=encargo.grano,
        personas=_personas(encargo),
        filas=len(filas),
        total_pelado=_suma(filas),
        limpieza=anotaciones,
        fichas=tuple(fichas),
        unidad=unidad,
    )


def _sin_correr(encargo: Encargo, archivo: Path, unidad: str) -> Resultado:
    return Resultado(
        archivo=str(archivo),
        grano=encargo.grano,
        personas="El archivo trae personas. La corrida se detiene.",
        filas=0,
        total_pelado=0,
        limpieza=(),
        fichas=(),
        unidad=unidad,
        detenido=FRASE_DE_PERSONAS,
    )


def _leer(archivo: Path, encargo: Encargo) -> tuple[list[str], list[dict[str, str]]]:
    if archivo.suffix.lower() == ".xlsx":
        if not encargo.hoja_del_archivo:
            raise ValueError("El asistente no nombró la hoja del Excel.")
        nombres, filas = leer_excel(archivo, encargo.hoja_del_archivo)
    else:
        nombres, filas = _leer_csv(archivo)
    faltan = [nombre for nombre in encargo.columnas.values() if nombre not in nombres]
    if faltan:
        columnas = ", ".join(faltan)
        raise ValueError(f"El match nombra columnas que el archivo no tiene: {columnas}.")
    return nombres, filas


def _leer_csv(archivo: Path) -> tuple[list[str], list[dict[str, str]]]:
    with archivo.open(encoding="utf-8", newline="") as origen:
        lector = csv.DictReader(origen)
        if lector.fieldnames is None:
            raise ValueError(f"{archivo.name} no tiene encabezado.")
        return list(lector.fieldnames), list(lector)


def _filas(
    crudas: list[dict[str, str]],
    encargo: Encargo,
    instruccion: Instruccion,
) -> list[Fila]:
    fecha = encargo.columna("fecha")
    unidades = encargo.columna("unidades")
    precio = encargo.columna("precio")
    costo = encargo.columna("costo")
    grupo = encargo.columna("grupo")
    importe = encargo.columna("importe")
    filas = []
    for cruda in crudas:
        texto = cruda.get(fecha or "", "")
        if not texto:
            continue
        dia = fecha_leida(texto, encargo)
        cantidad = numero(cruda.get(unidades, ""), encargo, dinero=False) if unidades else None
        valor = numero(cruda.get(precio, ""), encargo, dinero=True) if precio else None
        costo_celda = numero(cruda.get(costo, ""), encargo, dinero=True) if costo else None
        if importe:
            plata = numero(cruda[importe], encargo, dinero=True)
        else:
            plata = cantidad * valor
        if instruccion.medicion is not None and instruccion.medicion.venta == "neta":
            columna = encargo.columna("devolucion")
            if columna is None:
                raise ValueError("La regla de venta neta pide la columna de devolución.")
            texto_devolucion = cruda.get(columna, "")
            if texto_devolucion:
                plata -= numero(texto_devolucion, encargo, dinero=True)
        if instruccion.costo_es_por_unidad and costo_celda is not None and cantidad is not None:
            costo_fila = cantidad * costo_celda
        else:
            costo_fila = costo_celda
        filas.append(
            Fila(
                fecha=dia,
                importe=plata,
                unidades=cantidad,
                precio=valor,
                costo=costo_fila,
                grupo=cruda.get(grupo, "") or None if grupo else None,
            )
        )
    return filas


def _personas(encargo: Encargo) -> str:
    if encargo.hay_personas:
        return "El archivo trae personas. La corrida se detiene."
    return "No hay personas en el match. El grano escrito no las cuenta."


def _suma(filas: tuple[Fila, ...] | list[Fila]) -> int:
    return sum(fila.importe for fila in filas)


def _del_periodo(filas: tuple[Fila, ...] | list[Fila], periodo: Periodo) -> tuple[Fila, ...]:
    return tuple(fila for fila in filas if periodo.inicio <= fila.fecha <= periodo.fin)


def _importe(filas: tuple[Fila, ...]) -> int:
    return sum(fila.importe for fila in filas)


def _importe_de_cada_mes(filas: tuple[Fila, ...]) -> dict[str, int]:
    totales: dict[str, int] = {}
    for fila in filas:
        clave = f"{fila.fecha.year:04d}-{fila.fecha.month:02d}"
        totales[clave] = totales.get(clave, 0) + fila.importe
    return totales


def _nombre(periodo: Periodo) -> str:
    return periodo.etiqueta()


def _monitoreo(hoja, filas, encargo, instruccion) -> Ficha:
    periodo = _del_periodo(filas, instruccion.periodo)
    base = _del_periodo(filas, instruccion.periodo_anterior)
    total = _importe(periodo)
    total_base = _importe(base)
    diferencia = total - total_base
    pesa = _el_que_mas_pesa(periodo)
    huecos = {
        "total": total,
        "total_base": total_base,
        "diferencia": diferencia,
        "lo_que_mas_pesa": pesa,
        "importe_de_cada_mes": _importe_de_cada_mes(filas),
        "limite": None,
    }
    return _ficha(
        hoja,
        huecos,
        (
            f"Se suma el importe de {_nombre(instruccion.periodo)}.",
            f"Se suma el importe de {_nombre(instruccion.periodo_anterior)}.",
            "Se resta la base del período.",
        ),
        f"{total} - {total_base} = {diferencia}",
    )


def _anio_pasado(hoja, filas, encargo, instruccion) -> Ficha:
    total = _importe(_del_periodo(filas, instruccion.periodo))
    total_base = _importe(_del_periodo(filas, instruccion.anio_pasado))
    diferencia = total - total_base
    return _ficha(
        hoja,
        {
            "total": total,
            "total_base": total_base,
            "diferencia": diferencia,
            "limite": None,
        },
        (
            f"Se suma el importe de {_nombre(instruccion.periodo)}.",
            f"Se suma el importe de {_nombre(instruccion.anio_pasado)}.",
            "Se resta el mismo período del año pasado.",
        ),
        f"{total} - {total_base} = {diferencia}",
    )


def _piezas(hoja, filas, encargo, instruccion) -> Ficha:
    periodo = _del_periodo(filas, instruccion.periodo)
    base = _del_periodo(filas, instruccion.periodo_anterior)
    neto = _importe(periodo) - _importe(base)
    unidades_base = sum(fila.unidades or 0 for fila in base)
    unidades_periodo = sum(fila.unidades or 0 for fila in periodo)
    if unidades_base == 0:
        raise ValueError("La base no tiene unidades.")
    en_cantidad, red_cantidad = dividir(_importe(base) * unidades_periodo, unidades_base)
    en_mezcla, precios_variaron, red_precio = _a_precios_de_la_base(periodo, base)
    en_precio = _importe(periodo)
    tramo = {
        "cantidad": en_cantidad - _importe(base),
        "mezcla": en_mezcla - en_cantidad,
        "precio": en_precio - en_mezcla,
    }
    huecos = {
        "neto": neto,
        "tramo_de_cada_pieza": tramo,
        "camino": ", ".join(instruccion.camino),
        "limite": None,
    }
    if red_cantidad or red_precio:
        huecos["redondeado"] = _REDONDEO
    pasos = [
        "Primero se estiran las unidades de la base, con su mezcla y sus precios.",
        "Después se pone la mezcla del período, con los precios de la base.",
        "Al final se ponen los precios del período.",
    ]
    if precios_variaron:
        definicion = "El precio de la base es el importe del grupo dividido sus unidades."
        huecos["definicion_precio"] = definicion
        pasos.append(definicion)
    return _ficha(
        hoja,
        huecos,
        tuple(pasos),
        f"{tramo['cantidad']} + {tramo['mezcla']} + {tramo['precio']} = {neto}",
    )


def _lo_que_queda(hoja, filas, encargo, instruccion) -> Ficha:
    periodo = _del_periodo(filas, instruccion.periodo)
    base = _del_periodo(filas, instruccion.periodo_anterior)
    importe = _importe(periodo)
    costo = sum(fila.costo or 0 for fila in periodo)
    queda = importe - costo
    importe_base = _importe(base)
    costo_base = sum(fila.costo or 0 for fila in base)
    queda_base = importe_base - costo_base
    return _ficha(
        hoja,
        {
            "importe": importe,
            "costo": costo,
            "queda": queda,
            "importe_base": importe_base,
            "queda_base": queda_base,
            "limite": None,
        },
        (
            f"Se suma el importe de {_nombre(instruccion.periodo)}.",
            "Se suma el costo que viaja con la venta.",
            "Se resta el costo del importe. La base se resta igual.",
        ),
        f"{importe} - {costo} = {queda}; {queda} - {queda_base} = {queda - queda_base}",
    )


def _calendario(hoja, filas, encargo, instruccion) -> Ficha:
    if instruccion.calendario is None:
        raise ValueError("El asistente no declaró los días de apertura.")
    base = _del_periodo(filas, instruccion.periodo_anterior)
    periodo = _del_periodo(filas, instruccion.periodo)
    dias_base = instruccion.calendario.dias(instruccion.periodo_anterior)
    dias_periodo = instruccion.calendario.dias(instruccion.periodo)
    if not dias_base:
        raise ValueError("La regla no marca días de apertura en la base.")
    total_base = _importe(base)
    total_periodo = _importe(periodo)
    ritmo, redondeo = dividir(total_base, len(dias_base))
    if not dias_periodo:
        raise ValueError("La regla no marca días de apertura en el período.")
    ritmo_periodo, _ = dividir(total_periodo, len(dias_periodo))
    marca = ritmo * (len(dias_periodo) - len(dias_base))
    huecos = {
        "importe_en_dias_de_calendario": marca,
        "importe_en_dias_comparables": total_base,
        "importe_del_periodo": total_periodo,
        "facturacion_por_dia": {
            instruccion.periodo_anterior.etiqueta(): ritmo,
            instruccion.periodo.etiqueta(): ritmo_periodo,
        },
        "que_dia": instruccion.que_dia,
        "dias_de_apertura": len(dias_periodo),
        "dias_de_apertura_base": len(dias_base),
        "dias_sin_filas": _sin_filas(periodo, dias_periodo),
        "dias_sin_filas_base": _sin_filas(base, dias_base),
        "limite": None,
    }
    if redondeo:
        huecos["redondeado"] = _REDONDEO
        comprobacion = (
            f"{ritmo} por día, por {len(dias_periodo) - len(dias_base)} días, es {marca}. "
            f"{_REDONDEO}"
        )
    else:
        comprobacion = f"{total_base} + {marca} = {ritmo} * {len(dias_periodo)}"
    return _ficha(
        hoja,
        huecos,
        (
            f"La regla marca {len(dias_base)} días de apertura en la base y {len(dias_periodo)} en el período.",
            f"Días de apertura sin filas: {huecos['dias_sin_filas_base']} en la base y {huecos['dias_sin_filas']} en el período.",
            f"El ritmo de la base es {total_base} / {len(dias_base)}.",
            "La marca es ese ritmo por los días de diferencia.",
        ),
        comprobacion,
    )


def _el_que_se_aparta(hoja, filas, encargo, instruccion) -> Ficha:
    periodo = _por_grupo(_del_periodo(filas, instruccion.periodo))
    base = _por_grupo(_del_periodo(filas, instruccion.periodo_anterior))
    grupos = set(periodo) | set(base)
    cambios = {grupo: periodo.get(grupo, 0) - base.get(grupo, 0) for grupo in grupos}
    grupo = max(cambios, key=lambda nombre: abs(cambios[nombre]))
    resto = sum(valor for nombre, valor in cambios.items() if nombre != grupo)
    niveles = {nombre: periodo.get(nombre, 0) for nombre in grupos}
    return _ficha(
        hoja,
        {
            "corte": encargo.corte_elegido,
            "importe_del_grupo": {"grupo": grupo, "importe": cambios[grupo]},
            "importe_del_resto": resto,
            "neto": sum(cambios.values()),
            "nivel_de_cada_grupo": niveles,
            "resta_de_cada_grupo": cambios,
            "limite": None,
        },
        (
            f"El corte escrito es {encargo.corte_elegido}.",
            "Se resta, en cada grupo, el importe de la base.",
            "El grupo que más se lleva del neto queda nombrado. El resto queda junto.",
        ),
        f"{cambios[grupo]} + {resto} = {sum(cambios.values())}",
    )


def _pesos(hoja, filas, encargo, instruccion) -> Ficha:
    if instruccion.indice is None or instruccion.mes_del_indice is None:
        raise ValueError("Faltan el índice y el mes elegido, escritos por el asistente.")
    indice_base = instruccion.indice[instruccion.mes_del_indice]
    corrientes = {}
    constantes = {}
    redondeo = False
    meses = (instruccion.periodo, instruccion.periodo_anterior, instruccion.anio_pasado)
    for mes in meses:
        corriente = _importe(_del_periodo(filas, mes))
        indice = instruccion.indice[mes.clave()]
        constante, red = dividir(corriente * indice_base, indice)
        redondeo = redondeo or red
        corrientes[_nombre(mes)] = corriente
        constantes[_nombre(mes)] = constante
    huecos = {
        "corrientes": corrientes,
        "constantes": constantes,
        "fuente": instruccion.fuente_indice,
        "mes": instruccion.mes_escrito,
        "limite": None,
    }
    if redondeo:
        huecos["redondeado"] = _REDONDEO
    return _ficha(
        hoja,
        huecos,
        (
            f"El mes elegido es {instruccion.mes_del_indice}.",
            "Cada mes se multiplica por el índice de ese mes elegido y se divide por el suyo.",
        ),
        "corriente * indice_del_mes_elegido / indice_del_mes = constante",
    )


_CALCULO = {
    "monitoreo": _monitoreo,
    "anio_pasado": _anio_pasado,
    "piezas": _piezas,
    "lo_que_queda": _lo_que_queda,
    "calendario": _calendario,
    "el_que_se_aparta": _el_que_se_aparta,
    "pesos_de_un_mes": _pesos,
}


def _ficha(hoja, huecos: dict, pasos: tuple[str, ...], comprobacion: str) -> Ficha:
    return Ficha(
        hoja_id=hoja.id,
        estado="completa",
        motivo=None,
        pregunta=hoja.pregunta,
        base=hoja.grafico.base_escrita,
        grafico=hoja.grafico.tipo,
        huecos=huecos,
        pasos=pasos,
        comprobacion=comprobacion,
    )


def _el_que_mas_pesa(filas: tuple[Fila, ...]) -> dict | None:
    if not any(fila.grupo for fila in filas):
        return None
    totales: dict[str, int] = {}
    for fila in filas:
        totales[fila.grupo] = totales.get(fila.grupo, 0) + fila.importe
    grupo = max(totales, key=totales.get)
    return {"grupo": grupo, "importe": totales[grupo]}


def _por_grupo(filas: tuple[Fila, ...]) -> dict[str, int]:
    totales: dict[str, int] = {}
    for fila in filas:
        totales[fila.grupo] = totales.get(fila.grupo, 0) + fila.importe
    return totales


def _a_precios_de_la_base(
    periodo: tuple[Fila, ...],
    base: tuple[Fila, ...],
) -> tuple[int, bool, bool]:
    importe: dict[str, int] = {}
    unidades: dict[str, int] = {}
    precios_vistos: dict[str, set[int]] = {}
    for fila in base:
        grupo = fila.grupo or ""
        importe[grupo] = importe.get(grupo, 0) + fila.importe
        unidades[grupo] = unidades.get(grupo, 0) + (fila.unidades or 0)
        if fila.precio is not None:
            precios_vistos.setdefault(grupo, set()).add(fila.precio)
    variaron = any(len(vistos) > 1 for vistos in precios_vistos.values())
    precios: dict[str, int] = {}
    redondeo = False
    for grupo, cantidad in unidades.items():
        if cantidad == 0:
            raise ValueError(f"{grupo} no tiene unidades en la base.")
        precio, red = dividir(importe[grupo], cantidad)
        precios[grupo] = precio
        redondeo = redondeo or red
    total = 0
    for fila in periodo:
        grupo = fila.grupo or ""
        if fila.unidades is None:
            raise ValueError("La mezcla pide unidades.")
        if grupo not in precios:
            raise ValueError(f"{grupo} no tiene precio en la base.")
        total += fila.unidades * precios[grupo]
    return total, variaron, redondeo


def _sin_filas(filas: tuple[Fila, ...], apertura: tuple[date, ...]) -> int:
    con_filas = {fila.fecha for fila in filas}
    return sum(1 for dia in apertura if dia not in con_filas)


def _con_medicion(ficha: Ficha, instruccion: Instruccion) -> Ficha:
    if instruccion.medicion is None:
        return ficha
    huecos = dict(ficha.huecos)
    huecos["regla_de_medicion"] = instruccion.medicion.texto()
    if instruccion.medicion.salto:
        huecos["salto_de_regla"] = instruccion.medicion.salto
    return Ficha(
        hoja_id=ficha.hoja_id,
        estado=ficha.estado,
        motivo=ficha.motivo,
        pregunta=ficha.pregunta,
        base=ficha.base,
        grafico=ficha.grafico,
        huecos=huecos,
        pasos=ficha.pasos,
        comprobacion=ficha.comprobacion,
    )


def _exigir_periodo(instruccion: Instruccion) -> None:
    granos = {
        instruccion.periodo.grano,
        instruccion.periodo_anterior.grano,
        instruccion.anio_pasado.grano,
    }
    if len(granos) != 1:
        raise ValueError("Las tres bases se leen con el mismo grano de período.")

