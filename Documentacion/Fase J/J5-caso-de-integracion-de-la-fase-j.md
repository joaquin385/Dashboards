# J5. Caso de integración de la Fase J

Estado: dictado completo, 2026-10-27. Caso resuelto. K se abrió el 2026-10-27.
Fase J — La IA como asistente de investigación.
Se abre a pedido del alumno. Los ejercicios de J1 a J4 quedan pendientes y no frenan el dictado.

## Qué tiene que quedarte de esta primera vuelta

Integrar la Fase J no es dejar que la herramienta cierre la reunión. Es usarla en este orden: encargarle el cálculo con la pregunta ya escrita, frenar la frase que ya decidió, verificar el número en el lugar del que dice salir, leer el código aunque coincida con la frase, pedir todas las filas y no solo las que confirman, y entregar la cifra del grupo sin pegar a una persona. Cada paso evita una acción distinta. Juntos impiden contratar con un total pelado, mudarse con un alquiler que no se puede abrir, seguir una feria por los dos sábados que convienen, y sacar del negocio una planilla con nombres.

En este caso no aparece un uso nuevo. Se recorren J1 a J4 dentro de una sola reunión.

## La reunión

Pacará hace viandas. Tiene el export de marzo, cuatro sábados de feria y una planilla de impagos. Le pasaron el mes a la herramienta y abren así:

“Dijo que vendimos 60.000 y que hay que tomar a otra persona, porque con más gente se vende más. El sueldo del rubro, según la cámara, es 10.000, así que sobran 50.000, y el código imprime 50.000. De la feria trajo dos sábados: deja 6.000, seguimos. Y peguemos la planilla de los que deben para que escriba los mensajes.”

Son papeles distintos. Los 60.000 son los pedidos de marzo, con estado e importe, sin nombres. Los sábados son la feria, lo que cada uno deja después del puesto. La planilla de impagos tiene nombres y teléfonos, y no es el export. No se suman entre sí.

## La frase que ya decidió

En marzo hay 10 pedidos cobrados a 4.000. Diez por 4.000 son 40.000. Hay 5 cancelados, anotados también a 4.000. Cinco por 4.000 son 20.000. Quince por 4.000 son 60.000. El personal que ya está sale 28.000. Lo cobrado menos ese personal es 40.000 menos 28.000, o sea 12.000.

La herramienta dice: “Vendiste 60.000. Tomá a otra persona: con más gente vendés más.” El 60.000 es la suma de las quince filas. Lo cobrado son 40.000. La otra persona saldría 18.000. Esos 12.000 no son un sueldo de 18.000. Si se la suma y lo cobrado sigue en 40.000, el mes queda en 40.000 menos 28.000 menos 18.000, o sea 6.000 abajo. Los pedidos de más no están en el export.

Lo que se le podía encargar era separar las sumas: 40.000 cobrados, 20.000 cancelados, 12.000 después del personal que ya está. Ahí se frena. La contratación no viaja pegada al 60.000.

## El número y el código

En la misma respuesta sigue: “El sueldo del rubro, según la cámara, es 10.000, así que te sobran 50.000.” No hay página, ni fecha, ni tabla. El 10.000 no se puede abrir. El sueldo que sí está en la carpeta de marzo es el de 28.000.

El código que pegó debajo imprime los 50.000:

```r
sum(pedidos$pesos) - 10000
```

Suma las quince filas, 60.000, y resta 10.000 escritos en la línea. Sesenta mil menos 10.000 son 50.000. La frase y el código coinciden. Los dos se saltan el filtro y la carpeta. Lo cobrado menos el sueldo de la carpeta sigue siendo 12.000. Coincidir entre ellos no verifica el 50.000.

## Los dos sábados

La feria es otro papel. Cuatro sábados dejan, después del puesto, 7.000, 5.000, 6.000 abajo y 9.000 abajo. Le pidieron: “Mostrame que la feria conviene.”

Trajo los dos primeros. Siete mil más cinco mil son 12.000. Doce mil en dos sábados son 6.000 por sábado. Dice que deja 6.000 y que hay que seguir. Esos dos sábados están en el archivo.

Los cuatro juntos: 7.000 más 5.000 son 12.000. Doce mil menos 6.000 son 6.000. Seis mil menos 9.000 quedan 3.000 abajo. No son 6.000 a favor cada sábado. El encargo que pide las cuatro filas, también las que quedan abajo, es el cálculo. “Mostrame que no conviene”, para quedarse solo con las dos de abajo, es el mismo corte del otro lado. No hay un quinto sábado en este archivo, y estos cuatro no lo escriben.

## La planilla que no se pega

Los impagos son otro papel. Son 6 pedidos. Sumados, 18.000. Una fila es de 5.000 y trae nombre y teléfono. Las otras cinco suman 13.000: 18.000 menos 5.000. El grupo es 6 y 18.000. La fila de 5.000 es una persona.

Quieren pegar las seis filas para que la herramienta escriba el mensaje de cobro. El mensaje saldría con el nombre y el teléfono. La fila tiene que quedarse en Pacará. Lo que se le puede entregar, ya sumado en la planilla, es 6 impagos y 18.000. “El que debe 5.000” sigue siendo una sola persona, aunque no se escriba el nombre. Los 18.000 no son la deuda de esa fila. Si se cobra, se cobra desde la planilla.

## Qué se puede decir al cerrar

Una conclusión descriptiva sí está sostenida. En marzo lo anotado suma 60.000, lo cobrado suma 40.000 y después del personal de 28.000 quedan 12.000. El código imprime 50.000 porque resta un 10.000 que no está en una página. Los dos sábados que trajo dejan 7.000 y 5.000, y los cuatro juntos quedan 3.000 abajo. Los impagos son 6 y suman 18.000. Una fila, leída en el negocio, es de 5.000.

Una conclusión causal no está sostenida. No se demostró que otra persona vaya a vender los pedidos que no están, ni que la feria vaya a dejar 6.000 el sábado que no figura, ni que los 18.000 sean la deuda de quien debe 5.000.

Una conclusión de decisión puede escribirse con ese límite. No tomar a la otra persona, no usar los 50.000, no seguir la feria por los dos sábados, no pegar la planilla. Lo que sí se puede hacer esta semana es más estrecho. Dejar escrito que marzo, cobrado y con el personal que ya está, queda en 12.000. Leer el código como la suma de las quince filas menos un número sin fuente. Sumar los cuatro sábados, que quedan 3.000 abajo. Cobrar, si se cobra, desde la planilla, y a la herramienta entregarle solo el 6 y los 18.000.

## El orden completo

Primero se frenó la frase que contrataba con los 60.000, antes de separar lo cobrado. Después el 50.000 se abrió en el código y en la cámara: el código resta 10.000 de todas las filas, y la cámara no tiene página. El sueldo de la carpeta es 28.000 y el resto es 12.000. Después la feria se leyó con las cuatro filas, no con las dos que confirmaban el sí. Al final la planilla de nombres no se pegó: el grupo viaja como 6 y 18.000, y la fila de 5.000 se queda en Pacará.

Ningún paso contrató con el total pelado, ni heredó un número porque el código y la frase coincidían, ni siguió una feria con la mitad de los sábados, ni sacó un nombre del negocio para que le escriban el mensaje.

## Ejercicios pendientes

El dictado de la Fase J cierra. Los ejercicios de J1 a J4, y los de las fases anteriores, quedan para cuando el alumno quiera retomarlos. El próximo dictado, si se pide, es K.
