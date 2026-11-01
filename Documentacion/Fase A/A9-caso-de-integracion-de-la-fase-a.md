# A9. Caso de integración de la Fase A

Estado: dictado completo, 2026-10-23. Caso resuelto.
Fase A — De una queja a una pregunta que puede cambiar una decisión.
Se abre a pedido del alumno. Los ejercicios anteriores quedan pendientes, pero ya no frenan el dictado.

## Qué tiene que quedarte de esta primera vuelta

Integrar no es meter todas las cuentas en una sola pregunta. Es trabajar en orden. La observación abre el problema. La decisión dice para qué vale la pena investigarlo. La definición fija qué se va a contar. La primera cuenta separa historias que todavía estaban mezcladas. Ese resultado permite hacer una pregunta más estrecha. Recién al final se escribe qué se sabe, qué historia quedó herida y qué sigue sin saberse.

En este caso no aparece una técnica nueva. Se recorren A1 a A8 dentro de una sola reunión. Lo importante no es memorizar ocho nombres. Es ver que cada paso evita un error distinto y deja preparado el paso siguiente.

## La reunión

Pulso vende una suscripción mensual para entrenar con una aplicación. El 1 de noviembre, la dueña abre la reunión así:

“Octubre fue malo. Terminamos con 200 suscriptores menos porque se rompió la pantalla de pago. Hagamos una campaña, pongamos el primer mes con 30% de descuento y recuperemos la gente que se fue.”

La frase parece completa. Tiene un resultado, una causa y una acción. Justamente por eso hay que frenarla. Si se la acepta entera, el análisis queda reducido a buscar números que decoren una decisión ya elegida.

Antes de abrir el sistema, conviene separar lo que la frase está haciendo.

“Terminamos con 200 suscriptores menos” describe una diferencia entre dos saldos. Todavía hay que revisar cómo se contó, pero es una afirmación descriptiva.

“Se rompió la pantalla de pago” propone una causa. Es una hipótesis.

“Hagamos una campaña y demos 30% de descuento” pide una acción. Es una conclusión de decisión.

Las tres oraciones pueden terminar siendo razonables. No tienen la misma evidencia. Una resta puede sostener la primera y no decir nada sobre las otras dos.

## La decisión antes que el tablero

La acción propuesta cuesta dinero y toca dos cosas diferentes. 
La campaña intenta traer más visitas. 
El descuento intenta cambiar la decisión de compra de quienes ya llegaron.

No conviene tratarlas como una sola medida llamada “marketing”.

Las opciones reales para esta semana son tres. 
1) Pulso puede lanzar la campaña con descuento. 
2) Puede no lanzarla y revisar primero el camino de compra. 
3) Puede trabajar sobre las bajas de quienes ya estaban suscriptos.

Para que el análisis tenga valor, tiene que existir algún resultado que haga elegir una opción y dejar otra.

La pregunta para la dueña es concreta: “Si las bajas de clientes existentes no aumentaron, las visitas no cayeron y el cambio aparece dentro del camino de alta, ¿seguirías destinando esta semana el dinero a recuperar clientes y traer tráfico?”

Si la respuesta es “sí, la campaña sale de todos modos”, los números no están decidiendo esa acción. Servirán para un informe, pero no para elegir. Si la respuesta es “no; en ese caso primero revisamos el paso que cambió”, entonces vale la pena seguir. 
En Pulso, la dueña acepta esa segunda condición. La decisión está abierta.

Este paso viene antes que las cuentas porque determina qué diferencia sería útil encontrar. 
No hace falta explorar todo el negocio. Hace falta distinguir si el saldo cayó por más bajas, por menos altas, o por las dos; y, si faltaron altas, en qué momento del camino dejaron de aparecer.

## Definir antes de contar

Ahora aparecen palabras que parecen obvias y no lo son: suscriptor activo, alta, baja, visita y pago. Antes de usarlas, Pulso deja escrita una regla para cada una.

Un suscriptor activo al cierre es una cuenta con el servicio habilitado a las 23:59 del último día del mes y con el pago del período aprobado. 
El saldo es la cantidad de esas cuentas en esa fecha.

Un alta es una cuenta que consigue su primer pago aprobado durante el mes y queda habilitada. Crear un usuario sin pagar no cuenta como alta.

Una baja es una cuenta que estaba activa al inicio del mes y deja de estarlo durante ese mes, ya sea porque canceló o porque, después de los intentos definidos por Pulso, el pago siguió rechazado.

