---
title: Guía de Errores Comunes
---
Este documento es una guía rápida para identificar y corregir fallos en scripts personalizados en Monsta Tecnología. Si has encontrado un error de ejecución o un resultado inesperado en un sensor, consulta las categorías a continuación.

**Estructura de cada tema**:

1. **Error**: Descripción del síntoma o mensaje del registro.
2. **Causa Probable**: Lo que generalmente desencadena ese comportamiento.
3. **Solución**: Paso a paso para la corrección.

---

## Tiempo de espera del ejecutor de scripts Lua

| Campo | Descripción |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Lua script runner timeout: deadline has elapsed* |
| **Causa** | Este error ocurre cuando el motor de ejecución de Monsta interrumpe el script Lua porque excedió el tiempo límite (timeout) permitido para la ejecución de un sensor. Por defecto, Monsta finaliza scripts que tardan demasiado en responder para evitar que el sistema se quede bloqueado o consuma recursos excesivos del servidor. |
| **Solução** | Accede a **Configuración > Parámetros** y utiliza el campo de búsqueda para localizar la clave `lua.timeout`. El valor por defecto es de 130 segundos. Para cambiarlo, haz clic en **Desbloquear**, introduce el nuevo valor y guarda. |

---

## Pagefile: Timeout connecting

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Pagefile: Timeout connecting to xx.xx.xx.xx:xxxx stack traceback: [C]: in function 'poll' [string "?"]:x: in function 'connect' [string "script"]:xxx: in function <[string "script"]:xxx> (tail call): in function <(tail call):-1>* |
| **Causa** | Este error indica una falla al intentar establecer una conexión de red. El script Lua pudo iniciar la llamada, pero esta expiró antes de que el dispositivo de destino respondiera al "apretón de manos" (handshake) de la conexión. El *"stack traceback"* muestra que la falla ocurrió exactamente en el momento del intento de conexión (`in function 'connect'`), antes incluso de que se enviaran o recibieran datos. |
| **Solução** | Edita el dispositivo, accede al menú **Recopilación > WMI** y aumenta el campo WMI Timeout. Utiliza el botón "Probar" para validar la comunicación. Después, guarda las modificaciones. Si el problema persiste, otros factores relacionados con la red pueden impedir esta comunicación. En ese caso, verifica en tu red:<br />• **Firewall/Bloqueo**: ¿Existe una regla de firewall en el destino o en el camino (ACL, IPS) que bloquee la IP de Monsta en el puerto especificado?<br />• **Servicio Offline**: ¿El servicio que intentas monitorizar (por ejemplo: API, servidor web, base de datos) está detenido o no escucha en ese puerto específico?<br />• **Red Inalcanzable**: El servidor Monsta no tiene una ruta válida hacia la IP de destino.<br />• **Puerto Incorrecto**: El script está intentando conectar en un puerto distinto del que utiliza el servicio.<br />• **Carga Excesiva en el Destino**: El dispositivo objetivo tiene la CPU tan alta que no puede procesar nuevas solicitudes de conexión. |

---

## Tiempo de Respuesta: ping failed

| Campo | Descripción |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Tempo de Resposta: ping failed: Request timeout for icmp_seq x* |
| **Causa** | Este error ocurre cuando Monsta envía un paquete de eco ICMP (el famoso "ping") a un dispositivo, pero no recibe la respuesta (Echo Reply) dentro del tiempo esperado. |
| **Solução** | El dispositivo monitorizado no respondió a las solicitudes de ICMP (ping) de Monsta. 💡 **Consejo**: Si el equipo está en una red con alta latencia o pérdida de paquetes, ajusta la sensibilidad de detección. Para ello, edita el dispositivo y accede a **Detalles > Sensibilidad**, modificando los parámetros según las necesidades del entorno. |

---

## SNMP timeout stack traceback

| Campo | Descripción |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *SNMP timeout stack traceback: [C]: in function 'poll' [string robbery/snmp_checker]:xx: in function 'getex' [string "script"]:xx: in function 'get' [string "script"]:xx: in main chunk* |
| **Causa** | Este error ocurre cuando el script intenta realizar una lectura SNMP y la conexión expira sin recibir los datos solicitados. |
| **Solução** | El dispositivo monitorizado no respondió a las solicitudes SNMP de Monsta. Edita el dispositivo, accede al menú **Recopilación > SNMP** y aumenta el Timeout SNMP. Utiliza el botón "Probar" para validar la comunicación. Después, guarda las modificaciones. Si el problema persiste, verifica en tu red:<br />• **Community String Incorrecta**: La "Community String" (por ejemplo: `public` o `private`) configurada en Monsta no coincide con la configurada en el dispositivo.<br />• **Versión SNMP Divergente**: El dispositivo está usando SNMP v2c y el script/configuración está intentando v1 (o viceversa), o hay un error en las credenciales de v3.<br />• **ACL o Firewall**: El dispositivo posee una lista de control de acceso (ACL) que permite solo IPs específicas para realizar consultas SNMP, y la IP de Monsta no está incluida.<br />• **Puerto Bloqueado**: El puerto UDP 161 (por defecto de SNMP) está bloqueado en el camino.<br />• **Sobrecarga del Agente SNMP**: El procesador del dispositivo monitorizado está tan ocupado que el servicio (agente) SNMP no puede responder a la consulta a tiempo. |

---

## Error converting to type: Float

