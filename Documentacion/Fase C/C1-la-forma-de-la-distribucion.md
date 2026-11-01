# C1. La forma de la distribución

Estado: dictado completo; ejercicio pendiente. Viga se retoma cuando el alumno quiera. C2 se abrió el 2026-10-23.
Fase C — Leer un número sin dejarse engañar.
Área: estadística aplicada, en interpretación. No es una materia de combinatoria. El número se lee en un caso de negocio.

## Qué tiene que quedarte de esta primera vuelta

El promedio es un número útil y, a la vez, un número que puede describir a nadie. Multiplicado por la cantidad de casos, reconstruye el total. Eso siempre cierra. Lo que no siempre cierra es usarlo como si fuera “el cliente típico” o “el ticket del mes”. Cuando pocos casos se llevan una parte grande del total, el promedio se va con ellos. La mediana, los percentiles y una mirada a la cola dicen cómo es el montón, no solo cuánto suma.

En esta vuelta no se pide la fórmula del desvío de memoria ni se dibuja una campana. Se aprende a preguntar si el promedio está parado en el centro del negocio o arrastrado por unos pocos, y a no diseñar una promo, un stock o un descuento para un cliente que en la lista casi no existe.

## La clase

La Fase B enseñó a no leer un total contra el período equivocado, el calendario equivocado o el peso equivocado. Esta fase enseña a no leer un solo número como si resumiera a todos. El ticket promedio, el socio promedio, el día promedio: la reunión los usa como personas. Casi nunca lo son.

Antes del caso, las palabras, con una lista chica. Cinco tickets de una semana, en pesos:

10.000  
12.000  
13.000  
15.000  
100.000

El **total** es la suma: 150.000 pesos. Es un hecho, si esos cinco tickets están en el registro.

El **promedio**, también llamado media, es el total dividido por la cantidad de casos. Ciento cincuenta mil dividido cinco es 30.000. Esa es su virtud y su trampa. La virtud: cinco veces 30.000 vuelven a dar 150.000. El promedio **reconstruye el total**. Si la pregunta es cuánta plata entró, y se tiene el promedio y la cantidad, se recupera la suma. La trampa: 30.000 no es el ticket de nadie en esa lista. Cuatro tickets están entre 10.000 y 15.000. Uno está en 100.000. El 30.000 es un punto de equilibrio de la suma, no un cliente que se pueda ir a buscar a la tienda.

La **mediana** es el valor que queda en el medio cuando los casos se ordenan de menor a mayor. Con cinco tickets, el del medio es el tercero: 13.000. La mitad de los tickets es menor o igual que ese número, y la mitad es mayor o igual. La mediana no se va a 30.000 porque un ticket haya sido de 100.000. Si el 100.000 pasara a 1.000.000, el promedio saltaría y la mediana seguiría en 13.000. Por eso, cuando se pregunta cómo es “un ticket típico”, la mediana suele estar más cerca de esa frase que el promedio. No reconstruye el total. Cinco veces 13.000 son 65.000, no 150.000. Sirve para otra pregunta.

Un **percentil** corta la lista ordenada en un porcentaje. El percentil 50 es la mediana: la mitad quedó abajo. El percentil 90 es el valor que deja al 90% de los casos abajo y al 10% arriba. En la lista chica, con cinco tickets, los cortes finos no se ven bien. En una lista de cien, el percentil 90 es el ticket número 90, de menor a mayor. Sirve para decir “casi todos están debajo de tanto” sin usar el máximo, que puede ser un solo caso raro.

La **cola larga** es esa parte de la lista donde hay pocos casos y números muy altos, o a veces muy bajos. En los cinco tickets, el de 100.000 es la cola. Larga no quiere decir que haya muchos. Quiere decir que se estira lejos del montón. En ventas, la cola de arriba suele ser unos pocos clientes grandes, o unos pocos días de evento, o un pedido excepcional. El promedio camina hacia esa cola. La mediana se queda en el montón.

La **concentración** es cuánta parte del total se llevan esos pocos. En la lista chica, un ticket de cinco se lleva 100.000 de 150.000: dos tercios de la plata, un quinto de los tickets. Eso es concentración. No es lo mismo que cola: puede haber cola con poca plata si el número alto no pesa tanto, y puede haber concentración sin un único extremo si diez clientes se llevan la mitad. En la práctica suelen venir juntas. La pregunta útil es: de la facturación, ¿cuánto está en los diez más grandes, o en el 10% de arriba?

El **desvío**, en esta clase, nombra si los casos están pegados al centro o lejos. No hace falta, hoy, elevar al cuadrado ni sacar raíz. Con los cinco tickets se ve a ojo: cuatro están cerca de 13.000 y uno está a 87.000 de distancia. La lista está abierta. Si los cinco hubieran sido 29.000, 30.000, 30.000, 30.000 y 31.000, el promedio seguiría cerca de 30.000 y los casos estarían pegados. El mismo promedio describe dos negocios distintos. Un desvío chico dice que el promedio, además de reconstruir el total, se parece a casi todos. Un desvío grande dice que el promedio reconstruye el total y no se parece a casi nadie. El número exacto del desvío se puede calcular después. El juicio de esta clase es si la lista está pegada o abierta.

Conviene verlo en un caso concreto. Clavo vende herrajes a constructoras, ferreterías y a un par de cadenas. En la reunión de noviembre dicen: “El ticket promedio de octubre fue 80.000 pesos. El cliente tipo compra por 80.000. Armemos una promo de 10% a partir de 70.000, que es lo que mueve a nuestra base.”

