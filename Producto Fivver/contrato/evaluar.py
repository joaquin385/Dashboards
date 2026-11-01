"""Recorre un encargo ya escrito y dice qué hojas se completan."""

from dataclasses import dataclass

from contrato.encargo import Encargo
from contrato.hojas import HOJAS_POR_ID, OTRO_ENCARGO, Hoja
from contrato.nota import EsqueletoNota, esqueleto
from contrato.paquetes import PAQUETES


@dataclass(frozen=True)
class HojaVacia:
    hoja: Hoja
    motivo: str


@dataclass(frozen=True)
class Recorrido:
    """Lo que una persona puede leer del contrato para este encargo."""

    detenido: str | None
    se_completan: tuple[Hoja, ...]
    se_anuncian_vacias: tuple[HojaVacia, ...]
    fuera_del_paquete: tuple[str, ...]
    otro_encargo: tuple[tuple[str, str], ...]
    nota: EsqueletoNota | None

    def texto(self) -> str:
        return _texto(self)


def evaluar(encargo: Encargo) -> Recorrido:
    papeles = encargo.papeles_desconocidos()
    if papeles:
        nombres = ", ".join(papeles)
        return _detenido(
            f"El match usa papeles que el contrato no tiene: {nombres}."
        )

    if encargo.hay_personas:
        return _detenido(
            "El archivo trae personas identificables. Se pide un corte por día, "
            "producto, local o proyecto antes de seguir."
        )

    if not encargo.grano_coincide:
        return _detenido(
            "El grano declarado no coincide con el archivo. Se dice antes de calcular."
        )

    paquete = PAQUETES.get(encargo.paquete)
    if paquete is None:
        return _detenido(f"El paquete {encargo.paquete} no está en la ficha.")

    if encargo.filas is not None and encargo.filas > paquete["max_filas"]:
        return _detenido(
            f"{paquete['nombre']} llega hasta {paquete['max_filas']} filas "
            f"y el archivo tiene {encargo.filas}."
        )

    pedidas = encargo.hojas_pedidas
    otro = tuple(
        (hoja_id, OTRO_ENCARGO[hoja_id]) for hoja_id in pedidas if hoja_id in OTRO_ENCARGO
    )
    conocidas = tuple(hoja_id for hoja_id in pedidas if hoja_id not in OTRO_ENCARGO)
    desconocidas = tuple(
        hoja_id
        for hoja_id in conocidas
        if hoja_id not in HOJAS_POR_ID
    )
    if desconocidas:
        nombres = ", ".join(desconocidas)
        return _detenido(f"Esas hojas no están en el catálogo: {nombres}.")

    permitidas = set(paquete["hojas_fijas"]) | set(paquete["hojas_elegibles"])
    fuera = tuple(hoja_id for hoja_id in conocidas if hoja_id not in permitidas)
    dentro = tuple(hoja_id for hoja_id in conocidas if hoja_id in permitidas)

    if paquete["hojas_fijas"]:
        faltan_fijas = tuple(
            hoja_id for hoja_id in paquete["hojas_fijas"] if hoja_id not in dentro
        )
        if faltan_fijas:
            nombres = ", ".join(faltan_fijas)
            return _detenido(
                f"{paquete['nombre']} incluye {nombres}. "
                "El asistente la deja en las hojas pedidas, aunque después se anuncie vacía."
            )

    elegibles_pedidas = tuple(
        hoja_id for hoja_id in dentro if hoja_id in paquete["hojas_elegibles"]
    )
    if len(elegibles_pedidas) > paquete["max_elegibles"]:
        return _detenido(
            f"{paquete['nombre']} admite {paquete['max_elegibles']} "
            f"de las hojas elegibles y el asistente pidió {len(elegibles_pedidas)}. "
            "Elige cuáles entran."
        )

    if len(dentro) > 6:
        return _detenido("El paquete entrega hasta seis hojas. El asistente elige cuáles.")

    se_completan = []
    vacias = []
    for hoja_id in dentro:
        hoja = HOJAS_POR_ID[hoja_id]
        motivo = hoja.motivo_si_no_enciende(encargo)
        if motivo is None:
            se_completan.append(hoja)
        else:
            vacias.append(HojaVacia(hoja, motivo))

    orden = {hoja.id: n for n, hoja in enumerate(HOJAS_POR_ID.values())}
    se_completan.sort(key=lambda hoja: orden[hoja.id])
    vacias.sort(key=lambda item: orden[item.hoja.id])

    return Recorrido(
        detenido=None,
        se_completan=tuple(se_completan),
        se_anuncian_vacias=tuple(vacias),
        fuera_del_paquete=fuera,
        otro_encargo=otro,
        nota=esqueleto(encargo, paquete["profundidad_nota"]),
    )


def _detenido(motivo: str) -> Recorrido:
    return Recorrido(
        detenido=motivo,
        se_completan=(),
        se_anuncian_vacias=(),
        fuera_del_paquete=(),
        otro_encargo=(),
        nota=None,
    )


def _texto(recorrido: Recorrido) -> str:
    lineas = []
    if recorrido.detenido:
        lineas.append(f"Detenido. {recorrido.detenido}")
        return "\n".join(lineas)

    lineas.append("Se completan:")
    if recorrido.se_completan:
        for hoja in recorrido.se_completan:
            lineas.append(f"- {hoja.nombre}. {hoja.pregunta}")
            lineas.append(f"  Límite: {hoja.limite_obligatorio}")
    else:
        lineas.append("- Ninguna.")

    lineas.append("Se anuncian vacías:")
    if recorrido.se_anuncian_vacias:
        for item in recorrido.se_anuncian_vacias:
            lineas.append(f"- {item.hoja.nombre}. {item.motivo}")
    else:
        lineas.append("- Ninguna.")

    if recorrido.fuera_del_paquete:
        nombres = ", ".join(recorrido.fuera_del_paquete)
        lineas.append(f"Fuera del paquete: {nombres}.")

    if recorrido.otro_encargo:
        lineas.append("Otro encargo:")
        for hoja_id, motivo in recorrido.otro_encargo:
            lineas.append(f"- {hoja_id}. {motivo}")

    nota = recorrido.nota
    lineas.append(f"Nota ({nota.profundidad}):")
    lineas.append(f"- Orden: {', '.join(nota.orden)}.")
    lineas.append(f"- {nota.primera_oracion}")
    lineas.append(f"- {nota.regla_otra_historia}")
    lineas.append("Oraciones prohibidas en la nota:")
    for frase in nota.oraciones_prohibidas:
        lineas.append(f"- {frase}")
    return "\n".join(lineas)
