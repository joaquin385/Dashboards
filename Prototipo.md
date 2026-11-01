1. ¿El período fue bueno o malo?
Gráfico: evolución temporal de ventas.

- Línea de ventas del período actual.
- Línea del período comparable anterior.
- Variación porcentual.
- Posibilidad de cambiar entre facturación, unidades y transacciones.
La grilla puede complementar mostrando el acumulado y la variación contra el período anterior.


2. ¿De qué está hecho el resultado?
Acá utilizaría varias visualizaciones. No intentaría meter todo en un único gráfico.

A. ¿Cayó el tráfico, la conversión o el gasto por compra?
Gráfico: árbol de descomposición (driver tree)

B. ¿Vendimos menos unidades o las mismas más baratas?
Gráfico: descomposición de facturación en precio y volumen.
Permite distinguir si el negocio vende menos unidades, si vende a menor precio o si cambió la composición de lo vendido.

C. ¿Por qué bajó el ticket?
Acá usaría una grilla de descomposición del ticket.

Indicador	Anterior	Actual	Variación
Ticket promedio	$12.000	$10.500	-12,5%
Unidades por ticket	3,2	2,8	-12,5%
Precio promedio unitario	$3.750	$3.750	0%
Participación productos premium	25%	19%	-6 pp

Esto permite identificar tres posibles explicaciones:
- Precio: los productos se venden más baratos.
- Cantidad: el cliente se lleva menos unidades.
- Mix: se venden más productos económicos y menos productos caros.
Importante: para separar correctamente estos efectos hay que definir cómo se calcula el precio promedio y el efecto mix. No conviene interpretar cada indicador aisladamente.

D. ¿Dónde está la caída?
Gráfico: mapa de calor (Heatmap).

Por ejemplo:
Local	Canal físico	Online	Total
Local A	-15%	+8%	-10%
Local B	+5%	+12%	+7%
Local C	-22%	-10%	-18%
Local D	+3%	-5%	+1%

La ventaja es que permite detectar concentraciones de problemas.

También incorporaría filtros o niveles de exploración:
- Canal.
- Local.
- Categoría.
- Producto.
No haría un gráfico distinto para cada dimensión.


E. ¿Un canal subió y otro bajó, escondidos en el total?
Gráfico: barras divergentes.

Ejemplo:
Canal	Variación
Locales físicos	-18%
E-commerce	+24%
Mayoristas	-5%

Las barras divergentes permiten visualizar rápidamente qué canales crecen y cuáles caen.

También agregaría el peso de cada canal en la facturación para evitar interpretar un crecimiento del 50% en un canal que representa apenas el 2% del negocio como algo determinante.


4. Una consideración importante: los datos disponibles
No todas las empresas tienen datos para responder todas estas preguntas.
Pregunta	Datos necesarios
Evolución de ventas	Fecha, facturación
Tráfico	Cantidad de visitantes
Conversión	Visitantes y transacciones
Ticket	Facturación y transacciones
Unidades por compra	Unidades y transacciones
Precio promedio	Facturación y unidades
Mix de productos	Producto, unidades y facturación
Análisis por local	Local, fecha y facturación
Análisis por canal	Canal, fecha y facturación


cartera de clientes, su comportamiento y su valor a lo largo del tiempo.

1. ¿Cuántos clientes nuevos entraron y cuántos se fueron?
Visualización: grilla de movimiento de clientes (Customer Movement).
Usaría una grilla como esta:
Indicador	Clientes	Variación
Clientes período anterior	1.000	—
Clientes nuevos	180	+18%
Clientes que regresaron	60	+6%
Clientes retenidos	720	—
Clientes perdidos	220	-22%
Clientes período actual	960	-4%

La clave es distinguir:
- Nuevos: compraron por primera vez.
- Retenidos: compraron en ambos períodos.
- Recuperados: habían dejado de comprar y volvieron.
- Perdidos: compraban anteriormente y dejaron de hacerlo.
Hay que definir una ventana de inactividad para considerar perdido a un cliente. No comprar en un mes no necesariamente significa abandono.


