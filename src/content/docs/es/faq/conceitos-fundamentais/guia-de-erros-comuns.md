---
title: Guía de Errores Comunes
---
Este documento es una guía rápida para identificar y corregir fallos en scripts personalizados en Monsta Tecnologia. Si ha encontrado un error de ejecución o una devolución inesperada en un sensor, consulte las categorías a continuación.

**Estructura de cada apartado**:

1. **Error**: Descripción del síntoma o mensaje de registro.
2. **Causa Probable**: Lo que generalmente desencadena ese comportamiento.
3. **Solución**: Paso a paso para la corrección.

---

## Lua script runner timeout


| Campo | Descrição |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Lua script runner timeout: deadline has elapsed* |
| **Causa** | Este error ocurre cuando el motor de ejecución de Monsta interrumpe el script Lua porque ha superado el tiempo límite (timeout) permitido para la ejecución de un sensor. Por defecto, Monsta finaliza los scripts que tardan demasiado en responder para evitar que el sistema se quede bloqueado o consuma recursos excesivos del servidor. |
| **Solução** | Acceda a **Configuración > Parámetros** y utilice el campo de búsqueda para localizar la clave `lua.timeout`. El valor por defecto es de 130 segundos. Para cambiarlo, haga clic en **Desbloquear**, introduzca el nuevo valor y guarde. |


---

## Pagefile: Timeout connecting


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Pagefile: Timeout connecting to xx.xx.xx.xx:xxxx stack traceback: [C]: in function 'poll' [string "?"]:x: in function 'connect' [string "script"]:xxx: in function <[string "script"]:xxx> (tail call): in function <(tail call):-1>* |
| **Causa** | Este error indica una falla al intentar establecer una conexión de red. El script Lua logró iniciar la llamada, pero ésta expiró antes de que el dispositivo de destino respondiera al "apretón de manos" (handshake) de la conexión. El *"stack traceback"* muestra que la falla ocurrió exactamente en el momento del intento de conexión (`in function 'connect'`), antes incluso de que se enviaran o recibieran datos. |
| **Solução** | Edite el dispositivo, acceda al menú **Recolección > WMI** y aumente el campo WMI Timeout. Utilice el botón "Probar" para validar la comunicación. Después, guarde las modificaciones. Si el problema persiste, otros factores relacionados con la red pueden impedir esta comunicación. En ese caso, verifique en su red: • **Cortafuegos/Bloqueo**: ¿Existe una regla de cortafuegos en el destino o en el camino (ACL, IPS) que bloquee la IP de Monsta en el puerto especificado? • **Servicio Offline**: El servicio que está intentando monitorizar (por ej.: API, servidor web, base de datos) está detenido o no está escuchando en ese puerto específico. • **Red Inalcanzable**: El servidor Monsta no tiene una ruta válida hacia la IP de destino. • **Puerto Incorrecto**: El script está intentando conectar en un puerto diferente al que usa el servicio. • **Carga Excesiva en el Destino**: El dispositivo objetivo tiene la CPU tan alta que no puede procesar nuevas solicitudes de conexión. |


---

## Tempo de Resposta: ping failed


| Campo | Descrição |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Tempo de Resposta: ping failed: Request timeout for icmp_seq x* |
| **Causa** | Este error ocurre cuando Monsta envía un paquete de eco ICMP (el famoso "Ping") a un dispositivo, pero no recibe la respuesta (Echo Reply) dentro del tiempo esperado. |
| **Solução** | El dispositivo monitorizado no respondió a las solicitudes ICMP (ping) de Monsta. 💡 **Consejo**: Si el equipo está en una red con alta latencia o pérdida de paquetes, ajuste la sensibilidad de detección. Para ello, edite el dispositivo y acceda a **Detalles > Sensibilidad**, modificando los parámetros según las necesidades del entorno. |


---

## SNMP timeout stack traceback


| Campo | Descrição |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *SNMP timeout stack traceback: [C]: in function 'poll' [string robbery/snmp_checker]:xx: in function 'getex' [string "script"]:xx: in function 'get' [string "script"]:xx: in main chunk* |
| **Causa** | Este error ocurre cuando el script intenta realizar una lectura SNMP y la conexión expira sin recibir los datos solicitados. |
| **Solução** | El dispositivo monitorizado no respondió a las solicitudes SNMP de Monsta. Edite el dispositivo, acceda al menú **Recolección > SNMP** y aumente el Timeout SNMP. Utilice el botón "Probar" para validar la comunicación. Después, guarde las modificaciones. Si el problema persiste, verifique en su red: • **Comunidad SNMP Incorrecta**: la "Community String" (ej.: `public` o `private`) configurada en Monsta no coincide con la configurada en el dispositivo. • **Versión SNMP Divergente**: el dispositivo está usando SNMP v2c y el script/configuración intenta v1 (o viceversa), o hay un error en las credenciales de v3. • **ACL o Firewall**: el dispositivo posee una lista de control de acceso (ACL) que permite solo IPs específicas realizar consultas SNMP, y la IP de Monsta no está incluida. • **Puerto Bloqueado**: el puerto UDP 161 (por defecto de SNMP) está bloqueado en el camino. • **Sobrecarga del Agente SNMP**: el procesador del dispositivo monitorizado está tan ocupado que el servicio (agente) SNMP no puede responder a la consulta a tiempo. |


---

