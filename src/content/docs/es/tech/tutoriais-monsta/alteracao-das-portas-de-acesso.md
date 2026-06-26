---
title: "Cambio de Puertos de Acceso"
---

Esta guía describe el procedimiento para cambiar los puertos de escucha de la interfaz web de **Monsta**. Por defecto, el sistema utiliza puertos específicos que se pueden personalizar mediante la línea de comandos en el servidor Linux.

## Requisitos previos

- Acceso SSH al servidor donde está instalado Monsta.
- Privilegios de superusuario (`root` o `sudo`).
- Asegurarse de que los nuevos puertos elegidos no estén siendo utilizados por otros servicios (p. ej.: Apache, Nginx, Docker).

## Procedimiento paso a paso

1. **Acceda al Terminal**: Abra la consola de su servidor.
2. **Ejecute la utilidad de configuración**: Utilice el binario `monkerneld` con el parámetro `port` para definir el nuevo puerto HTTP y el puerto SSL (HTTPS).
    
```shell
/opt/monsta/bin/monkerneld port --port <porta http> 8090 --sslport <porta https>
```
    
**Ejemplo**:
```shell
/opt/monsta/bin/monkerneld port --port 8090 --sslport 8443  
```      

**Parámetros del Comando**:
- `--port`: Define el puerto para conexiones no cifradas (HTTP).
- `--sslport`: Define el puerto para conexiones seguras (HTTPS).

:::caution[Importante: Configuración de *Firewall*]
Tras el cambio, recuerde abrir los nuevos puertos en el *firewall* de Linux (UFW o Firewalld) y, si procede, en las reglas de seguridad de su infraestructura de red/nube.
:::