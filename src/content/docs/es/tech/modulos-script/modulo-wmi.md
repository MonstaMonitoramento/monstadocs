---
title: "Módulo WMI"
---

El módulo **wmi** proporciona funciones para interactuar con Windows Management Instrumentation (WMI), permitiendo consultar información del sistema, hardware, software y configuraciones en máquinas Windows remotas o locales. Este módulo soporta tanto la ejecución cross-platform (usando la utilidad `wmic`) como la ejecución nativa en Windows (usando la API COM).

## Funciones Disponibles

### 1. `wmi.buildwql(instance_id, table, fields)`

Construye una consulta WQL (WMI Query Language) a partir de parámetros simplificados.

**Parámetros**:

- `instance_id` (string opcional): Identificador de instancia en el formato "Tabla|Campo|Valor"

- `table` (string opcional): Nombre de la tabla WMI (usado cuando no hay instance_id)

- `fields` (tabla): Lista de campos a seleccionar

**Retorno**:

- `string`: Consulta WQL formateada

**Excepciones**:

- Lanza error si ninguno de los parámetros `instance_id` o `table` es proporcionado

- Lanza error si `instance_id` tiene un formato inválido

**Ejemplos**:

```lua
-- Consulta simple a una tabla
local wql1 = wmi.buildwql(nil, "Win32_OperatingSystem", {"Caption", "Version", "BuildNumber"})
-- Resultado: "select Caption,Version,BuildNumber from Win32_OperatingSystem"

-- Consulta a una instancia específica
local wql2 = wmi.buildwql("Win32_Process|Name|explorer.exe", nil, {"ProcessId", "WorkingSetSize"})
-- Resultado: "select ProcessId,WorkingSetSize from Win32_Process where Name = \"explorer.exe\""

-- Consulta con múltiples campos
local wql3 = wmi.buildwql(nil, "Win32_LogicalDisk", {"DeviceID", "Size", "FreeSpace", "FileSystem"})
-- Resultado: "select DeviceID,Size,FreeSpace,FileSystem from Win32_LogicalDisk"
```

### 2. `wmi.exec(config, wql, namespace)`

Ejecuta una consulta WMI usando la utilidad `wmic`

**Parámetros**:

- `config` (tabla): Configuración de conexión que contiene:

  - `net.address` (string): Dirección IP u hostname del objetivo

  - `wmi.username` (string): Nombre de usuario para autenticación

  - `wmi.password` (string): Contraseña para autenticación

  - `wmi.timeout` (número opcional, por defecto: 10): Timeout en segundos

- `wql` (string): Consulta WQL a ejecutar

- `namespace` (string opcional): Namespace WMI (por defecto: "root\\cimv2")

**Retorno**:

- `tabela`: Array de resultados, donde cada elemento es una tabla con pares campo-valor

**Nota**: En lugar de crear manualmente una tabla de configuración, puede usar la tabla global `params` que ya contiene todos los campos necesarios (`net.address`, `wmi.username`, `wmi.password`, etc.). Esta tabla es automáticamente proporcionada por el sistema cuando el script se ejecuta en el contexto de un dispositivo gestionado.

**Ejemplo usando `params`**:

```lua
-- A tabela 'device' já contém as credenciais e endereço do dispositivo alvo
-- with_coroutine aceita a função e seus argumentos, retornando (result, err)
local results, err = with_coroutine(wmi.exec, params, wql, "root\\cimv2")
local success = not err

if not success then
    print("Erro WMI: " .. tostring(err))
end
```

**Ejemplo práctico**:

```lua
-- Consulta simplificada usando la tabla device
local wql = "select Caption,Version from Win32_OperatingSystem"
local results = wmi.exec(device, wql)

-- Para consultas locales en el propio dispositivo
if device["net.address"] == "127.0.0.1" or device["net.address"] == "localhost" then
    -- Puede usarse exec_native para mejor rendimiento
    if wmi.exec_native then
        results = wmi.exec_native(device, wql)
    end
end
```

**Excepciones**:

- Lanza error si la conexión falla

- Lanza error "Timeout" si la consulta supera el tiempo límite

- Lanza error si la utilidad `wmic` devuelve código de error

**Ejemplos**:

```lua
-- Configuração básica
local config = {
    ["net.address"] = "192.168.1.100",
    ["wmi.username"] = "Administrator",
    ["wmi.password"] = "senha123",
    ["wmi.timeout"] = 15
}

-- Consulta informações do sistema operacional usando with_coroutine
local wql = "select Caption,Version,BuildNumber,OSArchitecture from Win32_OperatingSystem"
local results, err = with_coroutine(wmi.exec, config, wql, "root\\cimv2")

if not err then
    for _, row in ipairs(results) do
        print("Sistema: " .. row.Caption)
        print("Versão: " .. row.Version)
        print("Build: " .. row.BuildNumber)
        print("Arquitetura: " .. row.OSArchitecture)
    end
else
    print("Erro na consulta WMI: " .. tostring(err))
end

-- Consulta processos em execução
local process_wql = "select Name,ProcessId,WorkingSetSize,CommandLine from Win32_Process"
local process_results = wmi.exec(config, process_wql)

-- Consulta discos lógicos
local disk_wql = [[
select DeviceID,Size,FreeSpace,FileSystem
from Win32_LogicalDisk
where DriveType = 3
]]
local disk_results = wmi.exec(config, disk_wql, nil)  -- namespace padrão
```

### 3. `wmi.exec_native(config, wql, namespace)` (Solo en el agente Windows)

Ejecuta una consulta WMI usando la API nativa de Windows (COM). Esta función está disponible solo en sistemas Windows y ofrece mejor rendimiento e integración.

**Parámetros**:

- `config` (tabla): Configuración de conexión (ignoradа en la ejecución local)

- `wql` (string): Consulta WQL a ejecutar

- `namespace` (string opcional): Namespace WMI

**Retorno**:

- `tabela`: Array de resultados, donde cada elemento es una tabla con pares campo-valor

**Excepeciones**:

- Lanza error si la API COM falla

- Lanza error si la consulta es inválida

**Ejemplos**:

```lua
-- Apenas funciona em Windows
if wmi.exec_native then
    -- Consulta local (config é ignorado)
    local config = nil  -- Deixar vazio para consultas do agente
    local wql = "select Name,Manufacturer,Model from Win32_ComputerSystem"

    -- with_coroutine aceita a função e seus argumentos, retornando (result, err)
    local results, err = with_coroutine(wmi.exec_native, config, wql)

    if not err and results and #results > 0 then
        local computer = results[1]
        print("Computador: " .. computer.Name)
        print("Fabricante: " .. computer.Manufacturer)
        print("Modelo: " .. computer.Model)
    end
end
```

## Información Adicional

### 1. **Soporte Cross-Platform**

- La función `exec` usa la utilidad `wmic` que funciona en sistemas Linux

- Permite consultar máquinas Windows remotamente

- Esta funcionalidad es heredada, pues versiones más recientes de Windows no permiten conexiones WMI remotas.

### 2. **Ejecución Nativa en Windows**

- La función `exec_native` ofrece mejor rendimiento en sistemas Windows

- No requiere autenticación para consultas locales

- Usa la API COM de Windows directamente

### 3. **Timeout Configurable**

- Timeout por defecto de 10 segundos

- Configurable vía el parámetro `wmi.timeout` en la configuración

## Buenas Prácticas

### 1. **Optimización de Consultas**

```lua
-- RUIM: Seleciona todas as colunas
local bad_wql = "select * from Win32_Process"

-- BOM: Seleciona apenas colunas necessárias
local good_wql = "select Name,ProcessId,WorkingSetSize from Win32_Process"

-- MELHOR: Adiciona filtros para reduzir resultados
local best_wql = [[
select Name,ProcessId,WorkingSetSize
from Win32_Process
where WorkingSetSize > 10485760  -- > 10MB
]]
```

### 4. `wmi.exec(config, wql, namespace, replace_backslash)`

Versión extendida de la función `exec` con soporte a timeout y opción para reemplazar barras invertidas.

#### Parámetros

- **config** (tabla): Configuración de conexión

- **wql** (string): Consulta WQL a ejecutar

- **namespace** (string, opcional): Namespace WMI (usa `wmi._namespace` o `params.wmiNamespace` si no se especifica)

- **replace_backslash** (booleano, opcional): Si `true`, reemplaza `\` por `\\` en la WQL (por defecto: `true`)

#### Retorno

- **tabela**: Resultados de la consulta WMI

#### Comportamiento

- Soporta ejecución vía probe WMI cuando `params["wmi.type"] == 0`

- Para localhost (`127.0.0.1`), usa ejecución nativa

#### Ejemplo de Uso

```lua
-- Executar com timeout configurado
-- params.wmiTimeout = 10 (10 segundos)

local config = {
    address = "192.168.1.100",
    username = "administrator",
    password = "senha123"
}

local wql = "select Name, ProcessId, WorkingSetSize from Win32_Process"
local results = wmi.exec(config, wql, "root\\cimv2")

