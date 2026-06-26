---
title: "Caché Inteligente de Solicitudes"
---

El Monsta emplea un sistema de **caché inteligente de solicitudes de instancias** para optimizar el monitoreo de red, reduciendo significativamente el consumo de ancho de banda y el uso de recursos computacionales tanto en el dispositivo monitorizado como en el servidor donde Monsta está alojado. Este mecanismo funciona identificando y almacenando datos de solicitudes previamente consultadas, evitando la necesidad de nuevas peticiones para información ya conocida.

![image-1749751994277.png](../../../../../assets/images/p109_image-1749751994277.png)

## Funcionamiento Técnico

El proceso de caché inteligente puede detallarse en los siguientes pasos:

1. **Intercepción de la Solicitud**: Cuando un monitor inicia una solicitud para obtener información de un dispositivo de red (por ejemplo, velocidad de un puerto, memoria total, lista de instancias, etc.), la solicitud es primero interceptada por el módulo de caché inteligente.
2. **Validación de las instancias**: Monsta utiliza una técnica para validar si ha habido modificación de las propiedades de la instancia solicitada:
    1. Cuando existen cambios, el caché se marca como expirado y se realiza una nueva consulta;
    2. Si no existen cambios, la consulta será dirigida al caché.
3. **Verificación del Caché**: Antes de enviar la solicitud al dispositivo monitorizado, el módulo de caché verifica si la instancia solicitada ya existe en su **repositorio de caché local**. Esta verificación se basa en un identificador único para cada tipo de solicitud y para cada dispositivo.
4. **cache hit**:    
    1. **Búsquedas individuales**: Si la instancia se encuentra en el caché (**cache hit**) y está dentro de su período de validez, Monsta **no envía la solicitud al dispositivo**. En lugar de ello, la respuesta previamente almacenada se devuelve inmediatamente al módulo solicitante.
    2. **Walk**: Para consultas que necesiten obtener información de parte del árbol de OID's, como por ejemplo el nombre de interfaces de red a través de un snmpwalk, Monsta emplea técnicas que solo revalidan el caché cuando existen cambios en las posiciones de sus elementos. En este caso no se utiliza el tiempo de TTL (Time-to-Live).    
          
        Estos procesos eliminan la necesidad de tráfico de red y el procesamiento de la solicitud por parte de los dispositivos monitorizados, además de ahorrar recursos del servidor Monsta que se habrían gastado en la comunicación y el procesamiento de la respuesta.
5. **cache miss**: Si la instancia no se encuentra en el caché (**cache miss**) o si su período de validez ha expirado, la solicitud se **envía al dispositivo de red monitorizado**. Tras la respuesta del dispositivo, la información se procesa y, antes de entregarla al módulo solicitante, se almacena una copia en el caché junto con un nuevo TTL. El TTL es configurable y determina durante cuánto tiempo la información se considera válida en el caché.
6. **Gerenciamiento del TTL (*Time-To-Live*)**: Cada elemento almacenado en el caché posee un TTL asociado. Este valor define la "vida útil" de la información en el caché. Una vez que el TTL expira, la información se considera desactualizada y la siguiente solicitud por esa información resultará en un "cache miss", forzando una nueva consulta al dispositivo para garantizar la obtención de los datos más recientes. El TTL puede ajustarse en función de la criticidad y la frecuencia de actualización de la información. Para ajustarlo, acceda al menú Configuraciones, Parámetros y cambie su tiempo en la variable inst.cache\_ttl\_secs (el valor por defecto es de 10 segundos). Configurar este valor a "0" elimina el caché de las búsquedas individuales.

## Beneficios Técnicos

- **Reducción de Carga en el Dispositivo Monitorizado**: Disminuye el número de solicitudes procesadas por los dispositivos de red, liberando recursos para sus funciones principales.
- **Optimización del Uso de Ancho de Banda de Red**: Minimiza el tráfico de monitorización en la red, especialmente en entornos con gran volumen de dispositivos o enlaces de baja capacidad.
- **Ahorro de Recursos del Servidor Monsta**: Reduce el consumo de CPU y memoria en el servidor Monsta, dado que muchas respuestas se entregan directamente desde el caché, evitando el overhead de la comunicación de red.
- **Mejora de la Latencia de Respuesta**: Las solicitudes que resultan en un "cache hit" se responden instantáneamente, mejorando la experiencia del usuario y la agilidad en la visualización de los datos.

El caché inteligente de solicitudes de Monsta es un componente fundamental para garantizar la **escalabilidad** y la **eficiencia** del sistema, permitiendo monitorizar infraestructuras de red grandes y complejas con rendimiento optimizado.