Una visita es una entrada a la web. La misma persona puede producir más de una visita. Por eso las visitas no son personas ni cuentas.

Llegar a la página de planes significa que una visita abrió la pantalla donde se comparan los abonos. Iniciar el pago significa que eligió un plan y abrió el formulario de cobro. Pago aprobado significa que el cobro terminó bien. Para una cuenta nueva, ese pago aprobado produce un alta.

Estas reglas hacen dos trabajos. 
Permiten repetir la cuenta el mes siguiente y evitan mezclar unidades distintas. 
En el saldo se cuentan cuentas. En el recorrido de la web se cuentan visitas que alcanzaron cada paso. Una persona puede visitar tres veces antes de crear una sola cuenta. No se pueden restar visitas de suscriptores como si fueran la misma cosa.

También hay que fijar qué es una fila. En el archivo de saldos, cada fila es una cuenta en una fecha de cierre. En el archivo del recorrido web, cada fila es una visita y contiene el paso más lejano al que llegó. Si cada clic fuera una fila, una visita que abrió cuatro planes aparecería cuatro veces y la tasa quedaría inflada.

La definición no prueba nada sobre octubre. Hace que los números de octubre quieran decir algo estable.

## Abrir la foto con los movimientos del mes

Con las definiciones quietas, se mira primero el saldo. 
Septiembre empezó con 5.000 suscripciones activas. Durante septiembre hubo 600 altas y 500 bajas. El mes cerró con 5.100:

5.000 al inicio + 600 altas − 500 bajas = 5.100 al cierre.

Octubre empezó con esas mismas 5.100. Durante octubre hubo 300 altas y 500 bajas. Cerró con 4.900:

5.100 al inicio + 300 altas − 500 bajas = 4.900 al cierre.

La diferencia entre las dos fotos es de 200 cuentas. Esa resta era correcta. **La frase “recuperemos la gente que se fue” no lo era. Las bajas no aumentaron: fueron 500 en los dos meses. Lo que cambió fueron las altas, que pasaron de 600 a 300.**

Esto no demuestra que las bajas estén bien. Quinientas pueden ser muchas para Pulso. Para juzgar eso haría falta otra comparación. **Lo que sí permite afirmar esta cuenta es más estrecho: la caída del saldo entre septiembre y octubre no se produjo porque octubre tuviera más bajas que septiembre. Se produjo porque entraron 300 cuentas menos mientras las bajas se mantuvieron.**

La primera pregunta ya hizo su trabajo. Separó la historia de la fuga de la historia de la entrada. **Ahora hay una pregunta nueva y más estrecha: ¿por qué el camino de alta terminó con 300 pagos aprobados en lugar de 600?**

## Abrir las altas con el camino de compra

Pulso registra cuatro momentos en orden: la visita, la página de planes, el inicio del pago y el pago aprobado. Ese camino es el embudo. La tasa de cada paso compara a quienes siguieron con quienes habían llegado al paso anterior.

En septiembre hubo 20.000 visitas. 10000 llegaron a la página de planes: 50 de cada 100 visitas. un 50%.
De esas 10.000, 2.000 iniciaron el pago: 20 de cada 100 que vieron los planes.Un 20%
De esas 2.000, 600 consiguieron un pago aprobado: 30 de cada 100 que iniciaron el pago. Un 30%.

En octubre también hubo 20.000 visitas. Diez mil llegaron a la página de planes: otra vez 50 de cada 100. 50%
De esas 10.000, 1.000 iniciaron el pago: 10 de cada 100. Un 10%
De esas 1.000, 300 consiguieron un pago aprobado: otra vez 30 de cada 100. Un 30%

La conversión total pasó de 600 pagos sobre 20.000 visitas, que son 3 de cada 100, a 300 sobre 20.000, que son 1,5 de cada 100. Cayó a la mitad. Ese número final no dice por sí solo dónde ocurrió.

La apertura por pasos sí lo muestra. La cantidad de visitas quedó igual. La proporción que llegó a la página de planes quedó en 50 de cada 100. La proporción que completó el pago, una vez iniciado, quedó en 30 de cada 100. La que cambió fue la proporción que pasó de mirar los planes a iniciar el pago: bajó de 20 de cada 100 a 10 de cada 100.

**La pantalla final de pago no muestra una tasa peor. Llegó menos gente a esa pantalla. Son afirmaciones distintas. Si Pulso mira solamente que hubo 300 pagos en vez de 600, puede culpar al último lugar del camino porque ahí aparece la venta. Cuando compara cada paso con su propia base, el cambio aparece antes.**