El sistema muestra 100 clientes que compraron en octubre. La facturación total fue 8 millones. El promedio cierra: 8 millones / 100 = 80.000. Esa cuenta es correcta y reconstruye el total. Cien veces 80.000 son 8 millones. Hasta ahí, el promedio hizo su trabajo.

Se ordenan los 100 tickets de menor a mayor. La mediana, el ticket 50 y el 51, está en 25.000 pesos. El percentil 90 está en 60.000: noventa clientes compraron 60.000 o menos. Los diez de arriba compran más. De esos diez, dos cadenas compraron 1,5 millones cada una. Tres millones en dos clientes. El resto de los diez se reparte 1,5 millones. Los 90 de abajo, entre todos, facturan 3,5 millones.

El “cliente tipo” de 80.000 no está en el montón. El montón está cerca de 25.000. Noventa de cada cien ni siquiera llegan a 60.000. La promo a partir de 70.000 no mueve a la base. Mueve, si mueve a alguien, a quienes ya están en la cola, que son pocos y ya compran grande. Puede ser una buena promo para las cadenas. No es una promo para “nuestra base”, porque esa frase usaba el promedio como si fuera la mediana.

La concentración se puede decir en una oración. Dos clientes de cien se llevan 3 millones de 8: más de un tercio de la plata. Diez clientes se llevan 4,5 millones: más de la mitad. Eso no es un detalle del informe. Es el riesgo del negocio. Si una de las dos cadenas deja de comprar, como el cliente grande de La Esquina, el promedio se cae y el montón de ferreterías puede no haberse movido. Un tablero que solo muestra 80.000 no avisa. Un corte que muestra mediana, percentil 90 y la parte del total en los diez de arriba, sí.

Hay un uso del promedio que sigue siendo el correcto, y conviene no tirarlo. Si Clavo quiere saber cuánto facturó y solo le pasan “100 clientes a 80.000”, recupera los 8 millones. Si quiere cargar 8 millones en un presupuesto y repartir por mes, el promedio por día hábil puede alcanzar, con el calendario de B2. El promedio no es un enemigo. Es una herramienta de total. Se vuelve enemigo cuando se lo viste de persona: el ticket tipo, el socio tipo, el usuario medio que recorre el embudo.

El embudo de A7 puede pecar de lo mismo. Una conversión del 2% es un promedio de visitas. Puede ser que un canal convierta el 8% y otro el 0,5%, y que el 2% no describa ninguno. Eso es C5, segmentar. Hoy alcanza con el mismo ojo: un promedio es un total disfrazado de caso. Antes de usarlo como caso, se mira si los casos se parecen.

La forma, dicha en prosa, es esta. Se ordena la lista. Se mira el medio, la mediana. Se mira un corte alto, el percentil 90 o los diez más grandes. Se mira qué parte del total se llevan. Se compara ese retrato con el promedio. Si promedio y mediana están cerca, y la cola no se lleva la plata, el promedio puede hablar por el montón. Si el promedio está lejos de la mediana y unos pocos se llevan un tercio o más, el promedio habla por el total y miente sobre el montón. En ventas de empresas a empresas, en mayoristas, en software por contrato, en un restaurante con un cliente corporativo, esa segunda forma es la habitual. En una panadería de mostrador, con tickets parecidos, la primera es más frecuente. El rubro no decide. La lista sí.

Ahí está el criterio de esta clase. **El promedio reconstruye el total: cantidad por promedio da la suma.** No describe al caso típico cuando hay cola y concentración. La mediana y los percentiles describen el montón. La parte del total que se llevan los pocos de arriba describe el riesgo. Un desvío grande es la señal de que el promedio y el montón no son el mismo retrato. La promo, el stock y el “cliente tipo” se arman con el retrato que corresponde a la pregunta, no con el único número que reconstruye la suma.

Lo que sigue es tuyo. No voy a leerte la lista de Viga. Cuando respondas, te voy a marcar si usaste el promedio como persona, si la mediana y la concentración estaban en la mesa y las ignoraste, y qué acción ataste al total disfrazado de típico. Según eso, seguimos dentro de C1.

## Ejercicio

Viga vende materiales a obras y a particulares. En la reunión de noviembre dicen: “El ticket promedio de octubre fue 120.000 pesos. El cliente tipo está en 120.000. Bajemos 8% el precio de lista, que es lo que necesita esa base para volver a comprar como en septiembre.”

Octubre: 50 clientes, 6 millones de facturación corriente. El promedio cierra en 120.000.

Lista ordenada, resumida:

- Los 40 tickets más chicos van de 8.000 a 40.000. La mediana queda en 22.000.
- El percentil 90 queda en 80.000.
- Los 5 tickets más grandes suman 4,2 millones. De esos cinco, uno solo, una obra, facturó 2,4 millones.

Septiembre había tenido 52 clientes y 5,8 millones. Nadie abrió septiembre con la misma lista. Nadie trajo unidades ni costos.

Respondé en prosa, con párrafos. Necesito estas cuatro cosas.

Primero, qué reconstruye el 120.000 y qué no describe, con estos cortes.

Segundo, qué retrato dan la mediana, el percentil 90 y los 4,2 millones de los cinco de arriba. Decí si hay cola y si hay concentración.

Tercero, por qué un 8% de descuento “para la base de 120.000” no apunta al montón, y a quién podría estarle hablando.

Cuarto, qué dato faltaría para saber si septiembre era un mes de montón parecido o un mes sin la obra de 2,4 millones, y por qué el total de 5,8 no alcanza.

No elijas si hay que bajar el precio. No inventes las unidades.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
