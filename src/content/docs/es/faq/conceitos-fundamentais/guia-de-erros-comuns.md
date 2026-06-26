---
title: "Guía de Errores Comunes"
---

Este documento es una guía rápida para identificar y corregir fallos en scripts personalizados en Monsta Tecnologia. Si ha encontrado un error de ejecución o una respuesta inesperada en un sensor, consulte las categorías a continuación.

**Estructura de cada tema**:

1. **Error**: Descripción del síntoma o mensaje de registro.
2. **Causa Probable**: Lo que generalmente desencadena este comportamiento.
3. **Solución**: Paso a paso para la corrección.

---

### Lua script runner timeout

| Campo | Descripción |
| :--- | :--- |
| **Error** | *Lua script runner timeout: deadline has elapsed* |
| **Causa** | Este error ocurre cuando el motor de ejecución de Monsta detiene el script Lua porque superó el tiempo límite (timeout) permitido para la ejecución de un sensor. Por defecto, Monsta finaliza scripts que tardan demasiado en responder para evitar que el sistema se quede bloqueado o consuma recursos excesivos del servidor. |
| **Solución** | Acceda a **Configuración > Parámetros** y utilice el campo de búsqueda para localizar la clave `lua.timeout`. El valor por defecto es de 130 segundos. Para modificarlo, haga clic en **Desbloquear**, introduzca el nuevo valor y guarde. |

---

### Pagefile: Timeout connecting

| Campo | Descripción |
| :--- | :--- |
| **Error** | *Pagefile: Timeout connecting to xx.xx.xx.xx:xxxx stack traceback: [C]: in function 'poll' [string "?"]:x: in function 'connect' [string "script"]:xxx: in function <[string "script"]:xxx> (tail call): in function <(tail call):-1>* |
| **Causa** | Este error indica una falla en el intento de establecer una conexión de red. El script Lua pudo iniciar la llamada, pero expiró antes de que el dispositivo de destino respondiera al "apretón de manos" (handshake) de la conexión.<br /><br />El *"stack traceback"* muestra que la falla ocurrió exactamente en el momento del intento de conexión (`in function 'connect'`), antes incluso de que se enviaran o recibieran datos. |
| **Solución** | Edite el dispositivo, acceda al menú **Recopilación > WMI** y aumente el campo WMI Timeout. Utilice el botón "Probar" para validar la comunicación. Después, guarde las modificaciones.<br /><br />Si el problema persiste, otros factores relacionados con la red pueden impedir esta comunicación. En ese caso, verifique en su red:<br /><br />• **Firewall/Bloqueo**: ¿Existe una regla de firewall en el destino o en el camino (ACL, IPS) bloqueando la IP de Monsta en el puerto especificado?<br />• **Servicio Offline**: ¿El servicio que intenta monitorizar (ej.: API, servidor web, base de datos) está detenido o no está escuchando en ese puerto específico?<br />• **Red Inalcanzable**: El servidor Monsta no tiene una ruta válida hacia la IP de destino.<br />• **Puerto Incorrecto**: El script está intentando conectar en un puerto distinto del que utiliza el servicio.<br />• **Carga Excesiva en el Destino**: El dispositivo objetivo tiene la CPU tan alta que no puede procesar nuevas solicitudes de conexión. |

---

### Tiempo de Respuesta: ping failed

| Campo | Descripción |
| :--- | :--- |
| **Error** | *Tiempo de Respuesta: ping failed: Request timeout for icmp_seq x* |
| **Causa** | Este error ocurre cuando Monsta envía un paquete de eco ICMP (el conocido "Ping") a un dispositivo, pero no recibe la respuesta (Echo Reply) dentro del tiempo esperado. |
| **Solución** | El dispositivo monitorizado no respondió a las solicitudes ICMP (ping) de Monsta.<br /><br />💡 **Consejo**: Si el equipo está en una red con alta latencia o pérdida de paquetes, ajuste la sensibilidad de detección. Para ello, edite el dispositivo y acceda a **Detalles > Sensibilidad**, modificando los parámetros según las necesidades del entorno. |

---

### SNMP timeout stack traceback

| Campo | Descripción |
| :--- | :--- |
| **Error** | *SNMP timeout stack traceback: [C]: in function 'poll' [string robbery/snmp_checker]:xx: in function 'getex' [string "script"]:xx: in function 'get' [string "script"]:xx: in main chunk* |
| **Causa** | Este error ocurre cuando el script intenta realizar una lectura SNMP y la conexión expira sin recibir los datos solicitados. |
| **Solución** | El dispositivo monitorizado no respondió a las solicitudes SNMP de Monsta.<br /><br />Edite el dispositivo, acceda al menú **Recopilación > SNMP** y aumente el Timeout SNMP. Utilice el botón "Probar" para validar la comunicación. Después, guarde las modificaciones.<br /><br />Si el problema persiste, verifique en su red:<br /><br />• **Comunidad SNMP Incorrecta**: la "Community String" (ej.: `public` o `private`) configurada en Monsta no coincide con la configurada en el dispositivo.<br />• **Versión SNMP Divergente**: el dispositivo está usando SNMP v2c y el script/configuración está intentando v1 (o viceversa), o hay un error en las credenciales de v3.<br />• **ACL o Firewall**: el dispositivo tiene una lista de control de acceso (ACL) que permite solo a IPs específicas realizar consultas SNMP, y la IP de Monsta no está en ella.<br />• **Puerto Bloqueado**: el puerto UDP 161 (por defecto del SNMP) está bloqueado en el camino.<br />• **Sobrecarga del Agente SNMP**: el procesador del dispositivo monitorizado está tan ocupado que el servicio (agente) SNMP no puede responder a la consulta a tiempo. |

