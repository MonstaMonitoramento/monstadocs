---
title: PowerShell Module
---
The PowerShell module allows executing PowerShell commands and scripts securely and automatically on monitored devices, enabling information collection, performing administrative tasks, and validating system configurations. With it, you can create custom checks, automate maintenance routines, and integrate monitoring with native Windows resources, expanding the environment's diagnostic and management capabilities.

## 1.  `powershell.exec(string)`

Executes one or more PowerShell commands exclusively in Windows environments.

**Parameters**:

(string): One or more PowerShell commands.

**Return**:

(string): The standard output (`stdout`) of the executed command

**Usage Example**:

```lua
local script = [[
# Lists all installed printers with basic details
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