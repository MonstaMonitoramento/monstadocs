---
title: "Gestión de Servicios de Monsta desde la Línea de Comandos (Linux)"
description: Aprenda a detener, iniciar y comprobar el estado de los servicios de Monsta mediante comandos en Linux.
---

Este artículo describe los procedimientos estándar para iniciar, detener y comprobar el estado de los servicios de **Monsta** en sistemas operativos Linux utilizando la utilidad `systemd` (`systemctl`).

---

## 1. Inicialización de los Servicios (Inicio)

La inicialización de los servicios de Monsta debe seguir un **orden específico** de dependencias para garantizar que la infraestructura subyacente esté lista antes de que los módulos de enrutamiento y actualización se activen.

Ejecute los comandos a continuación secuencialmente en el terminal con privilegios de superusuario (`sudo`):

```bash
# 1. Iniciar la base de datos
sudo systemctl start monsta-com.monstadb.service

# 2. Iniciar monagent, responsable de las recopilaciones
sudo systemctl start monsta-com.monagent.service

# 3. Iniciar el núcleo del sistema, responsable de los logs y de la interfaz entre los demás servicios y la base de datos
sudo systemctl start monsta-com.monkernel.service

# 4. Iniciar el servidor http responsable de proporcionar la interfaz http al usuario
sudo systemctl start monsta-com.monrouter.service

# 5. Iniciar el subsistema que comprueba periódicamente si hay nuevas actualizaciones
sudo systemctl start monsta-com.monstaupd.service
```

---

## 2. Parada de los Servicios (Stop)

Para interrumpir el funcionamiento de los servicios, puede optar por detenerlos individualmente o todos a la vez.

### Parada Individual

Sustituya `<nome-do-servico>` por el identificador correspondiente (por ejemplo, `monstaupd`, `monrouter`, etc.):

```bash
sudo systemctl stop monsta-com.<nome-do-servico>.service
```

### Parada Completa (Todos los Servicios)

Para detener **todos** los servicios del ecosistema Monsta simultáneamente de forma rápida, utilice el comodín (`*`):

```bash
sudo systemctl stop monsta-com.*
```

---

## 3. Verificación del Estado

Para comprobar si un servicio específico se está ejecutando, está activo y si hay mensajes recientes de registro relacionados con su estado, utilice el comando `status`:

```bash
sudo systemctl status monsta-com.<nome-do-servico>.service
```

*Ejemplo para comprobar el estado de la base de datos:*

```bash
sudo systemctl status monsta-com.monstadb.service
```