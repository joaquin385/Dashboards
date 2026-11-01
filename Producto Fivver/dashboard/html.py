"""Una pantalla. Los números son los de las fichas y los de la nota.

El HTML no vuelve a sumar. Muestra la facturación por día, el nivel de cada
grupo y la línea de limpieza que el pipeline ya dejó escritas.
"""

import html
import json
import re
from datetime import timedelta
from pathlib import Path

from contrato.encargo import Encargo
from contrato.hojas import HOJAS_POR_ID
from informe.nota import HuecoVacio, NotaLista
from pipeline.correr import Ficha, Resultado
from pipeline.instruccion import Instruccion, Periodo
from pipeline.mirada import parece_persona

_MESES = {
    "es": (
        "",
        "enero",
        "febrero",
        "marzo",
        "abril",
        "mayo",
        "junio",
        "julio",
        "agosto",
        "septiembre",
        "octubre",
        "noviembre",
        "diciembre",
    ),
    "en": (
        "",
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ),
}

_CORTO = {
    "es": (
        "",
        "ene",
        "feb",
        "mar",
        "abr",
        "may",
        "jun",
        "jul",
        "ago",
        "sep",
        "oct",
        "nov",
        "dic",
    ),
    "en": (
        "",
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ),
}

_ESTILO = """
* { box-sizing: border-box; }
html, body { margin: 0; height: 100%; }
body {
  height: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  background: #f3f2f1;
  font-family: "Segoe UI", "Helvetica Neue", sans-serif;
  color: #252423;
}
.cabezal { position: relative; z-index: 2; flex: 0 0 auto; padding: 12px 16px 10px; }
.cabezal h1 { margin: 0; font-size: 22px; font-weight: 600; letter-spacing: 0; }
.escena { flex: 1 1 auto; min-height: 0; display: flex; }
.costado {
  flex: 0 0 212px;
  min-height: 0;
  position: relative;
  z-index: 4;
  background: #fff;
  border-right: 1px solid #edebe9;
  padding: 14px 12px;
}
.barra { display: flex; flex-wrap: wrap; gap: 10px 28px; padding-bottom: 8px; }
.costado .barra { flex-direction: column; align-items: stretch; gap: 16px; padding: 0; }
.slicer { display: flex; align-items: center; gap: 8px; }
.costado .slicer { flex-direction: column; align-items: stretch; gap: 6px; }
.costado .disparador { width: 100%; min-width: 0; }
.slicer .nombre { font-size: 12px; font-weight: 600; color: #605e5c; }
.caja { position: relative; }
.disparador {
  display: flex;
  align-items: center;
  gap: 16px;
  min-width: 168px;
  font: 13px/1.2 "Segoe UI", sans-serif;
  color: #252423;
  background: #fff;
  border: 1px solid #c8c6c4;
  border-radius: 2px;
  padding: 6px 10px;
  cursor: pointer;
}
.disparador .elegido { flex: 1 1 auto; text-align: left; }
.flecha {
  flex: 0 0 auto;
  display: inline-block;
  width: 0;
  height: 0;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 5px solid #605e5c;
}
.disparador[aria-expanded="true"] > .flecha {
  border-top: 0;
  border-bottom: 5px solid #605e5c;
}
.panel {
  position: absolute;
  top: calc(100% + 4px);
  left: 0;
  z-index: 3;
  min-width: 220px;
  max-height: 320px;
  overflow: auto;
  background: #fff;
  border: 1px solid #c8c6c4;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.12);
  padding: 4px 0;
}
.panel[hidden] { display: none; }
.opcion {
  display: block;
  width: 100%;
  font: 13px/1.3 "Segoe UI", sans-serif;
  color: #252423;
  text-align: left;
  background: transparent;
  border: 0;
  padding: 6px 10px;
  cursor: pointer;
}
.nodo { display: flex; flex-wrap: wrap; align-items: center; }
.nodo > .opcion { width: auto; flex: 1 1 auto; }
.abrir, .vacio { flex: 0 0 22px; width: 22px; height: 22px; padding: 0; border: 0; background: transparent; cursor: pointer; }
.vacio { cursor: default; }
.abrir .flecha {
  border-top: 4px solid transparent;
  border-bottom: 4px solid transparent;
  border-left: 5px solid #605e5c;
  border-right: 0;
}
.abrir[aria-expanded="true"] .flecha {
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-top: 5px solid #605e5c;
  border-bottom: 0;
}
.hijos { flex: 1 0 100%; padding-left: 16px; }
.hijos[hidden] { display: none; }
.opcion[aria-pressed="true"] { background: #deecf9; color: #0b5cab; }
.hallazgos {
  flex: 0 0 auto;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(160px, 1fr));
  gap: 12px;
  padding: 0 12px;
}
.hallazgo {
  min-width: 0;
  background: #fff;
  border-radius: 2px;
  box-shadow: 0 1.6px 3.6px rgba(0, 0, 0, 0.13), 0 0.3px 0.9px rgba(0, 0, 0, 0.11);
  padding: 10px 14px 12px;
}
.hallazgo .rotulo { margin: 0; font-size: 12px; font-weight: 600; color: #605e5c; }
.hallazgo .cifra {
  margin: 2px 0 0;
  font-size: 26px;
  font-weight: 650;
  line-height: 1.15;
  font-variant-numeric: tabular-nums;
  letter-spacing: -0.02em;
}
.hallazgo.baja .cifra { color: #a4262c; }
.hallazgo.sube .cifra { color: #0b6a0b; }
.hallazgo .pista { margin: 4px 0 0; font-size: 12px; color: #605e5c; }
.hallazgo.contando { outline: 2px solid #118dff; outline-offset: -2px; }
.glosario, .informe {
  display: none;
  flex: 1 1 auto;
  min-height: 0;
  overflow: auto;
  margin: 0 12px 12px;
  padding: 8px 20px 28px;
  background: #fff;
  box-shadow: 0 1.6px 3.6px rgba(0, 0, 0, 0.13), 0 0.3px 0.9px rgba(0, 0, 0, 0.11);
}
body.en-glosario .escena,
body.en-informe .escena { display: none; }
body.en-glosario .glosario,
body.en-informe .informe { display: block; flex: 1 1 auto; min-height: 0; }
.glosario h2, .informe h2 { margin: 14px 0 8px; font-size: 22px; font-weight: 600; }
.glosario h3 {
  margin: 18px 0 10px;
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #605e5c;
}
.glosario article { margin: 0 0 16px; max-width: 760px; }
.glosario h4 { margin: 0 0 4px; font-size: 16px; font-weight: 650; }
.glosario p { margin: 0; font-size: 15px; line-height: 1.45; }
.informe article h3 {
  margin: 22px 0 8px;
  font-size: 18px;
  font-weight: 650;
  letter-spacing: 0;
  text-transform: none;
  color: #252423;
}
.informe p { margin: 0 0 10px; max-width: 720px; font-size: 16px; line-height: 1.5; }
.informe .lead { max-width: 720px; margin: 0 0 8px; font-size: 15px; line-height: 1.45; color: #605e5c; }
#volver {
  font: 13px/1 "Segoe UI", sans-serif;
  color: #252423;
  background: #fff;
  border: 1px solid #c8c6c4;
  border-radius: 2px;
  padding: 8px 14px;
  cursor: pointer;
}
.visual.contando { outline: 2px solid #118dff; outline-offset: -2px; }
.visual [data-marca] { transition: opacity 0.35s ease; }
.reporte {
  flex: 1 1 auto;
  min-height: 0;
  display: grid;
  grid-template-columns: 1fr 1fr;
  grid-template-rows: minmax(0, 1.15fr) minmax(0, 1fr);
  gap: 12px;
  padding: 8px 12px 12px;
}
.visual.ancho { grid-column: 1 / -1; }
.visual {
  min-width: 0;
  min-height: 0;
  display: flex;
  flex-direction: column;
  background: #fff;
  border-radius: 2px;
  box-shadow: 0 1.6px 3.6px rgba(0, 0, 0, 0.13), 0 0.3px 0.9px rgba(0, 0, 0, 0.11);
  padding: 8px 12px 10px;
}
.visual h2 { margin: 0 0 8px; font-size: 14px; font-weight: 600; }
.filtros { display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 8px; }
.filtros button {
  font: 12px/1 "Segoe UI", sans-serif;
  color: #252423;
  background: #fff;
  border: 1px solid #c8c6c4;
  border-radius: 2px;
  padding: 6px 10px;
  cursor: pointer;
}
.filtros button[aria-pressed="true"] {
  background: #deecf9;
  border-color: #118dff;
  color: #0b5cab;
}
.visual figure.tarjeta {
  flex: 1 1 auto;
  min-height: 0;
  margin: 0;
  border: 0;
  border-radius: 0;
  box-shadow: none;
  background: transparent;
  padding: 0;
}
.visual [data-vista] { flex: 1 1 auto; min-height: 0; display: flex; }
.visual [data-vista][hidden] { display: none; }
section { display: none; }
section.activa {
  display: flex;
  flex-direction: column;
  height: 100%;
  overflow: hidden;
  padding: 14px 20px 8px;
  gap: 8px;
}
.cabeza { flex: 0 0 auto; display: flex; flex-direction: column; gap: 3px; }
.kicker {
  margin: 0;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: #8a8175;
}
h1 {
  margin: 0;
  font-size: 26px;
  font-weight: 650;
  letter-spacing: -0.02em;
  line-height: 1.1;
}
.respuesta {
  margin: 2px 0 0;
  max-width: 1100px;
  font-size: 16px;
  font-weight: 650;
  line-height: 1.35;
}
.limpieza { margin: 0; font-size: 13px; color: #3f3830; }
.procedencia { margin: 0; font-size: 12.5px; line-height: 1.4; color: #6b645c; }
.cuerpo-hoja {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  gap: 18px;
  align-items: stretch;
}
.lienzo {
  flex: 1 1 auto;
  min-width: 0;
  min-height: 0;
  display: flex;
  flex-direction: column;
}
.lectura {
  flex: 0 1 360px;
  min-width: 280px;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.lectura p { margin: 0; }
.pregunta { font-size: 15px; font-weight: 650; line-height: 1.35; }
.base, .nivel, .neto, .extra { font-size: 13.5px; line-height: 1.4; color: #3a342c; }
.cuenta {
  font-size: 13.5px;
  line-height: 1.4;
  font-variant-numeric: tabular-nums;
  background: #fffcf7;
  border: 1px solid #e4dccf;
  border-radius: 8px;
  padding: 8px 10px;
}
.limite {
  margin-top: auto;
  padding-top: 8px;
  border-top: 1px solid #e0d9cc;
  font-size: 12.5px;
  line-height: 1.4;
  color: #6b645c;
}
figure.tarjeta {
  flex: 0 0 auto;
  margin: 0;
  background: #fffcf7;
  border: 1px solid #e4dccf;
  border-radius: 14px;
  padding: 6px 10px 4px;
  display: flex;
  flex-direction: column;
}
.visual figure.tarjeta svg {
  width: 100%;
  height: 100%;
  max-height: none;
  aspect-ratio: auto;
}
.visual figcaption.eje { flex: 0 0 auto; margin: 4px 0 0; font-size: 13px; color: #605e5c; }
.lienzo [data-vista] {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  flex-direction: column;
}
.lienzo [data-vista][hidden] { display: none; }
.vacia {
  flex: 1 1 auto;
  display: flex;
  align-items: center;
  background: #fffcf7;
  border: 1px solid #e4dccf;
  border-radius: 14px;
  padding: 28px 32px;
}
.vacia p { margin: 0; max-width: 680px; font-size: 20px; font-weight: 650; line-height: 1.45; }
.filtro { flex: 0 0 auto; display: flex; flex-wrap: wrap; gap: 6px; margin: 0 0 8px; }
.filtro button {
  font: 13px/1 "Segoe UI", sans-serif;
  color: #1c1917;
  background: #fffcf7;
  border: 1px solid #d9d0c3;
  border-radius: 999px;
  padding: 7px 12px;
  cursor: pointer;
}
.filtro button[aria-pressed="true"] {
  background: #1c1917;
  color: #fffcf7;
  border-color: #1c1917;
}
nav {
  flex: 0 0 56px;
  display: flex;
  align-items: center;
  gap: 6px;
  padding: 0 12px;
  background: #1c1917;
  overflow: hidden;
}
nav button {
  flex: 0 0 auto;
  font: 13px/1 "Segoe UI", sans-serif;
  color: #f3efe6;
  background: transparent;
  border: 0;
  border-radius: 999px;
  padding: 8px 12px;
  cursor: pointer;
  white-space: nowrap;
}
nav button[aria-current="true"] { background: #f3efe6; color: #1c1917; }
.piramide {
  flex: 1 1 auto;
  min-height: 0;
  display: flex;
  align-items: flex-start;
  gap: 10px;
  overflow: hidden;
}
.columna {
  flex: 1 1 42%;
  min-width: 0;
  min-height: 0;
  display: flex;
  flex-direction: column;
  gap: 8px;
}
.piramide article {
  background: #fffcf7;
  border: 1px solid #e4dccf;
  border-radius: 12px;
  padding: 8px 12px;
  min-height: 0;
}
.piramide article.evidencia {
  flex: 1 1 58%;
  align-self: flex-start;
  overflow: hidden;
}
.piramide h2 {
  margin: 0 0 4px;
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.08em;
  text-transform: uppercase;
  color: #8a8175;
}
.piramide p { margin: 0; font-size: 13px; line-height: 1.35; white-space: pre-wrap; }
nav.pie {
  flex: 0 0 52px;
  background: #fff;
  border-top: 1px solid #edebe9;
  padding: 0 12px;
  gap: 4px;
  z-index: 5;
}
nav.pie button {
  color: #605e5c;
  background: transparent;
  border-radius: 2px;
  font-weight: 600;
}
nav.pie button[aria-current="page"] { background: #deecf9; color: #0b5cab; }
nav.pie .frase {
  flex: 1 1 auto;
  min-width: 0;
  margin: 0 8px;
  font-size: 13px;
  line-height: 1.3;
  color: #252423;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}
nav.pie #reproducir {
  margin-left: auto;
  color: #fff;
  background: #118dff;
  border-radius: 2px;
}
"""

