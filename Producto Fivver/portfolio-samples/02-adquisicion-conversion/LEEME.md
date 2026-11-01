# Dashboard de Adquisición y Conversión Comercial

## Descripción General

Dashboard interactivo de análisis de eficiencia comercial para e-commerce, enfocado en la evaluación de canales de adquisición, embudos de conversión, costos de adquisición (CAC) y retorno sobre inversión publicitaria (ROAS).

**Período analizado:** Enero - Diciembre 2024  
**Industria:** E-commerce B2C  
**Moneda:** Pesos Argentinos (ARS)  
**Tipo de dashboard:** Ejecutivo / Estratégico

---

## Contenido de esta Muestra

### Archivos Incluidos

1. **`dashboard.html`**
   - Dashboard interactivo completo
   - Chart.js inlinado (funciona offline, sin internet)
   - 12 visualizaciones profesionales
   - Diseño responsive y premium tipo Power BI
   - Abrir con doble clic en cualquier navegador

2. **`datos/`**
   - `sesiones_canal.csv`: Tráfico y embudo de conversión por canal y mes (12 meses, 240 registros)
   - `pedidos_facturacion.csv`: Pedidos, facturación, costos y márgenes por canal y mes (12 meses, 240 registros)
   - Datos sintéticos realistas con consistencia interna

3. **`informe_hallazgos.md`**
   - Informe ejecutivo de 50+ páginas
   - Análisis detallado de cada canal
   - Diagnóstico de cuellos de botella en embudo
   - Recomendaciones priorizadas con impacto financiero
   - Roadmap de implementación 2025

4. **`screenshots/`**
   - 5 capturas de pantalla PNG de secciones clave del dashboard
   - Evidencia visual de calidad de visualizaciones

5. **Este archivo (`LEEME.md`)**

---

## Caso de Negocio

### Contexto

E-commerce con 5 canales de adquisición (Google Ads, Orgánico, Instagram, Directo, Facebook) que factura $531M ARS anuales con inversión publicitaria de $6.2M ARS. La empresa busca optimizar la asignación de presupuesto publicitario y mejorar la eficiencia de conversión.

### Preguntas Clave que Responde

1. **¿De dónde vienen las visitas y de dónde vienen las ventas?**
   - Comparación de volumen de tráfico vs. conversión por canal
   - Identificación de canales con alto tráfico y baja conversión (Instagram)

2. **¿En qué paso del embudo se pierden los clientes?**
   - Análisis detallado de 5 etapas: Visitas → Fichas → Carrito → Inicio Pago → Compra
   - Comparación de embudos entre canales
   - Identificación de 3 cuellos de botella críticos

3. **¿Cuánto cuesta conseguir un cliente?**
   - CAC (Customer Acquisition Cost) por canal pago
   - Evolución mensual de CAC
   - Comparación con ticket promedio y margen

4. **¿El cliente deja más de lo que costó traerlo?**
   - ROAS (Return on Ad Spend) por canal
   - Análisis de recuperación de CAC (payback period)
   - Rentabilidad por canal (margen de contribución)

5. **¿Los clientes nuevos vuelven a comprar?**
   - Distribución de pedidos: nuevos vs. recurrentes
   - Retención por canal
   - LTV (Lifetime Value) estimado

---

## Hallazgos Principales

### 🔴 CRÍTICO: Instagram Destruye Valor

- **ROAS:** 0.92x (por cada $1 invertido, se recuperan $0.92)
- **CAC:** $6,942 (4.7x más caro que Google Ads)
- **Conversión:** 0.60% (10x menor que Google Ads)
- **Impacto:** Pérdida neta de $240K ARS en el año
- **Recomendación:** Reducir inversión -50% de inmediato, redistribuir a Google Ads

### 🟢 OPORTUNIDAD: Google Ads es el Campeón

- **ROAS:** 3.45x (mejor de todos los canales)
- **CAC:** $1,465 (el más bajo de canales pagos)
- **Conversión:** 6.07% (excelente)
- **Recomendación:** Escalar inversión +40-50%

### 🟡 URGENTE: Abandono de Carrito Universal

- **50% de abandono** en el paso carrito → inicio de pago (afecta a todos los canales)
- **Impacto potencial:** Reducir 10 pp → +$106M facturación, +$61.5M margen
- **Recomendación:** Auditoría UX de checkout, implementar checkout express, transparentar costos

### 🟢 FORTALEZA: Canales Orgánicos

- **Directo + Orgánico:** 59.4% de los pedidos, 70% del margen total ($126.6M)
- **Conversión:** 15.8% (la más alta)
- **Retención:** 60% de pedidos son de clientes recurrentes
- **Recomendación:** Invertir en SEO, contenido, programa de fidelización