## Traducir el cambio a pesos sin confundirlo con una causa

Pulso también quiere saber cuánto se movió la facturación de las primeras cuotas. En septiembre, cada una de las 600 altas pagó en promedio 20.000 pesos. Fueron 12 millones. En octubre, cada una de las 300 altas pagó en promedio 24.000 pesos. Fueron 7,2 millones.

La diferencia es de 4,8 millones menos. Esa diferencia es el neto: lo que queda después de combinar los movimientos. No es el tamaño de cada movimiento.

Para abrirla, se cambia una parte de la cuenta por vez. Primero se deja el pago promedio de septiembre, 20.000 pesos, y se cambia solamente la cantidad de altas de 600 a 300. Trescientas altas por 20.000 pesos son 6 millones. La menor cantidad de altas lleva la facturación de primeras cuotas de 12 millones a 6 millones: 6 millones para abajo.

Después se mantiene la cantidad de octubre, 300 altas, y se cambia el pago promedio de 20.000 a 24.000 pesos. Trescientas por 24.000 son 7,2 millones. El pago promedio más alto devuelve 1,2 millones.

El camino queda así: 12 millones, después 6 millones, después 7,2 millones. Seis millones para abajo y 1,2 millones para arriba dejan un neto de 4,8 millones menos.

Esta cuenta tampoco dice por qué el pago promedio subió. Puede haber cambiado el precio. Puede haberse vendido una mezcla distinta de planes. Sin abrir los planes y sus precios, las dos historias siguen juntas. Tampoco dice que Pulso haya perdido 4,8 millones de margen. No se presentaron los costos de prestar el servicio ni los descuentos realmente aplicados. Dice que la facturación de primeras cuotas fue 4,8 millones menor.

## Poner a prueba la historia de la pantalla rota

Hasta acá hay un patrón: menos visitas que llegaron a iniciar el pago. Todavía falta revisar la historia que la dueña trajo, “se rompió la pantalla de pago”.

Antes de mirar los números, esa historia tendría que haber escrito su predicción. Si la pantalla donde se carga y confirma el pago estuviera fallando, una cantidad parecida de visitas podría iniciarlo, pero una proporción menor debería terminar con el pago aprobado. En los datos, se vería caer la tasa entre inicio de pago y pago aprobado.

La predicción que la heriría también se puede escribir. Si la proporción aprobada entre quienes iniciaron el pago quedara igual, y lo que cayera fuera la cantidad que inició el pago, el problema estaría antes de la pantalla final tal como fue definida.

Eso es lo que muestran los datos. La tasa final quedó en 30 de cada 100. La tasa anterior cayó de 20 a 10 de cada 100. La hipótesis de una falla en la pantalla final queda herida.

“Queda herida” no significa que Pulso demostró que la pantalla funciona perfectamente. Puede tener errores que afecten a ciertos dispositivos y queden escondidos en el promedio. Lo que significa es que esa historia no explica, con estos datos agregados, por qué las altas totales cayeron a la mitad.

Aparece otra historia: algo cambió en la página de planes o en la decisión de elegir uno. Esa historia predice exactamente el patrón observado: las visitas y las llegadas a planes se mantienen, menos gente inicia el pago, y quienes lo inician lo completan en la misma proporción.

La historia queda viva, no demostrada. “Algo cambió en la página de planes” todavía junta causas distintas. Puede haber subido el precio mostrado. Puede haberse quitado una opción mensual. Puede haber un botón que no funciona en celulares. Puede haber empezado a cobrarse antes un costo que en septiembre aparecía después. Todas producirían menos inicios con una tasa final estable.

## El dato que falta

Para separar esas historias, hay que escribir qué mostraría cada una.

Si el botón falla en celulares, la caída de inicios debería concentrarse en las visitas desde celular, mientras que las computadoras se mantienen. Hace falta el tipo de dispositivo y el evento de clic en el botón.

Si el precio mostrado frenó la decisión, la caída debería empezar cuando cambió el precio y aparecer tanto en celulares como en computadoras. Hace falta la fecha exacta del cambio y la tasa diaria entre página de planes e inicio de pago.

Si se quitó una opción mensual, la caída debería concentrarse entre quienes antes elegían esa opción. Hace falta el plan que la visita intentó seleccionar. Si Pulso no registró ese intento antes de octubre, ese dato no existe para quienes abandonaron. No se puede reconstruir por intuición.

