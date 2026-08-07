---
title: Migración a un Nuevo Servidor
description: Aprenda cómo migrar Monsta a un nuevo servidor preservando configuraciones,
  monitorizaciones, historial y datos de la plataforma de forma segura.
---
Este tutorial muestra cómo migrar Monsta desde la versión >5.0 a otro servidor.

:::danger[Atención]

¡No instale Monsta en el nuevo servidor! Este procedimiento debe realizarse en un Linux sin Monsta instalado. El script de migración realiza todo el proceso de copia de datos e instalación de Monsta.

:::

## Requisitos mínimos

Requisitos mínimos para la migración de Monsta:

:::caution
Verifique que la partición "/var" del nuevo servidor tenga espacio suficiente para la transferencia de los datos de Monsta desde el servidor actual.
:::


| Item | Requisito Mínimo |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![Espacio en disco](/src/assets/images/p25_image-1645452261754.png) | **Espacio en disco** 40GB libre para /var (configuraciones, bases de datos y logs) 300MB libre para /opt/monsta (programas y bibliotecas) Certifique-se de que la nueva instalación tenga espacio suficiente para realizar la migración. |
| ![Memoria RAM](/src/assets/images/p25_image-1645452312898.png) | **Memoria RAM** 2GB de memoria RAM |
| ![Sistema operativo](/src/assets/images/p25_image-1645452455434.png) | **Sistema operativo** Linux 64bits Sistema operativo Linux recomendado: Fedora Server 40 (x86_64 systems) o Ubuntu Server 24. Puede utilizarse la instalación mínima para Monsta. |
| ![Procesador](/src/assets/images/p25_image-1645452542916.png) | **Procesador** Cores: 2 Velocidade: 1.8GHz |


:::note
Las configuraciones anteriores permiten, en general, monitorizar aproximadamente 500 dispositivos con 10 monitores cada uno o un total de 5.000 monitores.
:::

## Script de migración

Conectado como root en su servidor, descargue el script de migración como en el ejemplo a continuación:

### Fedora/Red-Hat/Ubuntu/Debian

```shell
yum install -y wget || apt-get install -y wget
wget https://www.monsta.com.br/monsta/download/migrate.sh
chmod +x migrate.sh
```

## Iniciando la transferencia

Tras descargar el script, ejecútelo con la siguiente sintaxis:

`./migrate.sh`

Antes de iniciar el proceso de migración e instalación de Monsta, el script solicitará la información de acceso SSH al servidor de origen: dirección IP/hostname, puerto de conexión y usuario con privilegios de root.

Estos datos son necesarios para establecer una conexión remota segura entre los entornos. A partir de ese acceso, el script detendrá los servicios en el servidor antiguo, transferirá la estructura completa de archivos, logs y bases de datos preservando los permisos de archivo, y registrará e iniciará los servicios de Monsta en el nuevo servidor.

:::note
El tiempo requerido para esta transferencia dependerá del tamaño de la base de datos existente, pudiendo tardar desde minutos hasta varias horas.
:::

:::danger[Importante]
Para que el script migrate se ejecute con éxito y garantice la copia y creación de todos los archivos y directorios con los permisos correctos (incluyendo archivos de sistema, logs y configuraciones sensibles), es **obligatorio** que la ejecución se realice por un usuario con privilegios de **superusuario (`root`)** en **ambos los servidores** (Origen y Destino). 

Si ocurre algún error de **timeout** durante la ejecución de `migrate.sh`, verifique que el puerto SSH en el servidor remoto esté abierto en el firewall para el acceso desde el servidor local.  

En caso de fallo, aun siguiendo las instrucciones de uso de `migrate.sh`, **envíe el archivo monsta_migration.log a nuestro soporte**.  
:::