---
title: Módulo PowerShell
---
El módulo PowerShell permite ejecutar comandos y scripts de PowerShell de forma segura y automatizada en los equipos monitorizados, posibilitando la recopilación de información, la ejecución de tareas administrativas y la validación de configuraciones del sistema. Con él, es posible crear comprobaciones personalizadas, automatizar rutinas de mantenimiento e integrar la monitorización con recursos nativos de Windows, ampliando la capacidad de diagnóstico y gestión del entorno.

## 1.  `powershell.exec(string)`

Ejecuta uno o más comandos PowerShell exclusivamente en entornos Windows.

**Parámetros**:

(string): Uno o más comandos de PowerShell.

**Retorno**:

(string): La salida estándar (`stdout`) del comando ejecutado

**Ejemplo de Uso**:

```lua
local script = [[
# Lista todas las impresoras instaladas con detalles básicos
try {
 Get-Printer | Select-Object Name, PrinterStatus, Type, ShareName | Format-Table -AutoSize
}
catch {
 Write-Host "Erro ao listar impressoras: $_" -ForegroundColor Red
}
]]

local ret = powershell.exec(script)
print(ret)
```