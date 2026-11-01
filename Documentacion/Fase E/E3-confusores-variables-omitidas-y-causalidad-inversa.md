# E3. Confusores, variables omitidas y causalidad inversa

Estado: dictado completo; ejercicio pendiente. Soga se retoma cuando el alumno quiera. E4 se abrió el 2026-10-24.
Fase E — Qué se puede afirmar.
Área: causalidad, sesgos y calidad de la evidencia.

## Qué tiene que quedarte de esta primera vuelta

En el diagrama de E2, un confusor es la causa común: un nodo con flechas hacia los otros dos. Si ese nodo cambia de mezcla cuando comparás, la asociación que ves puede ser la de él, no la flecha que la reunión quiere contratar. Una variable omitida es un nodo que correspondía al dibujo y no está en la lámina. Si el que falta es el confusor, su horquilla queda escondida dentro de la flecha que sí dibujaron. La causalidad inversa es esa flecha apuntando al revés: el resultado produjo lo que la reunión llama causa.

Dejar quieto al confusor es comparar adentro de un mismo valor de ese nodo. Si ahí la flecha ya no separa, el salto de afuera no era esa flecha. En esta vuelta no se pone un peso definitivo sobre el trazo, no se borra el nodo con una fórmula y no se frena una consecuencia como si fuera una causa.

## La clase

El momento en el que un confusor se vuelve peligroso es cuando la reunión ve dos cosas juntas y le pone la flecha del medio, sin mirar de dónde salen las dos. Alguien dice “con el volante hay más encargos, así que el volante los produce”. El volante y los encargos van juntos. También van juntos con otra cosa, que estaba moviendo a los dos. La flecha del medio se queda con un trabajo que hizo el nodo de arriba.

Conviene empezar por una palabra que vamos a usar toda la clase, con un ejemplo chico. Un confusor es una causa común que queda mezclada en la comparación. Cuatro días. Dos de playa: hay helado y hay quemadura. Dos de oficina: no hay helado y no hay quemadura. La reunión dice que el helado produce la quemadura, y dibuja solo esto:

```
helado ──► quemadura
```

El sol no está en la lámina. En el mundo, el sol manda a la gente a la playa, donde hay helado, y el sol quema. El dibujo completo es la causa común de E2:

```
      ┌──► helado
sol ──┤
      └──► quemadura
```

El sol es el confusor. Helado y quemadura viajan juntos porque los dos salen de él. Comparar “días con helado” contra “días sin helado” es, en estos cuatro días, comparar playa contra oficina. No es una comparación en la que el sol se quedó quieto.

Una variable omitida es ese sol cuando no se lo dibujó. No es un misterio aparte del confusor. Es un nodo que el dibujo de la reunión dejó afuera. Si el nodo que falta apunta a los otros dos, la horquilla entra de contrabando en la única flecha que quedó escrita. Omitir un nodo del medio de una cadena es otra cosa: si el camino real fuera sol → helado → quemadura, sacar el helado del dibujo saltea un paso, no inventa una horquilla. El olvido que cambia la decisión es el primero. La lámina queda con una flecha que está haciendo el trabajo de dos.

La causalidad inversa no es un tercer nodo. Es la dirección entre los dos que ya estás mirando. El quiosco repone helado al final de un día de mucha venta. La reunión dibuja reposición → venta. El reloj dibuja venta → reposición. La flecha al revés de E2, cuando es el patrón y no un pedido suelto, se llama así.

Conviene mirar esto en un caso concreto. Teja repara techos. En dieciséis semanas, algunas dejó volantes en la cuadra y otras no. En la reunión dicen: “Las semanas con volante tuvieron 8 encargos nuevos. Las semanas sin volante, 4. El volante produce 4 encargos. Hay que imprimir todas las semanas.”

La lámina de esa frase es una sola flecha:

```
volante ──► encargos nuevos
```

Eso es lo que se ve si no se abre la semana. Ocho semanas con volante suman 64 encargos nuevos: 64 dividido 8 es 8. Ocho semanas sin volante suman 32: 32 dividido 8 es 4. La diferencia es 4. La asociación es real. La flecha es la que todavía no se ganó.

El nodo que la lámina omitió es la obra ya contratada en la cuadra. Es un techo firmado la semana anterior, antes de estos encargos nuevos. Cuando esa obra existe, Teja suele dejar volantes, porque ya está en la cuadra. Y cuando esa obra existe, los vecinos llaman más, porque ven la cuadrilla trabajando. El dibujo que devuelve el nodo a la página es este:

```
                         ┌──► volante
obra ya contratada ──────┤
                         └──► encargos nuevos
```

La obra es el confusor. Tiene flecha hacia el volante y flecha hacia los encargos. Entre volante y encargos, en este dibujo, no hay trazo. Dejarla afuera de la lámina fue omitirla. Los 4 encargos de la reunión pueden ser esa horquilla, contada como si fuera la flecha del volante.

Dejar quieto al confusor es no mezclar las semanas de obra con las otras. Se compara volante contra no volante adentro de las semanas que ya tenían obra, y se vuelve a comparar adentro de las que no tenían. Hacen falta las dos situaciones del volante en cada lado. Si todas las semanas de obra tuvieran volante, y ninguna de las otras lo tuviera, el confusor y el volante seguirían atados, y no habría cómo dejar la obra quieta.

