---
title: "Guide to Common Errors"
---

This document is a quick guide to identify and fix failures in custom scripts on Monsta Tecnologia. If you encountered a runtime error or an unexpected return in a sensor, consult the categories below.

**Structure of each topic**:

1. **Error**: Description of the symptom or log message.
2. **Probable Cause**: What usually triggers this behavior.
3. **Solution**: Step-by-step instructions for correction.

---

### Lua script runner timeout

| Field | Description |
| :--- | :--- |
| **Error** | *Lua script runner timeout: deadline has elapsed* |
| **Cause** | This error occurs when Monsta's execution engine terminates the Lua script because it exceeded the allowed timeout for a sensor's execution. By default, Monsta kills scripts that take too long to respond to prevent the system from hanging or consuming excessive server resources. |
| **Solution** | Go to **Configuration > Parameters** and use the search field to locate the `lua.timeout` key. The default value is 130 seconds. To change it, click **Unlock**, enter the new value and save. |

---

### Pagefile: Timeout connecting

| Field | Description |
| :--- | :--- |
| **Error** | *Pagefile: Timeout connecting to xx.xx.xx.xx:xxxx stack traceback: [C]: in function 'poll' [string "?"]:x: in function 'connect' [string "script"]:xxx: in function <[string "script"]:xxx> (tail call): in function <(tail call):-1>* |
| **Cause** | This error indicates a failure attempting to establish a network connection. The Lua script was able to start the call, but it timed out before the destination device responded to the connection handshake.<br /><br />The *"stack traceback"* shows that the failure occurred exactly at the moment of attempting the connection (`in function 'connect'`), even before any data was sent or received. |
| **Solution** | Edit the device, go to **Collection > WMI** and increase the WMI Timeout field. Use the "Test" button to validate communication. Then save the changes.<br /><br />If the problem persists, other network-related factors may be blocking this communication. In that case, check the following on your network:<br /><br />• **Firewall/Blocking**: Is there a firewall rule on the destination or along the path (ACL, IPS) blocking Monsta's IP on the specified port.<br />• **Service Offline**: The service you are trying to monitor (e.g., API, web server, database) is stopped or not listening on that specific port.<br />• **Unreachable Network**: The Monsta server does not have a valid route to the destination IP.<br />• **Incorrect Port**: The script is attempting to connect to a different port than the service uses.<br />• **Excessive Load on Target**: The target device's CPU is so high that it cannot process new connection requests. |

---

### Response Time: ping failed

| Field | Description |
| :--- | :--- |
| **Error** | *Tempo de Resposta: ping failed: Request timeout for icmp_seq x* |
| **Cause** | This error occurs when Monsta sends an ICMP echo packet (the familiar "ping") to a device but does not receive the reply (Echo Reply) within the expected time. |
| **Solution** | The monitored device did not respond to Monsta's ICMP (ping) requests.<br /><br />💡 **Tip**: If the equipment is on a network with high latency or packet loss, adjust the detection sensitivity. To do this, edit the device and go to **Details > Sensitivity**, changing the parameters according to the environment's needs. |

---

### SNMP timeout stack traceback

| Field | Description |
| :--- | :--- |
| **Error** | *SNMP timeout stack traceback: [C]: in function 'poll' [string robbery/snmp_checker]:xx: in function 'getex' [string "script"]:xx: in function 'get' [string "script"]:xx: in main chunk* |
| **Cause** | This error occurs when the script attempts an SNMP read and the connection times out without receiving the requested data. |
| **Solution** | The monitored device did not respond to Monsta's SNMP requests.<br /><br />Edit the device, go to **Collection > SNMP** and increase the SNMP Timeout. Use the "Test" button to validate communication. Then save the changes.<br /><br />If the problem persists, check the following on your network:<br /><br />• **Incorrect SNMP Community**: The "Community String" (e.g., `public` or `private`) configured in Monsta does not match the one configured on the device.<br />• **SNMP Version Mismatch**: The device is using SNMP v2c and the script/configuration is trying v1 (or vice-versa), or there are credential errors for v3.<br />• **ACL or Firewall**: The device has an access control list (ACL) that only allows specific IPs to perform SNMP queries, and Monsta's IP is not included.<br />• **Port Blocked**: UDP port 161 (SNMP default) is blocked along the path.<br />• **SNMP Agent Overload**: The monitored device's processor is so busy that the SNMP agent cannot respond to the query in time. |

---

### Error converting to type: Float

| Field | Description |
| :--- | :--- |
| **Error** | *Error converting to type: Float* |
| **Cause** | This error occurs when the system expects a **decimal number (Float)** but received something it cannot convert to a number, such as an invalid text (String) or a null value (`nil`). |
| **Solution** | Review the monitor script to ensure the return value does not contain **strings** (such as commas or measurement units) in the value field. If the monitor shows normal readings but intermittently fails with this error, the device is likely returning a **null (nil)** value. This happens when there is no response to the query; in such cases, check the device logs for any failures. |

---

### Error: wamp.error.no_such_procedure

| Field | Description |
| :--- | :--- |
| **Error** | *`wamp.error.no_such_procedure`* |
| **Cause** | This usually indicates that the **`monkerneld`** service is not running on the Linux operating system where the software is installed. The `monkerneld` service is important for the software to function correctly, and its inactivity prevents Monsta from executing required procedures. |
| **Solution** | The solution involves ensuring the `monkerneld` service is started. The user can choose between two main approaches to work around this situation:<br /><br />**A. Reboot the System**: The most comprehensive way to resolve most service startup issues is to **reboot the Linux system** where the software is installed. On reboot, the operating system will attempt to load and start all configured services, including `monkerneld`, automatically.<br />**B. Start the Service Manually (Recommended)**: If rebooting is not feasible or takes too long, the user can try to start the service directly using **`systemctl`**, which is the standard service management tool on many modern Linux distributions (such as Ubuntu, Debian, CentOS, RHEL, etc.).<br />**Steps**: <br />1. Open a **Terminal** (or use an SSH session) on the Linux server.<br />2. Run the following command to attempt to start the service: `sudo systemctl start monsta-com.monkerneld`<br />**Note**: This command must be run with **superuser (sudo)** privileges.<br /><br /> After performing either action above (rebooting the system or starting the service manually), you can **check the service status** to ensure it is active and running: `systemctl status monsta-com.monkerneld`<br />The ideal status should indicate **`active (running)`** |

---

### Ssh error occured: Key exchange init failed

| Field | Description |
| :--- | :--- |
| **Error** | *Ssh error occured: Key exchange init failed stack traceback* |
| **Cause** | This error occurs during an SSH connection attempt between Monsta and a remote device (usually older models of switches, routers, or radios). It indicates that Monsta and the device could not agree on which **key exchange algorithm** to use, because the device uses standards now considered legacy or insecure by modern libraries. |
| **Solution** | Monsta uses up-to-date cryptographic libraries. A key exchange failure is a warning that your remote device is operating with obsolete security standards. The definitive fix is to upgrade the monitored device so it supports secure cryptographic algorithms. |

---

### No route to host (os error 113)

| Field | Description |
| :--- | :--- |
| **Error** | *No route to host (os error 113) stack traceback* |
| **Cause** | The `os error 113` is an operating system network error code indicating that the destination host could not be reached. The operating system does not know which network interface to use to send a packet to that specific IP. |
| **Solution** | To resolve the error, ensure the system's routing table has a valid path to the destination IP and that the default gateway is configured correctly to forward packets outside the local network. |