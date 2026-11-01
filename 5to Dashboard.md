capacidad operativa y la calidad del servicio

la operación puede cumplir con la demanda actual, dónde aparecen los cuellos de botella y si tiene sentido ampliar la capacidad.

Lo dividiría en cuatro dimensiones: cumplimiento, calidad, utilización de capacidad y expansión.


1. ¿Los pedidos llegan tarde y dónde nace el atraso?
Visualización: descomposición de tiempos del pedido.
Separaría el tiempo total en etapas:
Etapa	Tiempo promedio	Objetivo	Desvío
Preparación del pedido	4 h	2 h	+2 h
Espera de despacho	3 h	1 h	+2 h
Transporte	28 h	24 h	+4 h
Entrega final	5 h	3 h	+2 h

Gráfico recomendado: barras apiladas por etapa, comparando tiempo real y tiempo objetivo.

Complementaría con una grilla por depósito, transportista, zona geográfica y canal.

Esto permite distinguir si el problema está en la preparación, el despacho o la distribución.



2. ¿Hay reclamos, devoluciones o roturas y dónde se concentran?
Visualización: mapa de calor de incidencias.

Ejemplo:
Motivo	Depósito	Transporte	Local
Producto equivocado	25	3	12
Producto roto	5	45	8
Pedido incompleto	30	5	10
Demora	12	35	8

Usaría el mapa de calor para detectar dónde se concentran los problemas.

Agregaría dos indicadores:
- Tasa de reclamos sobre pedidos.
- Costo de devoluciones, reposiciones y compensaciones.
Es importante analizar tanto el volumen absoluto como la tasa. Un depósito con más reclamos puede simplemente procesar muchos más pedidos.


3. ¿El local, turno o cocina no dan abasto, o sobra capacidad?
Visualización: utilización de capacidad por día y turno.

Un heatmap sería ideal:
- Filas: días de la semana.
- Columnas: franjas horarias.
- Intensidad: utilización de capacidad.
Ejemplo:
Día / Turno	Mañana	Tarde	Noche
Lunes	45%	55%	85%
Martes	40%	50%	90%
Miércoles	50%	60%	95%
Jueves	55%	65%	110%
Viernes	70%	85%	125%
Sábado	90%	110%	130%
Domingo	85%	95%	115%

Ejemplo ilustrativo
 Una utilización superior al 100% representa demanda por encima de la capacidad definida.

Esto permitiría identificar:
- Días con capacidad ociosa.
- Turnos saturados.
- Picos recurrentes.
- Oportunidades para redistribuir personal o recursos.
También agregaría una curva de demanda por hora comparada con la capacidad disponible.


4. ¿Conviene abrir un día, un turno o una sede más?
Visualización: análisis de demanda no atendida y rentabilidad incremental.


Acá utilizaría una grilla de escenarios:
Alternativa	Demanda adicional estimada	Costo adicional	Resultado incremental
Abrir domingo	$3 M	$1 M	+$2 M
Extender turno noche	$2 M	$1,2 M	+$800 K
Abrir nueva sede	$8 M	$7 M	+$1 M

La idea es comparar alternativas, no solamente proyectar ventas.

Incluiría:
- Demanda potencial no atendida.
- Personal adicional.
- Costos fijos y variables.
- Capacidad disponible.
- Margen de contribución incremental.
- Punto de equilibrio.
Una precaución: la demanda no atendida no siempre equivale a ventas perdidas. Hay clientes que esperan, otros que cambian de horario y otros que abandonan. Hay que medirlo.


Datos necesarios
Información	Utilidad
ID y fecha del pedido	Seguir cada operación
Hora de recepción	Medir espera inicial
Inicio y fin de preparación	Medir depósito/cocina
Hora de despacho y entrega	Medir transporte
Transportista / responsable	Localizar demoras
Reclamos y devoluciones	Medir calidad
Motivo de incidencia	Identificar causas
Pedidos por hora y día	Medir demanda
Personal y recursos disponibles	Medir capacidad
Costos operativos	Evaluar expansión

Una consideración importante: no confundir capacidad teórica con capacidad efectiva. Una cocina puede producir 100 pedidos por hora en condiciones ideales, pero su capacidad real puede ser de 70 cuando hay ausencias, cambios de productos o picos de demanda.

Mi recomendación es que este módulo no se limite a mostrar problemas operativos. Debería permitir distinguir tres situaciones: capacidad insuficiente, capacidad mal distribuida y problemas de ejecución. Las tres pueden generar demoras, pero requieren decisiones muy diferentes.