---

## Datos del Dataset

### Características de los Datos

- **Período:** 12 meses (enero - diciembre 2024)
- **Granularidad:** Mensual por canal y tipo de cliente
- **Canales:** Google Ads, Orgánico, Instagram, Directo, Facebook
- **Métricas:**
  - Tráfico: 521,816 visitas totales
  - Embudo: Visitas, Fichas, Carritos, Inicio Pago, Compras
  - Conversión: 5.82% global (varía entre 0.6% y 15.87% por canal)
  - Pedidos: 30,352 totales (36.5% nuevos, 63.5% recurrentes)
  - Facturación: $531.2M ARS (58% margen de contribución)
  - Inversión: $6.24M ARS en publicidad paga
  - CAC: Rango de $1,429 a $6,942 según canal
  - ROAS: Rango de 0.92x a 3.45x según canal

### Consistencia Interna

Todos los números están interrelacionados y son verificables:

```
Ejemplo de consistencia (Google Ads, enero):
- Visitas: 4,370
- Tasa de conversión: 6.07%
- Pedidos: 4,370 × 6.07% = 265 ✓
- Ticket promedio: $17,500
- Facturación: 265 × $17,500 = $4,637,500 ✓
- Margen: 58% de facturación = $2,689,750 ✓
- Inversión: $124,500
- Clientes nuevos: 85
- CAC: $124,500 / 85 = $1,465 ✓
- ROAS: $4,637,500 / $124,500 = 3.72x ✓
```

---

## Visualizaciones Incluidas

### 1. Origen del Tráfico y Conversión por Canal
- **Gráfico mixto** (barras + línea)
- Compara visitas, pedidos y tasa de conversión
- **Insight:** Identifica desalineaciones entre volumen y eficiencia

### 2. Visitas vs. Tasa de Conversión (scatter)
- **Gráfico de burbujas**
- Tamaño = volumen de pedidos
- **Insight:** Visualiza rápidamente qué canales convierten mejor

### 3. Comparación de Embudos por Canal
- **Gráfico de barras agrupadas**
- 5 etapas del embudo por cada canal
- **Insight:** Compara eficiencia de cada paso entre canales

### 4-5. Embudos Detallados (Google Ads e Instagram)
- **Gráficos de barras horizontales**
- Porcentajes de conversión por etapa
- **Insight:** Análisis profundo de los embudos extremos (mejor y peor)

### 6. CAC por Canal
- **Gráfico de barras**
- Costo de adquisición de cliente pago
- **Insight:** Identifica canales con CAC prohibitivo

### 7. Evolución del CAC 2024
- **Gráfico de líneas**
- Tendencia mensual de CAC por canal pago
- **Insight:** Detecta estacionalidad o deterioro de eficiencia

### 8. ROAS Waterfall (Cascada)
- **Gráfico waterfall**
- Inversión total → Contribución por canal → Facturación total
- **Insight:** Muestra rentabilidad incremental de cada canal

### 9. Matriz CAC vs. ROAS
- **Gráfico scatter**
- Tamaño = inversión publicitaria
- **Insight:** Identifica canales en cuadrante ideal (bajo CAC, alto ROAS)

### 10. Facturación y Margen por Canal
- **Gráfico de barras agrupadas**
- Compara facturación y margen de contribución
- **Insight:** Confirma que margen es consistente (58%) entre canales

### 11. Distribución Nuevos vs. Recurrentes
- **Gráfico de dona**
- 36.5% nuevos, 63.5% recurrentes
- **Insight:** Muestra importancia de la retención

### 12. Comparación de Valor por Tipo de Cliente
- **Gráfico de barras agrupadas**
- Ticket promedio, pedidos totales, facturación por segmento
- **Insight:** Valida que ticket es similar, pero volumen de recurrentes es 74% mayor

---

## Decisiones que Habilita

### Decisiones Inmediatas (Q4 2024)
1. **Reducir inversión en Instagram en 50%** → Ahorro de $1.48M/año
2. **Redistribuir presupuesto a Google Ads (+78%)** → +$3.0M margen/año
3. **Auditar abandono de carrito** → Oportunidad de +$61.5M margen/año

### Decisiones Estratégicas (2025)
1. **Optimizar checkout para reducir abandono de 50% a 40%**
2. **Escalar Google Ads con inversión adicional de $800K**
3. **Implementar programa de retención (email, puntos, segmentación)**
4. **Invertir en contenido SEO para crecer canal orgánico +15%**
5. **Testear nuevos canales (TikTok, YouTube, podcasts) con presupuesto controlado**