_ENTEROS = re.compile(r"-?\d+")

_TEXTO = {
    "es": {
        "eje": "El eje arranca en cero.",
        "eje_resta": "El eje arranca en cero. Cada barra es la resta contra el período anterior.",
        "resto": "Resto",
        "neto": "El neto de las dos barras es {neto}.",
        "nivel": "En {cuando} lo que más pesa es {grupo}, {importe}.",
        "limpieza": (
            "La suma pelada arrancaba en {antes} y, después de las marcas, "
            "el total de los tres meses es {despues}."
        ),
        "marca": "La marca es {marca}, al lado de los {total} del mes. El día está marcado y no es la causa.",
        "fila": "una fila es {grano}",
        "entran": "entran las filas del período pedido",
        "por_precio": "el importe es unidades por precio",
        "columna": "el importe es la columna del match",
        "sin_importe": "el importe no está en el archivo",
        "sin_iva": (
            "no hay columna de IVA ni de devoluciones, así que la cifra es lo escrito en la fila"
        ),
        "no_cruza": "no se cruza otra lista",
        "cuenta_piezas": "{piezas} es {neto}, en el camino {camino}.",
        "mas": " más ",
        "corrientes": "En corrientes, {periodo} está {diferencia} de {anio}.",
        "constantes": "En pesos de {mes} está {lado}, {periodo} contra {anio}.",
        "abajo": "abajo",
        "arriba": "arriba",
        "cero": "0",
        "mismo": "en el mismo número",
        "nota": "Nota",
        "base": "Base",
        "camino": "Camino",
        "fuente": "Fuente",
        "vacia": "La hoja no se completa.",
        "falta": "Falta {dato}. Eso frena {frase}.",
        "evolucion": "Evolución",
        "piezas_titulo": "Piezas",
        "atributo": "Ventas por atributo",
        "cantidad": "Cantidad",
        "mezcla": "Mezcla",
        "precio_tramo": "Precio",
        "fecha": "Fecha",
        "todos": "Todos",
        "abrir": "Abrir",
        "reproducir": "Reproducir",
        "pausa": "Pausa",
        "seguir": "Seguir",
        "y": " y ",
        "historia_mes": (
            "En evolución, {periodo} facturó {total} contra {base} de {anterior}. "
            "La diferencia es {diferencia}."
        ),
        "historia_anio": "Contra {anio}, que facturó {base}, la diferencia es {diferencia}.",
        "historia_pieza": "En las piezas, {nombre} se lleva {resta}.",
        "historia_sigue_pieza": "{nombre} se lleva {resta}.",
        "historia_precio": "El {nombre} queda en {resta}.",
        "historia_neto": "El neto de las tres es {neto}.",
        "historia_grupo": "En ventas por {corte}, {nombre} queda en {importe}.",
        "historia_sigue": "{nombre} queda en {importe}.",
        "glosario": "Glosario",
        "volver": "Volver",
        "metricas": "Métricas",
        "atributos": "Atributos",
        "glosario_importe_precio": (
            "El importe de una fila es unidades por precio. Las métricas suman ese importe."
        ),
        "glosario_importe_columna": (
            "El importe de una fila es el de la columna del archivo. Las métricas suman ese importe."
        ),
        "glosario_importe_fila": "El importe es el que la fila ya trae. Las métricas suman ese importe.",
        "glosario_evolucion": (
            "Cada barra es la suma del importe de las filas de ese mes: {meses}. "
            "La diferencia contra el mes de al lado es {periodo} menos {anterior}."
        ),
        "glosario_anio": " La diferencia contra el año pasado es {periodo} menos {anio}.",
        "glosario_camino": "El camino escrito es {camino}. Se mueve una pieza por vez.",
        "glosario_cantidad": (
            "La cantidad estira las unidades de {anterior} con la mezcla y los precios de {anterior}. "
            "El tramo es esa cuenta menos el importe de {anterior}."
        ),
        "glosario_mezcla": (
            "La mezcla toma las unidades de {periodo} y les pone el precio de {anterior}. "
            "En cada grupo, ese precio es el importe de {anterior} dividido sus unidades. "
            "El tramo es esa cuenta menos la de la cantidad."
        ),
        "glosario_precio": (
            "El precio usa el importe de {periodo}. El tramo es ese importe menos la cuenta de la mezcla."
        ),
        "glosario_neto": (
            "El neto es el importe de {periodo} menos el importe de {anterior}. "
            "Las tres piezas suman ese neto. Una pieza no es una causa."
        ),
        "glosario_vacia": "No se arma: {motivo}",
        "glosario_corte": (
            "El corte se eligió antes de mirar: {corte}. "
            "Cada barra es la suma del importe de ese {corte} en {periodo}. "
            "No es la resta contra {anterior}."
        ),
        "glosario_fecha": (
            "Se abre por año, después por mes, después por día. El día es un día de apertura. {regla} "
            "Elegir un año, un mes o un día deja brillando las barras de ese recorte. No vuelve a sumar."
        ),
        "glosario_fecha_dias": (
            "Se abre por año, después por mes, después por día. "
            "El día es cada día del mes que está en el gráfico. "
            "Elegir uno deja brillando las barras de ese recorte. No vuelve a sumar."
        ),
        "glosario_filtro": (
            "Lista los valores de {corte}. Elegir uno deja brillando esa barra. "
            "Las otras siguen en el gráfico, más tenues. No vuelve a sumar."
        ),
        "glosario_redondeo": "La cuenta está redondeada a la unidad.",
        "importe_titulo": "Importe",
        "neto_titulo": "Neto",
        "tablero": "Tablero",
        "tarjeta_facturo": "Facturó",
        "tarjeta_contra": "Contra {cuando}",
        "tarjeta_de": "{cuando} facturó {importe}",
        "informe": "Informe",
        "informe_leer": (
            "Cada hallazgo dice tres cosas: el número, de dónde sale y qué no dice. "
            "Los números son los de las cuentas ya cerradas. Este texto no vuelve a sumar."
        ),
        "informe_agosto": "{periodo} facturó {total}. {anterior} facturó {base}. {periodo} está {diferencia} de {anterior}.",
        "informe_agosto_lee": (
            "Eso sale de restar los dos importes. Es la comparación contra el mes de al lado. No dice la causa."
        ),
        "informe_anio": "{anio} facturó {base}. {periodo} está {diferencia} de {anio}.",
        "informe_juntas": (
            "Las dos comparaciones se leen juntas. {periodo} está {dif_mes} de {anterior} "
            "y {dif_anio} de {anio}. Con una sola no se puede decir que el mes fue malo, ni que fue bueno."
        ),
        "informe_piezas_titulo": "De dónde sale la diferencia contra {anterior}",
        "informe_piezas": (
            "Esa diferencia, {neto}, se parte en tres piezas. El camino escrito es {camino}. "
            "Se mueve una pieza por vez."
        ),
        "informe_cantidad": (
            "La cantidad se lleva {resta}. Son las unidades de {periodo}, "
            "medidas con la mezcla y los precios de {anterior}."
        ),
        "informe_mezcla": (
            "La mezcla se lleva {resta}. Cambió el peso de cada grupo. "
            "El precio de cada grupo se deja en el de {anterior}."
        ),
        "informe_precio_cero": "El precio queda en 0. El precio de {periodo} no mueve esta diferencia.",
        "informe_precio": "El precio se lleva {resta}. Es el importe de {periodo} menos la cuenta de la mezcla.",
        "informe_pieza_grande": (
            "La pieza grande es {nombre}, con {resta}. No es la causa. "
            "Otro camino les cambiaría el tamaño a las piezas. "
            "Las tres juntas siguen sumando la diferencia."
        ),
        "informe_niveles": "En el gráfico, cada barra es lo facturado en {periodo}, no la baja: {lista}.",
        "informe_restas": "La resta de cada {corte} contra {anterior} es otra cuenta: {lista}.",
        "informe_aparta": (
            "{grupo} se lleva {importe}. El resto, junto, se lleva {resto}. "
            "El corte {corte} se eligió antes de mirar. Que {grupo} se lleve esa resta no quiere decir que sea la causa."
        ),
        "informe_persona": "El corte no entra en el informe: el grupo parece una persona.",
        "informe_calendario_titulo": "El día marcado",
        "informe_calendario": (
            "La marca es {marca}: un día al ritmo de {anterior}. "
            "Esos días de {anterior} facturaron {base}. El día marcado: {dia}."
        ),
        "informe_calendario_lee": (
            "El día queda marcado al lado del total. No es la causa del mes. "
            "La marca es {marca} y la diferencia contra {anterior} es {diferencia}. "
            "La marca no es esa diferencia."
        ),
        "informe_queda_titulo": "Lo que queda después del costo",
        "informe_queda": (
            "Después del costo que viaja con la venta, {periodo} deja {queda} y {anterior} deja {base}."
        ),
        "informe_queda_menos": "{periodo} deja menos que {anterior}.",
        "informe_queda_mas": "{periodo} deja más que {anterior}.",
        "informe_queda_igual": "{periodo} deja lo mismo que {anterior}.",
        "informe_queda_lee": (
            "Esa cuenta solo resta el costo que está en la fila. "
            "No es el margen del negocio si faltan costos que no viajan con la venta."
        ),
        "informe_pesos_titulo": "Los mismos meses en pesos de {mes}",
        "informe_pesos": (
            "En pesos de {mes}, {periodo} queda en {actual} y {anio} queda en {base}. "
            "Cada mes se multiplica por el índice de {mes} y se divide por el índice de ese mes. "
            "La fuente es {fuente}."
        ),
        "informe_vacia": "{nombre} no se arma. {motivo}",
        "informe_conclusion": "Conclusión",
        "informe_conclusion_juntas": (
            "{periodo} está {dif_mes} de {anterior} y {dif_anio} de {anio}. Esas dos frases van juntas."
        ),
        "informe_conclusion_pieza": (
            "La diferencia contra {anterior} aparece sobre todo en {pieza} y, en el corte {corte}, en {grupo}. "
            "Eso describe el mes."
        ),
        "informe_no_separa": "La tabla no separa la causa. Describe el mes contra {anterior} y contra {anio}.",
        "informe_firma": "Este archivo no alcanza para firmar una compra.",
        "informe_vacio": "Esta pantalla no cierra un hallazgo de facturación.",
    },
    "en": {
        "eje": "The axis starts at zero.",
        "eje_resta": "The axis starts at zero. Each bar is the subtraction against the previous period.",
        "resto": "Rest",
        "neto": "The net of the two bars is {neto}.",
        "nivel": "In {cuando} what weighs most is {grupo}, {importe}.",
        "limpieza": "The raw sum started at {antes} and, after the marks, the total is {despues}.",
        "marca": "The mark is {marca}, beside the {total} of the month. The day is marked and is not the cause.",
        "fila": "a row is {grano}",
        "entran": "the rows of the requested period enter",
        "por_precio": "the amount is units times price",
        "columna": "the amount is the matched column",
        "sin_importe": "the amount is not in the file",
        "sin_iva": "there is no VAT or refund column, so the figure is what the row says",
        "no_cruza": "no other list is joined",
        "cuenta_piezas": "{piezas} is {neto}, on the path {camino}.",
        "mas": " plus ",
        "corrientes": "In current prices, {periodo} is {diferencia} from {anio}.",
        "constantes": "In prices of {mes} it is {lado}, {periodo} against {anio}.",
        "abajo": "down",
        "arriba": "up",
        "cero": "0",
        "mismo": "the same number",
        "nota": "Note",
        "base": "Base",
        "camino": "Path",
        "fuente": "Source",
        "vacia": "The sheet is not completed.",
        "falta": "Missing {dato}. This stops {frase}.",
        "evolucion": "Trend",
        "piezas_titulo": "Pieces",
        "atributo": "Sales by attribute",
        "cantidad": "Quantity",
        "mezcla": "Mix",
        "precio_tramo": "Price",
        "fecha": "Date",
        "todos": "All",
        "abrir": "Open",
        "reproducir": "Play",
        "pausa": "Pause",
        "seguir": "Resume",
        "y": " and ",
        "historia_mes": (
            "In the trend, {periodo} billed {total} against {base} in {anterior}. "
            "The difference is {diferencia}."
        ),
        "historia_anio": "Against {anio}, which billed {base}, the difference is {diferencia}.",
        "historia_pieza": "In the pieces, {nombre} takes {resta}.",
        "historia_sigue_pieza": "{nombre} takes {resta}.",
        "historia_precio": "{nombre} stays at {resta}.",
        "historia_neto": "The net of the three is {neto}.",
        "historia_grupo": "In sales by {corte}, {nombre} stays at {importe}.",
        "historia_sigue": "{nombre} stays at {importe}.",
        "glosario": "Glossary",
        "volver": "Back",
        "metricas": "Metrics",
        "atributos": "Attributes",
        "glosario_importe_precio": "A row amount is units times price. The metrics add that amount.",
        "glosario_importe_columna": (
            "A row amount is the amount column in the file. The metrics add that amount."
        ),
        "glosario_importe_fila": "The amount is what the row already carries. The metrics add that amount.",
        "glosario_evolucion": (
            "Each bar is the sum of the row amounts in that month: {meses}. "
            "The difference against the month beside it is {periodo} minus {anterior}."
        ),
        "glosario_anio": " The difference against last year is {periodo} minus {anio}.",
        "glosario_camino": "The written path is {camino}. One piece moves at a time.",
        "glosario_cantidad": (
            "Quantity stretches the units of {anterior} with the mix and prices of {anterior}. "
            "The piece is that account minus the amount of {anterior}."
        ),
        "glosario_mezcla": (
            "Mix takes the units of {periodo} and gives them the price of {anterior}. "
            "In each group, that price is the amount of {anterior} divided by its units. "
            "The piece is that account minus the quantity account."
        ),
        "glosario_precio": (
            "Price uses the amount of {periodo}. The piece is that amount minus the mix account."
        ),
        "glosario_neto": (
            "The net is the amount of {periodo} minus the amount of {anterior}. "
            "The three pieces add up to that net. A piece is not a cause."
        ),
        "glosario_vacia": "It is not built: {motivo}",
        "glosario_corte": (
            "The cut was chosen before looking: {corte}. "
            "Each bar is the sum of that {corte} in {periodo}. "
            "It is not the subtraction against {anterior}."
        ),
        "glosario_fecha": (
            "It opens by year, then month, then day. A day is an opening day. {regla} "
            "Choosing a year, a month or a day leaves the bars of that cut bright. It does not add again."
        ),
        "glosario_fecha_dias": (
            "It opens by year, then month, then day. "
            "A day is each day of the month drawn on the chart. "
            "Choosing one leaves the bars of that cut bright. It does not add again."
        ),
        "glosario_filtro": (
            "It lists the values of {corte}. Choosing one leaves that bar bright. "
            "The others stay on the chart, dimmer. It does not add again."
        ),
        "glosario_redondeo": "The account is rounded to the unit.",
        "importe_titulo": "Amount",
        "neto_titulo": "Net",
        "tablero": "Board",
        "tarjeta_facturo": "Billed",
        "tarjeta_contra": "Against {cuando}",
        "tarjeta_de": "{cuando} billed {importe}",
        "informe": "Report",
        "informe_leer": (
            "Each finding says three things: the number, where it comes from, and what it does not say. "
            "The numbers are the ones the accounts already closed. This text does not add again."
        ),
        "informe_agosto": "{periodo} billed {total}. {anterior} billed {base}. {periodo} is {diferencia} from {anterior}.",
        "informe_agosto_lee": (
            "That comes from subtracting the two amounts. It is the comparison against the month beside it. "
            "It does not say the cause."
        ),
        "informe_anio": "{anio} billed {base}. {periodo} is {diferencia} from {anio}.",
        "informe_juntas": (
            "The two comparisons are read together. {periodo} is {dif_mes} from {anterior} "
            "and {dif_anio} from {anio}. One of them alone cannot say the month was bad, or that it was good."
        ),
        "informe_piezas_titulo": "Where the difference against {anterior} comes from",
        "informe_piezas": (
            "That difference, {neto}, splits into three pieces. The written path is {camino}. "
            "One piece moves at a time."
        ),
        "informe_cantidad": (
            "Quantity takes {resta}. Those are the units of {periodo}, "
            "measured with the mix and the prices of {anterior}."
        ),
        "informe_mezcla": (
            "Mix takes {resta}. The weight of each group changed. "
            "Each group's price stays at the price of {anterior}."
        ),
        "informe_precio_cero": "Price stays at 0. The price of {periodo} does not move this difference.",
        "informe_precio": "Price takes {resta}. It is the amount of {periodo} minus the mix account.",
        "informe_pieza_grande": (
            "The large piece is {nombre}, at {resta}. It is not the cause. "
            "Another path would change the size of the pieces. "
            "The three together still add up to the difference."
        ),
        "informe_niveles": "On the chart, each bar is what was billed in {periodo}, not the drop: {lista}.",
        "informe_restas": "The subtraction of each {corte} against {anterior} is another account: {lista}.",
        "informe_aparta": (
            "{grupo} carries {importe}. The rest, together, carries {resto}. "
            "The cut {corte} was chosen before looking. "
            "That {grupo} carries that subtraction does not mean it is the cause."
        ),
        "informe_persona": "The cut does not enter the report: the group looks like a person.",
        "informe_calendario_titulo": "The marked day",
        "informe_calendario": (
            "The mark is {marca}: one day at the pace of {anterior}. "
            "Those days of {anterior} billed {base}. The marked day: {dia}."
        ),
        "informe_calendario_lee": (
            "The day is marked beside the total. It is not the cause of the month. "
            "The mark is {marca} and the difference against {anterior} is {diferencia}. "
            "The mark is not that difference."
        ),
        "informe_queda_titulo": "What remains after cost",
        "informe_queda": (
            "After the cost that travels with the sale, {periodo} leaves {queda} and {anterior} leaves {base}."
        ),
        "informe_queda_menos": "{periodo} leaves less than {anterior}.",
        "informe_queda_mas": "{periodo} leaves more than {anterior}.",
        "informe_queda_igual": "{periodo} leaves the same as {anterior}.",
        "informe_queda_lee": (
            "That account only subtracts the cost that is on the row. "
            "It is not the margin of the business if costs that do not travel with the sale are missing."
        ),
        "informe_pesos_titulo": "The same months in prices of {mes}",
        "informe_pesos": (
            "In prices of {mes}, {periodo} stands at {actual} and {anio} stands at {base}. "
            "Each month is multiplied by the index of {mes} and divided by that month's index. "
            "The source is {fuente}."
        ),
        "informe_vacia": "{nombre} is not built. {motivo}",
        "informe_conclusion": "Conclusion",
        "informe_conclusion_juntas": (
            "{periodo} is {dif_mes} from {anterior} and {dif_anio} from {anio}. Those two sentences go together."
        ),
        "informe_conclusion_pieza": (
            "The difference against {anterior} shows up mainly in {pieza} and, on the {corte} cut, in {grupo}. "
            "That describes the month."
        ),
        "informe_no_separa": "The table does not separate the cause. It describes the month against {anterior} and against {anio}.",
        "informe_firma": "This file does not suffice to sign a purchase.",
        "informe_vacio": "This screen does not close a billing finding.",
    },
}


