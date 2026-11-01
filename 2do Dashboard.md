1. ¿El período fue bueno o malo?
Gráfico: evolución temporal de ventas.

- Línea de ventas del período actual.
- Línea del período comparable anterior.
- Variación porcentual.
- Posibilidad de cambiar entre facturación, unidades y transacciones.
La grilla puede complementar mostrando el acumulado y la variación contra el período anterior.

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