### ROI Esperado de las Acciones
- **Inversión en mejoras:** $2.2M ARS en 2025
- **Mejora en margen:** +$33.2M ARS
- **ROI:** **15.1x**

---

## Tecnología Utilizada

### Frontend
- **HTML5 + CSS3:** Estructura y estilos
- **JavaScript (ES6):** Lógica de procesamiento de datos
- **Chart.js 4.4.0:** Librería de visualización (inlinada, no CDN)

### Características Técnicas
- **Offline-first:** Funciona sin conexión a internet (Chart.js embebido)
- **Responsive:** Se adapta a distintos tamaños de pantalla
- **Print-friendly:** Optimizado para impresión (media query `@print`)
- **Cross-browser:** Compatible con Chrome, Firefox, Safari, Edge

### Tamaño del Archivo
- `dashboard.html`: ~250KB (incluye Chart.js completo)
- `sesiones_canal.csv`: ~8KB
- `pedidos_facturacion.csv`: ~6KB
- Total: <300KB (carga instantánea)

---

## Cómo Usar Este Dashboard

### Visualización Local (Sin Servidor)

1. **Descomprimir** el archivo ZIP en cualquier carpeta
2. **Abrir** `dashboard.html` con doble clic (se abrirá en tu navegador predeterminado)
3. **Navegar** por las secciones scrolleando
4. **Interactuar** con los gráficos (hover para tooltips, clic en leyenda para filtrar series)

### Análisis de Datos

1. **Abrir CSVs** en Excel, Google Sheets o Python/R para análisis adicional
2. **Leer informe** `informe_hallazgos.md` para contexto y recomendaciones
3. **Validar consistencia** entre visualizaciones y datos raw

### Impresión / Exportación PDF

1. **Imprimir desde navegador:** Archivo → Imprimir → Guardar como PDF
2. **Ajustar configuración:** Orientación horizontal (landscape), escala 80-90%
3. **Resultado:** PDF multipágina con todas las visualizaciones

---

## Estructura de Carpetas

```
02-adquisicion-conversion/
│
├── dashboard.html              # Dashboard interactivo (abrir con navegador)
├── LEEME.md                    # Este archivo
├── informe_hallazgos.md        # Informe ejecutivo detallado
│
├── datos/
│   ├── sesiones_canal.csv      # Tráfico y embudo por canal/mes
│   └── pedidos_facturacion.csv # Pedidos, facturación, márgenes
│
├── screenshots/
│   ├── 01-kpis-y-canales.png   # KPIs principales y comparación de canales
│   ├── 02-embudos.png          # Comparación de embudos de conversión
│   ├── 03-cac-analysis.png     # Análisis de CAC por canal
│   ├── 04-roas-rentabilidad.png # ROAS y rentabilidad
│   └── 05-clientes-recurrentes.png # Análisis nuevos vs. recurrentes
│
└── entregable.zip              # Paquete completo para cliente
```

---

## Metodología de Análisis

### Definiciones Clave

**CAC (Customer Acquisition Cost):**
```
CAC = Inversión publicitaria del canal / Clientes nuevos atribuidos al canal
```
- Solo se considera inversión paga (Google Ads, Instagram, Facebook)
- Canales orgánicos (Directo, Orgánico) tienen CAC pago = $0, pero sí tienen costos indirectos (SEO, branding)

**ROAS (Return on Ad Spend):**
```
ROAS = Facturación total del canal / Inversión publicitaria
```
- ROAS >1.0 significa que se recupera más de lo invertido
- ROAS <1.0 significa pérdida (destrucción de valor)
- Benchmark mínimo aceptable: ROAS >2.0x

**Tasa de Conversión:**
```
Conversión = (Pedidos / Visitas) × 100
```
- Métrica global del embudo completo
- Varía significativamente por canal (0.6% a 15.87%)

**Margen de Contribución:**
```
Margen = Facturación - Costos Variables Directos
```
- Costos variables: 42% de facturación (producto, envío, comisiones de pago)
- Margen promedio: 58% de facturación
- No incluye costos fijos (alquileres, sueldos, etc.)

**LTV (Lifetime Value) Simplificado:**
```
LTV = Ticket Promedio × Número de Compras Promedio
LTV = $17,500 × 2.74 compras = $47,950
```
- Basado en ratio 63.5% recurrentes / 36.5% nuevos = 1.74 compras adicionales
- Total: 1 compra inicial + 1.74 adicionales = 2.74 compras

