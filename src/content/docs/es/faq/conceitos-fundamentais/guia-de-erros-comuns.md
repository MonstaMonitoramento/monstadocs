---
title: Guía de Errores Comunes
---
Este documento es una guía rápida para identificar y corregir fallos en scripts personalizados en Monsta Tecnologia. Si ha encontrado un error de ejecución o una devolución inesperada en un sensor, consulte las categorías a continuación.

**Estructura de cada tópico**:

1. **Error**: Descripción del síntoma o mensaje de log.
2. **Causa Probable**: Qué suele provocar este comportamiento.
3. **Solución**: Paso a paso para la corrección.

---

## Tiempo de espera del ejecutor de scripts Lua

| Campo | Descripción |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Lua script runner timeout: deadline has elapsed* |
| **Causa** | Este error ocurre cuando el motor de ejecución de Monsta interrumpe el script Lua porque superó el tiempo límite (timeout) permitido para la ejecución de un sensor. Por defecto, Monsta finaliza scripts que tardan demasiado en responder para evitar que el sistema se bloquee o consuma recursos excesivos del servidor. |
| **Solución** | Acceda a **Configuración > Parámetros** y utilice el campo de búsqueda para localizar la clave `lua.timeout`. El valor predeterminado es de 130 segundos. Para modificarlo, haga clic en **Desbloquear**, introduzca el nuevo valor y guarde. |

---

## Pagefile: Tiempo de espera al conectar

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Pagefile: Timeout connecting to xx.xx.xx.xx:xxxx stack traceback: [C]: in function 'poll' [string "?"]:x: in function 'connect' [string "script"]:xxx: in function <[string "script"]:xxx> (tail call): in function <(tail call):-1>* |
| **Causa** | Este error indica una falla al intentar establecer una conexión de red. El script Lua pudo iniciar la llamada, pero esta expiró antes de que el dispositivo de destino respondiera al "apretón de manos" (handshake) de la conexión. El *"stack traceback"* muestra que la falla ocurrió exactamente en el momento del intento de conexión (`in function 'connect'`), antes incluso de que se enviara o recibiera cualquier dato. |
| **Solución** | Edite el dispositivo, acceda al menú **Coleta > WMI** y aumente el campo WMI Timeout. Utilice el botón de "Probar" para validar la comunicación. Luego, guarde los cambios. Si el problema persiste, otros factores relacionados con la red pueden impedir esta comunicación. En ese caso, verifique en su red:</br>• **Firewall/Bloqueo**: ¿Existe una regla de firewall en el destino o en el trayecto (ACL, IPS) que esté bloqueando la IP de Monsta en el puerto especificado?</br>• **Servicio Offline**: ¿El servicio que intenta monitorizar (p. ej., API, servidor web, base de datos) está detenido o no está escuchando en ese puerto específico?</br>• **Red Inalcanzable**: El servidor Monsta no tiene una ruta válida hacia la IP de destino.</br>• **Puerto Incorrecto**: El script está intentando conectar en un puerto distinto al que utiliza el servicio.</br>• **Carga Excesiva en el Destino**: El dispositivo objetivo tiene la CPU tan alta que no puede procesar nuevas solicitudes de conexión. |

---

## Tiempo de Respuesta: ping failed

| Campo | Descripción |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Tempo de Resposta: ping failed: Request timeout for icmp_seq x* |
| **Causa** | Este error ocurre cuando Monsta envía un paquete de eco ICMP (el conocido "Ping") a un dispositivo, pero no recibe la respuesta (Echo Reply) dentro del tiempo esperado. |
| **Solución** | El dispositivo monitorizado no respondió a las solicitudes ICMP (ping) de Monsta.</br>💡 **Consejo**: Si el equipo está en una red con alta latencia o pérdida de paquetes, ajuste la sensibilidad de detección. Para ello, edite el dispositivo y acceda a **Detalles > Sensibilidad**, modificando los parámetros según las necesidades del entorno. |

---

## Tiempo de espera SNMP: stack traceback

| Campo | Descripción |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *SNMP timeout stack traceback: [C]: in function 'poll' [string robbery/snmp_checker]:xx: in function 'getex' [string "script"]:xx: in function 'get' [string "script"]:xx: in main chunk* |
| **Causa** | Este error ocurre cuando el script intenta realizar una lectura SNMP y la conexión expira sin recibir los datos solicitados. |
| **Solución** | El dispositivo monitorizado no respondió a las solicitudes SNMP de Monsta. Edite el dispositivo, acceda al menú **Coleta > SNMP** y aumente el Timeout SNMP. Utilice el botón de "Probar" para validar la comunicación. Luego, guarde los cambios. Si el problema persiste, verifique en su red:</br>• **Comunidad SNMP Incorrecta**: La "Community String" (p. ej., `public` o `private`) configurada en Monsta no coincide con la configurada en el dispositivo.</br>• **Versión SNMP Divergente**: El dispositivo está usando SNMP v2c y el script/configuración está intentando v1 (o viceversa), o hay un error en las credenciales de v3.</br>• **ACL o Firewall**: El dispositivo posee una lista de control de acceso (ACL) que permite solo IPs específicas realizar consultas SNMP, y la IP de Monsta no está incluida.</br>• **Puerto Bloqueado**: El puerto UDP 161 (estándar de SNMP) está bloqueado en el trayecto.</br>• **Sobrecarga del Agente SNMP**: El procesador del dispositivo monitorizado está tan ocupado que el servicio (agente) SNMP no puede responder a la consulta a tiempo. |

