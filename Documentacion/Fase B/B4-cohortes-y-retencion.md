# B4. Cohortes y retención

Estado: dictado completo; ejercicio pendiente. Nube se retoma cuando el alumno quiera. B5 se abrió el 2026-10-23.
Fase B — El tiempo y la comparación.
B3 queda dictado. El ejercicio de Rueda sigue pendiente y no frena esta clase.

## Qué tiene que quedarte de esta primera vuelta

El promedio del mes mezcla gente que acaba de entrar con gente que lleva años. Quienes entraron juntos, en el mismo mes, se pueden seguir como un grupo. A ese grupo lo llamamos cohorte. La retención pregunta, de ese grupo, cuántos siguen después de uno, dos o tres meses. El saldo del mes puede verse sano mientras una cohorte nueva se cae, y puede verse flojo mientras las cohortes viejas no se mueven. Los que se van y los que vuelven después también entran en esta cuenta, y no son lo mismo que una baja definitiva.

En esta vuelta no se arma un modelo de vida del cliente ni se calcula cuánto cuesta conseguir uno. Se aprende a no leer el mes como si todos los socios tuvieran la misma edad, y a escribir la retención de un grupo que empezó junto.

## La clase

En A5, el saldo de fin de mes era una foto. Las altas y las bajas eran el flujo. Eso alcanzaba para no decir “se fueron 400” cuando lo que se había apagado era la entrada. Esta clase da un paso más. Las bajas de un mes no son todas iguales. Una parte puede ser gente que había entrado el mes anterior con una promo y no pagó el segundo mes. Otra parte puede ser gente que llevaba dos años y se fue. El mes suma esas dos cosas y entrega un solo número. La reunión habla de “la retención” como si fuera una temperatura del gimnasio. Es un promedio de edades distintas.

Antes del caso, las palabras, con un ejemplo chico.

Una **cohorte** es el conjunto de personas que empezaron en el mismo período, con la misma regla de “empezar”. En un gimnasio, la cohorte de marzo son quienes tuvieron su alta en marzo, según la definición operativa de A4: primer mes con cuota aprobada, por ejemplo. No son quienes visitaron en marzo. No son quienes estaban activos en marzo. Estar activo en marzo mezcla a la cohorte de marzo con las de febrero, enero y las de hace años.

La **edad de la cohorte** es cuántos meses pasaron desde ese alta. En el mes 0, la cohorte acaba de entrar. En el mes 1, va por el segundo mes de vida. La edad no es la edad de la persona. Es el tiempo desde que esa cuenta empezó.

La **retención de una cohorte** es, de las personas que formaban ese grupo al empezar, cuántas siguen activas después de n meses. Si en marzo entraron 100 y en abril siguen 40 de esas 100, la retención al mes 1 de la cohorte de marzo es 40 de cada 100. El denominador es siempre el tamaño original de esa cohorte, o el tamaño al inicio del tramo que se está midiendo, y hay que decir cuál. Mezclar los dos sin avisar es el mismo error de A7: usar la base equivocada.

La **retención del mes**, la que suele traer el tablero, es otra cuenta. Toma a todos los que estaban activos el día 1 y pregunta cuántos siguen el día 30. Ahí conviven el que entró ayer y el que lleva tres años. Si los nuevos se caen fuerte y los viejos casi no se mueven, el número del mes puede verse aceptable porque los viejos son más. El tablero felicita. La cohorte nueva se está yendo.

Una **reactivación** es alguien que había dejado de estar activo y vuelve a estarlo. No es un alta nueva si la regla de alta era el primer pago de la vida de esa cuenta. No es una retención de la cohorte original si entre medio estuvo afuera. Es un flujo distinto. Contarlo como alta infla la entrada. Contarlo como si nunca se hubiera ido infla la retención. Se nombra aparte.