2. ¿Por qué disminuyó la cartera?
Visualización: cascada de movimiento de clientes.

Ejemplo:
Movimiento	Clientes
Cartera inicial	1.000
Nuevos clientes	+180
Recuperados	+60
Clientes perdidos	-220
Cartera final	1.020

Pero agregaría una segunda dimensión: clasificar a los perdidos por su origen.
Segmento de origen	Clientes perdidos
Clientes habituales	120
Clientes de promociones	70
Clientes ocasionales	30

Esto responde algo mucho más interesante: no solamente cuántos clientes perdimos, sino qué tipo de clientes estamos perdiendo.

3. ¿Los que compraron una vez vuelven?
Visualización: curva de retención por cohortes.

Esta es una de las visualizaciones más interesantes de todo el conjunto.
Ejemplo:
Cohorte	Mes 0	Mes 1	Mes 2	Mes 3	Mes 4
Enero	100%	45%	35%	28%	22%
Febrero	100%	52%	40%	31%	—
Marzo	100%	38%	25%	—	—
Abril	100%	60%	—	—	—

Cada fila representa clientes que tuvieron su primera compra en ese mes.

Cada columna muestra qué proporción volvió a comprar.

Esto permite descubrir, por ejemplo:
- Los clientes nuevos están volviendo menos que antes.
- Una promoción genera muchas primeras compras, pero poca recurrencia.
- Una cohorte determinada tiene un comportamiento excepcionalmente bueno.
Es importante definir si la retención significa haber comprado exactamente en ese mes o haber comprado al menos una vez hasta ese momento. Son métricas diferentes.


4. ¿Cada cuánto vuelven y cuánto dejan en un año?
Acá utilizaría dos visualizaciones complementarias.

A. Frecuencia de compra: distribución de clientes.
Permite entender si el negocio depende de compradores ocasionales o recurrentes.

B. Valor anual por cliente (Customer Lifetime Value simplificado).
Usaría una grilla:
Indicador	Resultado
Venta anual promedio por cliente	$185.000
Venta anual mediana	$92.000
Compras promedio por año	4,2
Días promedio entre compras	54
Clientes con más de 5 compras	28%

La mediana es importante: el promedio puede quedar distorsionado por unos pocos clientes que compran muchísimo.

Una aclaración: esto sería valor observado durante 12 meses, no necesariamente un CLV predictivo.

5. ¿Unos pocos clientes explican casi toda la venta?
Visualización: curva de concentración de Pareto.
La curva mostraría cuánto de la facturación acumula el porcentaje de clientes más importantes.

Ejemplo:
- 10% de los clientes generan 45% de las ventas.
- 20% generan 65%.
- 50% generan 88%.
También acompañaría con una grilla:
Segmento	Clientes	Participación en ventas
Top 10%	100	45%
Siguiente 20%	200	20%
Siguiente 30%	300	23%
Último 40%	400	12%

Esto permite detectar dependencia comercial y riesgo de concentración.

6. ¿Los clientes que entraron juntos se comportan distinto?
Visualización: comparación de cohortes.
Acá compararía grupos según:
- Mes de primera compra.
- Promoción que los captó.
- Canal de adquisición.
- Campaña comercial.
Por ejemplo:
Cohorte	Clientes	Retención a 90 días	Compras promedio	Venta anual observada
Promo A	500	18%	1,4	$45.000
Promo B	300	42%	2,8	$110.000
Orgánicos	200	55%	3,5	$160.000

La pregunta interesante no es qué promoción consiguió más clientes, sino cuál consiguió clientes que después siguieron comprando.

Para comparar justamente, hay que utilizar cohortes con suficiente antigüedad y períodos de observación equivalentes.

Una cuestión fundamental: la identificación de clientes
Para construir este diagnóstico necesitamos poder reconocer al mismo cliente a través de sus distintas compras. Idealmente, un identificador único: CUIT, DNI, ID de cliente o cuenta.