def escribir(
    resultado: Resultado,
    nota: NotaLista,
    instruccion: Instruccion,
    titulo: str,
    encargo: Encargo | None = None,
    vacios: tuple[HuecoVacio, ...] = (),
) -> str:
    if resultado.detenido:
        raise ValueError(resultado.detenido)
    idioma = encargo.idioma if encargo else "es"
    cuerpo = _tablero(resultado, instruccion, idioma, titulo, encargo, nota)
    return f"""<!DOCTYPE html>
<html lang="{idioma}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(titulo)}</title>
<style>
{_ESTILO}
</style>
</head>
<body>
{cuerpo}
<script>
function cerrarPaneles(excepto) {{
  var abiertos = document.querySelectorAll(".disparador[aria-expanded='true']");
  for (var i = 0; i < abiertos.length; i++) {{
    if (abiertos[i] === excepto) {{
      continue;
    }}
    abiertos[i].setAttribute("aria-expanded", "false");
    abiertos[i].parentNode.querySelector(".panel").hidden = true;
  }}
}}
document.addEventListener("click", function (evento) {{
  var caja = evento.target.closest ? evento.target.closest(".caja") : null;
  cerrarPaneles(caja ? caja.querySelector(".disparador") : null);
}});
var filtros = document.querySelectorAll(".slicer");
for (var i = 0; i < filtros.length; i++) {{
  filtros[i].querySelector(".disparador").addEventListener("click", function () {{
    var abierto = this.getAttribute("aria-expanded") === "true";
    cerrarPaneles(this);
    this.setAttribute("aria-expanded", abierto ? "false" : "true");
    this.parentNode.querySelector(".panel").hidden = abierto;
  }});
  var ramas = filtros[i].querySelectorAll(".abrir");
  for (var r = 0; r < ramas.length; r++) {{
    ramas[r].addEventListener("click", function (evento) {{
      evento.stopPropagation();
      var hijos = this.parentNode.querySelector(".hijos");
      var abierto = this.getAttribute("aria-expanded") === "true";
      this.setAttribute("aria-expanded", abierto ? "false" : "true");
      if (hijos) {{
        hijos.hidden = abierto;
      }}
    }});
  }}
  var opciones = filtros[i].querySelectorAll(".opcion");
  for (var b = 0; b < opciones.length; b++) {{
    opciones[b].addEventListener("click", function () {{
      var filtro = this.closest(".slicer");
      var clave = filtro.getAttribute("data-filtro");
      var valor = this.getAttribute("data-valor");
      var anio = this.getAttribute("data-anio") || "";
      var mes = this.getAttribute("data-mes") || "";
      var dia = this.getAttribute("data-dia") || "";
      var hermanos = filtro.querySelectorAll(".opcion");
      for (var k = 0; k < hermanos.length; k++) {{
        hermanos[k].setAttribute("aria-pressed", hermanos[k] === this ? "true" : "false");
      }}
      filtro.querySelector(".elegido").textContent = this.getAttribute("data-rotulo");
      var grupos = document.querySelectorAll("[data-marca]");
      for (var g = 0; g < grupos.length; g++) {{
        if (grupos[g].getAttribute("data-marca") !== clave) {{
          continue;
        }}
        var sigue = false;
        if (valor === "*") {{
          sigue = true;
        }} else if (clave === "fecha") {{
          var ga = grupos[g].getAttribute("data-anio") || "";
          var gm = grupos[g].getAttribute("data-mes") || "";
          var gd = grupos[g].getAttribute("data-dia") || "";
          sigue = ga === anio && (mes === "" || gm === mes) && (dia === "" || gd === "" || gd === dia);
        }} else {{
          sigue = grupos[g].getAttribute("data-valor") === valor;
        }}
        grupos[g].setAttribute("opacity", sigue ? "1" : "0.28");
      }}
      cerrarPaneles(null);
    }});
  }}
}}
var historia = document.getElementById("historia");
var botonHistoria = document.getElementById("reproducir");
if (historia && botonHistoria) {{
  var pasos = JSON.parse(historia.textContent);
  var indiceHistoria = 0;
  var timerHistoria = null;
  var enCurso = false;
  function ponerFiltro(clave, valor, rotulo) {{
    var slicers = document.querySelectorAll(".slicer");
    for (var i = 0; i < slicers.length; i++) {{
      var es = clave && slicers[i].getAttribute("data-filtro") === clave;
      var opciones = slicers[i].querySelectorAll(".opcion");
      var elegido = slicers[i].querySelector(".elegido");
      if (!es) {{
        for (var k = 0; k < opciones.length; k++) {{
          opciones[k].setAttribute(
            "aria-pressed",
            opciones[k].getAttribute("data-valor") === "*" ? "true" : "false"
          );
        }}
        var todos = slicers[i].querySelector('.opcion[data-valor="*"]');
        if (elegido && todos) {{
          elegido.textContent = todos.getAttribute("data-rotulo");
        }}
        continue;
      }}
      for (var j = 0; j < opciones.length; j++) {{
        var coincide = valor !== "" && opciones[j].getAttribute("data-valor") === valor;
        opciones[j].setAttribute("aria-pressed", coincide ? "true" : "false");
      }}
      if (elegido) {{
        elegido.textContent = rotulo;
      }}
    }}
  }}
  function mostrarPaso(paso) {{
    var grupos = document.querySelectorAll("[data-marca]");
    for (var g = 0; g < grupos.length; g++) {{
      if (grupos[g].getAttribute("data-marca") !== paso.marca) {{
        grupos[g].setAttribute("opacity", "1");
        continue;
      }}
      var sigue = paso.valores.indexOf(grupos[g].getAttribute("data-valor")) !== -1;
      grupos[g].setAttribute("opacity", sigue ? "1" : "0.28");
    }}
    var cartas = document.querySelectorAll(".visual");
    for (var c = 0; c < cartas.length; c++) {{
      cartas[c].classList.toggle("contando", cartas[c].getAttribute("data-grafico") === paso.grafico);
    }}
    var hallazgos = document.querySelectorAll(".hallazgo");
    for (var h = 0; h < hallazgos.length; h++) {{
      hallazgos[h].classList.toggle(
        "contando",
        paso.hallazgo && hallazgos[h].getAttribute("data-hallazgo") === paso.hallazgo
      );
    }}
    ponerFiltro(paso.filtro, paso.valor, paso.rotulo);
    document.querySelector(".frase").textContent = paso.frase;
  }}
  function tickHistoria() {{
    if (indiceHistoria >= pasos.length) {{
      pararHistoria(true);
      return;
    }}
    mostrarPaso(pasos[indiceHistoria]);
    indiceHistoria += 1;
    botonHistoria.textContent = botonHistoria.getAttribute("data-pausa");
    enCurso = true;
  }}
  function pararHistoria(termino) {{
    if (timerHistoria) {{
      clearInterval(timerHistoria);
      timerHistoria = null;
    }}
    enCurso = false;
    botonHistoria.textContent = botonHistoria.getAttribute(termino ? "data-reproducir" : "data-seguir");
  }}
  botonHistoria.addEventListener("click", function () {{
    cerrarVista();
    if (enCurso) {{
      pararHistoria(false);
      return;
    }}
    if (indiceHistoria >= pasos.length) {{
      indiceHistoria = 0;
    }}
    tickHistoria();
    timerHistoria = setInterval(tickHistoria, 4000);
  }});
}}
var abrirGlosario = document.getElementById("abrir-glosario");
var abrirInforme = document.getElementById("abrir-informe");
function pausarSiCorre() {{
  var play = document.getElementById("reproducir");
  if (play && play.textContent === play.getAttribute("data-pausa")) {{
    play.click();
  }}
}}
function marcarPie(id) {{
  var botones = document.querySelectorAll("nav.pie button[data-vista]");
  for (var i = 0; i < botones.length; i++) {{
    if (botones[i].id === id) {{
      botones[i].setAttribute("aria-current", "page");
    }} else {{
      botones[i].removeAttribute("aria-current");
    }}
  }}
}}
function abrirVista(clase, id) {{
  pausarSiCorre();
  document.body.classList.remove("en-glosario", "en-informe");
  document.body.classList.add(clase);
  marcarPie(id);
}}
function cerrarVista() {{
  document.body.classList.remove("en-glosario", "en-informe");
  marcarPie("abrir-tablero");
}}
var abrirTablero = document.getElementById("abrir-tablero");
if (abrirTablero) {{
  abrirTablero.addEventListener("click", cerrarVista);
}}
if (abrirGlosario) {{
  abrirGlosario.addEventListener("click", function () {{ abrirVista("en-glosario", "abrir-glosario"); }});
}}
if (abrirInforme) {{
  abrirInforme.addEventListener("click", function () {{ abrirVista("en-informe", "abrir-informe"); }});
}}
var cierres = document.querySelectorAll(".cerrar");
for (var i = 0; i < cierres.length; i++) {{
  cierres[i].addEventListener("click", cerrarVista);
}}
</script>
</body>
</html>
"""