## Error converting to type: Float


| Campo | Descrição |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Error converting to type: Float* |
| **Causa** | Este error ocurre cuando el sistema espera un **número decimal (Float)**, pero recibe algo que no puede convertir a número, como un texto (String) inválido o un valor nulo (`nil`). |
| **Solução** | Revise el script del monitor para garantizar que la devolución no contenga **strings** (como comas o unidades de medida) en el campo de valor. Si el monitor presenta lecturas normales pero muestra fallos intermitentes con este error, es probable que el dispositivo esté devolviendo un valor **nulo (nil)**. Esto ocurre cuando no hay respuesta en la consulta; en esos casos, verifique en los registros del equipo la existencia de alguna falla. |


---

## Erro: wamp.error.no_such_procedure


| Campo | Descrição |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Erro** | *`wamp.error.no_such_procedure`* |
| **Causa** | Indica, en la mayoría de los casos, que el servicio `**monkernel**` no está en ejecución en el sistema operativo Linux donde está instalado el software. El servicio `monkerned` es importante para el correcto funcionamiento del software, y su inactividad impide que Monsta ejecute los procedimientos necesarios. |
| **Solução** | La solución implica asegurarse de que el servicio `monkernel` se inicie. El usuario puede optar por dos enfoques principales para solventar esta situación: **A. Reiniciar el Sistema**: La manera más amplia de resolver la mayoría de los problemas de arranque de servicios es simplemente **reiniciar el sistema Linux** donde está instalado el software. Al reiniciar, el sistema operativo intentará cargar e iniciar todos los servicios configurados, incluido `monkernel`, de forma automática. **B. Iniciar el Servicio Manualmente (Recomendado)**: Si el reinicio no es viable o resulta lento, el usuario puede intentar iniciar el servicio directamente usando `**systemctl**`, que es la herramienta estándar de gestión de servicios en muchas distribuciones Linux modernas (como Ubuntu, Debian, CentOS, RHEL, etc.). **Pasos**: 1. Abra un **Terminal** (o utilice una sesión SSH) en el servidor Linux. 2. Ejecute el siguiente comando para intentar iniciar el servicio: `sudo systemctl start monsta-com.monkernel` **Nota**: Es obligatorio que este comando requiera permisos de **superusuario (sudo)**. Tras ejecutar cualquiera de las acciones anteriores (reiniciar el sistema o iniciar el servicio manualmente), puede **verificar el estado del servicio** para asegurarse de que esté activo y en ejecución: `systemctl status monsta-com.monkerned` El estado ideal debe indicar `**active (running)**` |


---

## Ssh error occured: Key exchange init failed


| Campo | Descrição |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Ssh error occured: Key exchange init failed stack traceback* |
| **Causa** | Este error ocurre durante la tentativa de conexión SSH entre Monsta y un dispositivo remoto (generalmente modelos más antiguos de switches, routers o radios). Indica que Monsta y el dispositivo no pudieron ponerse de acuerdo sobre qué **algoritmo de intercambio de claves (*Key Exchange*)** utilizar, ya que el dispositivo emplea estándares que hoy se consideran heredados o inseguros por las bibliotecas modernas. |
| **Solução** | Monsta utiliza bibliotecas de criptografía de última generación. La falla en el intercambio de claves (*Key Exchange*) es una alerta de que su dispositivo remoto está operando con estándares de seguridad obsoletos. La corrección definitiva es actualizar el dispositivo monitorizado para que soporte algoritmos de cifrado seguros. |


---

## No route to host (os error 113)


| Campo | Descrição |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No route to host (os error 113) stack traceback* |
| **Causa** | El error `os error 113` es un código de error de red del sistema operativo que indica que el host de destino no pudo ser alcanzado. El sistema operativo no sabe por qué interfaz de red debe enviar el paquete para alcanzar esa IP específica. |
| **Solução** | Para resolver el error, asegúrese de que la tabla de enrutamiento del sistema tenga una ruta válida hacia la IP de destino y que la puerta de enlace predeterminada esté configurada correctamente para encaminar los paquetes fuera de la red local. |


## Command not supported on legacy WMI probe, please update to the latest version


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Command not supported on legacy WMI probe, please update to the latest version* |
| **Causa** | La sonda o agente en ejecución está desactualizado y no tiene soporte para el recurso o comando solicitado. |
| **Solução** | Para usar este recurso, es necesario actualizar la sonda. Acceda a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descargue el instalador de la versión más reciente en la sección de descargas e instale en el equipo monitorizado. |


## Powershell is not available: no agent or probe with min version 1.2.8 detected


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Powershell is not available: no agent or probe with min version 1.2.8 detected* |
| **Causa** | La sonda o agente en ejecución está desactualizado y no tiene soporte para el recurso o comando solicitado. |
| **Solução** | Para usar este recurso, es necesario actualizar la sonda. Acceda a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descargue el instalador de la versión más reciente en la sección de descargas e instale en el equipo monitorizado. |


## No agent or probe with min version 1.2.8 detected


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No agent or probe with min version 1.2.8 detected* |
| **Causa** | La sonda o agente en ejecución está desactualizado y no tiene soporte para el recurso o comando solicitado. |
| **Solução** | Para usar este recurso, es necesario actualizar la sonda. Acceda a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descargue el instalador de la versión más reciente en la sección de descargas e instale en el equipo monitorizado. |