Si las ventas no están asociadas a clientes identificables, podemos analizar transacciones y tickets, pero no medir correctamente retención, abandono, recurrencia ni cohortes.



**eficiencia de adquisición y conversión comercial**
acá queremos entender cómo llegan, cuánto cuesta conseguirlos y si la inversión comercial es rentable.

Lo dividiría en cuatro dimensiones: origen, conversión, costo de adquisición y rentabilidad.

1. ¿De dónde vienen las visitas y de dónde vienen las ventas?
Visualización: grilla comparativa de canales.

Canal	Visitas	Participación visitas	Ventas	Participación ventas	Conversión
Google Ads	20.000	40%	600	30%	3%
Orgánico	15.000	30%	750	37,5%	5%
Instagram	10.000	20%	100	5%	1%
Directo	5.000	10%	550	27,5%	11%

Esto permite detectar diferencias entre los canales que generan tráfico y los que generan ventas.

Alternativa visual: gráfico de dispersión con visitas en el eje X, conversión en el eje Y y tamaño de burbuja según facturación. Permite identificar canales con mucho tráfico y poca conversión.


2. ¿La publicidad trae gente que compra o gente que mira y se va?
Visualización: embudo de conversión por canal.

Ejemplo:
Embudo de Google Ads
Visitas

20.000



100% de las visitas iniciales
Fichas de producto

12.000



60% de las visitas iniciales
Carritos

3.000



15% de las visitas iniciales
Inicio de pago

1.500



7.5% de las visitas iniciales
Compras

600



3% de las visitas iniciales

Lo interesante es comparar el embudo de cada canal.

Por ejemplo:
- Instagram genera muchas visitas, pero pocas personas llegan a las fichas.
- Google Ads genera menos visitas, pero más carritos.
- El checkout tiene una caída importante en todos los canales.
Esto ayuda a distinguir un problema de adquisición de uno de experiencia de compra.


3. ¿En qué paso se pierden?
Visualización: grilla de conversión entre etapas.

En lugar de mostrar solamente el embudo, haría una grilla que permita comparar tasas de conversión y abandono.

Etapa	Personas	Conversión desde etapa anterior	Abandono
Visita	20.000	100%	—
Ficha	12.000	60%	40%
Carrito	3.000	25%	75%
Pago iniciado	1.500	50%	50%
Compra	600	40%	60%

Acá se identifica dónde está el cuello de botella.

También agregaría una comparación entre dispositivos, canales y segmentos de clientes.

La recompra no debería estar dentro de este mismo embudo: es un proceso posterior y se analiza mejor con las cohortes del bloque anterior.


4. ¿Cuánto cuesta conseguir un cliente?
Visualización: barras de CAC por canal.

CAC (Customer Acquisition Cost) = inversión de adquisición / clientes nuevos atribuidos al canal.
Canal	Inversión	Clientes nuevos	CAC
Google Ads	$1.200.000	300	$4.000
Instagram	$800.000	100	$8.000
Orgánico	$200.000	200	$1.000
Referidos	$150.000	150	$1.000

Importante: distinguir CAC pago de CAC total. El primero considera publicidad; el segundo incorpora también costos comerciales, herramientas, agencias y otros gastos de adquisición.

5. ¿El cliente deja más de lo que costó traerlo y en qué plazo?
Visualización: curva de recuperación de CAC (Payback).

Esta visualización compara cuánto margen acumulado genera un cliente contra lo que costó adquirirlo.

Ejemplo:
Tiempo desde adquisición	Margen acumulado	CAC	Resultado
Mes 1	$2.000	$4.000	-$2.000
Mes 2	$3.500	$4.000	-$500
Mes 3	$5.000	$4.000	+$1.000
Mes 6	$8.000	$4.000	+$4.000
Mes 12	$12.000	$4.000	+$8.000

El punto en que la curva supera el CAC es el período de recuperación.

