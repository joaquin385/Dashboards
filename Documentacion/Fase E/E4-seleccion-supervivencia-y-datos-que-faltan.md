# E4. Sesgo de selección, supervivencia y datos que faltan con un patrón

Estado: dictado completo; ejercicio pendiente. Trigo se retoma cuando el alumno quiera. E5 se abrió el 2026-10-24.
Fase E — Qué se puede afirmar.
Área: causalidad, sesgos y calidad de la evidencia.

## Qué tiene que quedarte de esta primera vuelta

En E3, dejar quieto servía cuando el nodo era una causa de los otros dos. Acá las dos flechas entran. El nodo es la puerta del archivo: queja, sigue empleado, contestó. Mirar solo las filas en las que esa puerta se abrió es un recorte. Adentro, dos cosas pueden verse pegadas, o una puede desaparecer, porque la otra era la única manera de entrar. Afuera, esa pegadura no está.

El sesgo de selección es ese recorte cuando la puerta es “pasó el filtro”. El sesgo de supervivencia es el mismo recorte cuando la puerta es “todavía está”. Los datos que faltan con un patrón son los huecos que quedaron justo porque algo pasó: el vacío no es un azar, y llenarlo con el promedio de los que sí están copia a los que pasaron la puerta.

En esta vuelta no se calcula una probabilidad condicionada, no se completa el hueco con una fórmula y no se dice que el filtro haya causado el resultado.

## La clase

El momento en el que un archivo se vuelve peligroso es cuando la reunión olvida la puerta y lee lo de adentro como si fuera el mundo. Alguien abre las quejas y dice: “Los que llegan a tiempo vienen rotos. Hay que apurarse menos.” Los que llegaron a tiempo y enteros no están en esa mesa. No llegaron a la queja. La frase describe a quien pudo entrar, no a los envíos.

Conviene empezar por el dibujo, con diez envíos. Una queja se abre si el pedido llegó tarde o si llegó roto, o las dos cosas. De los diez, uno llegó tarde y roto, dos llegaron tarde y enteros, dos llegaron a tiempo y rotos, y cinco llegaron a tiempo y enteros. La puerta es la queja. El dibujo tiene las dos flechas entrando:

```
demora ──► queja ◄── rotura
```

Eso no es un confusor. En el confusor, las flechas salían. Acá entran. El nodo del medio es una consecuencia de los otros dos. Quedarse solo con las filas en las que la queja es sí es el recorte: se cierra el camino de los cinco que no tienen nada que reclamar.

Esos cinco no están. En la mesa quedan cinco quejas. De las tres que llegaron tarde, una está rota. De las dos que llegaron a tiempo, las dos están rotas. Adentro del archivo, llegar a tiempo y venir roto van juntos. Afuera no. Los cinco enteros y puntuales son la mayoría del mundo, y no tienen fila. La pegadura se fabricó en la puerta: si no llegaste tarde, la única manera de estar en la queja era llegar roto.

Ese recorte, cuando la puerta es un filtro que deja afuera a una parte del mundo, es el sesgo de selección. Lo que se ve adentro se inclina hacia quien pudo pasar. No hace falta que nadie haya elegido mal a propósito. Alcanza con que la fila exista solo si ocurrió una de las dos cosas.

El sesgo de supervivencia es la misma puerta con otro nombre: “todavía está”. Se mira a los repartidores que siguen en diciembre y se dice cómo es el equipo. Los que echaron en julio, porque rompían paquetes, no llegan a diciembre. El equipo que queda se ve cuidadoso. El cuidado que se lee puede ser el filtro, no la receta. Quien no sobrevivió no está para desmentir el retrato.

Los datos que faltan con un patrón son los huecos que dejó esa puerta. No es una celda vacía porque alguien se olvidó de tipear. Está vacía porque el caso no entró, o porque el que tenía el problema no contestó. El vacío informa. Si se lo llena con el promedio de las celdas llenas, se les copia a los que no pasaron el número de los que sí pasaron. En D3, la tasa de los que contestaron no se les prestaba a los que no contestaron. Acá el problema es anterior: la relación entre las filas que sí tenés ya puede estar doblada por la puerta. Aunque no generalices, lo de adentro puede no ser el mundo.

