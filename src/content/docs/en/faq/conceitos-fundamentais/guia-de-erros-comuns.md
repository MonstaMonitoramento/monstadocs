---
title: Common Errors Guide
---
This document is a quick guide to identify and fix failures in custom scripts on Monsta Tecnologia. If you encountered a runtime error or an unexpected return in a sensor, consult the categories below.

**Structure of each topic**:

1. **Error**: Description of the symptom or log message.
2. **Probable Cause**: What usually triggers this behavior.
3. **Solution**: Step-by-step to fix it.

---

### Lua script runner timeout


| Campo | Descrição |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Lua script runner timeout: deadline has elapsed* |
| **Causa** | This error occurs when Monsta's execution engine stops the Lua script because it exceeded the allowed execution timeout for a sensor. By default, Monsta stops scripts that take too long to respond to prevent the system from becoming stuck or consuming excessive server resources. |
| **Solução** | Go to **Configuration > Parameters** and use the search field to locate the key `lua.timeout`. The default value is 130 seconds. To change it, click **Unlock**, enter the new value and save. |


---

### Pagefile: Timeout connecting


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Pagefile: Timeout connecting to xx.xx.xx.xx:xxxx stack traceback: [C]: in function 'poll' [string "?"]:x: in function 'connect' [string "script"]:xxx: in function <[string "script"]:xxx> (tail call): in function <(tail call):-1>* |
| **Causa** | This error indicates a failure to establish a network connection. The Lua script was able to initiate the call, but it timed out before the target device responded to the connection handshake. The *"stack traceback"* shows that the failure occurred exactly at the moment of attempting the connection (`in function 'connect'`), before any data was sent or received. |
| **Solução** | Edit the device, go to the **Collection > WMI** menu and increase the WMI Timeout field. Use the "Test" button to validate communication. Then save the changes. If the problem persists, other network-related factors may be preventing communication. In that case, check in your network: • **Firewall/Block**: Is there a firewall rule on the destination or along the path (ACL, IPS) blocking Monsta's IP on the specified port. • **Service Offline**: The service you are trying to monitor (e.g., API, web server, database) is stopped or not listening on that specific port. • **Unreachable Network**: The Monsta server does not have a valid route to the destination IP. • **Incorrect Port**: The script is attempting to connect to a port different from the one the service uses. • **Excessive Load on Destination**: The target device's CPU is so high that it cannot process new connection requests. |


---

### Response Time: ping failed


| Campo | Descrição |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Tempo de Resposta: ping failed: Request timeout for icmp_seq x* |
| **Causa** | This error occurs when Monsta sends an ICMP echo packet (the familiar "Ping") to a device but does not receive the reply (Echo Reply) within the expected time. |
| **Solução** | The monitored device did not respond to Monsta's ICMP (ping) requests. 💡 **Tip**: If the equipment is on a network with high latency or packet loss, adjust the detection sensitivity. To do this, edit the device and go to **Details > Sensitivity**, changing the parameters according to the environment needs. |


---

### SNMP timeout stack traceback


| Campo | Descrição |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *SNMP timeout stack traceback: [C]: in function 'poll' [string robbery/snmp_checker]:xx: in function 'getex' [string "script"]:xx: in function 'get' [string "script"]:xx: in main chunk* |
| **Causa** | This error occurs when the script attempts an SNMP read and the connection times out without receiving the requested data. |
| **Solução** | The monitored device did not respond to Monsta's SNMP requests. Edit the device, go to the **Collection > SNMP** menu and increase the SNMP Timeout. Use the "Test" button to validate communication. Then save the changes. If the problem persists, check in your network: • **Incorrect SNMP Community**: The "Community String" (e.g., `public` or `private`) configured in Monsta does not match the one configured on the device. • **SNMP Version Mismatch**: The device is using SNMP v2c and the script/configuration is attempting v1 (or vice versa), or there is an error in v3 credentials. • **ACL or Firewall**: The device has an access control list (ACL) that only allows specific IPs to perform SNMP queries, and Monsta's IP is not included. • **Blocked Port**: UDP port 161 (SNMP default) is blocked along the path. • **SNMP Agent Overload**: The monitored device's processor is so busy that the SNMP service (agent) cannot respond to the query in time. |