Usaría margen de contribución, no facturación, para medir la rentabilidad real.

6. ¿Conviene invertir más en el canal o mejorar la conversión?
Visualización: matriz de eficiencia de canales.

Un gráfico de dispersión:
- Eje X: CAC.
- Eje Y: tasa de conversión.
- Tamaño de burbuja: cantidad de clientes nuevos.
- Color: rentabilidad o recuperación de CAC.
Esto permite identificar cuatro situaciones:
Situación	Diagnóstico	Posible decisión
CAC bajo + conversión alta	Canal eficiente	Evaluar escalar
CAC alto + conversión alta	Canal costoso	Optimizar costos
CAC bajo + conversión baja	Tráfico barato, poco efectivo	Revisar audiencia
CAC alto + conversión baja	Canal ineficiente	Revisar o reducir inversión

Hay una precaución: un canal con CAC bajo no necesariamente admite más inversión al mismo costo. Al escalar, puede aumentar el CAC marginal.

Una condición importante: atribución y datos
Este bloque requiere datos más específicos que los anteriores:
- Fuente, medio y campaña de adquisición.
- Identificador de visitante y cliente.
- Eventos de navegación: visita, ficha, carrito, checkout y compra.
- Inversión publicitaria por canal.
- Fecha de adquisición.
- Compras posteriores.
- Costos variables y margen de contribución.
Además, hay que definir cómo atribuir una venta cuando un cliente interactúa con varios canales. Por ejemplo, ve un anuncio en Instagram, busca la marca en Google y finalmente compra directamente.

Sin una atribución consistente, podemos terminar adjudicándole la venta al canal equivocado.



**Este bloque analiza la rentabilidad de la oferta y la eficiencia del inventario**
qué estamos vendiendo, cuánto ganamos con ello y si estamos utilizando bien el capital invertido en mercadería.

Lo dividiría en cuatro dimensiones: composición de ventas, rentabilidad, precios y promociones, e inventario.

1. ¿Qué productos explican la venta?
Visualización: ranking de productos por facturación
Una grilla complementaria:
Producto	Unidades	Facturación	Participación
Producto A	1.200	$12 M	30%
Producto B	800	$8 M	20%
Producto C	600	$5 M	12,5%
Producto D	400	$3 M	7,5%

Ordenaría por facturación y permitiría cambiar la métrica a unidades.

Esto identifica los productos que sostienen comercialmente el negocio.


2. ¿Cuáles explican el margen?
Visualización: matriz de facturación vs. margen.

Utilizaría un gráfico de dispersión:
- Eje X: facturación.
- Eje Y: margen porcentual.
- Tamaño de burbuja: margen bruto generado en pesos.
Así aparecen cuatro perfiles:
Perfil	Característica	Interpretación
Alta venta / alto margen	Productos estrella	Proteger y potenciar
Alta venta / bajo margen	Mucho volumen, poca rentabilidad	Revisar costos y precios
Baja venta / alto margen	Nichos rentables	Evaluar oportunidades
Baja venta / bajo margen	Bajo aporte	Revisar continuidad

Es importante distinguir margen porcentual de margen absoluto. Un producto puede tener un margen del 50%, pero generar muy poca ganancia total.

3. ¿Conviene subir, bajar o mantener el precio?
Acá propondría dos visualizaciones.

A. Evolución de precio, unidades y margen.

Una grilla por producto:
Producto	Precio actual	Variación precio	Variación unidades	Variación margen
A	$10.000	+10%	-2%	+8%
B	$5.000	+5%	-15%	-8%
C	$8.000	0%	+12%	+12%

Permite detectar productos donde un aumento de precio coincide con una caída de volumen.

Pero hay una distinción importante: una correlación entre cambios de precio y ventas no demuestra elasticidad. Para recomendar subas o bajas de precio con cierta confianza necesitamos variaciones comparables, control de promociones, estacionalidad y, preferentemente, experimentos o estimaciones de elasticidad.

