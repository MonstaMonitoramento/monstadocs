---
title: "¿Cómo actualizar el Monsta de la v4 a la v5?"
---

A **versión 5 (v5)** de Monsta representa una reformulación completa del núcleo del sistema (*core*), ofreciendo nuevas funcionalidades y mayor eficiencia en comparación con la versión anterior (v4).

## ¿Por qué actualizar?

El soporte para la v4 fue **descontinuado** con el lanzamiento de la v5. Mantener Monsta desactualizado puede causar problemas críticos de compatibilidad y operación:

- **Validación de la licencia**: La v4 no es compatible con el nuevo modelo de suscripciones. Para aplicar o renovar la licencia, es obligatorio tener Monsta en la v5.
- **Importación de plantillas**: Las nuevas plantillas solicitadas al soporte siempre se proporcionan en la **última versión oficial**. Las plantillas de la v5 **no pueden importarse** en la v4, debido a la incompatibilidad de archivos.

Es fundamental actualizar su Monsta a la v5 para garantizar la continuidad y la validez de su monitorización.

Si su Monsta no muestra la nueva actualización en **Configuração &gt; Atualização**, puede haber ocurrido un error que impide la detección. Siga los pasos a continuación para intentar resolver el problema.

## (Opcional) Copia de seguridad completa

El proceso de actualización es **seguro** y no afecta la base de datos del historial de monitorización (gráficos). Sin embargo, para la máxima garantía de preservación de datos, recomendamos una **copia de seguridad completa**. La copia de seguridad en la nube guarda solo las configuraciones de Monsta.

## Opciones de copia de seguridad completa

1. **Máquina Virtual (VM)**: Si Monsta está instalado en Linux dentro de una VM, el método más sencillo es crear una copia (clone) completa de la máquina virtual.
2. **Servidor físico o copia de seguridad manual**: Si no es posible clonar la VM o si la instalación está en un servidor físico, siga estos pasos: 
    1. Verifique la versión de su Monsta en **Configuração &gt; Sobre o Monsta**
    2. Detenga Monsta:   
        **\#v4.1.18 o inferior**  
        `service monsta stop`  
        **\#4.1.19**  
        `systemctl stop monsta-com.*`
    3. Con Monsta detenido, copie las carpetas: `/var/monsta` y `/opt/monsta`

## Verificando los logs

Un problema conocido que puede bloquear la actualización es una falla en la rotación de logs de Linux, resultando en una acumulación excesiva de archivos de log del `monstadb` que sobrecargan el servidor.

1. Acceda al directorio de logs de Monsta:  
    `cd /var/log/monsta`
2. Verifique la cantidad de logs de `monstadb`:  
    \- Ejecute el comando para contar los archivos de log de monstadb. Si hay **cientos/miles** de archivos, es necesaria la corrección. Nota: También puede utilizar el comando `ls -la` para ver los archivos del directorio.  
    `ls -la monstadb.log* | wc -l`
3. Detenga el servicio de Monsta (use el comando adecuado según la versión, como se describe en el punto 2.2 de la sección de copia de seguridad completa.)
4. Elimine los archivos `monstadb.log`:  
    `rm -f monstadb.log.*`  
    `rm -f monstadb.log-*`  
    Nota: si ocurre el error "lista de argumentos demasiado larga" en el comando `rm -f monstadb.log.*`, use el siguiente comando:  
    `printf '%s\0' monstadb.log.* | xargs -0 rm -v`
5. Utilice `ls -la` para verificar si los archivos fueron eliminados
6. Inicie nuevamente Monsta  
    **\#v4.1.18 o inferior**  
    `service monsta start`
    
    **\#V4.1.19**  
    `systemctl start monsta-com.nginx`  
    `systemctl start monsta-com.monstadb`  
    `systemctl start monsta-com.monstad`  
    `systemctl start monsta-com.moncored`  
    `systemctl start monsta-com.monagentd`  
    `systemctl start monsta-com.monstaupd`

## Actualizando

Después de iniciar los servicios, acceda a la interfaz web de Monsta y verifique si la actualización está disponible. Dependiendo de su versión actual (p. ej.: 4.1.16 o 4.1.18), Monsta puede primero actualizar a la 4.1.19 (lo que provocará un reinicio) y, a continuación, permitir la actualización final a la v5.

Siga el progreso en tiempo real por el log:

`tail -f /var/log/monstaupd.log`

(use `Ctrl + C` para detener el comando `tail`)

:::tip
Durante la actualización, la pantalla de la interfaz web puede **no actualizarse automáticamente**. Tras unos minutos, intente acceder de nuevo a la dirección de su Monsta para ver la pantalla de inicio de sesión.
:::

## No hay problemas en los logs y aun así no aparece la actualización

Si la corrección de los logs no resuelve y la actualización a la v5 no aparece, por favor, contacte con el **soporte** técnico. Nuestros especialistas podrán analizar la causa raíz. **Se solicitará acceso a la interfaz web y al Linux de su Monsta** para que el equipo pueda diagnosticar y resolver el problema directamente.