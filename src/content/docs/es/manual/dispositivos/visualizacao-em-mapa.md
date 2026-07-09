---
title: "Visualización en Mapa"
sidebar:
  order: 4
---

La visualización en mapa permite una interpretación geográfica o lógica de la infraestructura de TI, facilitando la identificación visual de la topología de la red. En Monsta, cuentas con dos modos de operación: el **Mapa Dinámico** y el **Mapa Estático**

## Mapa Estático

Este modo ofrece una visualización simplificada y optimizada de la infraestructura.

- **Interactividad**: La posición de los iconos es fija y viene determinada por la jerarquía del sistema. El usuario tiene el control para habilitar o deshabilitar la visualización de los iconos de los dispositivos mediante los filtros.
- **Personalización**: No permite el desplazamiento de elementos ni la inserción de *widgets*, manteniendo la interfaz limpia y centrada en el estado de los activos.
- **Aplicación**: Recomendado para la visualización de grandes volúmenes de dispositivos e infraestructuras a gran escala que requieren un alto rendimiento de carga.

![image-1771270820757.png](../../../../../assets/images/p56_image-1771270820757.png)

## Mapa Dinámico

Este modo permite la personalización completa del diseño visual de la red.

- **Interactividad**: El usuario puede mover libremente los iconos de los dispositivos y posicionarlos manualmente en el mapa.
- **Personalización**: Permite la inserción de *widgets* informativos y elementos gráficos adicionales.
- **Aplicación**: Ideal para la creación de paneles de monitorización personalizados y redes que requieren una organización visual específica.

### **Organización y Posicionamiento**

El mapa ofrece total libertad de diseño para que la representación digital sea fiel a la instalación física:

- **Movimiento Libre**: Haz clic y arrastra cualquier dispositivo para posicionarlo manualmente en el cuadrante deseado.
- **Persistencia del Diseño**: La disposición definida por el usuario puede guardarse en cualquier momento, garantizando que la organización se mantenga en todos los accesos.

### **Gestión de Dependencias (Jerarquía)**

La estructura jerárquica define la relación de subordinación entre los dispositivos (dispositivos "padre" y "hijo").

- **Cambio de Jerarquía**: Para modificar el nodo padre de un dispositivo, haz clic sobre el nodo del dispositivo padre y arrastra el ratón hasta el nuevo dispositivo hijo.
- **Impacto Lógico**: Al cambiar el padre de un activo, el sistema actualiza automáticamente el árbol de dependencias y las reglas de propagación de alertas asociadas a esa rama.

### **Enriquecimiento con Widgets**

El mapa permite insertar **Widgets** informativos directamente en el área de visualización:

- **Monitorización en Tiempo Real**: Añade bloques de datos, gráficos de rendimiento, indicadores y mucho más junto a los dispositivos.
- **Personalización del Panel**: Los widgets pueden redimensionarse y posicionarse estratégicamente para destacar métricas críticas de activos específicos sin necesidad de navegar por otros menús.

![image-1768939041220.png](../../../../../assets/images/p56_image-1768939041220.png)

![image-1768939090089.png](../../../../../assets/images/p56_image-1768939090089.png) 
**Dispositivo principal**: El mapa posee un sistema de filtro inteligente que aísla ramas específicas. Al seleccionar un dispositivo a través del filtro, la interfaz oculta los dispositivos irrelevantes y muestra exclusivamente el linaje directo del elemento elegido.


![image-1771271034725.png](../../../../../assets/images/p56_image-1771271034725.png) 
**Propiedades del Mapa**: A través del botón de **Propiedades**, es posible personalizar la visualización de la topología para facilitar su lectura y visualización:
- **Elementos**: Ajusta el tamaño y la forma de los iconos de los dispositivos y de los textos.
- **Identificación**: Habilita u oculta la visualización de imágenes.
- **Conectividad**: Selecciona diferentes tipos de flechas y estilos de enlace para representar las conexiones de red.

![image-1739973711187.png](../../../../../assets/images/p56_image-1739973711187.png) 
**Edición**: Al activar el modo de **Edición**, el usuario obtiene control total sobre la interfaz visual de la red, permitiendo:
- **Organización Espacial**: Reposicionar dispositivos libremente mediante *drag-and-drop* para reflejar la topología física o lógica.
- **Métricas de Conexión**: Insertar indicadores de rendimiento directamente en las líneas de enlace entre dispositivos.
- **Enriquecimiento con Widgets**: Añadir componentes visuales extra (gráficos, medidores, etc.) para crear un panel de monitorización completo y personalizado.
- **Reorganiza las posiciones**: Restablece automáticamente el posicionamiento de todos los dispositivos de acuerdo con la jerarquía definida en el sistema.