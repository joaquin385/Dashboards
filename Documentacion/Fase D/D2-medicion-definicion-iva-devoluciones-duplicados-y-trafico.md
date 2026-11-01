# D2. Medición: la definición, el IVA, la devolución, el duplicado y el tráfico que no es de una persona

Estado: dictado completo; ejercicio pendiente. Jarra se retoma cuando el alumno quiera. D3 se abrió el 2026-10-24.
Fase D — De dónde sale la cifra.
La calidad del dato se trata como razonamiento, antes de tratarla como limpieza en una herramienta.

## Qué tiene que quedarte de esta primera vuelta

D1 preguntaba de quién era la cifra y de qué fechas. Esta clase pregunta con qué regla se fabricó el número. La misma venta, medida con otra regla, da otra cifra. Si a mitad de año cambia la regla y el mes viejo no se reescribe, el salto puede ser la regla.

En A6, neto era la diferencia entre dos meses. Acá no. La **venta neta** es la venta bruta menos las devoluciones. Conviene decir las dos palabras.

En esta vuelta no se borra una fila porque el total “queda alto”. Se reconoce una factura repetida, un impuesto metido en el precio, una devolución que sigue adentro y una visita que no hizo ninguna persona.

## La clase

Dos locales pueden haber vendido lo mismo y mostrar dos números. No porque uno mienta. Porque no usaron la misma regla para convertir la venta en una cifra. Esa regla es la **medición**. Si no se puede decir cuál fue, el número no se puede comparar con el de al lado.

Antes del caso, las palabras, con una venta chica.

La **venta bruta** es lo que se facturó, aunque después el cliente lo devuelva. Se facturan 10.000 pesos. Esos 10.000 son la bruta.

La **devolución** es esa venta deshecha. El cliente trae la mercadería y se le devuelven 2.000. La plata ya no es una venta. El producto volvió al estante.

La **venta neta** es lo que queda: 10.000 menos 2.000, o sea 8.000. Si un mes se publica la neta y el mes siguiente se publica la bruta, el segundo parece más grande con las mismas ventas, porque las devoluciones siguen adentro del número.

El **IVA incluido** es el precio que paga el cliente, con el impuesto adentro. El **IVA no incluido** es el precio sin ese impuesto. En este ejemplo la alícuota es 21%, la de estos productos, no la de cualquier cosa: un libro o un alimento pueden llevar otra. Diez mil pesos sin IVA, con el 21% adentro, son 10.000 × 1,21 = 12.100. Si junio está en 10.000 y julio está en 12.100 por la misma mercadería, no se vendió un 21% más. Se cambió el precio de lugar: el impuesto entró en la cifra. Para sacarlo, se divide por 1,21. 12.100 / 1,21 = 10.000. Sin escribir la alícuota, esa cuenta no se puede hacer.

Un **duplicado** es la misma factura sentada dos veces en el archivo. No es lo de D1. En D1, una persona en la web y en el local podía haber hecho dos compras reales, y el error era sumarla como si fueran dos personas. Acá la segunda fila no es otra venta. Es la misma factura, con el mismo número, importada otra vez. Cinco facturas de 1.000 pesos son 5.000. Si una se pegó dos veces, el archivo dice 6.000 y la caja dice 5.000. Los 1.000 de más no se cobraron.

El **tráfico que no es de una persona** es una carga de la página que no hizo ningún cliente. Un robot que vigila si el sitio sigue en pie. Alguien de la oficina que recarga la home. Entra en “visitas” si la regla de visita es “cualquier carga”. No entra si la regla es “una persona que se quedó”. Cien visitas de personas y diez compras son 10 de cada 100. Si al día siguiente se suman otras cien cargas del robot y las compras siguen en diez, el archivo dice 200 visitas y 5 de cada 100. La tienda no convirtió peor. El denominador dejó de ser gente.

Un **cambio de definición** es esa regla movida en una fecha. Hasta el 30 de junio, visita era una cosa. Desde el 1 de julio, es otra. Los dos meses se llaman visitas y no se pueden restar. Para compararlos hay que reescribir los dos con una sola regla. Si el mes viejo no se puede reconstruir con la regla nueva, la serie se corta ese día. No se inventa el mes que falta.

Conviene mirarlo en un caso concreto. Cerco vende pintura. En la reunión de agosto dicen: “Julio dio 13.310.000 pesos y junio 8.000.000. Son 5.310.000 más, más de un sesenta por ciento. La campaña funcionó. Hay que repetirla en agosto.”

Junio, en el informe viejo, es venta neta y sin IVA: 8.000.000. El 1 de julio cambiaron el tablero. Desde ese día el número de arriba es venta bruta, con IVA incluido, y nadie reescribió junio. Comparar 13.310.000 con 8.000.000 es comparar dos reglas.

El archivo de julio, además, tiene un duplicado. El 15 de julio la exportación de la web se importó dos veces. Son 100 facturas de 10.000 pesos sin IVA. Cada una, con el 21%, pesa 12.100. Cien filas repetidas son 1.210.000 pesos que no son otra venta: el número de factura ya estaba. Se sacan del total. 13.310.000 − 1.210.000 = 12.100.000. Eso ya es la bruta de julio, contada una vez, todavía con IVA.