---

### Error converting to type: Float

| Campo | Descripción |
| :--- | :--- |
| **Error** | *Error converting to type: Float* |
| **Causa** | Este error ocurre cuando el sistema espera un **número decimal (Float)**, pero recibió algo que no puede convertir en número, como un texto (String) inválido o un valor nulo (`nil`). |
| **Solución** | Revise el script del monitor para garantizar que el retorno no contenga **strings** (como comas o unidades de medida) en el campo de valor. Si el monitor presenta lecturas normales pero muestra fallos intermitentes con este error, es probable que el dispositivo esté devolviendo un valor **nulo (nil)**. Esto ocurre cuando no hay respuesta en la consulta; en esos casos, verifique en los registros del equipo la existencia de alguna falla. |

---

### Erro: wamp.error.no_such_procedure

| Campo | Descripción |
| :--- | :--- |
| **Error** | *`wamp.error.no_such_procedure`* |
| **Causa** | Indica, en la mayoría de los casos, que el servicio **`monkerneld`** no está en ejecución en el sistema operativo Linux donde está instalado el software. El servicio `monkerneld` es importante para el correcto funcionamiento del software, y su inactividad impide que Monsta ejecute procedimientos necesarios. |
| **Solución** | La solución implica garantizar que el servicio `monkerneld` se inicie. El usuario puede escoger entre dos enfoques principales para solventar esta situación:<br /><br />**A. Reiniciar el sistema**: La forma más completa de resolver la mayoría de los problemas de arranque de servicios es simplemente **reiniciar el sistema Linux** donde está instalado el software. Al reiniciar, el sistema operativo intentará cargar e iniciar todos los servicios configurados, incluido `monkerneld`, de forma automática.<br />**B. Iniciar el servicio manualmente (Recomendado)**: Si reiniciar no es viable o demora, el usuario puede intentar iniciar el servicio directamente usando **`systemctl`**, que es la herramienta estándar de gestión de servicios en muchas distribuciones Linux modernas (como Ubuntu, Debian, CentOS, RHEL, etc.).<br />**Pasos**: <br />1. Abra un **Terminal** (o utilice una sesión SSH) en el servidor Linux.<br />2. Ejecute el siguiente comando para intentar iniciar el servicio: `sudo systemctl start monsta-com.monkerneld`<br />**Nota**: Es obligatorio que este comando requiera permisos de **superusuario (sudo)**.<br /><br /> Tras ejecutar cualquiera de las acciones anteriores (reiniciar el sistema o iniciar el servicio manualmente), puede **verificar el estado del servicio** para asegurarse de que esté activo y en ejecución: `systemctl status monsta-com.monkerneld`<br />El estado ideal debe indicar **`active (running)`** |

---

### Ssh error occured: Key exchange init failed

| Campo | Descrição |
| :--- | :--- |
| **Error** | *Ssh error occured: Key exchange init failed stack traceback* |
| **Causa** | Este error ocurre durante el intento de conexión SSH entre Monsta y un dispositivo remoto (generalmente modelos más antiguos de switches, routers o radios). Indica que Monsta y el dispositivo no pudieron ponerse de acuerdo sobre qué **algoritmo de intercambio de claves (Key Exchange)** usar, ya que el dispositivo emplea estándares que hoy en día son considerados legados o inseguros por bibliotecas modernas. |
| **Solución** | Monsta utiliza bibliotecas de criptografía de última generación. La falla en el intercambio de claves (Key Exchange) es una advertencia de que el dispositivo remoto está operando con estándares de seguridad obsoletos. La corrección definitiva es actualizar el dispositivo monitorizado para que soporte algoritmos de cifrado seguros. |

---

### No route to host (os error 113)

| Campo | Descrição |
| :--- | :--- |
| **Error** | *No route to host (os error 113) stack traceback* |
| **Causa** | El error `os error 113` es un código de error de red del sistema operativo que indica que el host de destino no pudo ser alcanzado. El sistema operativo no sabe por qué interfaz de red debe enviar el paquete para alcanzar esa IP específica. |
| **Solución** | Para resolver el error, asegúrese de que la tabla de enrutamiento del sistema tenga una ruta válida hacia la IP de destino y que la puerta de enlace por defecto esté configurada correctamente para reenviar los paquetes fuera de la red local. |