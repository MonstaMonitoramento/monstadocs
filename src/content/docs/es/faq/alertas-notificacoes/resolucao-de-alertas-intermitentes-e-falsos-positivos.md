---
title: "¿Cómo resuelvo alertas intermitentes y falsos positivos?"
---

## Descripción del problema

Ocurrencia de alertas intermitentes en monitores específicos, generando notificaciones de caída o criticidad que no se corresponden con el estado real del servicio (Falsos Positivos).

## Causas comunes

Existen tres escenarios principales que disparan este comportamiento:

1. **Límites mal dimensionados**: Los disparadores de **Aviso** y **Crítico** están demasiado cerca de la operación normal del dispositivo.
2. **Fallo en la recolección de datos**: Monsta no recibe la respuesta de la solicitud, ya sea por inestabilidad en la red (pérdida de paquetes) o por sobrecarga en el hardware del dispositivo monitorizado.
3. **Fallo en el Uptime**: Monsta utiliza, por defecto, paquetes **ICMP (Ping)** para comprobar si el dispositivo está activo en la red. Caídas frecuentes en el Uptime indican que Monsta no recibe la respuesta del ping.

## Cómo resolver

### Escenario 1: Ajuste de umbrales (límites)

Si el monitor alterna entre estados de alerta debido a picos normales de uso, ejecute el siguiente procedimiento:

- Acceda al monitor con problema y edite sus configuraciones.
- Ajuste los campos de **Aviso** y **Crítico** a valores que se adecuen a la realidad de carga del equipo.

### Escenario 2: Fallo de lectura en un monitor

Generalmente, esta condición es causada por un *timeout* en el proceso de recolección de datos. Para identificar la causa, haga clic sobre el monitor con problema, pulse el botón "Editar" y seleccione la opción "Registro de errores" en la esquina inferior izquierda de la ventana. Si el registro indica fallo por timeout, haga lo siguiente:

1. **Solución para protocolos estándar (SNMP, WMI, SSH)**:    
    - Edite la configuración del **Dispositivo**.    
    - Aumente el tiempo de **Timeout** de la recolección para dar más margen de respuesta al equipo sobrecargado o a la red lenta.
2. **Solución para timeouts de scripts**:    
    - Acceda al menú superior: **Configuración** > **Parámetros**.    
    - Localice la variable `lua.timeout` y aumente su valor según sea necesario.

### Escenario 3: Fallos en el Uptime

El monitor de Uptime de Monsta utiliza paquetes **ICMP (Ping)** para validar la presencia del dispositivo en la red. Una falla en este monitor significa, técnicamente, que el servidor de Monsta envió el paquete y no recibió el "Echo Reply" dentro del tiempo esperado.

Cuando el dispositivo está encendido, pero Monsta informa "Down", las causas suelen ser:

1. **Inestabilidad de ruta**: Pérdida de paquetes en la red.  
2. **Sobrecarga de CPU en el destino**: El dispositivo prioriza el tráfico de producción y descarta paquetes ICMP para ahorrar procesamiento.  
3. **Sensibilidad alta**: Monsta está configurado para considerar el dispositivo "fuera de servicio" con pocas fallas consecutivas.

En el **1er caso (Inestabilidad de ruta)**, la correcta configuración de la jerarquía entre dispositivos (Padre e Hijo) permite que Monsta intente aislar la falla, disparando alertas solo para el 'dispositivo padre' e indicando dónde inicia el problema.

Para **2** y **3**, si el entorno presenta oscilaciones aceptables (ej.: latencia elevada en enlaces vía satélite), configure Monsta para que sea más permisivo. Esto se hace reduciendo la sensibilidad de detección en la configuración del dispositivo para evitar alertas innecesarias. Para ello, haga lo siguiente:

- Edite el dispositivo específico.
- En la pestaña Detalles, haga clic en el botón Sensibilidad.
- En esa ventana personaliza la cantidad de paquetes enviados, el tiempo de espera para una respuesta y el intervalo entre el envío de cada paquete.

:::tip
Puedes personalizar la sensibilidad de forma general haciendo clic en el botón "Opciones" / "Opciones globales de dispositivos" / "Sensibilidad". Este recurso también está disponible al editar un grupo de dispositivos en la pestaña "Sensibilidad".
:::