Esos 12.100.000 llevan el 21% adentro. Sin el impuesto: 12.100.000 / 1,21 = 10.000.000. Esa es la bruta de julio sin IVA. Junio no tenía el IVA adentro. Recién ahora las dos cifras están en el mismo tipo de peso. Pero julio sigue siendo bruta, y junio era neta.

Las devoluciones de julio son 2.000.000 sin IVA. Pintura que volvió. Si se la deja en los 10.000.000, se cuenta como vendido algo que está otra vez en el estante. La venta neta de julio es 10.000.000 − 2.000.000 = 8.000.000. Junio ya era 8.000.000, neta y sin IVA. Con la misma regla, julio no subió. Los 5.310.000 del tablero eran la factura repetida, el IVA metido en el precio y las devoluciones que junio ya había restado y julio no.

La visita tuvo su propio cambio el mismo día, porque cambiaron la herramienta de la web. En junio, una visita era una persona que se quedaba más de diez segundos. Hubo 10.000 visitas así, y 200 compras: 2 de cada 100. En julio la regla pasó a ser cualquier carga de la página. El archivo dice 20.000. Diez mil son el monitor de la oficina, que recarga la home para ver si el sitio responde. Las otras 10.000 son personas que se quedaron, como en junio. Las compras siguen en 200.

Con la regla nueva, 200 sobre 20.000 es 1 de cada 100. La reunión lee “el tráfico se duplicó y la conversión cayó a la mitad: la campaña trajo gente que no compra”. El tráfico no se duplicó. Se cambió la definición y entró una máquina. Con la regla de junio, julio también es 200 sobre 10.000, otra vez 2 de cada 100. No hay una conversión caída que la campaña tenga que arreglar. Y no hay una venta caída ni una venta subida: hay 8.000.000 contra 8.000.000.

Cerco podría haber hecho la cuenta al revés, pasar junio a bruta con IVA y a “cualquier carga”. No puede, sin inventar. El informe viejo no guardó la bruta de junio por separado de un modo que el tablero muestre, y en junio el monitor no se anotaba porque esa regla no existía. Cuando el mes viejo no se reconstruye, no se le pone un número para poder comparar. Se dice que el 1 de julio la serie se cortó. En este caso julio sí se podía volver a armar con la regla vieja, porque las facturas, las devoluciones y las cargas de más de diez segundos seguían en el archivo. Por eso la comparación se hizo para atrás, hacia la neta sin IVA y hacia la visita de una persona.

Nada de esto pide una herramienta que “limpie hasta que cierre”. Pide nombrar la regla de cada cifra. Si el número de factura se repite, la segunda fila no es una venta. Si el IVA está adentro en un solo mes, se lo saca o se lo pone en los dos, con la alícuota escrita. Si la devolución sigue adentro, la bruta no se compara con la neta. Si la visita nueva incluye un robot, el robot no es un cliente que la campaña dejó de convencer.

Ahí está el criterio de esta clase. **Dos meses solo se restan si la medición es la misma: la misma definición, el IVA en el mismo lugar, la devolución tratada igual, cada factura una vez, y las visitas limitadas a personas.** Si la regla cambió a mitad de año, se reescribe un lado o se declara cortada la serie. Un salto que desaparece al igualar la regla no es una campaña que funcionó.

Lo que sigue es tuyo. No voy a desarmar el archivo de Jarra. Cuando respondas, te voy a marcar si julio y agosto quedaron en la misma regla, si la factura repetida te quedó como otra venta, y si la caída de la conversión es de personas. Según eso, seguimos dentro de D2.

## Ejercicio

Jarra vende artículos de cocina. En la reunión de septiembre dicen: “Agosto dio 7.260.000 pesos y julio 4.000.000. La venta subió fuerte. Hay que sumar el mismo aviso en septiembre.”

Julio, en el informe viejo, es venta neta y sin IVA: 4.000.000. El 1 de agosto el tablero pasó a venta bruta con IVA incluido. En estos productos la alícuota es 21%. Nadie reescribió julio.

En el archivo de agosto hay 20 facturas de 50.000 pesos sin IVA importadas dos veces. La segunda fila de cada una no es otra venta. Las devoluciones de agosto, sin IVA, son 1.000.000.

En julio, una visita era una persona que se quedaba más de diez segundos. Hubo 4.000 visitas así y 80 compras. En agosto la regla pasó a ser cualquier carga de la página. El archivo dice 8.000 cargas. De esas, 4.000 son un robot que revisa si el sitio responde. Las otras 4.000 son personas que se quedaron más de diez segundos. Las compras de agosto también fueron 80.

Respondé en prosa, con párrafos. Necesito estas cuatro cosas.

Primero, qué está midiendo el 7.260.000 y qué está midiendo el 4.000.000 de julio. Por qué restarlos no dice cuánto creció Jarra.

Segundo, cuánto pesan las 20 filas repetidas con el IVA adentro, y cómo queda agosto en venta neta y sin IVA. Qué parte del salto era el duplicado, qué parte era el impuesto y qué parte eran devoluciones que julio ya no tenía adentro.

Tercero, qué pasa con las compras sobre las visitas si agosto se lee con la regla de agosto, y qué pasa si se lee con la regla de julio.

Cuarto, qué decisión no se puede apoyar en este salto. No sumes el aviso. No inventes una venta de septiembre.

## Iteraciones

### Respuesta del alumno

Pendiente.

### Corrección

Pendiente.

### Profundización

Pendiente. Se escribe después de la corrección, sobre el punto que la respuesta deje abierto.