for _, process in ipairs(results) do
    print(string.format("Processo: %s (PID: %d, Memória: %d bytes)",
                       process.Name, process.ProcessId, process.WorkingSetSize))
end
```

### 5. `wmi.query(wmiobj, ...)`

Consulta simplificada a una tabla WMI sin instancia específica.

#### Parámetros

- **wmiobj** (string): Nombre de la tabla WMI

- **...** (strings): Campos a seleccionar (puede incluir `namespace=...`)

#### Retorno

- **cualquier tipo**: Valor único si solo se selecciona un campo, tabla si se seleccionan múltiples campos

#### Comportamiento

- Construye WQL automáticamente con `wmi.buildwql`

- Almacena resultado internamente para uso con `prev` y `lapsed`

- Soporta especificación de namespace vía `namespace=` al inicio de los campos

#### Ejemplo de Uso

```lua
-- Consultar informações do sistema operacional
local os_name = wmi.query("Win32_OperatingSystem", "Caption")
print("Sistema Operacional:", os_name)

-- Consultar múltiplos campos
local disk_info = wmi.query("Win32_LogicalDisk", "DeviceID", "Size", "FreeSpace")
for _, disk in ipairs(disk_info) do
    local used_percent = 100 - (disk.FreeSpace / disk.Size * 100)
    print(string.format("Disco %s: %.1f%% usado", disk.DeviceID, used_percent))
end

-- Consultar com namespace específico
local cluster_info = wmi.query("MSCluster_Cluster", "namespace=root\\MSCluster", "Name", "State")
```

### 6. `wmi.queryinst(...)`

Consulta WMI para instancia específica definida en `params.InstanceId`.

#### Parámetros

- **...** (strings): Campos a seleccionar (puede incluir `namespace=...`)

#### Retorno

- **cualquier tipo**: Valor único si solo se selecciona un campo, tabla si se seleccionan múltiples campos

#### Comportamiento

- Usa `params.InstanceId` para construir consulta de instancia

- Lanza error si la instancia no es encontrada

- Almacena resultado en `_mem_store` para uso con `prev` y `lapsed`

#### Ejemplo de Uso

```lua
-- params.InstanceId = "Win32_Process|Name|explorer.exe"

-- Consultar informações do processo explorer.exe
local pid = wmi.queryinst("ProcessId")
local memory = wmi.queryinst("WorkingSetSize")

print(string.format("Explorer.exe - PID: %d, Memória: %d bytes", pid, memory))

-- Consultar múltiplos campos
local process_info = wmi.queryinst("ProcessId", "WorkingSetSize", "ThreadCount", "Priority")
```

### 7. `wmi.prev(wmiobj, ...)`

Obtiene el valor anterior de una consulta WMI.

#### Parámetros

- **wmiobj** (string): Nombre de la tabla WMI

- **...** (strings): Campos de la consulta original

#### Retorno

- **cualquier tipo**: Valor anterior almacenado

#### Comportamiento

- Reconstruye la WQL original

- Busca valor en `store.get("wmi.value." .. wql)`

- Retorna valor único si la consulta original devolvió un único valor

#### Ejemplo de Uso

```lua
-- Obter valor atual
local current_memory = wmi.query("Win32_OperatingSystem", "TotalVisibleMemorySize")

-- Obter valor anterior
local previous_memory = wmi.prev("Win32_OperatingSystem", "TotalVisibleMemorySize")

-- Calcular diferença
local memory_diff = current_memory - previous_memory
print("Variação de memória:", memory_diff, "bytes")
```

### 8. `wmi.previnst(...)`

Obtiene el valor anterior de una consulta WMI de instancia.

#### Parámetros

- **...** (strings): Campos de la consulta original

#### Retorno

- **cualquier tipo**: Valor anterior almacenado

#### Ejemplo de Uso

```lua
-- params.InstanceId = "Win32_Process|Name|svchost.exe"

-- Obter uso atual de CPU
local current_cpu = wmi.queryinst("PercentProcessorTime")

-- Obter uso anterior
local previous_cpu = wmi.previnst("PercentProcessorTime")

-- Calcular variação
local cpu_change = current_cpu - previous_cpu
print("Variação no uso de CPU:", cpu_change, "%")
```

### 9. `wmi.lapsed(wmiobj, ...)`

Obtiene el tiempo transcurrido desde la última consulta WMI.

#### Parámetros

- **wmiobj** (string): Nombre de la tabla WMI

- **...** (strings): Campos de la consulta original

#### Retorno

- **número**: Tiempo en segundos desde la última consulta

#### Ejemplo de Uso

```lua
-- Calcular taxa de transferência de disco
local current_reads = wmi.query("Win32_PerfRawData_PerfDisk_LogicalDisk", "DiskReadBytesPerSec")
local previous_reads = wmi.prev("Win32_PerfRawData_PerfDisk_LogicalDisk", "DiskReadBytesPerSec")
local time_elapsed = wmi.lapsed("Win32_PerfRawData_PerfDisk_LogicalDisk", "DiskReadBytesPerSec")