---

## Error converting to type: Float

| Campo | Descripción |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Error converting to type: Float* |
| **Causa** | Este error ocurre cuando el sistema espera un **número decimal (Float)**, pero recibe algo que no puede convertir a número, como un texto (String) inválido o un valor nulo (`nil`). |
| **Solución** | Revise el script del monitor para asegurarse de que el retorno no contenga **strings** (como comas o unidades de medida) en el campo de valor. Si el monitor presenta lecturas normales pero muestra fallos intermitentes con este error, es probable que el dispositivo esté devolviendo un valor **nulo (nil)**. Esto ocurre cuando no hay respuesta en la consulta; en esos casos, consulte los logs del equipo para detectar alguna falla. |

---

## Error: wamp.error.no_such_procedure

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *`wamp.error.no_such_procedure`* |
| **Causa** | Indica, en la mayoría de los casos, que el servicio `monkernel` no está en ejecución en el sistema operativo Linux donde el software está instalado. El servicio `monkernel` es importante para el correcto funcionamiento del software, y su inactividad impide que Monsta ejecute los procedimientos necesarios. |
| **Solución** | La solución consiste en garantizar que el servicio `monkernel` esté iniciado. El usuario puede elegir entre dos enfoques principales para solucionar esta situación:</br>**A. Reiniciar el Sistema**: La forma más amplia de resolver la mayoría de problemas de arranque de servicios es reiniciar el sistema Linux donde está instalado el software. Al reiniciar, el sistema operativo intentará cargar e iniciar todos los servicios configurados, incluido `monkernel`, de forma automática.</br>**B. Iniciar el Servicio Manualmente (Recomendado)**: Si reiniciar no es viable o lleva mucho tiempo, el usuario puede intentar iniciar el servicio directamente con `systemctl`, que es la herramienta estándar de gestión de servicios en muchas distribuciones Linux modernas (como Ubuntu, Debian, CentOS, RHEL, etc.).</br>**Pasos**:</br>1. Abra un **Terminal** (o utilice una sesión SSH) en el servidor Linux.</br>2. Ejecute el siguiente comando para intentar iniciar el servicio: `sudo systemctl start monsta-com.monkernel`</br>**Nota**: Este comando requiere permisos de **superusuario (sudo)**. Tras ejecutar cualquiera de las acciones anteriores (reiniciar el sistema o iniciar el servicio manualmente), puede **verificar el estado del servicio** para asegurarse de que esté activo y en ejecución: `systemctl status monsta-com.monkernel`</br>El estado ideal debe indicar `active (running)` |

---

## Error SSH ocurrido: Key exchange init failed

| Campo | Descripción |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Ssh error occured: Key exchange init failed stack traceback* |
| **Causa** | Este error ocurre durante el intento de conexión SSH entre Monsta y un dispositivo remoto (generalmente modelos más antiguos de switches, routers o radios). Indica que Monsta y el dispositivo no pudieron ponerse de acuerdo sobre qué **algoritmo de intercambio de claves (Key Exchange)** utilizar, ya que el dispositivo emplea estándares que hoy son considerados heredados o inseguros por las bibliotecas modernas. |
| **Solución** | Monsta utiliza bibliotecas de criptografía de última generación. La falla en el intercambio de claves (Key Exchange) es una advertencia de que su dispositivo remoto está operando con estándares de seguridad obsoletos. La corrección definitiva es actualizar el dispositivo monitorizado para que admita algoritmos de cifrado seguros. |

---

## No hay ruta al host (os error 113)

| Campo | Descripción |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No route to host (os error 113) stack traceback* |
| **Causa** | El error `os error 113` es un código de error de red del sistema operativo que indica que el host de destino no pudo ser alcanzado. El sistema operativo no sabe por qué interfaz de red debe enviar el paquete para alcanzar esa IP específica. |
| **Solución** | Para resolver el error, asegúrese de que la tabla de enrutamiento del sistema tenga una ruta válida hacia la IP de destino y que la puerta de enlace predeterminada esté configurada correctamente para reenviar los paquetes fuera de la red local. |

## Comando no compatible en sonda WMI heredada, por favor actualice a la última versión

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Command not supported on legacy WMI probe, please update to the latest version* |
| **Causa** | La sonda o el agente en ejecución está desactualizado y no tiene soporte para la función o comando solicitado. |
| **Solución** | Para utilizar esta función, es necesario actualizar la sonda. Acceda a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descargue el instalador de la versión más reciente en la sección de descargas e instálelo en el equipo monitorizado. |

## Powershell no disponible: no se detectó agente o sonda con versión mínima 1.2.8

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Powershell is not available: no agent or probe with min version 1.2.8 detected* |
| **Causa** | La sonda o el agente en ejecución está desactualizado y no tiene soporte para la función o comando solicitado. |
| **Solución** | Para utilizar esta función, es necesario actualizar la sonda. Acceda a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descargue el instalador de la versión más reciente en la sección de descargas e instálelo en el equipo monitorizado. |

## No se detectó agente o sonda con versión mínima 1.2.8

| Campo | Descripción |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No agent or probe with min version 1.2.8 detected* |
| **Causa** | La sonda o el agente en ejecución está desactualizado y no tiene soporte para la función o comando solicitado. |
| **Solución** | Para utilizar esta función, es necesario actualizar la sonda. Acceda a nuestro sitio ([https://www.monsta.com.br](https://www.monsta.com.br)), descargue el instalador de la versión más reciente en la sección de descargas e instálelo en el equipo monitorizado. |