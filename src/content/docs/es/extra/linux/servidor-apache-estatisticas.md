---
title: "Estadísticas para el Servidor Apache (Linux)"
---

El tutorial tiene como objetivo activar una configuración básica del servidor Apache HTTP para monitorizar. Dependiendo de la configuración de Apache o del sistema operativo en el que esté instalado, la información siguiente puede no funcionar.

## Habilitando el módulo mod\_stats

Las estadísticas de uso del servidor Apache HTTP están disponibles a través del módulo mod\_stats, que en general ya viene en la mayoría de las instalaciones pero no está habilitado.  
  
Conectado como root, edite el archivo de configuración del Apache. Para saber la ubicación de este archivo, escriba el siguiente comando:

```shell
httpd -V | grep 'SERVER_CONFIG_FILE'
```

Se mostrará el siguiente resultado:

`-D SERVER_CONFIG_FILE="/etc/httpd/conf/httpd.conf"`

Con base en esta información, el archivo de configuración del apache se encuentra en `/etc/httpd/conf/httpd.conf`. Añada las siguientes líneas al archivo (como sugerencia, puede añadirlas al final del archivo):

```vim
<Location /server-status>  
SetHandler server-status  
Order Deny,Allow  
Deny from all  
</Location>  
ExtendedStatus On
```

Las configuraciones anteriores permiten que cualquier host consulte las estadísticas en su servidor Apache. Para restringir las consultas a la IP de Monsta, añada la siguiente línea antes de `</Location>`

`Allow from IP_do_Monsta`

Reinicie Apache con el comando:

```shell
httpd -k restart
```

Con estas configuraciones, las estadísticas de Apache ya pueden ser monitorizadas mediante la plantilla “Apache – Servidor HTTP” de Monsta.