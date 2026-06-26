---
title: "How to Resolve Missing Data in Charts?"
---

If you see the symbol **"---"** in place of the values, this indicates that **the system couldn't use the selected protocol** to obtain the necessary information from the monitored resource.

In this case, data collection failed, and no information can be processed or displayed in the charts.

## **What to do?**

To investigate the specific cause of the protocol failure, you can check the event's **Error Log**:

1. **Edit the Monitor** in question.
2. On the edit screen that opens, look for and select the **"Error Log"** option located in the **bottom left corner** of the screen.

The Error Log will provide technical details about the reason for the communication failure, helping to resolve the issue.

## Some known failures:

### SNMP timeout (Multiple functions)

| Field | Description |
| :--- | :--- |
| **Error** | *SNMP timeout stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'getex' [string "script"]:157: in function 'get' [string "script"]:1: in main chunk* |
| **Cause** | The monitored device is not responding to SNMP. |
| **Solution** | Check whether there is communication between Monsta and the monitored device. If it's ok, verify the items below:<br /><br />• Is the SNMP service running on the monitored device?<br />• Is the port configured in Monsta the same as the device's?<br />• Is the community correct?<br />• If using SNMPv3, are the configured credentials in accordance with the device's configuration?<br />• Is there any firewall blocking communication on the selected port? |

---

### DNS resolution error (no record found)

| Field | Description |
| :--- | :--- |
| **Error** | *DNS error: DNS resolution error: no record found for Query { name: Name("meuhost.com.br"), query_type: AAAA, query_class: IN } stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'getex' [string "script"]:157: in function 'get' [string "script"]:1: in main chunk* |
| **Cause** | The host name is not resolved by the DNS server. |
| **Solution** | Check whether the DNS servers configured in the operating system are correct. |

---

### I/O: Timeout connecting

| Field | Description |
| :--- | :--- |
| **Error** | *I/O: Timeout connecting to xx.xx.xx.xx:pppp stack traceback: [C]: in function 'poll' [string "?"]:4: in function 'connect' [string "script"]:356: in function <[string "script"]:337> (tail call): in function <(tail call):-1>* |
| **Cause** | The query to host xx.xx.xx.xx on port pppp does not return information. |
| **Solution** | Check the following information:<br /><br />• Is there communication between Monsta and the monitored host?<br />• Is the service that reports information on the requested port running?<br />• Is there any firewall blocking the connection? |