B. Matriz de decisión de precios.
Situación	Qué investigar
Precio sube y margen mejora	¿La caída de unidades es aceptable?
Precio sube y margen cae	¿Se perdió demasiado volumen?
Precio baja y unidades suben	¿El margen total realmente mejora?
Precio estable y margen cae	¿Aumentaron los costos?

No mostraría una recomendación automática de subir o bajar sin evidencia suficiente.

4. ¿El descuento aumentó las unidades y se comió la ganancia?
Visualización: comparación de productos promocionados vs. no promocionados.

La grilla sería especialmente útil:
Indicador	Sin promoción	Con promoción
Precio promedio	$10.000	$8.000
Unidades	1.000	1.400
Facturación	$10 M	$11,2 M
Margen unitario	$3.000	$1.000
Margen total	$3 M	$1,4 M

En este ejemplo, la facturación aumentó un 12%, pero el margen total cayó un 53%.

Es una de las comparaciones más importantes para cualquier comercio que utiliza descuentos.

Idealmente, compararía contra un escenario sin promoción estimado con productos, períodos o grupos de clientes comparables. No asumiría que toda la diferencia de unidades fue causada por el descuento.

5. ¿Hay stock parado que no se vende y faltantes de lo que sí se vende?
Acá utilizaría dos visualizaciones complementarias.

A. Matriz de rotación de inventario.

Gráfico de dispersión:
- Eje X: unidades vendidas durante el período.
- Eje Y: días de inventario disponible.
- Tamaño de burbuja: valor económico del stock.
Permite identificar:
- Mucho stock y pocas ventas: mercadería inmovilizada.
- Poco stock y muchas ventas: riesgo de faltantes.
- Mucho stock y muchas ventas: productos de alta rotación.
- Poco stock y pocas ventas: baja prioridad.
B. Grilla de alertas de inventario.
Producto	Stock actual	Venta mensual	Días de stock	Diagnóstico
A	500	50	300	Exceso
B	20	200	3	Riesgo de quiebre
C	100	100	30	Normal
D	80	5	480	Inmovilizado

Esta grilla puede ser incluso más útil operativamente que el gráfico.

Datos necesarios
Información	Para qué sirve
Producto / categoría	Identificar composición
Unidades vendidas	Medir volumen
Precio de venta	Analizar precios
Costo unitario	Calcular margen
Descuentos	Evaluar promociones
Fecha de venta	Evolución y comparaciones
Stock actual	Detectar excesos y faltantes
Historial de movimientos de stock	Calcular rotación y quiebres
Compras y reposiciones	Evaluar abastecimiento

Una consideración: el margen bruto no siempre representa la rentabilidad final. Si hay costos de envío, comisiones, medios de pago u otros costos variables, conviene calcular también el margen de contribución.


evaluación de impacto de decisiones comerciales.
Queremos saber si subieron gracias a esa decisión y si el beneficio obtenido compensó sus posibles efectos negativos.

La pregunta central es: ¿qué habría pasado si no hubiéramos hecho nada?


1. ¿La acción produjo un resultado distinto del que habría habido sin ella?
Visualización: resultado observado vs. contrafactual.

Un gráfico de líneas con tres elementos:
- Resultado anterior a la acción.
- Resultado observado después de la acción.
- Resultado estimado sin la acción (contrafactual).
Ejemplo:

Una promoción comenzó en junio.
Indicador	Resultado
Ventas esperadas sin promoción	$10 M
Ventas observadas	$13 M
Incremento estimado	+$3 M
Costo de promoción	$1 M
Impacto neto estimado	+$2 M

Este es probablemente el gráfico más importante de todo este bloque.

La diferencia entre ventas observadas y ventas esperadas no puede calcularse simplemente prolongando una tendencia. Hay que construir un contrafactual razonable utilizando estacionalidad, tendencias, grupos de comparación u otros métodos.


2. ¿Mejoró lo que queríamos mejorar?
Visualización: grilla de objetivos e impacto.