| Campo | Descripción |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Error converting to type: Float* |
| **Causa** | Este error ocurre cuando el sistema espera un **número decimal (Float)**, pero recibió algo que no puede convertir en número, como un texto (String) inválido o un valor nulo (`nil`). |
| **Solução** | Revisa el script del monitor para asegurar que el retorno no contenga **strings** (como comas o unidades de medida) en el campo de valor. Si el monitor presenta lecturas normales pero muestra fallos intermitentes con este error, es probable que el dispositivo esté devolviendo un valor **nulo (nil)**. Esto ocurre cuando no hay respuesta en la consulta; en esos casos, revisa los logs del equipo en busca de alguna falla. |

---

## Error: wamp.error.no_such_procedure

| Campo | Descripción |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Erro** | *`wamp.error.no_such_procedure`* |
| **Causa** | Indica, en la mayoría de los casos, que el servicio `**monkerneld**` no está en ejecución en el sistema operativo Linux donde está instalado el software. El servicio `monkerneld` es importante para el correcto funcionamiento del software, y su inactividad impide que Monsta ejecute los procedimientos necesarios. |
| **Solução** | La solución implica asegurarse de que el servicio `monkerneld` esté iniciado. El usuario puede elegir entre dos enfoques principales para solventar esta situación:<br />**A. Reiniciar el Sistema**: La forma más amplia de resolver la mayoría de los problemas de arranque de servicios es simplemente **reiniciar el sistema Linux** donde está instalado el software. Al reiniciar, el sistema operativo intentará cargar e iniciar todos los servicios configurados, incluido `monkerneld`, de forma automática.<br />**B. Iniciar el Servicio Manualmente (Recomendado)**: Si reiniciar no es viable o lleva mucho tiempo, el usuario puede intentar iniciar el servicio directamente usando `**systemctl**`, que es la herramienta estándar de gestión de servicios en muchas distribuciones Linux modernas (como Ubuntu, Debian, CentOS, RHEL, etc.).<br />**Pasos**:<br />1. Abre un **Terminal** (o utiliza una sesión SSH) en el servidor Linux.<br />2. Ejecuta el siguiente comando para intentar iniciar el servicio: `sudo systemctl start monsta-com.monkerneld`<br /><br />**Nota**: Este comando requiere permisos de **superusuario (sudo)**. Tras ejecutar cualquiera de las acciones anteriores (reiniciar el sistema o iniciar el servicio manualmente), puedes **verificar el estado del servicio** para asegurarte de que esté activo y en ejecución: `systemctl status monsta-com.monkerneld` El estado ideal debe indicar `**active (running)**` |

---

## Ssh error occured: Key exchange init failed

| Campo | Descripción |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Ssh error occured: Key exchange init failed stack traceback* |
| **Causa** | Este error ocurre durante el intento de conexión SSH entre Monsta y un dispositivo remoto (generalmente modelos más antiguos de switches, routers o radios). Indica que Monsta y el dispositivo no pudieron ponerse de acuerdo sobre qué **algoritmo de intercambio de claves (Key Exchange)** utilizar, ya que el dispositivo emplea estándares que hoy son considerados legados o inseguros por las bibliotecas modernas. |
| **Solução** | Monsta utiliza bibliotecas de criptografía de última generación. La falla en el intercambio de claves (Key Exchange) es una advertencia de que tu dispositivo remoto está operando con estándares de seguridad obsoletos. La corrección definitiva es actualizar el dispositivo monitorizado para que soporte algoritmos de cifrado seguros. |

---

## No route to host (os error 113)

| Campo | Descripción |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No route to host (os error 113) stack traceback* |
| **Causa** | El error `os error 113` es un código de error de red del sistema operativo que indica que el host de destino no pudo ser alcanzado. El sistema operativo no sabe por cuál interfaz de red debe enviar el paquete para alcanzar esa IP específica. |
| **Solução** | Para resolver el error, asegúrate de que la tabla de enrutamiento del sistema tenga una ruta válida hacia la IP de destino y que la puerta de enlace por defecto esté configurada correctamente para encaminar los paquetes fuera de la red local. |

## Command not supported on legacy WMI probe, please update to the latest version

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Command not supported on legacy WMI probe, please update to the latest version* |
| **Causa** | La sonda o agente en ejecución está desactualizado y no tiene soporte para la característica o comando solicitado. |
| **Solução** | Para utilizar esta funcionalidad, es necesario actualizar la sonda. Accede a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descarga el instalador de la versión más reciente en la sección de descargas y realiza la instalación en el equipo monitorizado. |

## Powershell is not available: no agent or probe with min version 1.2.8 detected

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Powershell is not available: no agent or probe with min version 1.2.8 detected* |
| **Causa** | La sonda o agente en ejecución está desactualizado y no tiene soporte para la característica o comando solicitado. |
| **Solução** | Para utilizar esta funcionalidad, es necesario actualizar la sonda. Accede a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descarga el instalador de la versión más reciente en la sección de descargas y realiza la instalación en el equipo monitorizado. |

## No agent or probe with min version 1.2.8 detected

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No agent or probe with min version 1.2.8 detected* |
| **Causa** | La sonda o agente en ejecución está desactualizado y no tiene soporte para la característica o comando solicitado. |
| **Solução** | Para utilizar esta funcionalidad, es necesario actualizar la sonda. Accede a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descarga el instalador de la versión más reciente en la sección de descargas y realiza la instalación en el equipo monitorizado. |
