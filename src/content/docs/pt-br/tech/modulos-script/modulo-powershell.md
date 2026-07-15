---
title: Módulo Powershell
---
O módulo PowerShell permite executar comandos e scripts do PowerShell de forma segura e automatizada nos equipamentos monitorados, possibilitando a coleta de informações, a execução de tarefas administrativas e a validação de configurações do sistema. Com ele, é possível criar verificações personalizadas, automatizar rotinas de manutenção e integrar o monitoramento a recursos nativos do Windows, ampliando a capacidade de diagnóstico e gerenciamento do ambiente.

## 1.  `powershell.exec(string)`

Executa um ou mais comandos PowerShell exclusivamente em ambientes Windows.

**Parametros**:

(string): Um ou mais comandos PowerShell.

**Retorno**:

(string): A saída padrão (`stdout`) do comando executado

**Exemplo de Uso**:

```lua
local script = [[
# Lista todas as impressoras instaladas com detalhes básicos
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
