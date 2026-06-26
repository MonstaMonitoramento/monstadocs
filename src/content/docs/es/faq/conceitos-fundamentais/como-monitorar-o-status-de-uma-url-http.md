---
title: "¿Cómo monitorizar el estado de una URL HTTP?"
---

Este artículo explica el procedimiento correcto para supervisar el estado de una URL específica (como `http://192.168.0.200:8080/sistema`) en Monsta, comprobando si responde con un estado HTTP/200 (OK).

## ❌ Error común

Es un error común intentar añadir la ruta completa de la URL (p. ej.: `http://192.168.0.200:8080/sistema`) en el campo Dirección del dispositivo de la pantalla del dispositivo.

![image-1764180428270.png](../../../../../assets/images/p129_image-1764180428270.png)

El campo Dirección del dispositivo acepta solo la IP o el *hostname* (p. ej.: `192.168.10.16`, `www.foo.com`). Se utiliza para identificar el dispositivo y no comprueba rutas de URL ni puertos.

## ✅ Procedimiento correcto: Utilizando el Monitor de URL

Para supervisar si una ruta específica de una URL responde correctamente, debe añadir un monitor dedicado a ese dispositivo.

### 1. Añadir la plantilla de Servicio HTTP

- Edite el dispositivo.
- Añada la plantilla "Servicios - HTTP" al dispositivo.  
    ![image-1764180633849.png](../../../../../assets/images/p129_image-1764180633849.png)

### 2. Añadir y configurar el monitor "Verifica URL"

La plantilla "Servicios - HTTP" contiene varios monitores, incluido Verifica URL, que se utilizará.

- Haga clic en la opción para añadir un nuevo monitor  
    ![image-1764180781279.png](../../../../../assets/images/p129_image-1764180781279.png)
- Seleccione el monitor "Verifica URL" y haga clic en el icono del lápiz para editar  
    ![image-1764180854853.png](../../../../../assets/images/p129_image-1764180854853.png)
- Haga clic en Avanzado y añada la URL que desea supervisar (p. ej.: `http://192.168.0.200:8080/sistema`) ![image-1764180956419.png](../../../../../assets/images/p129_image-1764180956419.png)
- Guarde los cambios y cree el monitor



:::caution[Atención]
El monitor Verifica URL (de la plantilla "Servicios - HTTP") solo funciona para URLs que usan el protocolo HTTP. Si su URL es HTTPS (cifrada), póngase en contacto con el soporte para comprobar si existe algún monitor que verifique URLs HTTPS.
:::