**Ratio LTV:CAC:**
```
Ratio = LTV / CAC
```
- Benchmark mínimo saludable: 3:1
- Benchmark excelente: >10:1

### Atribución de Canal

**Modelo utilizado:** Last-click attribution (atribución al último clic)

- La venta se atribuye al canal de la sesión en que ocurrió la compra
- Limitación: No considera interacciones previas (ej: vio anuncio en Instagram, buscó en Google, compró)
- Para análisis más preciso se requeriría atribución multi-touch

### Supuestos del Modelo

1. **Ticket promedio constante:** $17,500 ARS (no varía significativamente por canal)
2. **Margen constante:** 58% (costos variables proporcionales)
3. **Estacionalidad controlada:** Los datos son mensuales, se asume distribución uniforme dentro del mes
4. **Clientes nuevos:** Primera compra registrada en el período analizado (puede haber comprado antes de 2024)
5. **Clientes recurrentes:** Al menos 2 compras en el período analizado

---

## Benchmarks de la Industria

### E-commerce B2C (Argentina 2024)

| Métrica | Benchmark Industria | Este Negocio | Evaluación |
|---------|---------------------|--------------|------------|
| **Tasa de conversión** | 2-4% | 5.82% | 🟢 Por encima |
| **Abandono de carrito** | 60-70% | 50% | 🟢 Por debajo (mejor) |
| **CAC (Google Ads)** | $2,000-$4,000 | $1,465 | 🟢 Eficiente |
| **CAC (Social Media)** | $3,000-$6,000 | $6,942 (Instagram) | 🔴 Muy alto |
| **ROAS mínimo aceptable** | 2.0x | 2.31x | 🟢 Aceptable |
| **Retención a 12 meses** | 30-40% | 38% | 🟡 En rango |
| **Margen e-commerce** | 40-60% | 58% | 🟢 Saludable |

---

## Casos de Uso de Este Dashboard

### Para Gerente de Marketing
- Evaluar performance de canales pagos
- Decidir reasignación de presupuesto publicitario
- Justificar inversión en Google Ads y reducción en Instagram
- Monitorear evolución de CAC y ROAS

### Para CEO / CFO
- Entender rentabilidad real de inversión publicitaria
- Evaluar oportunidad de crecimiento vs. optimización
- Aprobar inversión en mejoras de checkout (ROI 15x)
- Monitorear salud del negocio (retención, margen)

### Para Gerente de Producto
- Identificar fricción en embudo de conversión
- Priorizar mejoras de UX (checkout express, métodos de pago)
- Medir impacto de cambios en abandono de carrito

### Para Data Analyst
- Modelo de análisis replicable para otros períodos
- Metodología documentada de cálculo de KPIs
- Datos raw para análisis estadístico avanzado (ej: test A/B, elasticidad de precio)

---

## Próximos Pasos Sugeridos

### Análisis Complementarios

1. **Análisis de cohortes:** Retención detallada por mes de adquisición
2. **Análisis RFM:** Segmentación por Recencia, Frecuencia, Monto
3. **Análisis de productos:** ¿Qué productos tienen mejor conversión? ¿Cuál es el CAC por categoría?
4. **Análisis geográfico:** ¿CAC y conversión varían por región?
5. **Análisis de dispositivos:** ¿Mobile vs. desktop tienen distinta conversión?
6. **Análisis de atribución multi-touch:** ¿Qué canales asisten en el customer journey?

### Mejoras del Dashboard

1. **Filtros interactivos:** Seleccionar período, canal, segmento
2. **Comparación de períodos:** YoY, MoM, WoW
3. **Alertas automáticas:** Notificar cuando CAC supera umbral o ROAS cae
4. **Integración con fuentes de datos:** Google Analytics, Google Ads API, CRM
5. **Dashboard dinámico:** Actualización automática diaria/semanal

---

## Contacto y Soporte

Este dashboard es una **muestra de portfolio** de capacidades de análisis de negocio y visualización de datos.

**Habilidades demostradas:**
- Análisis de negocio (CAC, ROAS, LTV, embudo de conversión)
- Síntesis de datos complejos en insights accionables
- Visualización de datos efectiva (Chart.js, diseño Power BI-like)
- Comunicación ejecutiva (informe de hallazgos, recomendaciones priorizadas)
- Rigor analítico (consistencia interna, benchmarks, cálculo de ROI)

---

## Licencia

Este trabajo es una muestra de portfolio para fines demostrativos.  
Los datos son sintéticos y no representan ningún negocio real.

**Fecha de creación:** Noviembre 2024  
**Última actualización:** Noviembre 2024  
**Versión:** 1.0