def guardar(camino: Path, pagina: str) -> None:
    camino.write_text(pagina, encoding="utf-8")


def _tablero(
    resultado: Resultado,
    instruccion: Instruccion,
    idioma: str,
    titulo: str,
    encargo: Encargo | None,
    nota: NotaLista,
) -> str:
    texto = _TEXTO[idioma]
    serie_tiempo = _serie_evolucion(resultado, instruccion, idioma)
    periodos = _periodos_en_evolucion(resultado, instruccion)
    corte, serie_grupos = _serie_atributo(resultado)
    filtros = []
    if serie_tiempo:
        filtros.append(
            _slicer_fecha(
                "fecha",
                texto["fecha"],
                periodos,
                instruccion.calendario,
                idioma,
                texto["todos"],
                texto["abrir"],
            )
        )
    if corte and serie_grupos:
        filtros.append(
            _slicer(corte, _rotulo(corte), [nombre for nombre, _ in serie_grupos], texto["todos"])
        )
    monitoreo = _completa(resultado, "monitoreo")
    marca = ""
    if monitoreo and "diferencia" in monitoreo.huecos:
        marca = f' data-diferencia="{monitoreo.huecos["diferencia"]}"'
    graficos = [
        _visual(
            "evolucion",
            texto["evolucion"],
            _dibujo(
                serie_tiempo,
                texto["eje"],
                "fecha",
                ancho=1280,
                alto=280,
                datos=[_datos_fecha(periodo) for periodo in periodos],
                rotulos=[_eje_corto(periodo, idioma) for periodo in periodos]
                if len(periodos) > 6
                else None,
            ),
            marca,
            "ancho",
        ),
        _visual(
            "piezas",
            texto["piezas_titulo"],
            _dibujo(_serie_piezas(resultado, idioma), texto["eje"], "pieza"),
        ),
        _visual("atributo", texto["atributo"], _dibujo(serie_grupos, texto["eje"], corte)),
    ]
    hojas = "\n".join(graficos)
    pasos = _pasos(resultado, instruccion, idioma, periodos, corte, serie_grupos)
    hallazgos = _hallazgos(resultado, instruccion, idioma)
    return (
        f'<header class="cabezal"><h1>{html.escape(titulo)}</h1></header>\n'
        f'<div class="escena"><aside class="costado"><div class="barra">{"".join(filtros)}</div></aside>'
        f'<div class="lienzo">{hallazgos}'
        f'<main class="reporte">\n{hojas}\n</main></div></div>\n'
        f"{_glosario(resultado, instruccion, encargo, idioma, periodos, corte, serie_grupos)}\n"
        f"{_informe(resultado, instruccion, idioma, nota, corte, serie_grupos)}\n"
        f"{_controles(pasos, texto)}"
    )


def _hallazgos(resultado: Resultado, instruccion: Instruccion, idioma: str) -> str:
    texto = _TEXTO[idioma]
    monitoreo = _completa(resultado, "monitoreo")
    if monitoreo is None:
        return ""
    actual = _cuando(instruccion.periodo, idioma)
    anterior = _cuando(instruccion.periodo_anterior, idioma)
    tarjetas = [
        _hallazgo(
            "nivel",
            "total",
            _capital(actual),
            _pesos(monitoreo.huecos["total"]),
            texto["tarjeta_facturo"],
        ),
        _hallazgo(
            _sentido(monitoreo.huecos["diferencia"]),
            "mes",
            texto["tarjeta_contra"].format(cuando=_capital(anterior)),
            _como_resta(monitoreo.huecos["diferencia"], idioma),
            texto["tarjeta_de"].format(
                cuando=_capital(anterior), importe=_pesos(monitoreo.huecos["total_base"])
            ),
        ),
    ]
    anio = _completa(resultado, "anio_pasado")
    if anio is not None:
        nombre = _cuando(instruccion.anio_pasado, idioma)
        tarjetas.append(
            _hallazgo(
                _sentido(anio.huecos["diferencia"]),
                "anio",
                texto["tarjeta_contra"].format(cuando=_capital(nombre)),
                _como_resta(anio.huecos["diferencia"], idioma),
                texto["tarjeta_de"].format(cuando=_capital(nombre), importe=_pesos(anio.huecos["total_base"])),
            )
        )
    return f'<div class="hallazgos">{"".join(tarjetas)}</div>'


def _hallazgo(clase: str, clave: str, rotulo: str, cifra: str, pista: str) -> str:
    return (
        f'<article class="hallazgo {clase}" data-hallazgo="{html.escape(clave)}">'
        f'<p class="rotulo">{html.escape(rotulo)}</p>'
        f'<p class="cifra">{html.escape(cifra)}</p>'
        f'<p class="pista">{html.escape(pista)}</p></article>'
    )


def _sentido(valor: int) -> str:
    if valor < 0:
        return "baja"
    if valor > 0:
        return "sube"
    return "igual"


def _capital(texto: str) -> str:
    if not texto:
        return texto
    return texto[0].upper() + texto[1:]


def _controles(pasos: list[dict], texto: dict[str, str]) -> str:
    play = ""
    historia = ""
    frase = ""
    if pasos:
        play = (
            f'<button type="button" id="reproducir" '
            f'data-reproducir="{html.escape(texto["reproducir"])}" '
            f'data-pausa="{html.escape(texto["pausa"])}" '
            f'data-seguir="{html.escape(texto["seguir"])}">'
            f'{html.escape(texto["reproducir"])}</button>'
        )
        frase = '<p class="frase"></p>'
        datos = json.dumps(pasos, ensure_ascii=False).replace("<", "\\u003c")
        historia = f'<script type="application/json" id="historia">{datos}</script>'
    return (
        f'<nav class="pie">'
        f'<button type="button" id="abrir-tablero" data-vista="tablero" aria-current="page">'
        f'{html.escape(texto["tablero"])}</button>'
        f'<button type="button" id="abrir-informe" data-vista="informe">'
        f'{html.escape(texto["informe"])}</button>'
        f'<button type="button" id="abrir-glosario" data-vista="glosario">'
        f'{html.escape(texto["glosario"])}</button>'
        f"{frase}{play}</nav>{historia}"
    )


def _glosario(
    resultado: Resultado,
    instruccion: Instruccion,
    encargo: Encargo | None,
    idioma: str,
    periodos: list,
    corte: str | None,
    serie_grupos: list[tuple[str, int]] | None,
) -> str:
    texto = _TEXTO[idioma]
    metricas = [_termino(texto["importe_titulo"], _texto_importe(encargo, texto))]
    monitoreo = _completa(resultado, "monitoreo")
    if monitoreo is not None and periodos:
        actual = _cuando(instruccion.periodo, idioma)
        anterior = _cuando(instruccion.periodo_anterior, idioma)
        meses = ", ".join(_cuando(periodo, idioma) for periodo in periodos)
        frase = texto["glosario_evolucion"].format(meses=meses, periodo=actual, anterior=anterior)
        anio = _completa(resultado, "anio_pasado")
        if anio is not None:
            frase += texto["glosario_anio"].format(
                periodo=actual, anio=_cuando(instruccion.anio_pasado, idioma)
            )
        frase += " " + texto["eje"]
        metricas.append(_termino(texto["evolucion"], frase))
    piezas = _ficha_de(resultado, "piezas")
    if piezas is not None and piezas.estado == "vacia":
        metricas.append(_termino(texto["piezas_titulo"], texto["glosario_vacia"].format(motivo=piezas.motivo or "")))
    elif piezas is not None and piezas.estado == "completa":
        actual = _cuando(instruccion.periodo, idioma)
        anterior = _cuando(instruccion.periodo_anterior, idioma)
        camino = piezas.huecos.get("camino") or ", ".join(instruccion.camino)
        nota = ""
        if piezas.huecos.get("redondeado"):
            nota = " " + texto["glosario_redondeo"]
        metricas.append(
            _termino(
                texto["cantidad"],
                texto["glosario_camino"].format(camino=camino)
                + " "
                + texto["glosario_cantidad"].format(anterior=anterior)
                + nota,
            )
        )
        metricas.append(_termino(texto["mezcla"], texto["glosario_mezcla"].format(periodo=actual, anterior=anterior)))
        metricas.append(_termino(texto["precio_tramo"], texto["glosario_precio"].format(periodo=actual)))
        metricas.append(
            _termino(texto["neto_titulo"], texto["glosario_neto"].format(periodo=actual, anterior=anterior))
        )
    if corte and serie_grupos:
        actual = _cuando(instruccion.periodo, idioma)
        anterior = _cuando(instruccion.periodo_anterior, idioma)
        metricas.append(
            _termino(
                texto["atributo"],
                texto["glosario_corte"].format(corte=corte, periodo=actual, anterior=anterior),
            )
        )
    atributos = []
    if periodos:
        if instruccion.calendario is not None:
            frase = texto["glosario_fecha"].format(regla=instruccion.calendario.texto)
        else:
            frase = texto["glosario_fecha_dias"]
        atributos.append(_termino(texto["fecha"], frase))
    if corte and serie_grupos:
        atributos.append(_termino(_rotulo(corte), texto["glosario_filtro"].format(corte=corte)))
    grupos = f"<h3>{html.escape(texto['metricas'])}</h3>{''.join(metricas)}"
    if atributos:
        grupos += f"<h3>{html.escape(texto['atributos'])}</h3>{''.join(atributos)}"
    return (
        f'<section class="glosario">'
        f'<button type="button" class="cerrar" id="volver">{html.escape(texto["volver"])}</button>'
        f"<h2>{html.escape(texto['glosario'])}</h2>{grupos}</section>"
    )


