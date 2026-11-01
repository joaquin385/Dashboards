Todo en una hoja:


1. ¿El período fue bueno o malo?
Gráfico: evolución temporal de ventas.

- Línea de ventas del período actual.
- Línea del período comparable anterior.
- Variación porcentual.
- Posibilidad de cambiar entre facturación, unidades y transacciones.
La grilla puede complementar mostrando el acumulado y la variación contra el período anterior.


2. ¿De qué está hecho el resultado?
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
Gráfico: mapa de calor (Heatmap). (de atributos)

La ventaja es que permite detectar concentraciones de problemas.

También incorporaría filtros o niveles de exploración:
- Canal.
- Local.
- Categoría.
- Producto.
No haría un gráfico distinto para cada dimensión.

E. ¿Un canal subió y otro bajó, escondidos en el total?
Gráfico: barras divergentes.
Las barras divergentes permiten visualizar rápidamente qué canales crecen y cuáles caen.

También agregaría el peso de cada canal en la facturación para evitar interpretar un crecimiento del 50% en un canal que representa apenas el 2% del negocio como algo determinante.

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

