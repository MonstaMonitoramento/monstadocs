---
title: "La Arquitectura de Comunicación del Agente"
sidebar:
  order: 3
---

El **Agente Monsta** es un software instalado directamente en los dispositivos (End-points) para permitir la recopilación de métricas internas y la monitorización de redes geográficamente distribuidas. Su función principal es actuar como un túnel de datos seguro, eliminando la dependencia de infraestructuras de red complejas, como las **VPNs**.

## Instalación

La instalación del agente fue desarrollada para ser Zero Conf. Esto significa que el software fue diseñado para funcionar inmediatamente después de la instalación, sin que el usuario necesite realizar ajustes manuales.

**Paso a paso para la instalación**:

1. **Download**: Acceda a la página oficial de [Descargas do Monsta](https://www.monsta.com.br/downloads) y descargue la versión compatible con su sistema operativo.
2. **Ejecución**: Ejecute el instalador en el servidor o estación de trabajo que desee utilizar como punto principal.
3. **Vinculación**: Cuando se le solicite, informe la **Clave de Licencia** de su servidor Monsta para establecer la comunicación cifrada. La clave puede obtenerse en el menú **Configuración -> Agentes**.

Una vez conectado, el dispositivo aparecerá automáticamente en el menú de dispositivos para la configuración de los monitores. Para supervisar dispositivos de la red remota, basta con añadirlos en la jerarquía por debajo del agente.

## Conexión

El Agente Monsta ofrece flexibilidad en la forma en que se comunica con el Servidor Monsta, permitiendo la conexión de dos maneras: **Directa** o vía **Servidores proxy** de nuestra plataforma. Esto se define automáticamente por el protocolo durante el proceso de comunicación.

### Directa (Recomendada)

La conexión directa es el método de comunicación **predeterminado y más eficiente** para el Agente Monsta.

![image-1773247027332.png](../../../../../assets/images/p141_image-1773247027332.png)

#### Cómo Funciona

En este modo, el Agente, instalado en la red remota, establece una **comunicación punto a punto** segura (usando el protocolo QUIC) directamente con el Servidor Monsta.

- **Flujo**: Agente Remoto -> Internet/WAN -> Servidor Monsta.
- **Requisito**: El Servidor del Monsta debe tener el puerto de comunicación **58580/UDP (salida)** disponible en Internet.

#### Ventajas (¿Por qué es la Mejor Opción?)

| **Ventaja** | **Descripción** |
| --- | --- |
| **Rendimiento Puro** | El tráfico de métricas recorre el camino más corto posible, resultando en la **menor latencia** y mayor velocidad de respuesta para la detección de eventos. |
| **Seguridad Simple** | El túnel QUIC cifra la comunicación **de extremo a extremo**, sin intermediarios, garantizando que solo el Servidor Monsta pueda descifrar los datos. |
| **Mayor Resiliencia** | QUIC está optimizado para lidiar con pérdida de paquetes y cambios de red. En conexiones directas, su resiliencia es máxima, garantizando menos desconexiones. |
| **Menos Puntos de Falla** | La ausencia de un servidor intermedio significa que solo hay dos puntos a gestionar (Agente y Servidor Monsta), reduciendo la complejidad y los posibles cuellos de botella. |

### Conexión Vía Servidores Proxy de la Plataforma Monsta

Esta opción se ofrece para entornos con restricciones de red, donde el Servidor Monsta no posee comunicación en el puerto 58580/UDP hacia Internet.

![image-1773248921644.png](../../../../../assets/images/p141_image-1773248921644.png)

#### Cómo Funciona

En este modo, el Agente se conecta a uno de los servidores proxy mantenidos por nuestra plataforma. Este servidor intermediario recibe el tráfico del agente y lo reenvía al Servidor Monsta.

- **Flujo**: Agente Remoto -> Internet/WAN -> Servidor Proxy Monsta -> Servidor Monsta Principal.

#### Desventajas y Por qué Evitarlo (Si es Posible)

Aunque ofrece flexibilidad, la utilización de un proxy debe considerarse solo como último recurso debido a las siguientes desventajas en comparación con la Conexión Directa:

| **Desventaja** | **Impacto** |
| --- | --- |
| **Aumento de Latencia** | El tráfico necesita pasar por un nodo intermedio adicional. Esto **aumenta el tiempo de respuesta** y puede retrasar la detección de fallos críticos. |
| **Posible Cuello de Botella** | El servidor proxy puede convertirse en un cuello de botella de rendimiento si muchos agentes están conectados simultáneamente, sobrecargando el procesamiento del tráfico. |
| **Más Puntos de Falla** | Añadir un servidor intermedio aumenta el número de componentes que pueden fallar, afectando la estabilidad de su monitorización. |
| **Dificultad en la Resolución de Problemas** | La complejidad del camino de red es mayor, dificultando la identificación de dónde está ocurriendo un problema de conexión o latencia. |



## Compatibilidad con NAT y IPs Dinámicos

El **Agente Monsta** fue arquitectado específicamente para superar desafíos comunes en redes remotas, como el uso de NAT (traductor de direcciones de red) y la asignación de direcciones IP dinámicas.

### Funcionamiento en Entornos con NAT

NAT es la tecnología que permite a múltiples dispositivos en una red local (que poseen IPs privadas, como `192.168.x.x`) compartir una única dirección IP pública.

- **Problema Tradicional**: Herramientas que intentan iniciar la conexión desde el exterior (del servidor central hacia el dispositivo remoto) fallan, ya que el NAT bloquea la conexión entrante (inbound) y la dirección privada no es enrutable.
- **Solución de Monsta**: El Agente Monsta siempre **inicia la conexión desde dentro de la red remota** (el host del Agente) hacia el Servidor Monsta (que tiene una IP conocida en nuestra nube).
    
    Este método de "conexión de salida" (*outbound*) permite que el Agente "atraviese" el *firewall* y el NAT de la red remota sin la necesidad de configuraciones complejas como Port Forwarding (redireccionamiento de puertos).

### Tolerancia a IPs Dinámicos

Redes remotas residenciales o pequeñas sucursales frecuentemente utilizan direcciones IP públicas que cambian periódicamente (IP Dinámico), proporcionadas por el proveedor de Internet.

- **Protocolo QUIC**: El éxito del agente para manejar IPs dinámicos está garantizado por el uso del protocolo **QUIC**.
- **ID de Conexión**: A diferencia de TCP, que identifica la conexión por el par IP:Puerto, QUIC utiliza un **ID de Conexión Único**. Si el Agente Monsta está activo y la dirección IP pública de su red cambia:
        
    1. El Servidor Monsta Principal no finaliza la sesión.
    2. El agente simplemente reanuda el envío de datos usando la nueva dirección IP pública.

Esto significa que, incluso si la IP de su sucursal cambia, la conexión segura del Agente Connect se mantiene, garantizando una **monitorización continua e ininterrumpida**.

## Caché de Datos

### Visión General

La funcionalidad de **Caché de Datos** garantiza que la monitorización de redes remotas permanezca ininterrumpida y completa, incluso durante fallos o interrupciones en la comunicación con el servidor principal de Monsta.

El agente remoto incluye un mecanismo de **Caché** que almacena localmente todas las métricas recopiladas mientras la conexión esté indisponible. Esto elimina la pérdida de datos críticos y asegura la integridad histórica de la monitorización.

### Mecanismo de Funcionamiento

El proceso de caché opera de la siguiente manera:

1. **Detección de Fallos**: El Agente supervisa activamente la conectividad con el servidor Monsta. Al detectar una falla en la comunicación (ej: timeout, error de red), el Agente graba automáticamente los datos en el caché de la máquina local.
2. **Almacenamiento en Caché**: Durante el periodo de desconexión, todas las métricas de red (tráfico, latencia, estado de dispositivos, etc.) se recopilan normalmente y se almacenan en una cola persistente en el disco local del Agente.
3. **Sincronización (Reconexión)**: Tan pronto como la comunicación con el servidor Monsta se restablece, el Agente inicia automáticamente la **Sincronización**. Los datos almacenados en caché se transmiten al servidor, respetando el orden cronológico original. Tras el envío exitoso, los datos se eliminan del caché local.

## Cuándo Utilizar el Agente

El **Agente del Monsta** fue desarrollado para superar las limitaciones impuestas por arquitecturas de red complejas y distribuidas. Actúa como un colector de datos inteligente, permitiendo una monitorización completa y eficiente en diversas situaciones, como las destacadas a continuación:

### Monitorización de Redes Remotas (Sin VPN)

El Agente elimina la necesidad de configurar y mantener complejas Redes Privadas Virtuales (VPNs) o soluciones de túnel para supervisar entornos externos de forma sencilla y segura.

### Monitorización en Entornos con Restricción de Puertos (Sin Redireccionamiento)

En entornos con políticas de seguridad rígidas (como centros de datos de clientes o redes altamente segmentadas), a menudo no es posible abrir o redireccionar puertos para que el servidor de Monsta acceda directamente a los dispositivos. El Agente no necesita redireccionamiento de puertos.

### Monitorización de redes con la misma gama de direcciones

Una de las grandes diferencias del Agente Monsta es la capacidad de monitorizar diferentes clientes o unidades que utilizan la misma gama de direccionamiento IP (ej: `10.0.0.0/16`) sin ningún conflicto.

### Distribución Inteligente del Procesamiento de Recolección

Para grandes infraestructuras con miles de ítems siendo monitorizados, el Agente permite descentralizar la carga de trabajo de recopilación de datos del servidor principal. Al distribuir las tareas de recolección entre múltiples Agentes, usted asegura que el servidor de Monsta se concentre únicamente en el almacenamiento y la visualización, permitiendo que el sistema escale horizontalmente el procesamiento.