Conviene verlo en un caso concreto. Ritmo es un gimnasio de un solo local. En mayo hubo una promo: el primer mes a mitad de precio. En la reunión de septiembre, quien lo maneja dice: “La retención está bien. De 1.000 activos a principios de agosto, el 31 de agosto quedaban 920. Se nos fue el 8%, que es lo de siempre. El problema es que no entran socios nuevos.”

El sistema muestra el saldo, las altas y las bajas de agosto, y, si alguien las pide, las altas partidas por mes de origen. Agosto empezó con 1.000 activos y cerró con 920. Altas de agosto: 80. Bajas de agosto: 160. La cuenta de A5 cierra: 1.000 + 80 − 160 = 920. El 8% que nombra la reunión no es siquiera las bajas sobre el inicio. Ciento sesenta sobre 1.000 es 16 de cada 100. El 8% es la caída neta del saldo, 80 sobre 1.000, que mezcla altas y bajas. Eso ya es el error de A5. Esta clase asume que alguien lo corrige y pregunta por las 160 bajas: ¿de qué cohorte son?

Se abre el origen. De las 160 bajas de agosto, 120 son de la cohorte de mayo: gente que había entrado con la promo y no llegó al cuarto mes, o llegó y se fue en agosto. De las 80 altas de mayo, en junio habían quedado 50, en julio 40, en agosto 20. La retención de esa cohorte, mes a mes, se lee así. Mes 0, mayo: 80. Mes 1, junio: 50 de cada 80. Mes 2, julio: 40 de cada 80. Mes 3, agosto: 20 de cada 80. Se fueron, de esa promo, 60 personas entre mayo y agosto, y 20 de esas 60 se fueron en agosto.

El resto de las bajas de agosto, 40, vienen de cohortes más viejas: 40 sobre unos 920 que no eran de mayo, un orden de magnitud distinto. Las cohortes de hace un año, en este gimnasio, pierden unos pocos cada mes. El 16% de bajas sobre el saldo de agosto no es “lo de siempre”. Es una cohorte de promo que se está terminando de caer, más un goteo habitual de la base vieja. La frase “el problema es que no entran socios nuevos” mira las 80 altas de agosto, que pueden ser las de siempre, y no mira que las 80 de mayo no se convirtieron en base. Entraron. No se quedaron.

Fijate qué habría dicho el promedio. Retención del mes de agosto, bien definida: de los 1.000 del día 1, cuántos de esos 1.000 siguen el día 31. Las 80 altas de agosto no entran en ese denominador, porque no estaban el día 1. Las 160 bajas sí, si todas venían de esos 1.000. Quedarían 840 de los 1.000 originales, más 80 altas netas de las bajas de esas altas, según cuándo se cuente. El tablero que dice 920 sobre 1.000 está mezclando foto de cierre con foto de inicio. Aunque se limpie, un 84% o un 90% de “retención mensual” puede convivir con una cohorte de mayo que retuvo 20 de cada 80 al tercer mes. El promedio del mes no es la historia de quienes entraron juntos.

También puede pasar al revés, y conviene verlo para no tratar toda baja de cohorte nueva como un fracaso de la promo. La cohorte de marzo, sin promo, era de 40 altas. En abril quedaban 32, en mayo 30, en junio 28. Pierde al principio y después se aplana. Eso es habitual: el primer mes filtra a quien probó y no volvió. La de mayo no se aplanó: siguió cayendo. El patrón de “se cae el primer mes y después queda” no se afirma con un solo mes. Se ve en la curva de la cohorte. La de marzo se parece a esa curva. La de mayo no. La decisión, si la curva de mayo es la que ocurrió, no es “hay que traer más gente”. Es no repetir una promo que llena el mes 0 y vacía el mes 3, o cobrar el segundo mes de un modo que no sea un salto de precio tan brusco. Traer más gente con la misma promo reproduce la curva.

