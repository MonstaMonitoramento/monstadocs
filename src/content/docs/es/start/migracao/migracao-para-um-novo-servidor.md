---
title: "Migración a un Nuevo Servidor"
description: Aprenda cómo migrar Monsta a un nuevo servidor preservando configuraciones, monitorizaciones, historial y datos de la plataforma de forma segura.
---

Este tutorial muestra cómo migrar Monsta desde la versión >5.0 a otro servidor.

:::danger[Atención]

¡No instale Monsta en el nuevo servidor! Este procedimiento debe realizarse en un Linux sin Monsta instalado. El script de migración realiza todo el proceso de copia de los datos e instalación de Monsta.

:::

## Requisitos mínimos

Requisitos mínimos para la migración de Monsta:

:::caution
Compruebe si la partición "/var" del nuevo servidor tiene suficiente espacio para la transferencia de los datos de Monsta desde el servidor actual.
:::

| Elemento | Requisito mínimo |
| :---: | :--- |
| ![Espacio en disco](/src/assets/images/p25_image-1645452261754.png) | **Espacio en disco**<br />40GB libres para /var (configuraciones, base de datos y logs)<br />300MB libres para /opt/monsta (programas y bibliotecas)<br />Asegúrese de que la nueva instalación dispone del espacio suficiente para efectuar la migración. |
| ![Memoria RAM](/src/assets/images/p25_image-1645452312898.png) | **Memoria RAM**<br />2GB de memoria RAM |
| ![Sistema operativo](/src/assets/images/p25_image-1645452455434.png) | **Sistema operativo**<br />Linux de 64 bits<br />Sistema operativo Linux recomendado: Fedora Server 40 (sistemas x86_64) u Ubuntu Server 24. Puede utilizarse la instalación mínima para Monsta. |
| ![Procesador](/src/assets/images/p25_image-1645452542916.png) | **Procesador**<br />Núcleos: 2<br />Velocidad: 1.8 GHz |

:::note
Las configuraciones anteriores permiten, en general, monitorizar aproximadamente 500 dispositivos con 10 monitores cada uno o un total de 5.000 monitores.
:::

## Script de migración

Conectado como root en su servidor, descargue el script de migración según el ejemplo a continuación:

### Fedora/Red-Hat

```shell
yum install -y wget sshpass
wget https://www.monsta.com.br/monsta/download/migrate.sh
```

### Ubuntu/Debian

```shell
apt-get install -y wget sshpass
wget https://www.monsta.com.br/monsta/download/migrate.sh
```

## Iniciando la transferencia

Tras descargar el script, ejecútelo con la siguiente sintaxis:

`sh migrate.sh <usuario> <"contraseña"> <IP del servidor Monsta actual> <puerto ssh>`

Ejemplo:

```shell
sh migrate.sh root "minha senha" 192.168.1.1 22
```

El script finalizará los procesos de Monsta en ejecución en el servidor antiguo (192.168.1.1) e iniciará la copia de la estructura con los datos al nuevo servidor. Al finalizar el proceso podrá acceder a su Monsta en el nuevo servidor y el antiguo podrá ser desactivado.

:::note
El tiempo empleado en esta transferencia dependerá del tamaño de la base de datos existente, pudiendo tardar desde minutos hasta varias horas.
:::

:::danger[Importante]
Para que el script migrate se ejecute con éxito y garantice la copia y creación de todos los archivos y directorios con los permisos correctos (incluyendo archivos del sistema, logs y configuraciones sensibles), es **obligatorio** que la ejecución se realice por un usuario con privilegios de **superusuario (`root`)** en **ambos los servidores** (Origen y Destino). La ejecución con un usuario no root provocará problemas durante la transferencia de los datos.  
  
Si ocurre algún error de **timeout** durante la ejecución de `migrate.sh`, compruebe si el puerto SSH en el servidor remoto está abierto en el firewall para el acceso desde el servidor local.  
  
En caso de fallo, incluso siguiendo las instrucciones de uso de `migrate.sh`, **recoja los logs mostrados en pantalla y póngase en contacto con nuestro equipo de soporte**.
:::