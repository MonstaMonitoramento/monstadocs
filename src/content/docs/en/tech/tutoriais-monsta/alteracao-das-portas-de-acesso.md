---
title: "Changing the Access Ports"
---

This guide describes the procedure to change the listening ports of the **Monsta** web interface. By default, the system uses specific ports that can be customized via the command line on the Linux server.

## Prerequisites

- SSH access to the server where Monsta is installed.
- Superuser privileges (`root` or `sudo`).
- Ensure the new ports you choose are not being used by other services (e.g., Apache, Nginx, Docker).

## Step-by-Step Procedure

1. **Access the Terminal**: Open the console of your server.
2. **Run the configuration utility**: Use the `monkerneld` binary with the `port` parameter to set the new HTTP port and the SSL (HTTPS) port.
    
```shell
/opt/monsta/bin/monkerneld port --port <porta http> 8090 --sslport <porta https>
```
    
**Example**:
```shell
/opt/monsta/bin/monkerneld port --port 8090 --sslport 8443  
```      

**Command Parameters**:
- `--port`: Sets the port for unencrypted connections (HTTP).
- `--sslport`: Sets the port for secure connections (HTTPS).

:::caution[Important: *Firewall* Configuration]
After changing, remember to open the new ports in the Linux *firewall* (UFW or Firewalld) and, if applicable, in the security rules of your network/cloud infrastructure.
:::