No todos los experimentos buscan aumentar facturación. Algunos buscan mejorar conversión, captar clientes nuevos, aumentar recurrencia o reducir stock.
Objetivo	Antes	Después	Cambio
Nuevos clientes	100	180	+80%
Conversión	3%	4,5%	+1,5 pp
Ticket promedio	$15.000	$14.000	-6,7%
Recompra a 60 días	30%	38%	+8 pp

La visualización debería destacar el indicador objetivo y mostrar si se alcanzó la mejora esperada.

No confundiría un cambio observado con un efecto causal demostrado.

3. ¿Se rompió otra cosa al lado?
Visualización: matriz de efectos secundarios.

Por ejemplo, una campaña logró aumentar las ventas, pero:
Indicador	Impacto	Evaluación
Facturación	+25%	Positivo
Clientes nuevos	+40%	Positivo
Margen bruto	-12%	Negativo
Reclamos	+18%	Negativo
Recompra	-8%	Negativo
Ventas canal físico	-10%	Negativo

Esto evita declarar exitosa una acción que mejoró un indicador a costa de deteriorar otros.

También permite detectar efectos de desplazamiento: una campaña online puede aumentar las ventas digitales simplemente quitándoselas al canal físico.

4. ¿El resultado fue extraordinario o volvió a la normalidad?
Visualización: evolución temporal con intervención y período posterior.
jemplo:

Una campaña generó un pico de ventas en agosto.
- Julio: $10 M.
- Agosto: $16 M.
- Septiembre: $10,5 M.
- Octubre: $10 M.
La campaña produjo un pico, pero no necesariamente modificó el comportamiento habitual del negocio.

Compararía:
- Resultado durante la acción.
- Resultado inmediatamente posterior.
- Resultado de los meses siguientes.
- Evolución de clientes captados durante la acción.
Hay tres resultados posibles:
1. Impacto transitorio: generó un pico, pero luego todo volvió a la normalidad.
2. Impacto persistente: elevó el nivel habitual del negocio.
3. Impacto diferido: la acción generó clientes que produjeron ventas posteriores.

5. ¿Qué acción fue más rentable?
Visualización: matriz comparativa de intervenciones.

Compararía distintas acciones según su impacto económico incremental.
Acción	Ventas incrementales	Costo	Margen incremental	Resultado neto
Promo A	$3 M	$1 M	$1,2 M	+$200 K
Campaña B	$5 M	$1,5 M	$2,5 M	+$1 M
Cambio precio C	$2 M	$200 K	$1,4 M	+$1,2 M
Local nuevo D	$8 M	$4 M	$2 M	-$2 M

El gráfico podría utilizar:
- Eje X: inversión o costo de la acción.
- Eje Y: beneficio incremental neto.
- Tamaño de burbuja: ventas incrementales.
- Color: tipo de intervención.
Esto permite comparar acciones de naturaleza diferente.


Una distinción metodológica fundamental
Para este bloque establecería tres niveles de evidencia:
Nivel	Qué podemos afirmar
Descriptivo	Las ventas subieron después de la acción.
Comparativo	Las ventas subieron más que en un grupo comparable.
Causal	Tenemos evidencia razonable de que la acción produjo el incremento.

Por ejemplo, si un comercio hizo una promoción en diciembre, no podemos atribuirle todo el crecimiento: diciembre podría haber sido un mes de ventas altas de todas maneras.

Para fortalecer las conclusiones utilizaría:
- Experimentos A/B cuando sea posible.
- Locales de control y locales tratados.
- Diferencias en diferencias.
- Series temporales interrumpidas.
- Comparaciones con períodos estacionales equivalentes.
No todos los métodos sirven para todas las situaciones.

Mi recomendación: este bloque debería tener una identidad propia dentro del producto. No es otro dashboard de indicadores; es un módulo de evaluación de decisiones



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



