# J2. Verificar el número y la fuente

Estado: dictado completo; ejercicio pendiente. Guaraniná se retoma cuando el alumno quiera. J3 se abrió el 2026-10-27.
Fase J — La IA como asistente de investigación.

## Qué tiene que quedarte de esta primera vuelta

Un número se verifica en el lugar del que dice salir. Ese lugar es la fuente: se abre y el número tiene que estar ahí, en las filas que la pregunta pidió. Si el lugar no se puede abrir, o se abre y el número no está, no quedó verificado. El código que la herramienta generó también es una fuente: se lee. Si la frase y el código dicen lo mismo, pueden estar diciendo los dos la cuenta que no era.

En esta vuelta no se mira si la herramienta eligió solo lo que confirma, y no se decide qué lista de personas no se le entrega.

## La clase

El momento en el que una fuente se vuelve peligrosa es cuando el número y la frase coinciden, y nadie abre el lugar del que dicen salir. La herramienta escribe: “Cobraste 50.000. El alquiler del rubro, según la cámara, es 10.000, así que te quedaron 40.000.” Al lado pega un código que imprime 40.000. La reunión se muda con ese resto. Las dos versiones se dan la razón. Ninguna abrió la factura.

Conviene empezar por la palabra, con un kiosco y un ticket. La herramienta dice: “El mostrador dejó 1.800. Fuente: el ticket del martes.” El ticket tiene tres cafés cobrados, a 600. Tres por 600 son 1.800. Se abre el ticket y el número está. Esa es una fuente, y el número quedó verificado.

En la frase siguiente dice: “En el barrio el café sale 900, según la cámara.” No hay página, ni fecha, ni una tabla donde buscar el 900. La cámara, dicha así, es un nombre. No es un lugar que se pueda abrir. El 900 no quedó verificado. Verificar es rehacer el número en el lugar que la frase nombra. Rastrear la fuente es encontrar ese lugar. Si no aparece, el número se queda sin fuente.

Conviene mirarlo en un caso concreto. Coronillo le pidió a la herramienta el mes de marzo. El archivo tiene importes y estado, sin nombres. Hay 6 pedidos cobrados a 5.000. Seis por 5.000 son 30.000. Hay 4 cancelados, anotados también a 5.000. Cuatro por 5.000 son 20.000. Diez pedidos por 5.000 son 50.000. La factura del alquiler, que está en la carpeta de marzo, dice 18.000. Lo cobrado menos esa factura es 30.000 menos 18.000, o sea 12.000.

La respuesta dice otra cosa. “Cobraste 50.000. El alquiler del rubro, según la cámara, es 10.000, así que te quedaron 40.000. Conviene mudarse a un local más grande.” El 50.000 sí está en el archivo: es la suma de las diez filas, cobradas y canceladas. No es lo cobrado. Lo cobrado son 30.000. El 10.000 de la cámara no está en el archivo, y no hay una página, una fecha ni una tabla. No se puede abrir. El alquiler que sí se puede abrir es la factura: 18.000.

El código que pegó debajo imprime los 40.000:

```r
sum(pedidos$pesos) - 10000
```

`pedidos$pesos` es la columna de todos los importes. La línea suma las diez filas, 50.000, y resta 10.000 escritos ahí, no leídos de la factura. Cincuenta mil menos 10.000 son 40.000. El código y la frase coinciden. Los dos hacen la misma cuenta, y los dos se saltan el filtro y la factura. Coincidir entre ellos no verifica nada. Verificar es abrir el archivo y la factura. Seis cobrados por 5.000 son 30.000. Menos 18.000 son 12.000.

Acá hay que frenar, antes de mudarse porque quedaron 40.000. Esos 40.000 salen de sumar los cancelados y de restar un alquiler que no tiene página. El mes, con lo cobrado y la factura, deja 12.000. La frase de la mudanza venía pegada al 40.000. Ya se frenó el salto a la decisión. Esta vuelta es la razón por la que ese 40.000 no sobrevive: la fuente del 50.000 son todas las filas, y la fuente del 10.000 no se puede abrir.

Lo que esta clase no hace es recorrer el lenguaje, ni salir a buscar si la herramienta ocultó los meses que no le convenían. Tampoco se pega una lista de clientes para “darle más contexto”. El archivo de Coronillo era importes y estado. El trabajo es no heredar un número que la frase y el código repiten y el lugar de origen no tiene.

Se puede decir que las diez filas suman 50.000, que lo cobrado son 30.000, que la factura dice 18.000 y que el mes deja 12.000. No se puede decir que quedaron 40.000. No se puede mudarse con el alquiler de una cámara que no se puede abrir. No se puede dar el código por revisado porque imprime lo mismo que la frase.

Ahí está el criterio de esta clase. **Un número se verifica en el lugar del que dice salir.** Si ese lugar no se abre, o se abre y el número no es el de la pregunta, no quedó verificado. El código es uno de esos lugares. Que coincida con la frase no lo vuelve la fuente.

Lo que sigue es tuyo. No voy a decirte cuánto le quedó a Guaraniná ni qué imprime su código. Cuando respondas, te voy a marcar si el número del archivo te quedó rehecho en las filas de la pregunta, si la fuente nombrada te quedó abierta o sin lugar, si el código te quedó leído aunque coincida con la frase, y dónde un número repetido dos veces se tomó por verificado. Según eso, seguimos dentro de J2.

## Ejercicio

Guaraniná le pidió a la herramienta el mes de junio. El archivo tiene importes y estado, sin nombres. Hay 7 pedidos cobrados a 3.000 y 3 que no se cobraron, anotados también a 3.000. La factura de la combi, en la carpeta de junio, dice 11.000.

La respuesta dice: “Facturaste 30.000. El reparto del sector, según el informe del gremio, es 6.000, así que te quedaron 24.000. Conviene sumar otra combi.” No hay página, ni fecha, ni tabla del informe. Debajo pega esto:

```r
sum(pedidos$pesos) - 6000
```

Respondé en prosa, con párrafos, como si le contestaras a quien está por sumar la otra combi con esos 24.000. Necesito estas cuatro cosas, desarrolladas, no en una lista de consignas.

Primero, cuánto suman todas las filas y cuánto suma lo cobrado.

Segundo, si el 6.000 tiene un lugar que se pueda abrir, y cuál es el costo de la combi que sí está en la carpeta.

Tercero, qué hace el código, cuánto imprime, y por qué coincidir con la frase no lo verifica.

Cuarto, qué decisión no sale de esa respuesta. No sumes la otra combi porque quedaron 24.000. No reemplaces la factura por el informe que no se puede abrir. No des el código por revisado porque imprime la misma cifra que el párrafo. No mires si la herramienta escondió otros meses, ni pegues nombres.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
