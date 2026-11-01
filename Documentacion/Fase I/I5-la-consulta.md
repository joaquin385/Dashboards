# I5. La consulta

Estado: dictado completo; ejercicio pendiente. Jarilla se retoma cuando el alumno quiera. I6 se abrió el 2026-10-27.
Fase I — Herramientas al servicio de la pregunta.

## Qué tiene que quedarte de esta primera vuelta

Una consulta es la pregunta escrita para que la tabla la conteste igual cada vez. Filtrar dice qué filas quedan. Agrupar dice el grano del resultado: una fila por local, no una por pedido. Cruzar escribe la regla con la otra lista. Una suma sin esas tres partes responde otra pregunta.

En esta vuelta no se dibuja el gráfico, no se recorre cada comando, y los ejercicios cortos de SQLBolt quedan para repetir la sintaxis después de esta pregunta.

## La clase

El momento en el que una consulta se vuelve peligrosa es cuando el número ya salió y la reunión lo usa. Alguien dice “cobramos 48.000” porque la suma de la tabla dice 48.000. La consulta sumó todo lo que estaba escrito. La pregunta era otra.

Conviene empezar por la palabra, con un kiosco y cuatro cafés. Dora pidió uno en el mostrador, de 500. Ema pidió uno en el mostrador, de 500. Dora pidió otro por la aplicación, de 700. Fran pidió uno por la aplicación, de 500. Cuatro filas. Quinientos más quinientos más setecientos más quinientos son 2.200.

La pregunta es cuánto vendió el mostrador. Una consulta es esa pregunta, escrita. Filtrar es la parte que dice qué filas quedan. Quedan las dos en las que el canal es el mostrador: 500 y 500, o sea 1.000. Sin ese filtro, la suma sigue en 2.200 y le pone el nombre del mostrador.

```sql
SELECT SUM(pesos) FROM cafes WHERE canal = 'mostrador';
```

`WHERE` es el filtro. `SUM` suma la columna que se le dice. Lo que no es mostrador no entra.

Conviene mirarlo en un caso concreto. Molle reparte viandas y tiene dos tablas. En `pedidos`, cada fila es un pedido.

Norte: Paz, entregado, 8.000. Ramiro, entregado, 8.000. Selva, pendiente, 8.000.

Sur: Tadeo, entregado, 8.000. Uma, cancelado, 8.000. Vasco, entregado, 8.000.

Seis por 8.000 son 48.000. La reunión corre esto y lee el cobro de la semana:

```sql
SELECT SUM(pesos) FROM pedidos;
```

Esos 48.000 suman a Selva, que sigue pendiente, y a Uma, que se canceló. No es lo cobrado.

La pregunta, dicha antes de escribir, es cuánto se cobró de lo que sí se entregó, separado por local. Primero el filtro. Entregado es Paz, Ramiro, Tadeo y Vasco. Cuatro por 8.000 son 32.000. Selva y Uma quedan afuera.

```sql
SELECT SUM(pesos) FROM pedidos WHERE estado = 'entregado';
```

Esos 32.000 son lo entregado. Vasco está adentro y todavía no pagó. Entregado no es cobrado.

Hace falta un número por local. Agrupar es eso: el resultado pasa a tener una fila por local, no una por pedido. El grano de la respuesta es el local.

```sql
SELECT local, SUM(pesos)
FROM pedidos
WHERE estado = 'entregado'
GROUP BY local;
```

Norte suma a Paz y a Ramiro: 16.000. Sur suma a Tadeo y a Vasco: 16.000. El 16.000 de Sur sigue contando un entregado que no se cobró.

Los cobros están en otra tabla, `cobros`, una fila por persona: Paz, Ramiro, Tadeo, Uma y Wanda, 8.000 cada una. Cinco por 8.000 son 40.000. Wanda no tiene pedido. Uma pagó y el pedido se canceló. Vasco entregó y no está en esta tabla. Sumar `cobros` da 40.000 y tampoco es la pregunta.

El cruce se escribe con `JOIN` y la regla va en `ON`. La regla es el nombre, la misma de las dos listas. Cada persona está una vez en `cobros`. Si alguien estuviera dos veces, su pedido se repetiría en el resultado y la suma lo contaría dos veces.