liquidez, el capital de trabajo y la recuperación de las inversiones.
Lo dividiría en tres dimensiones: conversión de ventas en efectivo, previsión de caja y recuperación de inversiones.

1. ¿Cobramos lo que vendimos o queda plata pendiente?
Visualización: grilla de ventas vs. cobranzas.


Concepto	Importe	Participación
Ventas del período	$50 M	100%
Cobrado	$32 M	64%
Pendiente de cobro	$18 M	36%
Vencido	$5 M	10%

Después descompondría el pendiente según su origen:
Origen	Pendiente	Días promedio de cobro
Tarjetas en liquidación	$5 M	7 días
Marketplace	$4 M	14 días
Facturas a cobrar	$7 M	35 días
Otros	$2 M	10 días

Visualización complementaria: antigüedad de cuentas por cobrar (Aging).


Clasificaría los saldos en:
- No vencidos.
- 1 a 30 días.
- 31 a 60 días.
- 61 a 90 días.
- Más de 90 días.
Esto permite distinguir dinero que simplemente está pendiente de liquidación de dinero que corre riesgo de no cobrarse.

Una consideración: las ventas en cuotas requieren mostrar tanto el calendario de cobros como los importes efectivamente acreditados. No son equivalentes.
2. ¿Alcanza la caja de las próximas semanas?
Visualización: proyección de flujo de caja.


Utilizaría un gráfico de evolución del saldo de caja proyectado.

Ejemplo:
Semana	Saldo inicial	Ingresos	Egresos	Saldo final
1	$10 M	$5 M	$7 M	$8 M
2	$8 M	$4 M	$6 M	$6 M
3	$6 M	$3 M	$7 M	$2 M
4	$2 M	$6 M	$5 M	$3 M

El gráfico debería tener:
- Saldo de caja proyectado.
- Ingresos esperados.
- Egresos previstos.
- Nivel mínimo de liquidez deseado.
La visualización más importante sería detectar cuándo el saldo proyectado cae por debajo del mínimo necesario.

También mostraría tres escenarios:
Escenario	Supuesto
Optimista	Cobranzas en fecha y ventas esperadas
Base	Comportamiento habitual
Pesimista	Demoras en cobros y menores ventas

Esto permite anticipar problemas de liquidez antes de que sucedan.
3. ¿Esta decisión se recupera en un mes, seis o no se recupera?
Visualización: curva de recuperación de inversión (Payback).

Ejemplo de una inversión de $12 millones:
Mes	Flujo incremental acumulado
Inicial	-$12 M
1	-$10 M
2	-$8 M
3	-$5 M
4	-$2 M
5	+$1 M
6	+$4 M

El gráfico mostraría cuándo la curva cruza cero.

Acompañaría con una grilla:
Indicador	Resultado
Inversión inicial	$12 M
Recuperación estimada	5 meses
Beneficio acumulado a 12 meses	$18 M
ROI	150%

Hay que utilizar flujos de fondos incrementales, no facturación. También distinguir recuperación simple de recuperación descontada, que considera el valor del dinero en el tiempo.

Datos necesarios
Información	Utilidad
Ventas y fechas	Identificar ingresos generados
Medios y condiciones de pago	Conocer cuándo se cobra
Liquidaciones de tarjetas	Medir acreditaciones
Cuentas por cobrar	Identificar pendientes
Cuentas por pagar	Proyectar obligaciones
Gastos fijos y variables	Proyectar egresos
Saldos bancarios y caja	Conocer liquidez inicial
Inversiones y flujos incrementales	Calcular recuperación

Una distinción que considero fundamental
Este bloque responde tres preguntas financieras que no deberían confundirse:
1. Rentabilidad: ¿ganamos dinero?
2. Liquidez: ¿tenemos dinero disponible para pagar?
3. Recuperación: ¿cuánto tardamos en recuperar lo que invertimos?
Un negocio puede tener margen positivo, una cartera de clientes creciente y ventas récord, pero quedarse sin caja porque cobra a 45 días y paga a 15.