Los que vuelven. En agosto, 10 de las 80 “altas” no eran altas según la definición de primer pago. Eran cuentas que habían dado de baja en abril y pagaron de nuevo. Si el sistema las anota como altas, la entrada de agosto está inflada en 10 y la cohorte de agosto mezcla gente nueva con gente que ya conocía el gimnasio. Si no se las anota, desaparecen del flujo y el saldo no cierra con altas menos bajas. La tercera vía es nombrarlas: reactivaciones. Diez personas volvieron. No dicen que la retención de mayo haya mejorado. Dicen que una parte de quienes se fueron no se fue para siempre. La pregunta siguiente, si importara, sería de qué cohorte venían y cuánto duran después de volver. Hoy alcanza con no sumarlas al mes 0 de agosto.

Hay un límite, el mismo de A4 y de La Esquina. La cohorte se puede armar si cada cuenta tiene una fecha de alta. Si el negocio es una rotisería de mostrador sin nombre, no hay cohorte de clientes. Puede haber cohorte de un producto, o de un canal, si esa fecha existe. Si no existe, se dice que no se puede seguir a las mismas personas en el tiempo. El promedio del mes, entonces, es lo que hay, y las historias de “los nuevos se van” quedan sin probar, no refutadas.

La relación con B1 es directa. Comparar el saldo de agosto con el de julio es una variación temporal del mix. Comparar la cohorte de mayo a los tres meses con la de marzo a los tres meses es una diferencia entre grupos, del mismo “edad”, en distintos calendarios. No son la misma frase. Mayo contra marzo en el mes 3 pregunta si quienes llevan tres meses se parecen, hayan empezado cuando hayan empezado. Agosto contra julio pregunta cómo se movió la foto de todos juntos.

Ahí está el criterio de esta clase. **Quienes entraron juntos se siguen como cohorte. La retención se calcula sobre ese grupo, mes a mes, con la base escrita.** El porcentaje del mes mezcla edades y puede tapar una promo que no se queda. Las reactivaciones se nombran aparte. Sin fecha de alta, no hay cohorte. El promedio no se inventa una.

Lo que sigue es tuyo. No voy a armarte las curvas de Nube. Cuando respondas, te voy a marcar si usaste el saldo como retención, si cambiaste el denominador a mitad de frase, si contaste reactivaciones como altas, y qué historia del promedio quedó viva sin merecerlo. Según eso, seguimos dentro de B4.

## Ejercicio

Nube es un estudio de yoga con abono mensual. En abril hubo una promo de primer mes gratis. En la reunión de julio dicen: “La retención de junio está bien: empezamos el mes con 400 abonos y lo cerramos con 390. El problema es el invierno, se anotan menos.”

Junio:

- Saldo al 1: 400. Saldo al 30: 390.
- Altas registradas por el sistema: 30.
- Bajas: 40.

De esas 30 altas, 8 son personas que habían dado de baja en marzo y volvieron a pagar en junio. Las otras 22 son altas verdaderas de junio.

La cohorte de abril, la de la promo, había sido de 80 altas. En mayo quedaban 35 de esas 80. En junio quedaban 15. De las 40 bajas de junio, 20 eran de esa cohorte.

La cohorte de febrero, sin promo, había sido de 25 altas. En marzo quedaban 20, en abril 18, en mayo 17, en junio 16.

Nadie trajo junio del año pasado. Nadie midió el invierno.

Respondé en prosa, con párrafos. Necesito estas cuatro cosas.

Primero, qué afirma de verdad la caída de 400 a 390, y por qué no es “la retención de junio”.

Segundo, la retención de la cohorte de abril al mes 0, 1 y 2, y cómo se compara ese patrón con el de febrero. Decí las bases.

Tercero, qué son esas 8 personas que volvieron, y qué le hacen a la frase “se anotan menos” si se las cuenta como altas.

Cuarto, qué quedaría herido, y qué seguiría sin probarse, si la dueña insiste en que el problema es el invierno.

No elijas la causa del invierno. No inventes junio del año pasado.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
