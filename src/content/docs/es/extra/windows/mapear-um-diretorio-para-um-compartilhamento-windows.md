---
title: "Mapear un directorio a un recurso compartido de Windows"
---

Tutorial para montar una unidad compartida en un sistema Windows en un servidor Linux CentOS.

## Instalando el cliente Samba

Conectado como root, en la terminal de Linux escriba:

```shell
yum install samba-client cifs-utils
```

## Creando el mapeo

Conectado como root, en la terminal de Linux ejecute los siguientes comandos reemplazando los elementos abajo por sus configuraciones:  

:::note
Windows utiliza el protocolo **SMB** (*Server Message Block*) para el uso compartido de archivos en red. Dependiendo de la versión utilizada, sustituya el parámetro `vers=2.0` por la versión adecuada, por ejemplo: `vers=1.0`
:::


:::danger[Precaución]
La inserción de la línea en el archivo /etc/fstab se realiza con `>>`. No elimine ni quite configuraciones existentes en su archivo /etc/fstab sin conocimiento, bajo riesgo de que el servidor Linux no inicie.
:::



> **usuario** = Usuario de Windows  
> **contraseña** = Contraseña de Windows  
> **192.168.0.48** = IP u host de Windows  
> **unidade** = Nombre del recurso compartido en Windows  
> **media** = Directorio en Linux donde se montará el recurso compartido

```shell
echo username=usuário > /root/.credencial
echo password=senha >> /root/.credencial
echo //192.168.0.48/unidade /media cifs vers=2.0,credentials=/root/.credencial 0 0 >> /etc/fstab
```

Los comandos anteriores crearán el archivo `/root/.credencial` que contendrá, de forma segura, los datos del usuario para el recurso compartido en Windows y añadirán una línea de configuración en el archivo `/etc/fstab`, haciendo que este recurso compartido se monte siempre cuando el servidor Linux se reinicie.

Para montar el recurso compartido, en la línea de comandos escriba:

```shell
mount /media 
```