En Teja sí se puede abrir. De las 8 semanas con obra ya contratada, 6 tuvieron volante y 2 no. Las 6 y las 2 tuvieron 10 encargos nuevos cada una. Diez contra diez. De las 8 semanas sin esa obra, 2 tuvieron volante y 6 no. Las 2 y las 6 tuvieron 2 encargos nuevos cada una. Dos contra dos.

El 4 de la reunión no aparece adentro. Aparece porque las semanas con volante son, en 6 de 8, semanas de obra, y las semanas sin volante son, en 6 de 8, semanas sin obra. El volante se llevó consigo las cuadras donde ya había un techo. Al dejar esa obra quieta, con volante y sin volante se ve el mismo número de encargos. Algunas de esas celdas tienen dos semanas. Dos semanas se mueven con un solo encargo de más. No se firma, con eso, que el volante sea inútil para siempre. Se firma que estos papeles no muestran los 4 encargos que la reunión le atribuye. El salto de afuera era la mezcla de la obra, no una flecha que sobreviva cuando la obra no cambia.

La causalidad inversa está en el reloj del volante, y no es la misma flecha que la de la obra. En 6 de las 8 semanas con volante, el volante se imprimió después del primer WhatsApp de esa semana. El encargo ya había entrado. La reunión dibuja volante → encargo. Esas seis semanas dibujan encargo → volante. Las otras dos son las únicas en las que el volante salió antes de cualquier mensaje, y son dos semanas sin obra en la cuadra: 2 encargos, los mismos que las semanas quietas sin volante. No se anota ahí un efecto. Se anota que, donde el calendario sí deja la flecha en la dirección de la reunión, el encargo no se separa del de al lado.

Acá hay que frenar, antes de la imprenta. Imprimir todas las semanas trata el 8 contra 4 como si fuera la flecha del volante. Ese 4 es la obra cambiando de mezcla, con el nodo omitido en la lámina. Y en seis de las ocho semanas el volante llegó tarde para ser la causa del primer mensaje. Las dos correcciones se leen en el dibujo: una devuelve un nodo con dos flechas que salen, la otra da vuelta el trazo que ya estaba.

Lo que esta clase no hace es escribir un peso, o un encargo, sobre la flecha que queda. Tampoco frena cualquier tercer nodo. Dejar quieto sirve cuando ese nodo es una causa de los otros dos, como la obra. Si las dos flechas entran a ese nodo, el nodo es una consecuencia, no un confusor, y frenarlo es otro dibujo. Esa figura se mira cuando se hable de a quién entra en el archivo. Hoy el paso es otro: poner en la lámina lo que se había omitido, dejar quieta la causa común, y mirar si la flecha del medio sigue separando. Si no separa, la decisión que vivía de esa flecha no se firma.

Ahí está el criterio de esta clase. **Un confusor se ve en el diagrama: flechas que salen hacia la supuesta causa y hacia el resultado. Si al dejarlo quieto la diferencia desaparece, esa diferencia no era la flecha del medio.** Omitirlo esconde la horquilla dentro del único trazo que quedó. Si el reloj muestra que el resultado ocurrió antes, la flecha va al revés, y tampoco se contrata.

Lo que sigue es tuyo. No voy a dejar quieto el fin de mes de Soga ni a dar vuelta sus avisos. Cuando respondas, te voy a marcar si el confusor te quedó con las dos flechas saliendo, si la comparación cruda y la comparación con el fin de mes quieto te dieron números distintos, si “omitida” te quedó como un nodo fuera de la lámina y no como un sinónimo de cualquier cosa rara, y si las reservas anteriores al aviso te invirtieron el trazo. Según eso, seguimos dentro de E3.

## Ejercicio

Soga hace mudanzas. En dieciséis semanas, algunas tuvo un aviso en la radio y otras no. En la reunión dicen: “Con el aviso hay más mudanzas. El aviso las produce. Hay que firmar el año de radio.” La lámina de esa frase tiene una sola flecha, del aviso a las mudanzas. El fin de mes no está dibujado.

El fin de mes es una causa de las dos cosas: la gente se muda cuando cierra el contrato, y Soga pone el aviso en esas semanas porque ya sabe que el teléfono suena.

Estas son las semanas, con las mudanzas de cada una.

Fin de mes, con aviso: 6 semanas, 12 mudanzas cada una. Fin de mes, sin aviso: 2 semanas, 12 mudanzas cada una.

Resto del mes, con aviso: 2 semanas, 4 mudanzas cada una. Resto del mes, sin aviso: 6 semanas, 4 mudanzas cada una.

En 5 de las 8 semanas con aviso, el aviso se contrató al día siguiente de que un consorcio ya hubiera reservado la mudanza.

Respondé en prosa, con párrafos, como si le mostraras los dibujos a quien quiere firmar el año, y después me dejaras las dos comparaciones por escrito. Necesito estas cuatro cosas, desarrolladas, no en una lista de consignas.

Primero, el dibujo de la reunión y el dibujo con el fin de mes como causa común. Qué afirma cada flecha, y cuál flecha no está en el segundo.

Segundo, qué dice la comparación cruda, con aviso contra sin aviso, y qué dice la comparación cuando el fin de mes se deja quieto. Los dos números tienen que estar.

Tercero, por qué el fin de mes, en la lámina de la reunión, es una variable omitida, y qué le hace esa omisión a la única flecha que dibujaron.

Cuarto, qué les pasa a esas 5 semanas en las que la reserva es anterior al aviso, y qué decisión no sale de estos papeles. No firmes el año de radio. No escribas sobre una flecha la cantidad de mudanzas que el aviso habría producido. No conviertas las celdas de dos semanas en un cero para siempre.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