Sin el filtro, el cruce se queda con quien está en las dos tablas: Paz, Ramiro, Tadeo y Uma. Uma entra porque pagó, aunque el pedido esté cancelado. Con el filtro de entregado, Uma sale. Vasco no está en `cobros`, así que sale. Wanda no está en `pedidos`, así que sale.

```sql
SELECT local, SUM(pedidos.pesos)
FROM pedidos
JOIN cobros ON pedidos.persona = cobros.persona
WHERE pedidos.estado = 'entregado'
GROUP BY local;
```

Norte: Paz y Ramiro, 16.000. Sur: Tadeo, 8.000. Dieciséis mil más ocho mil son 24.000. Eso es lo entregado y cobrado, por local.

Si la pregunta fuera a quién hay que cobrarle, Vasco tiene que seguir en el resultado aunque el cobro esté vacío. Esta consulta lo deja afuera. Sirve para lo que se cobró de lo entregado. No sirve para armar la lista de deuda.

Acá hay que frenar, antes de cerrar la semana en 48.000, o en los 32.000 de lo entregado, o en los 40.000 de la tabla de cobros. Las tres sumas están bien hechas. Ninguna es la pregunta. La consulta que la escribe filtra entregado, cruza por el nombre y agrupa por local: 16.000 en Norte y 8.000 en Sur.

Lo que esta clase no hace es recorrer el resto de los comandos, ni anidar una consulta adentro de otra, ni dibujar estas barras. SQLBolt, al lado, sirve para repetir filtro, grupo y cruce con otras tablas chicas. No reemplaza la pregunta de Molle. Tampoco se limpia un nombre escrito de dos maneras: si Paz estuviera como “Paz” y como “PAZ”, el `ON` no las junta, y eso se resuelve antes de escribir, no con una suma más larga.

Se puede decir que la tabla de pedidos suma 48.000, que lo entregado suma 32.000, que los cobros suman 40.000, y que lo entregado y cobrado son 16.000 en Norte y 8.000 en Sur. No se puede cerrar la semana con la primera suma. No se puede usar esta consulta para ir a buscar a Vasco.

Ahí está el criterio de esta clase. **La consulta escribe la pregunta: qué filas quedan, en qué grano se agrupan y con qué otra lista se cruzan.** Una suma sin esas tres partes responde otra cosa.

Lo que sigue es tuyo. No voy a decirte cuánto cobró Jarilla. Cuando respondas, te voy a marcar si el filtro te quedó en las filas que salen, si el grupo te quedó en un número por local y no en el total pelado, si el cruce te quedó en el nombre y con las personas que se caen, y dónde una suma bien hecha cerró una pregunta que no era la de la consulta. Según eso, seguimos dentro de I5.

## Ejercicio

Jarilla reparte almuerzos. La pregunta, dicha antes de escribir, es cuánto se cobró de lo que sí se entregó, separado por local.

En `pedidos`, cada fila es un pedido de 5.000. Centro: Iris, entregado. Joaco, entregado. Kenia, pendiente. Costa: Lara, entregado. Mauro, cancelado. Nina, entregado.

En `cobros`, una fila por persona y 5.000 cada una: Iris, Joaco, Lara, Mauro y Omar. Omar no tiene pedido. Nina no está en `cobros`. Mauro sí está: pagó, y el pedido se canceló.

En la reunión corren la suma de todos los pesos de `pedidos` y dicen que la semana está cobrada.

Respondé en prosa, con párrafos, como si le contestaras a quien está por cerrar la semana con esa suma. Necesito estas cuatro cosas, desarrolladas, no en una lista de consignas.

Primero, cuánto suma la tabla entera, qué filas deja afuera el filtro de entregado y cuánto queda después de ese filtro.

Segundo, cuánto suma cada local con ese filtro, y quién sigue adentro aunque no haya pagado.

Tercero, el cruce por el nombre con el filtro puesto: cuánto queda en cada local, y por qué se caen Mauro, Nina y Omar.

Cuarto, qué decisión no sale de la suma pelada. No cierres la semana con el total de `pedidos`. No uses la consulta de lo cobrado para ir a buscar a quien no pagó. No dibujes el gráfico ni recorras otros comandos. La consulta, si la escribís, va dentro del párrafo, no como una lista de órdenes.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
