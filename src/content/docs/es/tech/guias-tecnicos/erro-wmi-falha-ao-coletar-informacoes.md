---
title: "Error WMI - Fallo al recopilar información"
---

## Problema:

Los monitores recopilan alguna información y después fallan. Los registros de error muestran el siguiente mensaje: "**HRESULT Call failed with: 0x80041017**".

## Solución: 

El error **0x80041017** en Windows está relacionado con **WMI**(*Windows Management Instrumentation*) y significa **WBEM\_E\_INVALID\_QUERY**, es decir, se realizó una **consulta inválida** a WMI. Este error suele aparecer cuando scripts o herramientas intentan acceder a datos de rendimiento o información del sistema, pero la consulta falla por algún motivo.

Para resolver este problema puedes recompilar todos los contadores de rendimiento, incluidos los de terceros. Para hacerlo, escribe los comandos siguientes en un símbolo del sistema con privilegios de Administrador. Pulsa **ENTER** después de cada comando.

- Reconstruir los contadores:

```powershell
cd c:\windows\system32
lodctr /R
cd c:\windows\sysWOW64
lodctr /R
```

- Sincronizar con el WMI:

```powershell
WINMGMT.EXE /RESYNCPERF
```

- Reiniciar servicios de Registro y Alto Rendimiento:

```powershell
net stop pla & net start pla
net stop winmgmt & net start winmgmt
```