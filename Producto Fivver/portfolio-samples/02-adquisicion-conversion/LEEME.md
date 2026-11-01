# Dashboard de Adquisición y Conversión Comercial

> **Muestra de Portfolio** - Análisis de eficiencia de adquisición y conversión para e-commerce

## 📋 Contenido del Entregable

Este paquete contiene un dashboard completo de análisis de eficiencia comercial, incluyendo:

- **`dashboard.html`**: Dashboard interactivo completo (funciona offline, doble clic para abrir)
- **`informe_hallazgos.md`**: Informe detallado de hallazgos y recomendaciones estratégicas
- **`datos/`**: Datasets fuente en CSV (sesiones, pedidos, facturación)
- **`screenshots/`**: 5 capturas de pantalla de alta resolución (1920x1080) de cada sección del dashboard

## 🎯 Objetivo del Análisis

Evaluar la **eficiencia de los canales de adquisición** (Google Ads, Facebook, Instagram, Orgánico, Directo) analizando:

1. Origen del tráfico y conversión por canal
2. Embudos de conversión detallados
3. Costo de Adquisición de Clientes (CAC)
4. Retorno sobre Inversión Publicitaria (ROAS)
5. Comportamiento de clientes nuevos vs. recurrentes

## 📊 Indicadores Clave (2024)

| Métrica | Valor |
|---------|-------|
| **Visitas totales** | 558,399 |
| **Tasa de conversión** | 5.87% |
| **Pedidos totales** | 32,753 |
| **Facturación** | $582.1M ARS |
| **CAC promedio** | $11,637 ARS |
| **ROAS canales pagos** | **3.17x** |
| **Margen de contribución** | $337.6M (58.0%) |

### ROAS por Canal (Canales Pagos)

| Canal | ROAS | CAC |
|-------|------|-----|
| **Google Ads** | **4.50x** | $8,807 |
| **Facebook** | 3.50x | $11,078 |
| **Instagram** | 1.20x | $21,120 |

**Google Ads lidera en rentabilidad** con el mejor ROAS y CAC más eficiente.

### Valor de Cliente

| Tipo de Cliente | Pedidos | Ticket Promedio | Facturación |
|----------------|---------|-----------------|-------------|
| **Nuevos** | 13,802 (42.1%) | $16,500 | $227.7M |
| **Recurrentes** | 18,951 (57.9%) | **$18,700** | $354.4M |

*Los clientes recurrentes gastan 13.3% más por pedido.*

## 🔍 Hallazgos Principales

### ✅ Fortalezas

1. **Google Ads altamente rentable** (ROAS 4.50x, CAC $8,807)
2. **Canales orgánicos sólidos** (Directo 6.80% conversión, Orgánico 7.50%)
3. **Base de clientes recurrentes** (57.9% de pedidos, ticket +13.3%)
4. **Margen saludable** (58.0% promedio)

### ⚠️ Oportunidades de Mejora

1. **Instagram sub-rentable** (ROAS 1.20x, apenas sobre break-even en margen)
2. **CAC elevado en Instagram** ($21,120, 2.4x más caro que Google Ads)
3. **Conversión baja en Instagram** (0.59%, vs. 4.49% Google Ads)
4. **Embudo Instagram ineficiente** (solo 9.7% llega a fichas de producto)

### 🎯 Recomendaciones Priorizadas

1. **Aumentar inversión en Google Ads** (+20-30%, mantener CAC)
2. **Optimizar campañas de Instagram** (mejorar segmentación, creativos, landing pages)
3. **Implementar recuperación de carritos** (oportunidad en paso carrito → pago)
4. **Programa de fidelización** (capitalizar valor de clientes recurrentes)
5. **Invertir en SEO** (fortalecer canal orgánico de bajo costo)

## 💻 Cómo Usar el Dashboard

### Opción 1: Abrir Localmente (Recomendado)

1. Descomprimir el archivo ZIP
2. Hacer **doble clic** en `dashboard.html`
3. Se abrirá en el navegador predeterminado (Chrome/Firefox/Edge)

**✅ Funciona completamente offline** - Chart.js está embebido, sin dependencias de CDN

### Opción 2: Servidor Web Local

```bash
# Python 3
python -m http.server 8000

# Navegar a http://localhost:8000/dashboard.html
```

## 📁 Estructura de Archivos

```
02-adquisicion-conversion/
├── dashboard.html                          # Dashboard interactivo (auto-contenido)
├── LEEME.md                               # Este archivo
├── informe_hallazgos.md                  # Informe detallado con recomendaciones
├── entregable-adquisicion-conversion.zip  # Paquete completo para entrega
├── datos/
│   ├── sesiones_canal.csv                # Visitas, embudos, inversión (120 filas)
│   ├── pedidos_facturacion.csv           # Pedidos, facturación, margen (120 filas)
│   └── kpis_computed.json                # KPIs calculados (uso interno)
└── screenshots/
    ├── 01-kpis-y-canales.png             # KPIs globales y origen de tráfico
    ├── 02-embudos.png                     # Embudos de conversión por canal
    ├── 03-cac-analysis.png                # Análisis de CAC
    ├── 04-roas-rentabilidad.png           # ROAS waterfall y matriz CAC vs ROAS
    └── 05-clientes-recurrentes.png        # Análisis nuevos vs. recurrentes
```