Los registros de dispositivo, clic y fecha están en el sistema, pero nadie los trajo a la reunión. La intención de la persona que vio los planes y se fue no está en el sistema. Una entrevista o una prueba con usuarios puede aportar otra evidencia, pero no transforma retroactivamente una visita anónima en una causa conocida.

Cuando un dato falta, la historia no queda refutada. Queda sin separar de las otras. Decir “no lo sabemos con estos registros” no es abandonar el análisis. Es impedir que una ausencia de información se rellene con la explicación más cómoda.

## Volver a la decisión

La reunión empezó con tres acciones pegadas: recuperar gente, traer visitas y dar un descuento.

La cuenta de altas y bajas muestra que el cambio de octubre está en las altas, no en un aumento de las bajas. Una campaña de recuperación de antiguos suscriptores no toca el movimiento que cambió entre los dos meses.

El embudo muestra que las visitas no cayeron. Comprar más tráfico manda más gente a un recorrido que, entre la página de planes y el inicio del pago, deja avanzar a la mitad que antes.

El descuento podría tocar la decisión de elegir un plan, pero los datos no muestran que el precio sea la causa. También son compatibles con un botón roto en celulares o con un cambio de opciones. Lanzar 30% de descuento a todos antes de distinguir esas historias paga un costo y puede no tocar el problema.

La decisión razonable para esta semana no es “no hacer nunca una campaña” ni “el descuento está refutado”. Es más estrecha: no lanzar todavía la campaña general; revisar primero el paso entre la página de planes y el inicio del pago, abierto por dispositivo, por día y por plan; confirmar qué cambios se hicieron en esa pantalla; y volver a decidir con ese resultado.

Ese trabajo tiene valor porque sus respuestas cambian la acción. Si la caída está solo en celulares y coincide con un error del botón, se corrige el error. Si aparece en todos los dispositivos desde el día que subió el precio, se discute precio, plan y descuento. Si no hay un cambio claro y el registro no permite separar, se puede hacer una prueba chica antes de comprometer toda la campaña.

## Qué se puede decir al cerrar

Una conclusión descriptiva sí está sostenida. Pulso cerró octubre con 200 suscripciones activas menos que septiembre. Las bajas fueron 500 en ambos meses. Las altas pasaron de 600 a 300. En el recorrido de alta, visitas, llegada a planes y aprobación después de iniciar el pago conservaron sus tasas. La tasa que cayó fue la que va de la página de planes al inicio del pago.

Una conclusión causal todavía no está sostenida. Los datos hieren la historia de una falla general en la pantalla final. Son compatibles con un problema anterior, en la elección del plan, pero no distinguen entre precio, opciones, diseño o una falla limitada a ciertos dispositivos.

Una conclusión de decisión puede escribirse con su límite. Antes de gastar en tráfico, recuperación o un descuento general, conviene abrir el paso que cambió con los datos que ya existen. No porque se haya demostrado una causa, sino porque esas acciones tocan movimientos que no cambiaron o suponen una causa que todavía no fue separada.

También queda escrito lo que no se sabe. No se sabe si 500 bajas son muchas o pocas para Pulso. No se sabe por qué el pago promedio subió. No se sabe cuánto cambió el margen. No se sabe qué pensaron quienes vieron los planes y se fueron. Ninguna de esas ausencias invalida lo que sí se pudo afirmar.

## El orden completo

La integración de la Fase A se puede leer en el orden del caso.

Primero se frenó una frase que mezclaba resultado, causa y acción. Después se preguntó qué decisión podía cambiar. Se definió qué contaba como suscriptor, alta, baja, visita y pago, y qué representaba cada fila. Se abrió la foto de suscriptores con las altas y las bajas. Al encontrar que faltaban altas, se abrió su recorrido con el embudo. Se tradujo el cambio de facturación en movimientos separados, sin convertirlos en causas. Se escribió qué predecía la historia de la pantalla rota, qué la habría herido y qué dato faltaba. Finalmente se volvió a la decisión con una conclusión descriptiva, una causa todavía abierta y un siguiente paso acotado.

Ningún paso resolvió todo. Cada uno achicó el problema sin afirmar más de lo que el dato permitía. Ese es el cierre de la Fase A: pasar de una queja con una solución pegada a una pregunta definida, una comparación que separa historias y una decisión que sabe qué evidencia está esperando.

## Ejercicios pendientes

El dictado sigue. Los ejercicios de A3 a A8 quedan disponibles para practicar y corregir cuando el alumno quiera retomarlos. No bloquean la apertura de la Fase B.
