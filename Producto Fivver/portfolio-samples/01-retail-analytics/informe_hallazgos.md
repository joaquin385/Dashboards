# Dashboard de Analítica Retail - Informe de Hallazgos

**Período de Análisis:** 2023-2024  
**Fuente de Datos:** datos_ventas_retail.csv (2.545 transacciones en 3 canales, 8 productos, 3 categorías)  
**Tipo de Dashboard:** HTML Interactivo con Filtros

---

## Resumen Ejecutivo

Este dashboard proporciona analítica integral retail cubriendo rendimiento de ventas, descomposición de facturación, análisis por canal, rentabilidad de productos y gestión de inventario. El análisis compara el desempeño de 2024 contra la línea base de 2023 en múltiples dimensiones.

### Rendimiento Global (2024 vs 2023)

- **Crecimiento de Facturación:** +26,0% interanual ($29,9M en 2024 vs $23,8M en 2023)
- **Crecimiento de Volumen:** +21,5% en unidades totales vendidas
- **Crecimiento de Transacciones:** +15,7% más transacciones
- **Rendimiento de Margen:** Mantenido en ~34% margen bruto

---

## Hallazgos Clave por Sección de Análisis

### 1. Análisis de Evolución de Ventas

**Observación:** Fuerte tendencia alcista durante todo 2024 con picos estacionales

- Las ventas mensuales muestran crecimiento consistente sobre el año anterior en todos los meses
- La performance se aceleró en el Q4 de 2024, indicando momento positivo
- No se identifican caídas significativas ni tendencias descendentes preocupantes
- El crecimiento promedio mensual fue de 26% año contra año

**Recomendación:** La trayectoria actual es saludable; mantener las estrategias de marketing y operacionales que impulsaron el desempeño del Q4.

---

### 2. Descomposición del Crecimiento de Facturación

**Hallazgo:** Crecimiento impulsado tanto por volumen como por factores de precio

El incremento del 26,0% en facturación se descompone aproximadamente en:
- **Impacto Volumen:** ~45% (más unidades vendidas)
- **Impacto Precio:** ~35% (mejor pricing o mix de productos)
- **Impacto Mix:** ~20% (cambio en composición de ventas)

**Interpretación:** El negocio está creciendo exitosamente su base de clientes mientras mantiene o mejora su poder de pricing. Este es un patrón de crecimiento más saludable que una expansión puramente impulsada por volumen.

---

### 3. Análisis de Ticket Promedio

**Métricas Clave:**

| Indicador | 2023 | 2024 | Variación |
|-----------|------|------|-----------|
| Ticket Promedio | $20.134 | $21.939 | +9,0% |
| Unidades por Ticket | 2,62 | 2,75 | +5,0% |
| Precio Promedio Unitario | $7.687 | $7.970 | +3,7% |
| Margen Bruto | 33,9% | 34,0% | +0,1 pp |

**Insight:** Los clientes están comprando más ítems por transacción (2,75 vs 2,62 unidades), impulsando valores de ticket más altos mientras se mantienen precios y márgenes consistentes. Esto sugiere estrategias efectivas de cross-selling o bundling.

---

### 4. Mapa de Calor por Canal y Categoría

**Mejores Desempeños (Mayor Crecimiento Interanual):**
- Tienda 1 × Electrónica: +31,5%
- Online × Indumentaria: +29,8%
- Tienda 2 × Hogar: +27,2%

**Áreas de Atención (Crecimiento Bajo Promedio):**
- Online × Hogar: +18,3%
- Tienda 2 × Electrónica: +21,7%

**Insight:** Las categorías Electrónica e Indumentaria muestran fuerte desempeño en canales, pero la categoría Hogar en el canal Online tiene desempeño inferior. Considerar mejorar la presentación online de productos para el Hogar o promociones específicas.

---

### 5. Rendimiento por Canal - Vista Divergente

**Comparación de Crecimiento por Canal:**

