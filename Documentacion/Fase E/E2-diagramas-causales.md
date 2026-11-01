# E2. Diagramas causales

Estado: dictado completo; ejercicio pendiente. Yeso se retoma cuando el alumno quiera. E3 se abrió el 2026-10-24.
Fase E — Qué se puede afirmar.
Área: causalidad, sesgos y calidad de la evidencia.

## Qué tiene que quedarte de esta primera vuelta

Un diagrama causal es la causa escrita como dibujo. Un nodo es una variable, algo que se puede nombrar y que puede tomar valores. Una flecha es una causa que se afirma: de quién sale y a quién entra. No es una asociación que se vio. La ausencia de una flecha también se afirma: en ese dibujo, eso no produce aquello.

Tres dibujos con los mismos nombres pueden ser tres decisiones distintas. Una cadena, una causa común y una flecha al revés no se contratan igual. En esta vuelta no se pone un peso sobre la flecha, no se borra un nodo para ver qué queda y no se elige cuál dibujo es el verdadero.

## La clase

El momento en el que un diagrama se vuelve peligroso es cuando la reunión acuerda los nombres y no acuerda las flechas. Alguien dice “la visita y la facturación van juntas, así que contratemos”. Otro asiente. Los dos están hablando de visita y de facturación. Uno está afirmando que la visita produce la facturación. El otro puede estar afirmando que las dos salen de la licitación. Sin el dibujo, el asentimiento tapa que son dos causas distintas.

Conviene empezar por una palabra que vamos a usar toda la clase, con un ejemplo chico. Un diagrama causal es un dibujo de qué se afirma que produce qué. En un kiosco, la lluvia y la venta de paraguas suelen ir juntas. Eso, dicho así, es una asociación. El dibujo de una causa es este:

```
lluvia ──► venta de paraguas
```

El nodo de la izquierda es la lluvia. El nodo de la derecha es la venta. La flecha dice: afirmamos que la lluvia produce la venta. No dice “llovió y se vendió”. Si la flecha no está, el dibujo afirma otra cosa: la lluvia no produce la venta, al menos no por ese trazo. Un diagrama no es un adorno de la frase. Es la frase, con la dirección escrita.

Con esa flecha se pueden reconocer tres dibujos. Los tres usan lluvia, cartel y venta. No son el mismo argumento.

La cadena es una flecha que llega al final pasando por el medio. La lluvia hace que pongan el cartel, y el cartel produce la venta. La lluvia alcanza la venta solo porque pasa por el cartel.

```
lluvia ──► cartel ──► venta
```

Ese dibujo licencia hacer más carteles si se quiere vender más, porque hay una flecha del cartel a la venta. También dice que la lluvia no salta el cartel: sin el cartel, la lluvia no llega a la venta por este camino.

La causa común es un nodo con dos flechas que salen. La lluvia hace que pongan el cartel, y la lluvia hace que la gente compre paraguas. Entre el cartel y la venta no hay flecha.

```
        ┌──► cartel
lluvia ─┤
        └──► venta
```

El cartel y la venta igual viajan juntos: los dos días de lluvia hay cartel y hay venta. La asociación sigue en pie. La causa que el dibujo afirma no es la del cartel. Es la de la lluvia. Hacer más carteles en un día de sol no está escrito en estas flechas. No hay un trazo que lleve del cartel a la venta. Contratar carteles “porque cuando hay cartel se vende” lee la asociación y le pone una flecha que este dibujo no tiene.

La flecha al revés usa los mismos dos nodos y apunta para el otro lado. La reunión dice que el cartel produjo la venta. El dueño cuenta que puso el cartel después de ver la cola. El dibujo que sostiene ese relato es este:

```
venta ──► cartel
```

La cola produjo el cartel. El cartel no produjo la cola. La decisión de imprimir más carteles para armar la cola no sale de esta flecha. Sale de la flecha contraria, que este relato no afirma.

Fijate que los tres dibujos nombran las mismas cosas y no autorizan la misma acción. La cadena y una flecha directa del cartel a la venta autorizan el cartel. La causa común no. La flecha al revés tampoco. Antes de discutir cuánto vende el cartel, hay que escribir cuál de estos dibujos se está afirmando. Si no se puede señalar la flecha, no se sabe qué decisión está sobre la mesa.

Conviene mirar esto en un caso concreto. Ladrillo es el corralón del semestre pasado. Los meses con visitador facturaron en promedio 7.000.000, y los meses sin visitador, 4.100.000. La diferencia, 2.900.000, es la asociación. En la reunión de julio dicen: “La visita causa la venta. Hay que contratar dos visitadores.” Esa frase ya trae un dibujo, aunque nadie lo haya puesto en la pizarra:

```
visita ──► facturación
```

La flecha afirma que la visita produce la facturación. Contratar dos visitadores es actuar sobre el nodo de la izquierda esperando que se mueva el de la derecha. El 2.900.000 no se escribe sobre la flecha. El dibujo no dice cuánto. Dice qué se está afirmando. Ponerle el 2.900.000 encima es hacer pasar la asociación por el tamaño de la causa, y esa cuenta esta clase no la hace.

El semestre, mirado de nuevo, admite otro dibujo con los mismos meses. Cada mes con visita fue un mes de licitación, y cada mes sin visita fue un mes sin licitación. La causa común se dibuja así:

```
               ┌──► visita
licitación ────┤
               └──► facturación
```

