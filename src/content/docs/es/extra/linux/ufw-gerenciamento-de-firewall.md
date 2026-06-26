---
title: "Gestión del Firewall - UFW"
sidebar:
  order: 4
---

**UFW** significa **Uncomplicated Firewall** (Cortafuegos Descomplicado).

Es una interfaz para gestionar el firewall Netfilter en Linux, que es el sistema de filtrado de paquetes del sistema. UFW fue desarrollado con el objetivo de simplificar el proceso de configuración de reglas de firewall mediante la utilidad `iptables`.

UFW es el método más popular y recomendado para gestionar el firewall en distribuciones basadas en Debian y Ubuntu.

### Ejemplos de comandos UFW (Guía práctica)

La mayoría de los comandos de UFW requieren privilegios de superusuario (`sudo`).

#### 1. Comprobación del estado

Compruebe si UFW está activo y vea las reglas actuales:



| **Acción** | **Comando** | **Salida de ejemplo** |
| --- | --- | --- |
| **Verificar Status** | `ufw status` | `Status: inactive` (o `active`) |
| **Ver detalles** | `ufw status verbose` | Lista todas las reglas de forma detallada. |



#### 2. Activación y desactivación

Es crucial definir las reglas antes de activar, para no quedarse fuera del servidor.



| **Acción** | **Comando** | **Observación** |
| --- | --- | --- |
| **Activar UFW** | `ufw enable` | **Atención**: Si no tiene una regla `allow ssh`, perderá el acceso remoto. |
| **Desactivar UFW** | `ufw disable` | Elimina el firewall (no recomendado). |
| **Restablecer reglas** | `ufw reset` | Elimina todas las reglas definidas por el usuario. |



#### 3. Políticas predeterminadas (Default)

Configure lo que ocurre con el tráfico que no coincide con ninguna regla específica.



| **Acción** | **Comando** | **Resultado** |
| --- | --- | --- |
| **Bloquear entrada (Recomendado)** | `ufw default deny incoming` | Ninguna conexión externa está permitida, a menos que se especifique. |
| **Permitir salida** | `ufw default allow outgoing` | Su servidor puede iniciar conexiones con el exterior. |



#### 4. Añadir reglas (Permisos)



| **Objetivo** | **Comando** | **Observación** |
| --- | --- | --- |
| **Permitir SSH (Puerto 22)** | `ufw allow ssh` | Usa el nombre del servicio para abrir el puerto 22/TCP. |
| **Permitir HTTP (Puerto 80)** | `ufw allow http` | Abre el puerto 80/TCP. |
| **Permitir HTTPS (Puerto 443)** | `ufw allow 443/tcp` | Abre usando el número de puerto y protocolo. |
| **Puerto específico** | `ufw allow 5432/udp` | Abre el puerto 5432 solo para el protocolo UDP. |
| **Tráfico desde IP específico** | `ufw allow from 192.168.1.100 to any port 3306` | Permite que solo la IP `192.168.1.100` acceda al puerto 3306 (MySQL). |



#### 5. Eliminar reglas

La eliminación puede realizarse por el número de la regla o por el texto de la regla.



| **Acción** | **Comando** | **Observación** |
| --- | --- | --- |
| **Eliminar por texto** | `ufw delete allow http` | Elimina la regla de acceso al puerto http (80/TCP). |
| **Eliminar por número** | `ufw status numbered` `ufw status delete [número]` | El primer comando devuelve una lista con las reglas existentes y su posición, el segundo elimina la regla en la posición seleccionada. |