---

### Error converting to type: Float


| Campo | Descrição |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Error converting to type: Float* |
| **Causa** | This error occurs when the system expects a **decimal number (Float)** but received something it cannot convert to a number, such as an invalid text (String) or a null value (`nil`). |
| **Solução** | Review the monitor script to ensure the return does not contain **strings** (such as commas or measurement units) in the value field. If the monitor shows normal readings but displays intermittent failures with this error, it is likely the device is returning a **null (nil)** value. This happens when there is no response to the query; in those cases, check the equipment logs for any failure. |


---

### Error: wamp.error.no_such_procedure


| Campo | Descrição |
| ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **Erro** | *`wamp.error.no_such_procedure`* |
| **Causa** | It usually indicates that the `**monkerneld**` service is not running on the Linux operating system where the software is installed. The `monkerneld` service is important for the correct operation of the software, and its inactivity prevents Monsta from executing necessary procedures. |
| **Solução** | The solution involves ensuring the `monkerneld` service is started. The user can choose between two main approaches to work around this situation: **A. Reboot the System**: The most comprehensive way to resolve most service startup issues is simply to **reboot the Linux system** where the software is installed. On reboot, the operating system will attempt to load and start all configured services, including `monkerneld`, automatically. **B. Start the Service Manually (Recommended)**: If a reboot is not feasible or takes too long, the user can try to start the service directly using `**systemctl**`, which is the standard service management tool in many modern Linux distributions (such as Ubuntu, Debian, CentOS, RHEL, etc.). **Steps**: 1. Open a **Terminal** (or use an SSH session) on the Linux server. 2. Run the following command to try to start the service: `sudo systemctl start monsta-com.monkerneld` **Note**: This command requires **superuser (sudo)** permissions. After performing either action (rebooting the system or starting the service manually), you can **check the service status** to ensure it is active and running: `systemctl status monsta-com.monkerneld` The ideal status should indicate `**active (running)**` |


---

### Ssh error occured: Key exchange init failed


| Campo | Descrição |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Ssh error occured: Key exchange init failed stack traceback* |
| **Causa** | This error occurs during an SSH connection attempt between Monsta and a remote device (usually older models of switches, routers or radios). It indicates that Monsta and the device could not agree on which **Key Exchange** algorithm to use, because the device uses patterns that are considered legacy or insecure by modern libraries. |
| **Solução** | Monsta uses up-to-date cryptography libraries. The Key Exchange failure is an alert that your remote device is operating with obsolete security standards. The definitive fix is to update the monitored device so it supports secure cryptographic algorithms. |


---

### No route to host (os error 113)


| Campo | Descrição |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No route to host (os error 113) stack traceback* |
| **Causa** | The `os error 113` is an operating system network error code indicating that the destination host could not be reached. The OS does not know which network interface should be used to send the packet to that specific IP. |
| **Solução** | To resolve the error, ensure the system's routing table has a valid path to the destination IP and that the default gateway is configured correctly to forward packets outside the local network. |


### Command not supported on legacy WMI probe, please update to the latest version


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Command not supported on legacy WMI probe, please update to the latest version* |
| **Causa** | The probe or agent running is outdated and does not support the requested feature or command. |
| **Solução** | To use this feature, you must update the probe. Visit our website ([https://www.monsta.com.br](https://www.monsta.com.br)), download the latest installer from the downloads section and install it on the monitored equipment. |


### Powershell is not available: no agent or probe with min version 1.2.8 detected


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *Powershell is not available: no agent or probe with min version 1.2.8 detected* |
| **Causa** | The probe or agent running is outdated and does not support the requested feature or command. |
| **Solução** | To use this feature, you must update the probe. Visit our website ([https://www.monsta.com.br](https://www.monsta.com.br)), download the latest installer from the downloads section and install it on the monitored equipment. |


### No agent or probe with min version 1.2.8 detected


| Campo | Descrição |
| ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Erro** | *No agent or probe with min version 1.2.8 detected* |
| **Causa** | The probe or agent running is outdated and does not support the requested feature or command. |
| **Solução** | To use this feature, you must update the probe. Visit our website ([https://www.monsta.com.br](https://www.monsta.com.br)), download the latest installer from the downloads section and install it on the monitored equipment. |