La licitación manda al visitador y la licitación trae la compra de materiales. Entre visita y facturación no hay flecha. Las dos igual viajan juntas, y por eso el promedio de 7.000.000 cae en los meses de visita: esos meses son los de licitación. El dibujo afirma que la asociación sale de arriba, no de una flecha de la visita a la caja. Contratar visitadores para un mes sin licitación es pedir un efecto que esta figura no tiene dibujado.

Hay un tercer dibujo, y es el que la reunión suele creer que está diciendo cuando dice “la visita genera la obra”:

```
licitación ──► visita ──► facturación
```

Esa es una cadena. La licitación produce la visita, y la visita produce la facturación. Acá sí hay una flecha de la visita a la caja, y por eso este dibujo sí hablaría de mandar visitadores. No es el dibujo de la causa común, aunque use la misma palabra, licitación. En la cadena, la licitación llega a la plata pasando por la visita. En la causa común, la licitación llega a la plata por su propia flecha, y la visita es otra consecuencia, al lado. Las dos figuras tienen tres nodos. La decisión no es la misma. Conviene poder señalar cuál de las dos se está defendiendo antes de hablar de sueldos.

Marzo agrega la flecha al revés, en un pedido concreto. El 4 de marzo el visitador fue a la obra del parque. Esa obra compró 2.000.000, y la orden está fechada el 2 de marzo. La reunión dibuja:

```
visita ──► compra del parque
```

La fecha dibuja al revés:

```
compra del parque ──► visita
```

La compra ya estaba escrita cuando el visitador llegó. En ese pedido, la flecha de la visita a la compra no es la que el papel sostiene. No se bajan 2.000.000 de los 7.000.000 del mes para anotar un efecto. Se cambia la dirección de esa flecha, y se deja el resto del mes sin un número sobre ningún trazo.

Acá hay que frenar. La reunión puede seguir diciendo que “todo está relacionado”. Relacionado no es una flecha. Para contratar hacen falta la flecha de la visita a la facturación, y un mes en el que esa flecha no venga atada a la licitación. Ese mes no está. Mientras no esté, se pueden dejar los dos dibujos sobre la mesa, el de la cadena y el de la causa común, y decir en voz alta qué afirma cada uno. Elegir uno porque cierra la contratación es elegir el dibujo por la decisión, no la decisión por el dibujo.

Lo que esta clase no hace es borrar la licitación y recalcular los 7.000.000, ni declarar ganador uno de los dos dibujos. Cómo un tercer nodo mueve a los otros dos, y cómo se lee una flecha que apunta al revés cuando es el patrón y no un pedido suelto, se hace en la clase siguiente, sobre este mismo dibujo. Hay otra figura, con dos flechas entrando al mismo nodo, que aparece cuando el recorte de quién entra en el archivo cambia lo que se ve. Esa queda para cuando se hable de a quién se está mirando. Hoy alcanza con no firmar sueldos sobre una flecha que no se escribió, o sobre una flecha que el calendario apunta para el otro lado.

Ahí está el criterio de esta clase. **Antes de la decisión se dibujan los nodos y las flechas, y se dice en una oración qué produce qué.** Una cadena, una causa común y una flecha al revés pueden usar los mismos nombres y no autorizar la misma acción. La asociación no se anota sobre la flecha. Si no se puede señalar el trazo, no se sabe qué se está por hacer.

Lo que sigue es tuyo. No voy a dibujarte Yeso ni a elegir cuál de tus flechas es la verdadera. Cuando respondas, te voy a marcar si cada nodo es una variable, si cada flecha afirma una causa y no un “van juntos”, si la causa común te quedó sin flecha entre el descuento y la venta, si la factura anterior al cartel te dio vuelta la dirección, y dónde le pusiste un peso a un trazo. Según eso, seguimos dentro de E2.

## Ejercicio

Yeso vende pintura. En enero y febrero no hubo descuento y no hubo una obra en la esquina. Se facturó 4.000.000 y 4.200.000 pesos. En marzo y abril hubo descuento y hubo obra en la esquina. Se facturó 9.000.000 y 8.500.000 pesos.

En la reunión dicen: “El descuento causa la venta. Hay que dejarlo todos los meses.”

Dentro de los 9.000.000 de marzo hay una factura de un contratista por 3.000.000. Está fechada tres días antes de que se pegara el cartel del descuento.

Respondé en prosa, con párrafos, como si le estuvieras mostrando los dibujos a quien quiere dejar el descuento, y después me dejaras por escrito qué afirma cada flecha. Necesito estas cuatro cosas, desarrolladas, no en una lista de consignas. Los dibujos podés hacerlos con flechas, como los de la clase.

Primero, cuáles son los nodos. Cada uno tiene que ser una variable, no el argumento de la reunión.

Segundo, el dibujo que la reunión está usando cuando dice que hay que dejar el descuento todos los meses. Qué afirma cada flecha, en una oración.

Tercero, el dibujo de la causa común y el dibujo de la flecha al revés para la factura del contratista. En la causa común tiene que verse qué flecha no está. En la factura, tiene que verse para qué lado apunta el trazo.

Cuarto, qué decisión autoriza el dibujo de la reunión y qué decisión no autorizan los otros dos. No dejes el descuento todos los meses. No elijas cuál dibujo es el verdadero. No le pongas un peso a ninguna flecha.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