Conviene mirar esto en un caso concreto. Porche reparte muebles. En octubre hubo 100 envíos. En la reunión de noviembre abren el archivo de quejas y dicen: “Cuando el envío llega a tiempo, viene roto. De las quejas a tiempo, las 16 están rotas. De las quejas que llegaron tarde, solo 4 de 20 están rotas. Llegar a tiempo viaja con la rotura. Aflojemos el horario: los que se demoran casi no rompen.”

Los 100 envíos, antes de la puerta, son estos. Tarde y roto: 4. Tarde y entero: 16. A tiempo y roto: 16. A tiempo y entero: 64. Llegaron tarde 20. De esos 20, 4 están rotos: 20 de cada 100. Llegaron a tiempo 80. De esos 80, 16 están rotos: también 20 de cada 100. En el mes, la rotura no cambia con la demora. Van cada una por su lado.

La queja se abre si hubo demora o hubo rotura. Entran los 4 que tuvieron las dos, los 16 que solo se demoraron y los 16 que solo se rompieron. Son 36 filas. Los 64 que llegaron a tiempo y enteros no entran. El camino de esos 64 a la reunión está cerrado. El dibujo es el de los diez envíos, ahora con el mes entero:

```
demora ──► queja ◄── rotura
```

Adentro de las 36, la cuenta de la reunión es cierta y está mal leída. Los envíos a tiempo que lograron entrar son 16, y los 16 están rotos, porque sin la rotura no había puerta. Los envíos tarde que entraron son 20, y solo 4 están rotos. Parece que la puntualidad viaja con la rotura, y que la demora viaja con el mueble entero. Esa pegadura no está en los 100. Está en la puerta. Aflojar el horario para romper menos usa una asociación que el filtro fabricó. En el mes, llegar tarde o no no separa la rotura: las dos están en 20 de cada 100.

La supervivencia aparece en el mismo equipo, con otra puerta. Porche tenía 10 choferes en enero. En julio echó a 4. Los 4 habían roto al menos un mueble. En diciembre quedan 6. De esos 6, uno rompió algo y cinco no. La reunión mira a los que siguen y dice: “El equipo rompe poco. Uno de seis. Copiemos la recorrida de estos seis.” Uno de seis es verdad de quien sobrevivió. De los 10 que empezaron el año, rompieron 5. Los 4 que ya no están se fueron por eso, y por eso no llegan al retrato. El dibujo es el mismo tipo de puerta:

```
rotura ──► sigue en diciembre ◄── el resto de las razones para quedarse
```

Quedarse solo con “sigue en diciembre = sí” cierra el camino de los echados. La recorrida de los seis puede ser buena por otra cosa. Estos papeles no la eligen. Muestran un equipo adelgazado por la misma rotura que la reunión dice que casi no ocurre.

La encuesta cierra el tercer hueco. Se la mandaron a los 100 envíos. Contestaron los 64 que llegaron a tiempo y enteros, y pusieron un 9. Los 36 de la queja no contestaron. El promedio de lo que hay es 9. Publicar “la satisfacción de octubre es 9” llena el mes con quien no tuvo nada que reclamar. El hueco no es un olvido de carga. Falta porque hubo demora o rotura, que es justo lo que una nota de satisfacción tendría que poder bajar. Copiar el 9 en esas 36 celdas les presta a los problemas la nota de los que no los tuvieron. Dejar el 9 como nota del mes hace lo mismo, sin escribirlo.