## 📊 Secciones del Dashboard

### 1. Origen del Tráfico y Conversión
- **Gráfico de barras**: Visitas, pedidos y tasa de conversión por canal
- **Scatter plot**: Visitas vs. conversión (tamaño = volumen de pedidos)
- **Insight**: Análisis comparativo de eficiencia de canales

### 2. Embudos de Conversión
- **Comparación multi-canal**: 5 canales en un solo gráfico
- **Embudos individuales**: Google Ads e Instagram (detalle granular)
- **Insight**: Identificación de cuellos de botella por etapa

### 3. Costo de Adquisición (CAC)
- **Comparación CAC por canal**: Canales pagos vs. orgánicos
- **Evolución temporal**: Tendencia CAC 2024
- **Insight**: Eficiencia relativa de adquisición

### 4. Rentabilidad y ROAS
- **Waterfall chart**: Flujo de inversión a facturación (floating bars)
- **Matriz CAC vs. ROAS**: Scatter con cuadrantes de eficiencia
- **Margen por canal**: Facturación vs. margen de contribución
- **Insight**: Análisis de rentabilidad integral

### 5. Nuevos vs. Clientes Recurrentes
- **Donut chart**: Distribución de pedidos
- **KPI cards**: 6 métricas comparativas (pedidos, tickets, facturación)
- **Insight**: Valor diferencial de clientes recurrentes

## 🎨 Características de Diseño

- ✅ **Responsive**: Se adapta a diferentes tamaños de pantalla
- ✅ **Offline-first**: Sin dependencias externas (Chart.js embebido)
- ✅ **Interactivo**: Tooltips detallados en todos los gráficos
- ✅ **Profesional**: Estilo Power BI con gradientes y sombras
- ✅ **Accesible**: Colores diferenciados, etiquetas claras
- ✅ **Print-friendly**: Optimizado para impresión/PDF

## 📐 Metodología

### Datos Sintéticos Realistas

- **12 meses** de datos (Enero-Diciembre 2024)
- **5 canales** (Google Ads, Facebook, Instagram, Orgánico, Directo)
- **2 tipos de cliente** (Nuevos, Recurrentes)
- **Consistencia matemática**: Todos los KPIs derivan de los mismos datos fuente

### Fórmulas Clave

```
Conversión = Pedidos / Visitas × 100
CAC = Inversión Publicitaria / Clientes Nuevos Pagos
ROAS = Facturación Canal / Inversión Canal
Margen % = (Facturación - Costos Variables) / Facturación × 100
Ticket Promedio = Facturación / Pedidos
```

### Verificaciones Implementadas

- ✅ Total de visitas = suma de visitas por canal
- ✅ Total de pedidos = suma de pedidos por canal
- ✅ Total de facturación = suma de facturación por canal
- ✅ ROAS calculado = facturación pagos / inversión pagos
- ✅ CAC calculado = inversión pagos / clientes nuevos pagos
- ✅ Tasas de conversión en rango realista (0.5-8%)
- ✅ Screenshots únicas (verificado con MD5)

## 🔧 Tecnologías Utilizadas

- **HTML5 + CSS3**: Estructura y diseño
- **Chart.js 4.4.1**: Visualizaciones (embebido, 269 KB)
- **JavaScript Vanilla**: Lógica de renderizado
- **Python**: Generación de datos sintéticos y validación
- **Playwright**: Captura automatizada de screenshots

## 📝 Notas Metodológicas

1. **Números formateados en estilo argentino:** Puntos como separador de miles (ej. $16.500, $573.177.500)
2. **Montos en pesos argentinos (ARS)** salvo indicación contraria
3. **Período de análisis:** Enero-Diciembre 2024 (12 meses completos)
4. **Margen de contribución:** Calculado como facturación menos costos variables directos (58.0% promedio)
5. **CAC solo canales pagos:** Google Ads, Facebook, Instagram (canales orgánicos tienen CAC implícito en SEO/contenido, no medido aquí)
6. **ROAS solo canales pagos:** Facturación generada por cada peso invertido en publicidad

## 📧 Contacto

Este dashboard es una **muestra de portfolio** que demuestra capacidades de:

- ✅ Análisis de eficiencia comercial
- ✅ Visualización de datos con Chart.js
- ✅ Generación de insights accionables
- ✅ Documentación técnica completa
- ✅ Diseño profesional estilo Power BI

Para más información o consultas sobre proyectos similares, contactar al analista.

---

**Última actualización:** 2025  
**Versión:** 3.0 (ROAS realistic, differentiated tickets, unique screenshots)  
**Dashboard auto-contenido:** ✅ Funciona offline sin dependencias