local read_rate = (current_reads - previous_reads) / time_elapsed
print("Taxa de leitura de disco:", read_rate, "bytes/segundo")
```

### 10. `wmi.lapsedinst(...)`

Obtiene el tiempo transcurrido desde la última consulta WMI de instancia.

#### Parámetros

- **...** (strings): Campos de la consulta original

#### Retorno

- **número**: Tiempo en segundos desde la última consulta

#### Ejemplo de Uso

```lua
-- params.InstanceId = "Win32_PerfRawData_PerfDisk_LogicalDisk|Name|C:"

-- Calcular taxa de escrita para disco C:
local current_writes = wmi.queryinst("DiskWriteBytesPerSec")
local previous_writes = wmi.previnst("DiskWriteBytesPerSec")
local time_elapsed = wmi.lapsedinst("DiskWriteBytesPerSec")

local write_rate = (current_writes - previous_writes) / time_elapsed
print("Taxa de escrita no disco C:", write_rate, "bytes/segundo")
```

### 11. `wmi.diff(typ, lhs, rhs)`

Calcula la diferencia entre dos valores WMI, manejando rollover de contadores.

#### Parámetros

- **typ** (número): Tipo del contador (32 o 64 bits)

- **lhs** (número): Valor actual

- **rhs** (número): Valor anterior

#### Retorno

- **número**: Diferencia entre los valores

#### Comportamiento

- Usa la misma implementación que `snmp.diff`

- Maneja rollover de contadores de 32 y 64 bits

- Señala `RepeatPrevValue` si la diferencia es negativa

#### Ejemplo de Uso

```lua
-- Calcular diferença para contador de 64 bits
local current_bytes = wmi.queryinst("DiskReadBytesPerSec")
local prev_bytes = wmi.previnst("DiskReadBytesPerSec")
local bytes_diff = wmi.diff(64, current_bytes, prev_bytes)

print("Bytes lidos desde última leitura:", bytes_diff)
```

## Ejemplos Completos

### Monitorización de Proceso Específico

```lua
-- Configurar instância para monitorar processo específico
-- params.InstanceId = "Win32_PerfRawData_PerfProc_Process|Name|chrome.exe"

-- Obter métricas atuais
local cpu_usage = wmi.queryinst("PercentProcessorTime")
local memory_usage = wmi.queryinst("WorkingSetPrivate")
local thread_count = wmi.queryinst("ThreadCount")

-- Calcular variações
local prev_cpu = wmi.previnst("PercentProcessorTime")
local prev_memory = wmi.previnst("WorkingSetPrivate")
local time_elapsed = wmi.lapsedinst("PercentProcessorTime")

local cpu_delta = wmi.diff(32, cpu_usage, prev_cpu)
local memory_delta = memory_usage - prev_memory

print(string.format("Chrome.exe - CPU: %d%%, Memória: %d bytes, Threads: %d",
                   cpu_delta / time_elapsed, memory_delta, thread_count))
```

### Inventario de Hardware con Caché

```lua
-- Função para obter informações de hardware com cache
local function get_hardware_info()
    local cache_key = "hardware_info_" .. params.device.address
    local cached = cache.get(cache_key)

    if cached then
        return cached
    end

    -- Coletar informações diversas
    local hardware_info = {
        os = wmi.query("Win32_OperatingSystem", "Caption", "Version", "BuildNumber"),
        cpu = wmi.query("Win32_Processor", "Name", "NumberOfCores", "MaxClockSpeed"),
        memory = wmi.query("Win32_ComputerSystem", "TotalPhysicalMemory"),
        disks = wmi.query("Win32_LogicalDisk", "DeviceID", "Size", "FreeSpace", "FileSystem")
    }

    -- Armazenar em cache por 1 hora
    cache.put(cache_key, hardware_info, 3600)

    return hardware_info
end

-- Usar informações em cache
local info = get_hardware_info()
print("Sistema:", info.os.Caption, info.os.Version)
print("Processador:", info.cpu.Name, "(" .. info.cpu.NumberOfCores .. " núcleos)")
print("Memória total:", info.memory / (1024*1024*1024), "GB")
```