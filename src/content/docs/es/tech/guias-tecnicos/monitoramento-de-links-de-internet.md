---
title: "Monitorización de enlaces de Internet"
---

Monsta es una herramienta potente para garantizar la disponibilidad y el rendimiento de la conectividad de red de su empresa. El monitoreo de enlaces a Internet es importante para detectar fallos de conectividad e identificar cuellos de botella en el consumo de ancho de banda.

## Principio de funcionamiento

Monsta monitorea el enlace de Internet en la **interfaz de red de su equipo local** donde llega el enlace.

1. **Recopilación de datos**: Monsta se conecta a su equipo de red (como router, firewall o switch) y recoge información de la interfaz configurada para el enlace de Internet (puerto WAN). Se pueden monitorizar varias interfaces simultáneamente.
2. **Métricas monitorizadas**:
    
    
    - **Velocidad y estado de la interfaz**: Indica si la interfaz está activa (*UP*) o inactiva (*DOWN*) y su velocidad de conexión, notificando si ésta queda inactiva o con velocidad de conexión física por debajo de la esperada.
    - **Volumen de tráfico**: Mide la cantidad de datos entrantes (*Inbound*) y salientes (*Outbound*) en bits por segundo, métricas utilizadas para el monitoreo del consumo.
    - **Cálculo del volumen transferido**: Monsta puede calcular el volumen total de datos transferidos en el intervalo de tiempo que seleccione.
3. **Procesamiento**: Los datos recopilados se almacenan y se presentan en gráficos y pueden configurarse en los paneles para el análisis de tendencias e histórico.

## Creación de alertas proactivas

La principal ventaja de monitorear el enlace es la capacidad de configurar **alertas proactivas y reactivas** en función de las métricas recopiladas.



| Tipo de Alerta | Condición de Umbral | Impacto y Acción |
| --- | --- | --- |
| **Caída del enlace** | La interfaz cambia de **Estado UP a DOWN**. | **Alerta crítica.** Indica fallo total de conectividad con el proveedor. |
| **Reducción de la velocidad de conexión física** | La interfaz de red reduce la velocidad de conexión física debido a algún problema de cableado o de la propia interfaz de red. | **Alerta de advertencia/problema.** Indica si la interfaz física está operando por debajo de su capacidad total. |
| **Exceso de consumo (ancho de banda)** | La tasa de tráfico (Inbound o Outbound) supera un **límite de utilización** preconfigurado (ej.: 90% de la capacidad total del enlace) durante un periodo de tiempo. | **Alerta de advertencia/problema.** Indica que el enlace está saturado. La alerta sugiere la necesidad de **gestión de ancho de banda** o una *actualización* del enlace. |


:::tip[Ejemplo práctico]
Si su enlace tiene 100 Mbps, puede configurar una alerta para que se dispare cuando el consumo alcance de forma constante 90 Mbps.
:::

## Configuración en la práctica

Para configurar el monitoreo de un enlace de internet en Monsta, siga estos pasos básicos:

1. **Agregue el dispositivo**: Cree un dispositivo en Monsta para supervisar su router/firewall.
2. **Añada los monitores**: Seleccione el dispositivo y haga clic en el botón "+" para agregar el monitor de tráfico de red y Velocidad de la Interfaz.
3. **Configure las alertas**: Seleccione los monitores creados y haga clic en "Editar" para configurar los límites de alerta de los que desea recibir información.



:::note
Para recibir avisos, recuerde añadir un Grupo de Alertas a su dispositivo. Para más información, consulte [Alertas](/es/manual/grupos-alertas/alertas)
:::