def _texto_importe(encargo: Encargo | None, texto: dict[str, str]) -> str:
    if encargo is None:
        return texto["glosario_importe_fila"]
    if encargo.importe_sale_de_unidades_por_precio:
        return texto["glosario_importe_precio"]
    if encargo.columna("importe"):
        return texto["glosario_importe_columna"]
    return texto["glosario_importe_fila"]


def _termino(titulo: str, cuerpo: str) -> str:
    return f"<article><h4>{html.escape(titulo)}</h4><p>{html.escape(cuerpo)}</p></article>"


def _ficha_de(resultado: Resultado, hoja_id: str) -> Ficha | None:
    try:
        return resultado.ficha(hoja_id)
    except KeyError:
        return None


def _informe(
    resultado: Resultado,
    instruccion: Instruccion,
    idioma: str,
    nota: NotaLista,
    corte: str | None,
    serie_grupos: list[tuple[str, int]] | None,
) -> str:
    texto = _TEXTO[idioma]
    actual = _cuando(instruccion.periodo, idioma)
    anterior = _cuando(instruccion.periodo_anterior, idioma)
    articulos: list[str] = []
    conclusion: list[str] = []
    monitoreo = _completa(resultado, "monitoreo")
    anio = _completa(resultado, "anio_pasado")
    if monitoreo is None:
        articulos.append(f"<p>{html.escape(texto['informe_vacio'])}</p>")
    else:
        dif_mes = _como_resta(monitoreo.huecos["diferencia"], idioma)
        articulos.append(
            _bloque(
                f"{_frase(actual)} / {_frase(anterior)}",
                [
                    texto["informe_agosto"].format(
                        periodo=actual,
                        total=_pesos(monitoreo.huecos["total"]),
                        anterior=anterior,
                        base=_pesos(monitoreo.huecos["total_base"]),
                        diferencia=dif_mes,
                    ),
                    texto["informe_agosto_lee"],
                ],
            )
        )
        dif_anio = ""
        nombre_anio = ""
        if anio is not None:
            nombre_anio = _cuando(instruccion.anio_pasado, idioma)
            dif_anio = _como_resta(anio.huecos["diferencia"], idioma)
            articulos.append(
                _bloque(
                    f"{_frase(actual)} / {_frase(nombre_anio)}",
                    [
                        texto["informe_anio"].format(
                            anio=nombre_anio,
                            base=_pesos(anio.huecos["total_base"]),
                            periodo=actual,
                            diferencia=dif_anio,
                        ),
                        texto["informe_juntas"].format(
                            periodo=actual,
                            dif_mes=dif_mes,
                            anterior=anterior,
                            dif_anio=dif_anio,
                            anio=nombre_anio,
                        ),
                    ],
                )
            )
            conclusion.append(
                texto["informe_conclusion_juntas"].format(
                    periodo=actual,
                    dif_mes=dif_mes,
                    anterior=anterior,
                    dif_anio=dif_anio,
                    anio=nombre_anio,
                )
            )
        pieza_grande = ""
        piezas = _completa(resultado, "piezas")
        if piezas is not None:
            tramo = piezas.huecos["tramo_de_cada_pieza"]
            nombres = [
                (texto["cantidad"], tramo["cantidad"], "cantidad"),
                (texto["mezcla"], tramo["mezcla"], "mezcla"),
                (texto["precio_tramo"], tramo["precio"], "precio"),
            ]
            parrafos = [
                texto["informe_piezas"].format(
                    neto=_como_resta(piezas.huecos["neto"], idioma),
                    camino=piezas.huecos.get("camino") or ", ".join(instruccion.camino),
                ),
                texto["informe_cantidad"].format(
                    resta=_como_resta(tramo["cantidad"], idioma),
                    periodo=actual,
                    anterior=anterior,
                ),
                texto["informe_mezcla"].format(
                    resta=_como_resta(tramo["mezcla"], idioma),
                    anterior=anterior,
                ),
            ]
            if tramo["precio"] == 0:
                parrafos.append(texto["informe_precio_cero"].format(periodo=actual))
            else:
                parrafos.append(
                    texto["informe_precio"].format(
                        resta=_como_resta(tramo["precio"], idioma),
                        periodo=actual,
                    )
                )
            grande = max(nombres, key=lambda item: abs(item[1]))
            pieza_grande = grande[0]
            parrafos.append(
                texto["informe_pieza_grande"].format(
                    nombre=grande[0],
                    resta=_como_resta(grande[1], idioma) if grande[1] else _pesos(0),
                )
            )
            articulos.append(_bloque(texto["informe_piezas_titulo"].format(anterior=anterior), parrafos))
        grupo_nombre = ""
        aparta = _completa(resultado, "el_que_se_aparta")
        if aparta is not None and _grupos_son_personas(aparta):
            articulos.append(_bloque(texto["atributo"], [texto["informe_persona"]]))
        elif corte and serie_grupos and aparta is not None:
            niveles = _unir(
                [f"{nombre} {_pesos(valor)}" for nombre, valor in serie_grupos],
                texto["y"],
            )
            restas = aparta.huecos["resta_de_cada_grupo"]
            orden = sorted(restas.items(), key=lambda par: (-abs(par[1]), par[0]))
            lista_restas = _unir(
                [f"{nombre} {_como_resta(valor, idioma)}" for nombre, valor in orden],
                texto["y"],
            )
            quien = aparta.huecos["importe_del_grupo"]
            grupo_nombre = str(quien["grupo"])
            articulos.append(
                _bloque(
                    texto["atributo"],
                    [
                        texto["informe_niveles"].format(periodo=actual, lista=niveles),
                        texto["informe_restas"].format(corte=corte, anterior=anterior, lista=lista_restas),
                        texto["informe_aparta"].format(
                            grupo=grupo_nombre,
                            importe=_como_resta(quien["importe"], idioma),
                            resto=_como_resta(aparta.huecos["importe_del_resto"], idioma),
                            corte=corte,
                        ),
                    ],
                )
            )
        if pieza_grande and grupo_nombre:
            conclusion.append(
                texto["informe_conclusion_pieza"].format(
                    anterior=anterior,
                    pieza=pieza_grande,
                    corte=corte or "",
                    grupo=grupo_nombre,
                )
            )
        calendario = _completa(resultado, "calendario")
        if calendario is not None:
            articulos.append(
                _bloque(
                    texto["informe_calendario_titulo"],
                    [
                        texto["informe_calendario"].format(
                            marca=_pesos(calendario.huecos["importe_en_dias_de_calendario"]),
                            anterior=anterior,
                            base=_pesos(calendario.huecos["importe_en_dias_comparables"]),
                            dia=calendario.huecos["que_dia"],
                        ),
                        texto["informe_calendario_lee"].format(
                            marca=_pesos(calendario.huecos["importe_en_dias_de_calendario"]),
                            anterior=anterior,
                            diferencia=dif_mes,
                        ),
                    ],
                )
            )
        queda = _completa(resultado, "lo_que_queda")
        if queda is not None:
            if queda.huecos["queda"] < queda.huecos["queda_base"]:
                lado = texto["informe_queda_menos"].format(periodo=actual, anterior=anterior)
            elif queda.huecos["queda"] > queda.huecos["queda_base"]:
                lado = texto["informe_queda_mas"].format(periodo=actual, anterior=anterior)
            else:
                lado = texto["informe_queda_igual"].format(periodo=actual, anterior=anterior)
            articulos.append(
                _bloque(
                    texto["informe_queda_titulo"],
                    [
                        texto["informe_queda"].format(
                            periodo=actual,
                            queda=_pesos(queda.huecos["queda"]),
                            anterior=anterior,
                            base=_pesos(queda.huecos["queda_base"]),
                        ),
                        lado,
                        texto["informe_queda_lee"],
                    ],
                )
            )
        pesos = _completa(resultado, "pesos_de_un_mes")
        if pesos is not None and anio is not None:
            constantes = pesos.huecos["constantes"]
            articulos.append(
                _bloque(
                    texto["informe_pesos_titulo"].format(mes=pesos.huecos["mes"]),
                    [
                        texto["informe_pesos"].format(
                            mes=pesos.huecos["mes"],
                            periodo=actual,
                            actual=_pesos(constantes[instruccion.periodo.etiqueta()]),
                            anio=nombre_anio,
                            base=_pesos(constantes[instruccion.anio_pasado.etiqueta()]),
                            fuente=pesos.huecos["fuente"],
                        )
                    ],
                )
            )
        if nombre_anio:
            conclusion.append(
                texto["informe_no_separa"].format(anterior=anterior, anio=nombre_anio)
            )
        firma = "no alcanza para firmar" if idioma == "es" else "does not suffice to sign"
        if firma in nota.texto.casefold():
            conclusion.append(texto["informe_firma"])
    for ficha in resultado.fichas:
        if ficha.estado == "vacia" and ficha.motivo:
            nombre = HOJAS_POR_ID[ficha.hoja_id].nombre if ficha.hoja_id in HOJAS_POR_ID else ficha.hoja_id
            articulos.append(
                _bloque(
                    nombre,
                    [texto["informe_vacia"].format(nombre=nombre, motivo=ficha.motivo)],
                )
            )
    cierre = ""
    if conclusion:
        cierre = _bloque(texto["informe_conclusion"], conclusion)
    return (
        f'<section class="informe">'
        f'<button type="button" class="cerrar">{html.escape(texto["volver"])}</button>'
        f"<h2>{html.escape(texto['informe'])}</h2>"
        f'<p class="lead">{html.escape(texto["informe_leer"])}</p>'
        f"{''.join(articulos)}{cierre}</section>"
    )


def _bloque(titulo: str, parrafos: list[str]) -> str:
    cuerpo = "".join(f"<p>{html.escape(_frase(parrafo))}</p>" for parrafo in parrafos)
    return f"<article><h3>{html.escape(titulo)}</h3>{cuerpo}</article>"


def _frase(texto: str) -> str:
    if not texto:
        return texto
    partes = texto.split(". ")
    return ". ".join(parte[0].upper() + parte[1:] if parte else parte for parte in partes)


def _unir(partes: list[str], y: str) -> str:
    if len(partes) <= 1:
        return "".join(partes)
    return ", ".join(partes[:-1]) + y + partes[-1]