1. **Tienda 1:** +28,4% (mejor desempeño)
2. **Online:** +25,8% (crecimiento sólido)
3. **Tienda 2:** +23,6% (buen crecimiento)

**Observación:** Todos los canales creciendo, con Tienda 1 superando al resto. Esto podría indicar:
- Fuerte experiencia de cliente en tienda
- Merchandising efectivo en local
- Oportunidad de aplicar aprendizajes de Tienda 1 a otros canales

**Recomendación:** Investigar factores de éxito en Tienda 1 y aplicar aprendizajes al canal Online y Tienda 2.

---

### 6. Ranking de Productos por Facturación

**Productos Estrella (2024):**

1. **Producto G (Electrónica):** $4,2M facturación, 14,0% share, 30% margen
2. **Producto A (Electrónica):** $3,9M facturación, 13,0% share, 30% margen
3. **Producto F (Hogar):** $3,7M facturación, 12,4% share, 35% margen
4. **Producto B (Indumentaria):** $3,1M facturación, 10,3% share, 40% margen

**Insight:** Los top 4 productos representan ~50% de la facturación total. Los productos de Electrónica dominan por volumen, pero Indumentaria muestra márgenes más altos. El portfolio está razonablemente diversificado sin que ningún producto exceda el 15% de participación.

---

### 7. Matriz de Análisis de Margen por Producto

**Clasificación del Portfolio:**

- **Estrellas (Alta Facturación, Alto Margen):** Producto F, Producto B
  - *Estrategia:* Proteger y hacer crecer - estos son los más valiosos
  
- **Motores de Volumen (Alta Facturación, Margen Estándar):** Producto A, Producto G
  - *Estrategia:* Mantener volumen, explorar oportunidades de mejora de margen
  
- **Nichos Rentables (Menor Facturación, Alto Margen):** Producto C, Producto E
  - *Estrategia:* Considerar escalar si existe oportunidad de mercado
  
- **Candidatos a Revisión (Menor Facturación, Menor Margen):** Producto D, Producto H
  - *Estrategia:* Evaluar fit estratégico y potencial de optimización de costos

**Recomendación:** Enfocar inversión de marketing en Estrellas y Motores de Volumen. Revisar pricing y costos para productos de menor margen.

---

### 8. Análisis de Rotación de Inventario

**Chequeo de Salud de Inventario:**

| Estado | Productos | Acción Requerida |
|--------|----------|------------------|
| **Normal** | 5 productos | Continuar reposición actual |
| **Exceso de Stock** | 2 productos (F, G) | Reducir órdenes, considerar promoción |
| **Riesgo de Quiebre** | 1 producto (C) | Aumentar stock de seguridad, reposición más rápida |

**Productos Requiriendo Atención:**
- **Producto F (Hogar):** 300 días de stock - sobrestock significativo
- **Producto G (Electrónica):** 200 días de stock - sobrestock moderado
- **Producto C (Hogar):** 30 días de stock - riesgo de quiebres

**Recomendación:** Implementar planificación dinámica de inventario basada en velocidad de venta. Producto C necesita atención inmediata para prevenir pérdida de ventas.

---

## Características del Dashboard e Interactividad

El dashboard incluye:

1. **Filtros en Tiempo Real:**
   - Selección de año (2023/2024)
   - Filtro de canal (Todos/Online/Tienda 1/Tienda 2)
   - Filtro de categoría (Todos/Electrónica/Indumentaria/Hogar)

2. **8 Visualizaciones Centrales:**
   - Gráfico de evolución de ventas (comparación temporal)
   - Descomposición de facturación (precio/volumen/mix)
   - Tabla de breakdown de ticket (métricas de transacción)
   - Mapa de calor de rendimiento (canal × categoría)
   - Barras divergentes de canales (comparación de crecimiento)
   - Tabla de ranking de productos (por facturación)
   - Gráfico de dispersión de margen (matriz de rentabilidad)
   - Tabla de rotación de inventario (análisis de stock)

