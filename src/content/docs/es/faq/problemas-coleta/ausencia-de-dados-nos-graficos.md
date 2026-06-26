---
title: "¿Cómo resolver la ausencia de datos en los gráficos?"
---

Se você visualizar o símbolo **"---"** no lugar dos valor, isso indica que **o sistema não conseguiu utilizar o protocolo selecionado** para obter as informações necessárias do recurso monitorado.

Neste caso, a coleta de dados falhou, e nenhuma informação pode ser processada ou exibida nos gráficos.

## **¿Qué hacer?**

Para investigar la causa específica de la falla del protocolo, puede checar el **Registro de Errores** del evento:

1. **Edite el Monitor** en cuestión.
2. En la pantalla de edición que se abrirá, busque y seleccione la opción **"Registro de Errores"** ubicada en la **esquina inferior izquierda** de la pantalla.

El Registro de Errores proporcionará detalles técnicos sobre el motivo de la falla de comunicación, ayudando a resolver el problema.

## Algunas fallas conocidas:

### SNMP timeout (Múltiplas funções)

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *SNMP timeout stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'getex' [string "script"]:157: in function 'get' [string "script"]:1: in main chunk* |
| **Causa** | El equipo monitorizado no está respondiendo al SNMP. |
| **Solução** | Verifique si hay comunicación entre Monsta y el equipo monitorizado. Si está OK, compruebe los siguientes puntos:<br /><br />• ¿El servicio SNMP se está ejecutando en el equipo monitorizado?<br />• ¿El puerto configurado en Monsta es el mismo que el del equipo?<br />• ¿La comunidad es correcta?<br />• Si utiliza SNMPv3, ¿los datos configurados coinciden con la configuración del equipo?<br />• ¿Hay algún firewall que bloquee la comunicación en el puerto seleccionado? |

---

### Error de resolución DNS (registro no encontrado)

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *DNS error: DNS resolution error: no record found for Query { name: Name("meuhost.com.br"), query_type: AAAA, query_class: IN } stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'getex' [string "script"]:157: in function 'get' [string "script"]:1: in main chunk* |
| **Causa** | El nombre del host no se resuelve en el servidor DNS. |
| **Solução** | Verifique si los servidores DNS configurados en el sistema operativo son correctos. |

---

### E/S: Tiempo de espera al conectar

| Campo | Descrição |
| :--- | :--- |
| **Erro** | *I/O: Timeout connecting to xx.xx.xx.xx:pppp stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'connect' [string "script"]:356: in function <[string "script"]:337> (tail call): in function <(tail call):-1>* |
| **Causa** | La consulta al host xx.xx.xx.xx en el puerto pppp no devuelve información. |
| **Solução** | Compruebe la siguiente información:<br /><br />• ¿Hay comunicación entre Monsta y el host monitorizado?<br />• ¿El servicio que reporta información en el puerto solicitado está en ejecución?<br />• ¿Hay algún firewall bloqueando la conexión? |