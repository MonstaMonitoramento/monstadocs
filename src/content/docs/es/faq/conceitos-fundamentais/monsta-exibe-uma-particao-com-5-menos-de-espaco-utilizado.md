---
title: "¿Por qué Monsta muestra una partición con un 5% menos de espacio utilizado?"
---

Esa diferencia del 5% en el espacio en disco de una partición Linux, al ser monitorizada vía [SNMP](/es/tech/protocolos-coleta/snmp), es una característica estándar de los sistemas de archivos **Ext2, Ext3 y Ext4**. No es un error de cálculo, sino una reserva de espacio intencionada.

Esta reserva existe para garantizar que el sistema siga funcionando de forma estable, incluso cuando el disco esté casi totalmente lleno. El 5% se reserva principalmente para el usuario **`root`**, el administrador del sistema.

Los principales motivos de esta reserva son:

- **Evitar la fragmentación de archivos**: La reserva ayuda a garantizar que el sistema de archivos tenga suficiente espacio para asignar nuevos datos de forma contigua, lo que mejora el rendimiento.
- **Permitir el funcionamiento del sistema**: Si el disco se llena al 100%, el sistema operativo puede bloquearse o volverse inutilizable. Esta reserva garantiza que el `root` tenga espacio para, por ejemplo, escribir logs, mover archivos o ejecutar comandos esenciales para liberar espacio.

En resumen, la diferencia del 5% es una característica del sistema de archivos **Ext** diseñada para protección. Garantiza que el administrador siempre disponga de un margen para realizar operaciones críticas y mantener la estabilidad del servidor.