def _pasos(
    resultado: Resultado,
    instruccion: Instruccion,
    idioma: str,
    periodos: list,
    corte: str | None,
    serie_grupos: list[tuple[str, int]] | None,
) -> list[dict]:
    texto = _TEXTO[idioma]
    pasos: list[dict] = []
    monitoreo = _completa(resultado, "monitoreo")
    if monitoreo is not None and len(periodos) >= 2:
        actual = _cuando(instruccion.periodo, idioma)
        anterior = _cuando(instruccion.periodo_anterior, idioma)
        pasos.append(
            _paso(
                texto["historia_mes"].format(
                    periodo=actual,
                    total=_pesos(monitoreo.huecos["total"]),
                    base=_pesos(monitoreo.huecos["total_base"]),
                    anterior=anterior,
                    diferencia=_como_resta(monitoreo.huecos["diferencia"], idioma),
                ),
                "evolucion",
                "fecha",
                [actual, anterior],
                "fecha",
                "",
                actual + texto["y"] + anterior,
                "mes",
            )
        )
        anio = _completa(resultado, "anio_pasado")
        if anio is not None:
            nombre_anio = _cuando(instruccion.anio_pasado, idioma)
            pasos.append(
                _paso(
                    texto["historia_anio"].format(
                        anio=nombre_anio,
                        base=_pesos(anio.huecos["total_base"]),
                        diferencia=_como_resta(anio.huecos["diferencia"], idioma),
                    ),
                    "evolucion",
                    "fecha",
                    [actual, nombre_anio],
                    "fecha",
                    "",
                    actual + texto["y"] + nombre_anio,
                    "anio",
                )
            )
    piezas = _completa(resultado, "piezas")
    if piezas is not None:
        tramo = piezas.huecos["tramo_de_cada_pieza"]
        nombres = [
            (texto["cantidad"], tramo["cantidad"]),
            (texto["mezcla"], tramo["mezcla"]),
            (texto["precio_tramo"], tramo["precio"]),
        ]
        for indice, (nombre, valor) in enumerate(nombres):
            if nombre == texto["precio_tramo"] and valor == 0:
                frase = texto["historia_precio"].format(nombre=nombre, resta=_pesos(0))
            elif indice == 0:
                frase = texto["historia_pieza"].format(nombre=nombre, resta=_como_resta(valor, idioma))
            else:
                frase = texto["historia_sigue_pieza"].format(
                    nombre=nombre, resta=_como_resta(valor, idioma)
                )
            pasos.append(_paso(frase, "piezas", "pieza", [nombre], "", "", ""))
        pasos.append(
            _paso(
                texto["historia_neto"].format(neto=_como_resta(piezas.huecos["neto"], idioma)),
                "piezas",
                "pieza",
                [nombre for nombre, _ in nombres],
                "",
                "",
                "",
            )
        )
    if corte and serie_grupos:
        for indice, (nombre, valor) in enumerate(serie_grupos):
            if indice == 0:
                frase = texto["historia_grupo"].format(
                    corte=corte, nombre=nombre, importe=_pesos(valor)
                )
            else:
                frase = texto["historia_sigue"].format(nombre=nombre, importe=_pesos(valor))
            pasos.append(_paso(frase, "atributo", corte, [nombre], corte, nombre, nombre))
    return pasos


def _paso(
    frase: str,
    grafico: str,
    marca: str,
    valores: list[str],
    filtro: str,
    valor: str,
    rotulo: str,
    hallazgo: str = "",
) -> dict:
    return {
        "frase": frase,
        "grafico": grafico,
        "marca": marca,
        "valores": valores,
        "filtro": filtro,
        "valor": valor,
        "rotulo": rotulo,
        "hallazgo": hallazgo,
    }


def _slicer(clave: str, nombre: str, valores: list[str], todos: str) -> str:
    opciones = [_opcion(todos, "*", presionado=True)]
    for valor in valores:
        opciones.append(_opcion(valor, valor))
    return _desplegable(clave, nombre, "".join(opciones), todos)


def _slicer_fecha(
    clave: str,
    nombre: str,
    periodos: list,
    calendario,
    idioma: str,
    todos: str,
    abrir: str,
) -> str:
    arbol: dict[int, dict[int, str]] = {}
    for periodo in periodos:
        etiqueta = _cuando(periodo, idioma)
        for dia in _dias_del_periodo(periodo, calendario):
            arbol.setdefault(dia.year, {}).setdefault(dia.month, etiqueta)
    nodos = [_opcion(todos, "*", presionado=True)]
    for anio in sorted(arbol):
        meses = []
        for mes in sorted(arbol[anio]):
            etiqueta = arbol[anio][mes]
            dias = []
            for dia in _dias_del_periodo_mes(periodos, calendario, anio, mes):
                rotulo_dia = f"{dia.day} {etiqueta}"
                dias.append(
                    _opcion(
                        str(dia.day),
                        rotulo_dia,
                        anio=str(anio),
                        mes=str(mes),
                        dia=str(dia.day),
                        rotulo=rotulo_dia,
                    )
                )
            meses.append(
                _nodo(
                    _MESES[idioma][mes],
                    etiqueta,
                    abrir,
                    "".join(dias),
                    anio=str(anio),
                    mes=str(mes),
                    rotulo=etiqueta,
                )
            )
        nodos.append(_nodo(str(anio), str(anio), abrir, "".join(meses), anio=str(anio), rotulo=str(anio)))
    return _desplegable(clave, nombre, "".join(nodos), todos)


def _desplegable(clave: str, nombre: str, panel: str, elegido: str) -> str:
    return (
        f'<div class="slicer" data-filtro="{html.escape(clave)}">'
        f'<span class="nombre">{html.escape(nombre)}</span>'
        f'<div class="caja">'
        f'<button type="button" class="disparador" aria-expanded="false">'
        f'<span class="elegido">{html.escape(elegido)}</span>'
        f'<span class="flecha" aria-hidden="true"></span></button>'
        f'<div class="panel" hidden>{panel}</div></div></div>'
    )


def _nodo(
    texto: str,
    valor: str,
    abrir: str,
    hijos: str,
    anio: str = "",
    mes: str = "",
    rotulo: str = "",
) -> str:
    rama = (
        f'<button type="button" class="abrir" aria-expanded="false" aria-label="{html.escape(abrir)}">'
        f'<span class="flecha" aria-hidden="true"></span></button>'
    )
    return (
        f'<div class="nodo">{rama}'
        f"{_opcion(texto, valor, anio=anio, mes=mes, rotulo=rotulo or texto)}"
        f'<div class="hijos" hidden>{hijos}</div></div>'
    )


def _opcion(
    texto: str,
    valor: str,
    anio: str = "",
    mes: str = "",
    dia: str = "",
    rotulo: str = "",
    presionado: bool = False,
) -> str:
    extra = ""
    if anio:
        extra += f' data-anio="{html.escape(anio)}"'
    if mes:
        extra += f' data-mes="{html.escape(mes)}"'
    if dia:
        extra += f' data-dia="{html.escape(dia)}"'
    estado = "true" if presionado else "false"
    return (
        f'<button type="button" class="opcion" data-valor="{html.escape(valor)}"'
        f'{extra} data-rotulo="{html.escape(rotulo or texto)}" aria-pressed="{estado}">'
        f"{html.escape(texto)}</button>"
    )


def _dias_del_periodo(periodo, calendario) -> list:
    if calendario is not None:
        return list(calendario.dias(periodo))
    dias = []
    dia = periodo.inicio
    while dia <= periodo.fin:
        dias.append(dia)
        dia += timedelta(days=1)
    return dias


def _dias_del_periodo_mes(periodos, calendario, anio: int, mes: int) -> list:
    vistos = []
    for periodo in periodos:
        for dia in _dias_del_periodo(periodo, calendario):
            if dia.year == anio and dia.month == mes and dia not in vistos:
                vistos.append(dia)
    return vistos


def _datos_fecha(periodo) -> str:
    dia = f' data-dia="{periodo.inicio.day}"' if periodo.inicio == periodo.fin else ""
    return f'data-anio="{periodo.inicio.year}" data-mes="{periodo.inicio.month}"{dia}'


def _periodos_en_evolucion(resultado: Resultado, instruccion: Instruccion) -> list:
    return _meses_de_la_evolucion(resultado, instruccion)


def _eje_corto(periodo, idioma: str) -> str:
    if periodo.grano != "mes":
        return _cuando(periodo, idioma)
    return f"{_CORTO[idioma][periodo.inicio.month]} {periodo.inicio.year % 100:02d}"


def _serie_atributo(resultado: Resultado) -> tuple[str | None, list[tuple[str, int]] | None]:
    ficha = _completa(resultado, "el_que_se_aparta")
    if ficha is None or _grupos_son_personas(ficha):
        return None, None
    corte = str(ficha.huecos.get("corte") or "")
    niveles = ficha.huecos.get("nivel_de_cada_grupo") or {}
    if not corte or not niveles:
        return None, None
    orden = sorted(niveles.items(), key=lambda par: (-par[1], par[0]))
    return corte, orden


def _visual(grafico_id: str, titulo: str, dibujo: str, extra: str = "", clase: str = "") -> str:
    marca = f" {clase}" if clase else ""
    return (
        f'<article class="visual{marca}" data-grafico="{grafico_id}"{extra}>'
        f"<h2>{html.escape(titulo)}</h2>{dibujo}</article>"
    )


def _visual_atributo(resultado: Resultado, texto: dict[str, str]) -> str:
    ficha = _completa(resultado, "el_que_se_aparta")
    cuerpo = ""
    if ficha and not _grupos_son_personas(ficha):
        corte = str(ficha.huecos.get("corte") or "")
        niveles = ficha.huecos.get("nivel_de_cada_grupo") or {}
        orden = sorted(niveles.items(), key=lambda par: (-par[1], par[0]))
        dibujo = grafico([(nombre, valor) for nombre, valor in orden], eje=texto["eje"], alto=520)
        cuerpo = (
            f'<div class="filtros" data-filtro="atributo">'
            f'<button type="button" data-atributo="{html.escape(corte)}" aria-pressed="true">'
            f"{html.escape(_rotulo(corte))}</button></div>"
            f'<div data-vista="{html.escape(corte)}">{dibujo}</div>'
        )
    return _visual("atributo", texto["atributo"], cuerpo)


def _dibujo(
    serie: list[tuple[str, int]] | None,
    eje: str | None = None,
    marca: str | None = None,
    ancho: int = 680,
    alto: int = 300,
    datos: list[str] | None = None,
    rotulos: list[str] | None = None,
) -> str:
    if not serie:
        return ""
    return grafico(
        serie,
        eje=eje or _TEXTO["es"]["eje"],
        alto=alto,
        marca=marca,
        ancho=ancho,
        datos=datos,
        rotulos=rotulos,
    )


def _meses_de_la_evolucion(resultado: Resultado, instruccion: Instruccion) -> list:
    monitoreo = _completa(resultado, "monitoreo")
    if monitoreo is None:
        return []
    meses = monitoreo.huecos.get("importe_de_cada_mes")
    if meses:
        periodos = []
        for clave in sorted(meses):
            anio, mes = clave.split("-")
            periodos.append(Periodo.mes(int(anio), int(mes)))
        return periodos
    periodos = []
    if _completa(resultado, "anio_pasado") is not None:
        periodos.append(instruccion.anio_pasado)
    periodos.append(instruccion.periodo_anterior)
    periodos.append(instruccion.periodo)
    return periodos


def _serie_evolucion(resultado: Resultado, instruccion: Instruccion, idioma: str) -> list[tuple[str, int]] | None:
    monitoreo = _completa(resultado, "monitoreo")
    if monitoreo is None:
        return None
    meses = monitoreo.huecos.get("importe_de_cada_mes")
    if meses:
        serie = []
        for periodo in _meses_de_la_evolucion(resultado, instruccion):
            clave = f"{periodo.inicio.year:04d}-{periodo.inicio.month:02d}"
            serie.append((_cuando(periodo, idioma), int(meses[clave])))
        return serie
    serie = []
    anio = _completa(resultado, "anio_pasado")
    if anio is not None:
        serie.append((_cuando(instruccion.anio_pasado, idioma), anio.huecos["total_base"]))
    serie.append((_cuando(instruccion.periodo_anterior, idioma), monitoreo.huecos["total_base"]))
    serie.append((_cuando(instruccion.periodo, idioma), monitoreo.huecos["total"]))
    return serie


def _serie_piezas(resultado: Resultado, idioma: str) -> list[tuple[str, int]] | None:
    ficha = _completa(resultado, "piezas")
    if ficha is None:
        return None
    texto = _TEXTO[idioma]
    tramo = ficha.huecos["tramo_de_cada_pieza"]
    return [
        (texto["cantidad"], tramo["cantidad"]),
        (texto["mezcla"], tramo["mezcla"]),
        (texto["precio_tramo"], tramo["precio"]),
    ]


def _completa(resultado: Resultado, hoja_id: str) -> Ficha | None:
    try:
        ficha = resultado.ficha(hoja_id)
    except KeyError:
        return None
    if ficha.estado != "completa":
        return None
    return ficha


def _grupos_son_personas(ficha: Ficha) -> bool:
    nombres = list(ficha.huecos.get("nivel_de_cada_grupo", {}))
    grupo = ficha.huecos.get("importe_del_grupo") or {}
    if grupo.get("grupo"):
        nombres.append(grupo["grupo"])
    return any(parece_persona(nombre) for nombre in nombres)


def _rotulo(nombre: str) -> str:
    limpio = nombre.strip()
    if not limpio:
        return limpio
    return limpio[:1].upper() + limpio[1:]


def _ancho_texto(texto: str, fuente: int, factor: float) -> float:
    return max(len(texto), 1) * fuente * factor


