# I8. El mismo análisis en código

Estado: dictado completo; ejercicio pendiente. Aruera se retoma cuando el alumno quiera. I9 se abrió el 2026-10-27.
Fase I — Herramientas al servicio de la pregunta.

## Qué tiene que quedarte de esta primera vuelta

El código es el análisis escrito para que una máquina lo corra. Se lee como los pasos: qué archivo abre, qué filas se quedan, qué suma y qué resta. Que corra y que imprima un número no dice que haya contestado la pregunta. La herramienta puede escribir un código que termina bien y suma otra cosa.

En esta vuelta no se aprende el lenguaje entero, y no se le encarga a la herramienta que explore por su cuenta.

## La clase

El momento en el que el código se vuelve peligroso es cuando el número salió de una máquina y la reunión lo trata como revisado. Alguien dice “la herramienta lo calculó: son 3.000”. El código corrió. Nadie leyó qué filas sumó.

Conviene empezar por la palabra, con el kiosco de tres cafés cobrados y dos de cortesía, todos a 600. Tres por 600 son 1.800. Cinco por 600 son 3.000. El código es esos pasos escritos para que la máquina los haga. Está en R, el lenguaje que este momento del mapa deja para leer un análisis. `cafes$pesos` es la columna de los pesos. La línea que suma toda la columna no pregunta si el café se cobró:

```r
sum(cafes$pesos)
```

Imprime 3.000. Corrió bien. La pregunta era lo cobrado en el mostrador. La línea que se queda con esas filas es otra. `cobrado == "si"` quiere decir: el café se cobró. Los corchetes se quedan con esas filas.

```r
cobrados <- cafes[cafes$cobrado == "si", ]
sum(cobrados$pesos)
```

Imprime 1.800. Leer el código es mirar si esa línea está. Si no está, la máquina suma la cortesía y el número sale igual de prolijo.

Conviene mirarlo en un caso concreto. Guayabo hace service. En marzo la pregunta fue cuánto quedó de lo terminado y cobrado, después de la combi. El archivo es el export del 2 de abril y tiene solo marzo. Cada trabajo está anotado a 4.000. Hay 6 cobrados, 2 impagos y 3 cancelados.

Seis por 4.000 son 24.000. La combi sale 15.000. Quedan 9.000. Los impagos son 8.000 y los cancelados son 12.000. Seis más dos más tres son 11 trabajos. Once por 4.000 son 44.000.

La herramienta escribe esto, y la reunión lee el 29.000 que imprime:

```r
pedidos <- read.csv("guayabo-marzo-export-2026-04-02.csv")
alquiler <- 15000
sum(pedidos$pesos) - alquiler
```

La primera línea abre el archivo de marzo. Esa parte está bien: tiene la fecha. La segunda deja la combi a la vista, con nombre. Quince mil son la combi de marzo, no un número escondido. La tercera suma toda la columna de pesos y le resta la combi. Cuarenta y cuatro mil menos 15.000 son 29.000. No hay una línea que se quede con `estado == "cobrado"`. Los 2 impagos y los 3 cancelados entran en la suma. Son 5 trabajos de más, 20.000. Nueve mil más 20.000 son los 29.000 que imprimió. El código terminó sin error. Contestó cuánto suman todos los trabajos anotados, menos la combi.

El mismo análisis, con la línea que la pregunta pide, queda así:

```r
cobrados <- pedidos[pedidos$estado == "cobrado", ]
sum(cobrados$pesos) - alquiler
```

Veinticuatro mil menos 15.000 son 9.000. Esa es la comprobación de marzo. Si el código imprime 29.000, no hace falta volver a sacar el archivo: falta el filtro. Si imprime 24.000, el filtro está y falta la combi. Si abre un archivo que se llama `datos.csv`, sin fecha, ni siquiera se sabe si marzo sigue solo.

Acá hay que frenar, antes de llevar los 29.000 a la reunión porque los imprimió una máquina. La herramienta escribió los pasos. Leerlos es la revisión. El archivo y la combi, en este código, se pueden seguir. La suma no se queda con lo cobrado. En abril, si se copia este código, la combi sigue en 15.000 aunque la combi de abril sea otra, y las filas de abril se suman todas.

Lo que esta clase no hace es recorrer R, ni escribir un programa desde cero, ni pedirle a la herramienta que busque ella la pregunta. El curso de R, al lado, sirve para repetir esta lectura. El trabajo final de ese curso es del caso de cierre, no de esta vuelta. Tampoco se decide todavía qué archivos del negocio no se le entregan. El trabajo de ahora es no firmar un número porque el código corrió.

Se puede decir que el código de la herramienta imprime 29.000, que son las 11 filas menos la combi, y que lo cobrado menos la combi son 9.000. No se puede llevar los 29.000 como si fueran marzo. No se puede dar por revisado un código porque no tiró un error.

Ahí está el criterio de esta clase. **El código se lee como los pasos. Que corra y que imprima un número no dice que haya contestado la pregunta.**

Lo que sigue es tuyo. No voy a decirte qué imprime el código de Aruera ni cuánto queda de verdad. Cuando respondas, te voy a marcar si cada línea te quedó leída como un paso, si el número que imprime te quedó separado del número de la pregunta, si te quedó dicho qué línea falta, y dónde un código que terminó bien se llevó a la reunión. Según eso, seguimos dentro de I8.

## Ejercicio

Aruera reparte pedidos. En junio la pregunta fue cuánto quedó de lo entregado y cobrado, después del alquiler del puesto. El archivo es el export del 1 de julio y tiene solo junio. Cada pedido está anotado a 6.000. Hay 7 cobrados, 3 impagos y 1 cancelado. El alquiler de junio sale 20.000.

La herramienta escribe esto y la reunión quiere llevar el número que imprime:

```r
pedidos <- read.csv("aruera-junio-export-2026-07-01.csv")
alquiler <- 20000
sum(pedidos$pesos) - alquiler
```

Respondé en prosa, con párrafos, como si le contestaras a quien está por llevar ese número. Necesito estas cuatro cosas, desarrolladas, no en una lista de consignas.

Primero, qué hace cada línea y cuánto imprime ese código.

Segundo, cuánto queda si la pregunta se respeta: solo lo cobrado, menos el alquiler.

Tercero, qué línea no está, y qué filas están entrando de más en el número que imprime.

Cuarto, qué decisión no sale de ese código. No lleves el número impreso a la reunión. No lo des por revisado porque corrió. No reescribas el lenguaje ni recorras R. Si proponés la línea que falta, va dentro del párrafo.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