Acá hay que frenar, antes de aflojar el horario y antes del 9 en el informe. Aflojar no sale de las 16 roturas a tiempo, porque esas 16 son la puerta, no el mes. El uno de seis no es la rotura del equipo: es la rotura de quien no fue echado. El 9 no es octubre: es el puntaje de los 64 que no tenían una queja que los hiciera callar. Lo que sí se puede decir es más chico. En los 100, la rotura es 20 de cada 100 con demora y 20 de cada 100 sin demora. Hay 36 quejas, y cada una es un envío con al menos un problema, que se puede revisar como problema, no como retrato del mes. Los 4 choferes que ya no están se cuentan si se quiere hablar de rotura. La encuesta se publica como la nota de quien contestó, con la puerta escrita al lado.

Lo que esta clase no hace es calcular la probabilidad de una rotura “dado que” hubo queja, ni completar las 36 celdas con un modelo. Esa lectura de un resultado dentro de otro archivo es la clase siguiente. Tampoco se decide si la prisa causa roturas en otro mes. Acá el límite es la puerta. Si las dos flechas entran al nodo que te dejó las filas, lo que ves adentro puede ser el filtro. Si la puerta es “todavía está”, el retrato es de los que duraron. Si el hueco coincide con el problema, el promedio de lo lleno no se sienta en lo vacío.

Ahí está el criterio de esta clase. **Antes de leer una asociación, se dibuja la puerta del archivo. Si las dos flechas entran a esa puerta, el recorte puede pegar adentro lo que afuera va cada uno por su lado.** Selección, supervivencia y hueco con patrón son esa puerta con tres nombres: pasó el filtro, todavía está, y el vacío quedó justo ahí. La frase se achica hasta quien entró, o se vuelve a abrir el camino de quien no entró. No se publica lo de adentro como si la puerta no hubiera estado.

Lo que sigue es tuyo. No voy a leer el diciembre de Trigo como si fueran todas las panaderías. Cuando respondas, te voy a marcar si las dos flechas te entraron a la puerta, si lo que solo es cierto entre los que siguen te quedó separado de lo que pasa entre los que empezaron, si el hueco de la nota te quedó con un patrón y no como un olvido, y dónde un retrato de sobrevivientes te autorizó una visita. Según eso, seguimos dentro de E4.

## Ejercicio

Trigo les vende harina a panaderías. En enero había 80. En diciembre siguen 25. Las otras 55 dejaron de comprar. En la reunión miran solo a las 25 y dicen: “De las que siguen, 15 tuvieron visita del vendedor y 10 no. Casi todas las que duran fueron visitadas. Y las 10 que siguen sin visita son todas del barrio del depósito. La visita retiene, y sin visita solo se quedan los vecinos. Hay que visitar al resto y dejar de insistir fuera del barrio. La satisfacción es 8.”

Esas 25 que siguen pusieron un 8. Las 55 que se fueron no tienen nota.

Las 80, contadas enteras, son estas. Con visita y siguen: 15, ninguna es del barrio del depósito. Con visita y se fueron: 15. Sin visita, del barrio, y siguen: 10. Sin visita, del barrio, y se fueron: 5. Sin visita, de otro barrio, y siguen: ninguna. Sin visita, de otro barrio, y se fueron: 35.

Respondé en prosa, con párrafos, como si le contestaras a quien quiere visitar a todas y publicar el 8, y después me dejaras el dibujo de la puerta. Necesito estas cuatro cosas, desarrolladas, no en una lista de consignas.

Primero, el dibujo de quién entra al archivo de diciembre. Qué nodo es la puerta, qué dos flechas le entran, y a quién se le cierra el camino.

Segundo, qué es cierto solo entre las 25 que siguen, y qué se ve cuando se cuentan también las 55 que se fueron. La visita y el barrio tienen que aparecer en las dos lecturas.

Tercero, por qué el hueco de la nota no es un olvido de carga, y qué se les hace a las 55 si el 8 de las 25 se publica como la satisfacción de las 80.

Cuarto, qué decisión no sale de este archivo. No visites al resto porque las que duran fueron visitadas. No dejes el otro barrio porque, entre las que siguen, las no visitadas son vecinas. No publiques el 8 como la nota del año.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
