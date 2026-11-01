"""La nota de Loma, escrita sobre las fichas. Los pesos entran por los huecos."""

from informe.nota import Cierre, HuecoVacio, Nota
from pipeline.correr import Resultado


def escribir_loma(resultado: Resultado) -> Nota:
    return Nota(
        destinatario=(
            "Quien podría firmar en Loma no está nombrado. La nota queda en la comparación."
        ),
        primera_oracion=(
            "Septiembre de 2026 está {monitoreo|diferencia|resta} de agosto "
            "y {anio_pasado|diferencia|resta} de septiembre de 2025. "
            "Este archivo no alcanza para firmar una compra."
        ),
        evidencia=(
            (
                "monitoreo",
                "La base es agosto de 2026. Septiembre facturó {monitoreo|total} "
                "contra {monitoreo|total_base}. Lo que más pesa en septiembre es "
                "{monitoreo|lo_que_mas_pesa|grupo}, con {monitoreo|lo_que_mas_pesa|importe}.",
            ),
            (
                "anio_pasado",
                "La otra base es septiembre de 2025, con {anio_pasado|total_base}. "
                "Septiembre de 2026 facturó {anio_pasado|total}.",
            ),
            (
                "piezas",
                "El camino escrito es {piezas|camino}. La cantidad se lleva "
                "{piezas|tramo_de_cada_pieza|cantidad|resta}, la mezcla "
                "{piezas|tramo_de_cada_pieza|mezcla|resta} y el precio queda "
                "{piezas|tramo_de_cada_pieza|precio|resta}. El neto es {piezas|neto|resta}.",
            ),
            (
                "lo_que_queda",
                "Después del costo que viaja con la venta, septiembre deja "
                "{lo_que_queda|queda} y agosto deja {lo_que_queda|queda_base}.",
            ),
            (
                "calendario",
                "La marca es {calendario|importe_en_dias_de_calendario}, un día al ritmo "
                "de agosto. Esos días de agosto facturaron "
                "{calendario|importe_en_dias_comparables}. El día marcado: "
                "{calendario|que_dia}.",
            ),
            (
                "el_que_se_aparta",
                "El corte, elegido antes, es {el_que_se_aparta|corte}. "
                "{el_que_se_aparta|importe_del_grupo|grupo} se lleva "
                "{el_que_se_aparta|importe_del_grupo|importe|resta}. "
                "El resto se lleva {el_que_se_aparta|importe_del_resto|resta}.",
            ),
        ),
        limite=(
            "Las dos bases se leen juntas. Una pieza no es una causa, y otro camino "
            "les cambiaría el tamaño. Lo que queda resta solo el costo de la fila. "
            "El feriado está marcado. El sábado, en este caso, pesa como un día de semana. "
            "Hay unidades, así que esta nota no pasa la serie a pesos de otro mes."
        ),
        otra_historia=(
            "También cabe la mezcla, con la lista de Cordel y de Soga quieta, "
            "y cabe que el día de más no haya alcanzado. Las dos caben en estos pesos. "
            "La primera oración sigue con las dos bases."
        ),
        cierres=(
            Cierre(
                "descriptivo",
                "Septiembre facturó {monitoreo|total} contra {monitoreo|total_base} de agosto, "
                "y {anio_pasado|total} contra {anio_pasado|total_base} de septiembre de 2025.",
            ),
            Cierre(
                "causal",
                "La tabla no separa la causa de las filas que faltan. "
                "Describe el mes contra agosto y contra el año pasado.",
            ),
        ),
    )


def escribir_copia(resultado: Resultado) -> Nota:
    return Nota(
        destinatario=(
            "Quien podría firmar en Loma no está nombrado. Esta copia no tiene unidades."
        ),
        primera_oracion=(
            "En pesos corrientes, septiembre de 2026 está {monitoreo|diferencia|resta} "
            "de agosto y {anio_pasado|diferencia|resta} de septiembre de 2025. "
            "En pesos de {pesos_de_un_mes|mes}, septiembre de 2026 queda en "
            "{pesos_de_un_mes|constantes|2026-09} contra "
            "{pesos_de_un_mes|constantes|2025-09}. "
            "Este archivo no alcanza para firmar una compra."
        ),
        evidencia=(
            (
                "monitoreo",
                "La base corriente es agosto, con {monitoreo|total_base}. "
                "Septiembre facturó {monitoreo|total}.",
            ),
            (
                "anio_pasado",
                "Septiembre de 2025 facturó {anio_pasado|total_base} en pesos de ese mes.",
            ),
            (
                "calendario",
                "La marca sigue siendo {calendario|importe_en_dias_de_calendario}. "
                "{calendario|que_dia}.",
            ),
            (
                "pesos_de_un_mes",
                "El mes elegido es {pesos_de_un_mes|mes}. Agosto queda en "
                "{pesos_de_un_mes|constantes|2026-08} y septiembre de 2026 en "
                "{pesos_de_un_mes|constantes|2026-09}. La fuente: {pesos_de_un_mes|fuente}.",
            ),
        ),
        limite=(
            "El índice es de práctica. No es la canasta de Loma y no cuenta unidades. "
            "La suba en corrientes y la baja en pesos del mes elegido se leen juntas."
        ),
        otra_historia=(
            "La otra historia es la vara. En corrientes el año está arriba. "
            "En pesos de septiembre de 2025, septiembre de 2026 está abajo. "
            "Por eso las dos entran en la primera oración."
        ),
        cierres=(
            Cierre(
                "descriptivo",
                "En corrientes, septiembre está {anio_pasado|diferencia|resta} "
                "de septiembre de 2025. En pesos de {pesos_de_un_mes|mes}, "
                "queda en {pesos_de_un_mes|constantes|2026-09} contra "
                "{pesos_de_un_mes|constantes|2025-09}.",
            ),
            Cierre(
                "causal",
                "La copia no separa la causa. Pasa los pesos de mes. "
                "No dice cuántas unidades se vendieron.",
            ),
        ),
        huecos_vacios=(
            HuecoVacio(
                "lo_que_queda",
                "el costo que aparece con la venta",
                "decir lo que queda después de ese costo",
                "La comparación de facturación sigue en pie.",
            ),
        ),
    )
