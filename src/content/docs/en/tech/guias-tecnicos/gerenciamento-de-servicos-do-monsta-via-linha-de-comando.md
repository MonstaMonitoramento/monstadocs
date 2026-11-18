---
title: "Monsta Service Management via Command Line (Linux)"
description: Learn how to stop, start, and check the status of Monsta services using commands on Linux.
---

This article describes the standard procedures to start, stop, and check the status of **Monsta** services on Linux operating systems using the `systemd` (`systemctl`) utility.

---

## 1. Starting Services (Start)

Starting Monsta services must follow a **specific order** of dependencies to ensure the underlying infrastructure is ready before the routing and update modules are activated.

Run the commands below sequentially in the terminal with superuser privileges (`sudo`):

```bash
# 1. Start the database
sudo systemctl start monsta-com.monstadb.service

# 2. Start monagent, responsible for collections
sudo systemctl start monsta-com.monagent.service

# 3. Start the system core, responsible for logs and the interface between other services and the database
sudo systemctl start monsta-com.monkernel.service

# 4. Start the HTTP server responsible for providing the HTTP interface to the user
sudo systemctl start monsta-com.monrouter.service

# 5. Start the subsystem that periodically checks for new updates
sudo systemctl start monsta-com.monstaupd.service
```

---

## 2. Stopping Services (Stop)

To stop the services, you can choose to stop them individually or all at once.

### Stopping Individually

Replace `<nome-do-servico>` with the corresponding identifier (for example, `monstaupd`, `monrouter`, etc.):

```bash
sudo systemctl stop monsta-com.<nome-do-servico>.service
```

### Complete Stop (All Services)

To stop **all** Monsta ecosystem services at once quickly, use the wildcard (`*`):

```bash
sudo systemctl stop monsta-com.*
```

---

## 3. Checking Status

To check whether a specific service is running, active, and if there are recent log messages related to its state, use the `status` command:

```bash
sudo systemctl status monsta-com.<nome-do-servico>.service
```

*Example to check the database status:*

```bash
sudo systemctl status monsta-com.monstadb.service
```