def _fuente_en_ranura(textos: list[str], ranura: float, tope: int, factor: float) -> int:
    largo = max((len(texto) for texto in textos), default=1)
    cabe = int(ranura * 0.92 / (largo * factor)) if largo else tope
    return max(12, min(tope, cabe))


def grafico(
    series: list[tuple[str, int]],
    debajo_del_corte: str | None = None,
    eje: str | None = None,
    alto: int = 320,
    marca: str | None = None,
    ancho: int = 680,
    datos: list[str] | None = None,
    rotulos: list[str] | None = None,
) -> str:
    n = max(len(series), 1)
    if ancho <= 720 and n >= 6:
        dibujo = _barras_horizontales(series, alto, marca, ancho, datos, rotulos)
    else:
        dibujo = _barras_verticales(series, alto, marca, ancho, datos, rotulos)
    frase = eje or "El eje arranca en cero."
    if debajo_del_corte:
        frase += f" Debajo del corte quedó {debajo_del_corte}."
    return (
        f'<figure class="tarjeta">{dibujo}'
        f'<figcaption class="eje">{html.escape(frase)}</figcaption></figure>'
    )


def _barras_verticales(
    series: list[tuple[str, int]],
    alto: int,
    marca: str | None,
    ancho: int,
    datos: list[str] | None,
    rotulos: list[str] | None,
) -> str:
    n = max(len(series), 1)
    visibles = [
        rotulos[i] if rotulos and i < len(rotulos) else etiqueta
        for i, (etiqueta, _) in enumerate(series)
    ]
    numeros = [_pesos(valor) for _, valor in series]
    margen = 36
    slot = (ancho - margen * 2) / n
    fuente_cat = _fuente_en_ranura(visibles, slot, 36, 0.54)
    fuente_val = _fuente_en_ranura(numeros, slot * 2, 28, 0.58)
    escalonar = bool(numeros) and _ancho_texto(max(numeros, key=len), fuente_val, 0.58) > slot * 0.96
    if not escalonar:
        fuente_val = _fuente_en_ranura(numeros, slot, 28, 0.58)
    bar_w = min(240, slot * 0.82)
    negativos = [numeros[i] for i, (_, valor) in enumerate(series) if valor < 0]
    if negativos:
        while fuente_val > 18 and _ancho_texto(max(negativos, key=len), fuente_val, 0.58) > bar_w * 0.9:
            fuente_val -= 2
    if escalonar:
        linea_alta = fuente_val * 1.05
        linea_baja = linea_alta + fuente_val * 1.75
        arriba = int(linea_baja + 14)
    else:
        linea_alta = linea_baja = 0
        arriba = int(fuente_val * 1.35) + 12
    margen_bajo = int(fuente_cat * 1.45) + 24
    alto = max(alto, arriba + margen_bajo + 80)
    plot_h = alto - arriba - margen_bajo
    extremo = max((abs(valor) for _, valor in series), default=1) or 1
    hay_negativo = any(valor < 0 for _, valor in series)
    if hay_negativo:
        cero = arriba + plot_h / 2
        escala = (plot_h / 2) / extremo
    else:
        cero = arriba + plot_h
        escala = plot_h / extremo
    familia = "Segoe UI, sans-serif"
    partes = [
        f'<svg viewBox="0 0 {ancho} {alto}" role="img" data-eje="cero" preserveAspectRatio="xMidYMid meet">',
        f'<line x1="{margen}" y1="{cero}" x2="{ancho - margen}" y2="{cero}" stroke="#d5cdc0"/>',
        (
            f'<text x="{margen + 4}" y="{cero - 8}" fill="#8a8175" font-size="{max(18, fuente_val - 4)}" '
            f'font-family="{familia}">0</text>'
        ),
    ]
    for i, (etiqueta, valor) in enumerate(series):
        x = margen + i * slot + (slot - bar_w) / 2
        alto_barra = abs(valor) * escala
        y = cero - alto_barra if valor >= 0 else cero
        color = "#118dff" if valor >= 0 else "#d13438"
        extra = f" {datos[i]}" if datos and i < len(datos) and datos[i] else ""
        if marca:
            partes.append(
                f'<g data-marca="{html.escape(marca)}" data-valor="{html.escape(etiqueta)}"{extra}>'
            )
        partes.append(
            f'<rect x="{x:.1f}" y="{y:.1f}" width="{bar_w:.1f}" height="{alto_barra:.1f}" rx="5" fill="{color}"/>'
        )
        if valor < 0 and alto_barra >= fuente_val * 1.3:
            valor_y = y + alto_barra / 2 + fuente_val * 0.32
            valor_fill = "#fffcf7"
        elif escalonar:
            valor_y = linea_baja if i % 2 else linea_alta
            valor_fill = "#1c1917"
        else:
            valor_y = max(y - fuente_val * 0.28, fuente_val)
            valor_fill = "#1c1917"
        centro = x + bar_w / 2
        partes.append(
            f'<text x="{centro:.1f}" y="{valor_y:.1f}" text-anchor="middle" fill="{valor_fill}" '
            f'font-size="{fuente_val}" font-weight="650" font-family="{familia}">'
            f"{html.escape(numeros[i])}</text>"
        )
        partes.append(
            f'<text class="categoria" x="{centro:.1f}" y="{alto - 10}" text-anchor="middle" fill="#252423" '
            f'font-size="{fuente_cat}" font-family="{familia}">{html.escape(visibles[i])}</text>'
        )
        if marca:
            partes.append("</g>")
    partes.append("</svg>")
    return "".join(partes)


def _barras_horizontales(
    series: list[tuple[str, int]],
    alto: int,
    marca: str | None,
    ancho: int,
    datos: list[str] | None,
    rotulos: list[str] | None,
) -> str:
    n = max(len(series), 1)
    visibles = [
        rotulos[i] if rotulos and i < len(rotulos) else etiqueta
        for i, (etiqueta, _) in enumerate(series)
    ]
    numeros = [_pesos(valor) for _, valor in series]
    fuente = 26
    fila = max(alto - 16, 80) / n

    def columnas(tamano: int) -> tuple[float, float]:
        izquierda = max(_ancho_texto(texto, tamano, 0.56) for texto in visibles) + 20
        derecha = max(_ancho_texto(texto, tamano, 0.58) for texto in numeros) + 16
        return izquierda, derecha

    izquierda, derecha = columnas(fuente)
    while (izquierda + derecha > ancho * 0.7 or fuente > fila * 0.7) and fuente > 16:
        fuente -= 2
        izquierda, derecha = columnas(fuente)
    alto = max(alto, int(n * (fuente / 0.62) + 16))
    fila = (alto - 16) / n
    extremo = max((abs(valor) for _, valor in series), default=1) or 1
    hay_negativo = any(valor < 0 for _, valor in series)
    zona = ancho - izquierda - derecha
    if hay_negativo:
        cero_x = izquierda + zona / 2
        escala = (zona / 2) / extremo
    else:
        cero_x = izquierda
        escala = zona / extremo
    familia = "Segoe UI, sans-serif"
    partes = [
        f'<svg viewBox="0 0 {ancho} {alto}" role="img" data-eje="cero" preserveAspectRatio="xMidYMid meet">',
        (
            f'<line x1="{cero_x:.1f}" y1="4" x2="{cero_x:.1f}" y2="{alto - 4}" '
            f'stroke="#d5cdc0"/>'
        ),
    ]
    for i, (etiqueta, valor) in enumerate(series):
        centro_y = 8 + i * fila + fila / 2
        largo = abs(valor) * escala
        bar_h = min(fila * 0.62, fuente * 1.15)
        y = centro_y - bar_h / 2
        x = cero_x if valor >= 0 else cero_x - largo
        color = "#118dff" if valor >= 0 else "#d13438"
        extra = f" {datos[i]}" if datos and i < len(datos) and datos[i] else ""
        if marca:
            partes.append(
                f'<g data-marca="{html.escape(marca)}" data-valor="{html.escape(etiqueta)}"{extra}>'
            )
        if largo > 0:
            partes.append(
                f'<rect x="{x:.1f}" y="{y:.1f}" width="{largo:.1f}" height="{bar_h:.1f}" rx="4" fill="{color}"/>'
            )
        base = centro_y + fuente * 0.32
        partes.append(
            f'<text class="categoria" x="{izquierda - 12:.1f}" y="{base:.1f}" text-anchor="end" '
            f'fill="#252423" font-size="{fuente}" font-family="{familia}">'
            f"{html.escape(visibles[i])}</text>"
        )
        partes.append(
            f'<text x="{ancho - derecha + 10:.1f}" y="{base:.1f}" text-anchor="start" fill="#1c1917" '
            f'font-size="{fuente}" font-weight="650" font-family="{familia}">'
            f"{html.escape(numeros[i])}</text>"
        )
        if marca:
            partes.append("</g>")
    partes.append("</svg>")
    return "".join(partes)


def _pagina(
    ficha: Ficha,
    resultado: Resultado,
    instruccion: Instruccion,
    encargo: Encargo | None,
    vacios: tuple[HuecoVacio, ...],
    idioma: str,
    abre: str,
    bloques: dict[str, str],
    titulo: str,
) -> str:
    texto = _TEXTO[idioma]
    hoja = HOJAS_POR_ID[ficha.hoja_id]
    marca_activa = ' class="activa"' if ficha.hoja_id == abre else ""
    procedencia = _procedencia(resultado, encargo, idioma)
    if ficha.estado == "vacia":
        lienzo = f'<div class="vacia"><p>{html.escape(_frase_vacia(ficha, vacios, idioma))}</p></div>'
        frases: list[str] = []
    else:
        lienzo, frases = _cuerpo(ficha, resultado, instruccion, idioma)
    cabeza = [f'<p class="kicker">{html.escape(titulo)}</p>', f"<h1>{html.escape(hoja.nombre)}</h1>"]
    if ficha.hoja_id == abre:
        cabeza.append(_respuesta(bloques, idioma).rstrip("\n"))
        limpieza = _limpieza(resultado, idioma)
        if limpieza:
            cabeza.append(f'<p class="limpieza">{html.escape(limpieza)}</p>')
    cabeza.append(f'<p class="procedencia">{html.escape(procedencia)}</p>')
    base = ficha.base
    if ficha.hoja_id == "piezas" and ficha.huecos.get("camino"):
        base = f"{base}. {texto['camino']}: {ficha.huecos['camino']}"
    lectura = [
        f'<p class="pregunta">{html.escape(ficha.pregunta)}</p>',
        f'<p class="base">{html.escape(texto["base"])}: {html.escape(base)}</p>',
        *frases,
        f'<p class="limite">{html.escape(hoja.limite_obligatorio)}</p>',
    ]
    return (
        f'<section id="{html.escape(ficha.hoja_id)}"{marca_activa} '
        f'data-hoja="{html.escape(ficha.hoja_id)}" {_marca(ficha)}>\n'
        f'<header class="cabeza">{"".join(cabeza)}</header>\n'
        f'<div class="cuerpo-hoja"><div class="lienzo">{lienzo}</div>'
        f'<aside class="lectura">{"".join(lectura)}</aside></div>\n'
        f"</section>"
    )


def _cuerpo(
    ficha: Ficha,
    resultado: Resultado,
    instruccion: Instruccion,
    idioma: str,
) -> tuple[str, list[str]]:
    texto = _TEXTO[idioma]
    if ficha.hoja_id == "el_que_se_aparta":
        return _corte(ficha, idioma)
    dibujo = grafico(_series(ficha, instruccion, idioma), eje=texto["eje"], alto=280)
    frases = []
    cuenta = _cuenta(ficha, idioma)
    if cuenta:
        frases.append(f'<p class="cuenta">{html.escape(cuenta)}</p>')
    if ficha.hoja_id == "monitoreo":
        pesa = ficha.huecos.get("lo_que_mas_pesa")
        if pesa:
            frase = texto["nivel"].format(
                cuando=_cuando(instruccion.periodo, idioma),
                grupo=pesa["grupo"],
                importe=_pesos(pesa["importe"]),
            )
            frases.append(f'<p class="nivel">{html.escape(frase)}</p>')
    if ficha.hoja_id == "calendario":
        frases.append(f'<p class="extra">{html.escape(_frase_calendario(ficha, instruccion, idioma))}</p>')
    if ficha.hoja_id == "pesos_de_un_mes":
        frases.append(f'<p class="extra">{html.escape(_frase_pesos(ficha, resultado, instruccion, idioma))}</p>')
    return dibujo, frases