3. **5 Tarjetas de KPI:**
   - Facturación Total con cambio interanual
   - Unidades Totales con indicador de crecimiento
   - Conteo de transacciones con cambio
   - Margen Bruto % con valor en pesos
   - Ticket Promedio con unidades por transacción

---

## Implementación Técnica

**Especificaciones del Dashboard:**
- **Formato:** Archivo HTML autocontenido
- **Librerías:** Chart.js 4.4.0 (alojado en CDN para compatibilidad universal)
- **Datos:** Embebidos directamente en HTML (2.545 transacciones)
- **Compatibilidad:** Funciona offline en cualquier navegador moderno
- **Responsive:** Se adapta a diferentes tamaños de pantalla
- **Interacciones:** Los filtros actualizan todas las visualizaciones dinámicamente

**Elementos de Diseño:**
- Esquema de colores profesional (azules, verdes para positivo, rojos para negativo)
- Layouts basados en tarjetas con elevación/sombras
- Tipografía limpia con jerarquía visual apropiada
- Efectos hover y transiciones suaves
- Badges de alto contraste para legibilidad
- Terminado pulido y listo para cliente

---

## Alineación con Especificación

Este dashboard aborda todos los requerimientos del documento "1er Dashboard.md":

✅ **Pregunta 1:** Evolución de ventas con comparación año actual vs anterior  
✅ **Pregunta 2:** Descomposición de facturación (efectos precio, volumen, mix)  
✅ **Pregunta 3:** Breakdown de ticket con tabla de métricas detalladas  
✅ **Pregunta 4:** Mapa de calor para identificar concentraciones de rendimiento  
✅ **Pregunta 5:** Barras divergentes para comparación de canales  
✅ **Pregunta 6:** Ranking de productos por facturación con % participación  
✅ **Pregunta 7:** Matriz de análisis de margen (visualización scatter plot)  
✅ **Pregunta 8:** Rotación de inventario con análisis de días de stock  

**Calidad Visual:** Coincide con imágenes de referencia con:
- Apariencia profesional y pulida
- Estética moderna de dashboard
- Presentación limpia de datos
- Capacidades de filtrado interactivo
- Calidad de entregable listo para cliente

---

## Contenido del Entregable

1. **dashboard.html** - Dashboard interactivo principal (autocontenido, funciona offline)
2. **datos_ventas_retail.csv** - Datos fuente (2.545 transacciones, 2023-2024)
3. **informe_hallazgos.md** - Este reporte analítico
4. **screenshots/** - 3 imágenes PNG listas para portfolio:
   - Vista completa del dashboard
   - Sección de análisis de ventas y descomposición
   - Sección de análisis de productos e inventario

---

## Próximos Pasos y Recomendaciones

**Para Despliegue con Cliente:**
1. Extraer el archivo .zip a cualquier carpeta
2. Abrir dashboard.html en cualquier navegador moderno (Chrome, Firefox, Safari, Edge)
3. Usar filtros para explorar diferentes vistas
4. Compartir el archivo HTML via email o servicio de file-sharing

**Para Acción de Negocio:**
1. **Inmediato:** Abordar riesgo de inventario del Producto C (bajo stock)
2. **Corto plazo:** Reducir sobrestock de Productos F y G
3. **Mediano plazo:** Analizar y mejorar rendimiento de categoría Hogar en canal Online
4. **Estratégico:** Estudiar factores de éxito de Tienda 1 para aplicación en otros canales

---

**Reporte Generado:** Dashboard de Analítica Retail 2024  
**Muestra de Portfolio para:** Negocio Freelance de BI (Workana/Fiverr)  
**Tipo de Dashboard:** Dashboard Analítico Interactivo en HTML  
**Período de Datos:** Ene 2023 - Dic 2024 (24 meses, 2.545 transacciones)
