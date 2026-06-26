---
title: "SNMP (Protocolo simple de gestión de red)"
sidebar:
  order: 1
---

# ¿Qué es SNMP?

El *Simple Network Management Protocol* (**SNMP**) es un protocolo estándar de Internet utilizado para recopilar y organizar información sobre dispositivos gestionados en redes IP (Protocolo de Internet) y para modificar esa información con el fin de cambiar el comportamiento del dispositivo. En términos más sencillos, el SNMP permite a los administradores de red supervisar y gestionar sus equipos de red, como routers, switches, servidores, impresoras y mucho más, desde un punto central.

Imagine tener un panel de control para toda su infraestructura de red. El SNMP funciona proporcionando datos a ese panel, permitiéndole:

- **Supervisar el estado y el rendimiento de sus dispositivos**: Comprobar si un router funciona correctamente, cuál es la utilización de la CPU de un servidor, cuánta tinta queda en una impresora, etc.
- **Recibir alertas sobre problemas**: Ser notificado automáticamente si un dispositivo falla, si el ancho de banda está alto o si ocurre cualquier otro evento que requiera atención.
- **Configurar remotamente algunos dispositivos**: En algunos casos, el SNMP permite que cambie configuraciones en sus dispositivos de red sin necesidad de acceder a ellos directamente.
- **Recopilar datos para análisis**: El SNMP proporciona datos históricos de rendimiento que pueden utilizarse para identificar tendencias, planificar la capacidad de la red y resolver problemas futuros.

El SNMP funciona mediante el intercambio de mensajes entre un **agente SNMP**, que reside en el dispositivo gestionado, y un **gestor SNMP**, que es el sistema central de monitorización, como el **Monsta**, por ejemplo. Los agentes SNMP recopilan información sobre el dispositivo y la almacenan en una estructura llamada **MIB (Management Information Base)**. El gestor SNMP puede entonces consultar a los agentes para obtener esa información o enviar comandos para cambiar configuraciones (en algunos casos).

En resumen, el SNMP es una herramienta fundamental para la gestión eficiente y proactiva de redes de ordenadores, ayudando a garantizar la disponibilidad y el buen funcionamiento de sus servicios de TI.

Desde su creación, el SNMP ha sufrido evoluciones significativas para adaptarse a las crecientes demandas de seguridad y funcionalidad. Las versiones más conocidas y utilizadas son la v1, v2c y v3. Aunque todas tienen el mismo propósito central, se distinguen por características, principalmente en términos de seguridad.

## SNMP v1: El pionero simple e inseguro

Lanzada en 1988, la versión SNMPv1 fue la primera en ser ampliamente adoptada. Se destacó por su simplicidad, utilizando un modelo de gestión basado en comunidades. Una comunidad es, esencialmente, una contraseña en texto plano (llamada cadena de comunidad) que permite el acceso de solo lectura o lectura/escritura a un dispositivo.

- **Cadena de Comunidad**: Es el único mecanismo de "autenticación". Si la cadena de comunidad del gestor de red coincide con la del dispositivo, se concede el acceso.
- **Mensajes**: Utiliza tres tipos básicos de mensajes: GET (para obtener valores), SET (para cambiar valores) y TRAP (para notificar eventos).
- **Vulnerabilidad**: La principal debilidad de SNMPv1 es la falta de seguridad. Las cadenas de comunidad se transmiten en texto plano, lo que las hace susceptibles de interceptación y uso malicioso. Esto significa que cualquiera con acceso a la red puede capturar el tráfico y descubrir la comunidad, obteniendo acceso al SNMP de los dispositivos.

:::caution[Importante]
Se recomienda usar SNMP v1 solo si el equipo no es compatible con las versiones posteriores, debido a sus limitaciones.
:::

## SNMP v2c: Mejoras y mayor flexibilidad

SNMPv2 fue un intento de modernizar el protocolo, introduciendo mejoras sustanciales. La versión SNMPv2c (donde la "c" significa Community-Based, es decir, "basado en comunidades") mantuvo el modelo de seguridad de SNMPv1, pero aportó avances importantes en otras áreas.