def _corte(ficha: Ficha, idioma: str) -> tuple[str, list[str]]:
    texto = _TEXTO[idioma]
    grupo = ficha.huecos["importe_del_grupo"]
    neto = ficha.huecos["neto"]
    vistas = [
        _vista(
            "corte",
            [(grupo["grupo"], grupo["importe"]), (texto["resto"], ficha.huecos["importe_del_resto"])],
            idioma,
            visible=True,
        )
    ]
    botones = [
        f'<button type="button" data-grupo="" aria-pressed="true">'
        f'{html.escape(ficha.huecos["corte"] or "")}</button>'
    ]
    for nombre, resta in ficha.huecos["resta_de_cada_grupo"].items():
        resto = neto - resta
        vistas.append(
            _vista(nombre, [(nombre, resta), (texto["resto"], resto)], idioma, visible=False)
        )
        botones.append(
            f'<button type="button" data-grupo="{html.escape(nombre)}" aria-pressed="false">'
            f"{html.escape(nombre)}</button>"
        )
    lienzo = f'<div class="filtro" data-filtro="corte">{"".join(botones)}</div>' + "\n".join(vistas)
    frases = [
        f'<p class="neto">{html.escape(texto["neto"].format(neto=_como_resta(neto, idioma)))}</p>',
        f'<p class="cuenta">{html.escape(_presentar_cuenta(ficha.comprobacion))}</p>',
    ]
    return lienzo, frases


def _vista(nombre: str, series: list[tuple[str, int]], idioma: str, visible: bool) -> str:
    oculto = "" if visible else " hidden"
    dibujo = grafico(series, eje=_TEXTO[idioma]["eje_resta"], alto=260)
    return f'<div data-vista="{html.escape(nombre)}"{oculto}>{dibujo}</div>'


def _nota(nota: NotaLista, titulo: str, activa: bool, kicker: str) -> str:
    marca_activa = ' class="activa"' if activa else ""
    evidencia = ""
    otros = []
    for rotulo, cuerpo in _piramide(nota.texto):
        tarjeta = _tarjeta(rotulo, cuerpo, evidencia=rotulo in ("Evidencia", "Evidence"))
        if rotulo in ("Evidencia", "Evidence"):
            evidencia = tarjeta
        else:
            otros.append(tarjeta)
    return (
        f'<section id="nota"{marca_activa} data-hoja="nota" data-estado="nota">\n'
        f'<header class="cabeza"><p class="kicker">{html.escape(kicker)}</p>'
        f"<h1>{html.escape(titulo)}</h1></header>\n"
        f'<div class="piramide"><div class="columna">{"".join(otros)}</div>{evidencia}</div>\n'
        f"</section>"
    )


def _tarjeta(rotulo: str, cuerpo: str, evidencia: bool) -> str:
    clase = ' class="evidencia"' if evidencia else ""
    titulo = f"<h2>{html.escape(rotulo)}</h2>" if rotulo else ""
    return f"<article{clase}>{titulo}<p>{html.escape(cuerpo)}</p></article>"


def _piramide(texto: str) -> list[tuple[str, str]]:
    if texto.startswith("Addressee"):
        etiquetas = ("Addressee", "First sentence", "Evidence", "Limit", "Other story", "Closings")
    else:
        etiquetas = ("Destinatario", "Primera oración", "Evidencia", "Límite", "Otra historia", "Cierres")
    hallados = []
    for etiqueta in etiquetas:
        indice = texto.find(etiqueta + "\n")
        if indice >= 0:
            hallados.append((indice, etiqueta))
    if not hallados:
        return [("", texto.strip())]
    hallados.sort()
    bloques = []
    for i, (indice, etiqueta) in enumerate(hallados):
        inicio = indice + len(etiqueta) + 1
        fin = hallados[i + 1][0] if i + 1 < len(hallados) else len(texto)
        bloques.append((etiqueta, texto[inicio:fin].strip()))
    return bloques


def _presentar_cuenta(texto: str) -> str:
    return _ENTEROS.sub(lambda hallado: _pesos(int(hallado.group(0))), texto)


def _boton(hoja_id: str, nombre: str, actual: bool) -> str:
    marca = "true" if actual else "false"
    return (
        f'<button type="button" data-ir="{html.escape(hoja_id)}" aria-current="{marca}">'
        f"{html.escape(nombre)}</button>"
    )


def _series(ficha: Ficha, instruccion: Instruccion, idioma: str) -> list[tuple[str, int]]:
    huecos = ficha.huecos
    if ficha.hoja_id == "monitoreo":
        return [
            (_cuando(instruccion.periodo, idioma), huecos["total"]),
            (_cuando(instruccion.periodo_anterior, idioma), huecos["total_base"]),
        ]
    if ficha.hoja_id == "anio_pasado":
        return [
            (_cuando(instruccion.periodo, idioma), huecos["total"]),
            (_cuando(instruccion.anio_pasado, idioma), huecos["total_base"]),
        ]
    if ficha.hoja_id == "piezas":
        tramo = huecos["tramo_de_cada_pieza"]
        return [("Cantidad", tramo["cantidad"]), ("Mezcla", tramo["mezcla"]), ("Precio", tramo["precio"])]
    if ficha.hoja_id == "lo_que_queda":
        return [
            (_cuando(instruccion.periodo, idioma), huecos["queda"]),
            (_cuando(instruccion.periodo_anterior, idioma), huecos["queda_base"]),
        ]
    if ficha.hoja_id == "calendario":
        por_dia = huecos["facturacion_por_dia"]
        return [
            (_cuando(instruccion.periodo_anterior, idioma), por_dia[instruccion.periodo_anterior.etiqueta()]),
            (_cuando(instruccion.periodo, idioma), por_dia[instruccion.periodo.etiqueta()]),
        ]
    if ficha.hoja_id == "pesos_de_un_mes":
        return [(mes, valor) for mes, valor in huecos["constantes"].items()]
    raise ValueError(f"La hoja {ficha.hoja_id} no tiene gráfico.")


def _cuenta(ficha: Ficha, idioma: str) -> str:
    if ficha.hoja_id != "piezas":
        return _presentar_cuenta(ficha.comprobacion)
    texto = _TEXTO[idioma]
    tramo = ficha.huecos["tramo_de_cada_pieza"]
    piezas = texto["mas"].join(
        _como_resta(tramo[nombre], idioma, cero=texto["cero"])
        for nombre in ("cantidad", "mezcla", "precio")
    )
    return texto["cuenta_piezas"].format(
        piezas=piezas,
        neto=_como_resta(ficha.huecos["neto"], idioma, cero=texto["cero"]),
        camino=ficha.huecos["camino"],
    )


def _frase_calendario(ficha: Ficha, instruccion: Instruccion, idioma: str) -> str:
    texto = _TEXTO[idioma]
    regla = instruccion.calendario.texto if instruccion.calendario else ""
    frase = texto["marca"].format(
        marca=_pesos(ficha.huecos["importe_en_dias_de_calendario"]),
        total=_pesos(ficha.huecos["importe_del_periodo"]),
    )
    return f"{regla} {frase}".strip()


def _frase_pesos(ficha: Ficha, resultado: Resultado, instruccion: Instruccion, idioma: str) -> str:
    texto = _TEXTO[idioma]
    corrientes = ficha.huecos["corrientes"]
    constantes = ficha.huecos["constantes"]
    meses = (instruccion.anio_pasado, instruccion.periodo_anterior, instruccion.periodo)
    lista = "; ".join(
        f"{_cuando(mes, idioma)} {_pesos(corrientes[mes.etiqueta()])}" for mes in meses
    )
    fuente = f"{texto['fuente']}: {ficha.huecos['fuente']}. {ficha.huecos['mes']}."
    anio = next(
        (item for item in resultado.fichas if item.hoja_id == "anio_pasado" and item.estado == "completa"),
        None,
    )
    if anio is None:
        return f"{lista}. {fuente}"
    periodo = constantes[instruccion.periodo.etiqueta()]
    base = constantes[instruccion.anio_pasado.etiqueta()]
    lado = texto["abajo"] if periodo < base else texto["arriba"]
    lectura = texto["corrientes"].format(
        periodo=_cuando(instruccion.periodo, idioma),
        diferencia=_como_resta(anio.huecos["diferencia"], idioma),
        anio=_cuando(instruccion.anio_pasado, idioma),
    )
    constantes_frase = texto["constantes"].format(
        mes=ficha.huecos["mes"],
        lado=lado,
        periodo=_pesos(periodo),
        anio=_pesos(base),
    )
    return f"{lista}. {lectura} {constantes_frase} {fuente}"


def _frase_vacia(ficha: Ficha, vacios: tuple[HuecoVacio, ...], idioma: str) -> str:
    texto = _TEXTO[idioma]
    for hueco in vacios:
        if hueco.hoja_id != ficha.hoja_id:
            continue
        frase = texto["falta"].format(dato=hueco.dato_que_falta, frase=hueco.frase_que_frena)
        if hueco.sigue_en_pie:
            frase = f"{frase} {hueco.sigue_en_pie}"
        return frase
    return f"{ficha.motivo or ''} {texto['vacia']}".strip()


def _procedencia(resultado: Resultado, encargo: Encargo | None, idioma: str) -> str:
    if encargo is None:
        return Path(resultado.archivo).name
    texto = _TEXTO[idioma]
    origen = encargo.origen or Path(resultado.archivo).name
    if encargo.importe_sale_de_unidades_por_precio:
        regla = texto["por_precio"]
    elif encargo.columna("importe"):
        regla = texto["columna"]
    else:
        regla = texto["sin_importe"]
    if encargo.columna("devolucion") or encargo.columna("impuesto"):
        medida = _medicion(resultado)
    else:
        medida = texto["sin_iva"]
    fila = texto["fila"].format(grano=encargo.grano)
    return f"{origen}; {fila}; {texto['entran']}; {regla}; {medida}; {texto['no_cruza']}."


def _medicion(resultado: Resultado) -> str:
    for ficha in resultado.fichas:
        regla = ficha.huecos.get("regla_de_medicion")
        if not regla:
            continue
        salto = ficha.huecos.get("salto_de_regla")
        if salto:
            return f"{regla}. {salto}"
        return str(regla)
    return ""


def _limpieza(resultado: Resultado, idioma: str) -> str:
    movieron = [nota for nota in resultado.limpieza if nota.antes != nota.despues]
    if not movieron:
        return ""
    return _TEXTO[idioma]["limpieza"].format(
        antes=_pesos(movieron[0].antes),
        despues=_pesos(movieron[-1].despues),
    )


def _respuesta(bloques: dict[str, str], idioma: str) -> str:
    if idioma == "en":
        quien = bloques.get("Addressee", "")
        frase = bloques.get("First sentence", "")
    else:
        quien = bloques.get("Destinatario", "")
        frase = bloques.get("Primera oración", "")
    if not quien and not frase:
        return ""
    return f'<p class="respuesta">{html.escape(quien)} {html.escape(frase)}</p>\n'


def _bloques(texto: str) -> dict[str, str]:
    salida = {}
    for parte in texto.split("\n\n"):
        titulo, _, resto = parte.partition("\n")
        salida[titulo.strip()] = resto.strip()
    return salida


def _que_abre(encargo: Encargo | None, fichas: tuple[Ficha, ...]) -> str:
    ids = [ficha.hoja_id for ficha in fichas if not _oculta(ficha)]
    pedida = None if encargo is None else encargo.abre
    if pedida in ids:
        return pedida
    if "monitoreo" in ids:
        return "monitoreo"
    if not ids:
        return "nota"
    return ids[0]


def _oculta(ficha: Ficha) -> bool:
    if ficha.hoja_id != "el_que_se_aparta" or ficha.estado != "completa":
        return False
    grupos = list(ficha.huecos.get("nivel_de_cada_grupo", {}))
    return any(parece_persona(nombre) for nombre in grupos)


def _marca(ficha: Ficha) -> str:
    if ficha.estado != "completa":
        return 'data-estado="vacia"'
    if "diferencia" in ficha.huecos:
        return f'data-estado="completa" data-diferencia="{ficha.huecos["diferencia"]}"'
    return 'data-estado="completa"'


def _cuando(periodo, idioma: str) -> str:
    if periodo.grano != "mes":
        return periodo.etiqueta()
    return f"{_MESES[idioma][periodo.inicio.month]} {periodo.inicio.year}"


def _como_resta(valor: int, idioma: str, cero: str | None = None) -> str:
    texto = _TEXTO[idioma]
    if valor < 0:
        return f"{_pesos(abs(valor))} {texto['abajo']}"
    if valor > 0:
        return f"{_pesos(valor)} {texto['arriba']}" if cero is None else _pesos(valor)
    return texto["mismo"] if cero is None else cero


def _pesos(valor: int) -> str:
    signo = "−" if valor < 0 else ""
    return signo + f"{abs(valor):,}".replace(",", ".")