- **Mejoras en los Mensajes**: Introdujo nuevos tipos de mensajes, como GETBULK, que permite la recuperación de grandes volúmenes de datos de forma más eficiente, reduciendo la carga en la red. También mejoró el mecanismo de TRAP con la introducción del INFORM, que confirma la recepción de la notificación.
- **Tipos de Datos**: Mejoró la definición de tipos de datos, ofreciendo más flexibilidad y precisión en la representación de la información gestionada.
- **Soporte para Variables de 64 bits**: Una mejora técnica significativa es la capacidad de gestionar valores mayores, como contadores de tráfico de red. SNMPv1 está limitado a contadores de 32 bits, que pueden alcanzar el valor máximo y "desbordarse" (reiniciarse a cero) rápidamente en redes de alta velocidad. SNMPv2c y v3 soportan contadores de 64 bits, que pueden rastrear volúmenes de datos mucho mayores antes de desbordarse, ofreciendo estadísticas más precisas y fiables para la monitorización del tráfico.
- **Modelo de Comunidad**: A pesar de las mejoras, SNMPv2c sigue utilizando el mismo enfoque de seguridad que SNMPv1, con cadenas de comunidad transmitidas en texto plano. Por ello, hereda las mismas vulnerabilidades de seguridad, lo que lo hace inadecuado para entornos donde la confidencialidad es crítica.

## SNMP v3: La respuesta para la seguridad

SNMPv3 representa un salto enorme en términos de seguridad y es la versión recomendada para la gestión de redes modernas. Abandona el modelo de comunidades e implementa un marco robusto de seguridad y autenticación.

- **Autenticación (Authentication)**: SNMPv3 requiere la configuración de un nombre de usuario y una contraseña para cada dispositivo. Los mensajes están firmados digitalmente para garantizar que provienen de una fuente fiable. Esto evita que terceros malintencionados inyecten mensajes falsos en la red. Los algoritmos de autenticación más comunes son MD5 y SHA.
- **Privacidad (Privacy)**: Además de la autenticación, SNMPv3 ofrece cifrado. Los datos transmitidos entre el gestor y el dispositivo pueden cifrarse, impidiendo que sean leídos si son interceptados. Los algoritmos de cifrado más utilizados son DES y AES.
- **Modelo de Usuario**: La seguridad se basa en usuarios, donde cada uno puede tener diferentes niveles de acceso y permisos. Esto permite un control de acceso granular y más riguroso.



| **Característica** | **SNMP v1** | **SNMP v2c** | **SNMP v3** |
| --- | --- | --- | --- |
| **Seguridad** | Ninguna (texto plano) | Ninguna (texto plano) | Autenticación y Cifrado |
| **Autenticación** | Cadena de Comunidad | Cadena de Comunidad | Usuario y Contraseña (MD5/SHA) |
| **Cifrado** | No | No | Sí (DES/AES) |
| **Tipos de Mensaje** | GET, SET, TRAP | GETBULK, INFORM (y los de la v1) | GETBULK, INFORM (y los de la v1) |



## Puertos de comunicación

El protocolo utiliza dos puertos de comunicación por defecto:

- **161/UDP**: para la comunicación del gestor (sistema de monitorización) al agente (equipo que se monitoriza);
- **162/UDP**: para la comunicación del agente al gestor (comunicaciones iniciadas por el equipo monitorizado, como en el caso del **TRAP**).

Algunos equipos permiten cambiar la configuración del SNMP, como la comunidad, el puerto y, en el caso de SNMPv3, las credenciales de autenticación y el tipo de cifrado. Siempre es importante verificar en la configuración del equipo esa información para utilizarla en el sistema de monitorización.

## Monsta

Monsta admite las tres versiones de SNMP y permite indicar los parámetros necesarios para monitorizar los equipos según cada versión (comunidad, puerto, usuario, contraseña, tipo de cifrado).

En la actualidad, Monsta actúa únicamente con la comunicación **gestor > agente**, utilizando los tipos de mensaje **GET** y **GETBULK**.