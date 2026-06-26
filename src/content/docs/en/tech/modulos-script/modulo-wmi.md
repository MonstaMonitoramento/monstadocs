---
title: "WMI Module"
---

The **wmi** module provides functions to interact with Windows Management Instrumentation (WMI), allowing queries for system, hardware, software and configuration information on remote or local Windows machines. This module supports both cross-platform execution (using the `wmic` utility) and native execution on Windows (using the COM API).

## Available Functions

### 1. `wmi.buildwql(instance_id, table, fields)`

Builds a WQL (WMI Query Language) query from simplified parameters.

**Parameters**:

- `instance_id` (optional string): Instance identifier in the format "Table|Field|Value"

- `table` (optional string): Name of the WMI table (used when instance_id is not provided)

- `fields` (table): List of fields to select

**Return**:

- `string`: Formatted WQL query

**Exceptions**:

- Throws error if neither `instance_id` nor `table` is provided

- Throws error if `instance_id` is in an invalid format

**Examples**:

```lua
-- Simple query to a table
local wql1 = wmi.buildwql(nil, "Win32_OperatingSystem", {"Caption", "Version", "BuildNumber"})
-- Resultado: "select Caption,Version,BuildNumber from Win32_OperatingSystem"

-- Query to a specific instance
local wql2 = wmi.buildwql("Win32_Process|Name|explorer.exe", nil, {"ProcessId", "WorkingSetSize"})
-- Resultado: "select ProcessId,WorkingSetSize from Win32_Process where Name = \"explorer.exe\""

-- Query with multiple fields
local wql3 = wmi.buildwql(nil, "Win32_LogicalDisk", {"DeviceID", "Size", "FreeSpace", "FileSystem"})
-- Resultado: "select DeviceID,Size,FreeSpace,FileSystem from Win32_LogicalDisk"
```

### 2. `wmi.exec(config, wql, namespace)`

Executes a WMI query using the `wmic` utility.

**Parameters**:

- `config` (table): Connection configuration containing:

    - `net.address` (string): Target IP address or hostname

    - `wmi.username` (string): Username for authentication

    - `wmi.password` (string): Password for authentication

    - `wmi.timeout` (optional number, default: 10): Timeout in seconds

- `wql` (string): WQL query to execute

- `namespace` (optional string): WMI namespace (default: "root\\cimv2")

**Return**:

- `table`: Array of results, where each element is a table of field-value pairs

**Note**: Instead of creating a configuration table manually, you can use the global `params` table which already contains all required fields (`net.address`, `wmi.username`, `wmi.password`, etc.). This table is automatically provided by the system when the script runs in the context of a managed device.

**Example using `params`**:

```lua
-- The 'device' table already contains the target device credentials and address
local success, results = pcall(function()
    return wmi.exec(params, wql, "root\\cimv2")
end)
```

**Practical example**:

```lua
-- Simplified query using the device table
local wql = "select Caption,Version from Win32_OperatingSystem"
local results = wmi.exec(device, wql)

-- For local queries on the device itself
if device["net.address"] == "127.0.0.1" or device["net.address"] == "localhost" then
    -- You can use exec_native for better performance
    if wmi.exec_native then
        results = wmi.exec_native(device, wql)
    end
end
```

**Exceptions**:

- Throws error if the connection fails

- Throws error "Timeout" if the query exceeds the timeout

- Throws error if the `wmic` utility returns a non-zero exit code

**Examples**:

```lua
-- Basic configuration
local config = {
    ["net.address"] = "192.168.1.100",
    ["wmi.username"] = "Administrator",
    ["wmi.password"] = "senha123",
    ["wmi.timeout"] = 15
}

-- Query operating system information
local wql = "select Caption,Version,BuildNumber,OSArchitecture from Win32_OperatingSystem"
local success, results = pcall(function()
    return wmi.exec(config, wql, "root\\cimv2")
end)

if success then
    for _, row in ipairs(results) do
        print("Sistema: " .. row.Caption)
        print("Versão: " .. row.Version)
        print("Build: " .. row.BuildNumber)
        print("Arquitetura: " .. row.OSArchitecture)
    end
else
    print("Erro na consulta WMI: " .. results)
end

-- Query running processes
local process_wql = "select Name,ProcessId,WorkingSetSize,CommandLine from Win32_Process"
local process_results = wmi.exec(config, process_wql)

-- Query logical disks
local disk_wql = [[
select DeviceID,Size,FreeSpace,FileSystem
from Win32_LogicalDisk
where DriveType = 3
]]
local disk_results = wmi.exec(config, disk_wql, nil)  -- default namespace
```

### 3. `wmi.exec_native(config, wql, namespace)` (Windows agent only)

Executes a WMI query using the native Windows API (COM). This function is available only on Windows systems and provides better performance and integration.

**Parameters**:

- `config` (table): Connection configuration (ignored for local execution)

- `wql` (string): WQL query to execute

- `namespace` (optional string): WMI namespace

**Return**:

- `table`: Array of results, where each element is a table of field-value pairs

**Exceptions**:

- Throws error if the COM API fails

- Throws error if the query is invalid

**Examples**:

```lua
-- Only works on Windows
if wmi.exec_native then
    -- Local query (config is ignored)
    local config = nil  -- Leave empty for agent queries
    local wql = "select Name,Manufacturer,Model from Win32_ComputerSystem"

    local success, results = pcall(function()
        return wmi.exec_native(config, wql)
    end)

    if success and #results > 0 then
        local computer = results[1]
        print("Computador: " .. computer.Name)
        print("Fabricante: " .. computer.Manufacturer)
        print("Modelo: " .. computer.Model)
    end
end
```

## Additional Information

### 1. Cross-Platform Support

- The `exec` function uses the `wmic` utility which works on Linux systems

- Allows querying Windows machines remotely

- This functionality is legacy, as newer Windows versions do not allow remote WMI connections.

### 2. Native Execution on Windows

- The `exec_native` function offers better performance on Windows systems

- Does not require authentication for local queries

- Uses the Windows COM API directly

### 3. Configurable Timeout

- Default timeout of 10 seconds

- Configurable via the `wmi.timeout` parameter in the configuration

## Best Practices

### 1. Query Optimization

```lua
-- BAD: Selects all columns
local bad_wql = "select * from Win32_Process"

-- GOOD: Selects only necessary columns
local good_wql = "select Name,ProcessId,WorkingSetSize from Win32_Process"

-- BEST: Adds filters to reduce results
local best_wql = [[
select Name,ProcessId,WorkingSetSize
from Win32_Process
where WorkingSetSize > 10485760  -- > 10MB
]]
```

### 4. `wmi.exec(config, wql, namespace, replace_backslash)`

Extended version of the `exec` function with timeout support and an option to replace backslashes.

#### Parameters:

- **config** (table): Connection configuration

- **wql** (string): WQL query to execute

- **namespace** (string, optional): WMI namespace (uses `wmi._namespace` or `params.wmiNamespace` if not specified)

- **replace_backslash** (boolean, optional): If `true`, replaces `\` with `\\` in the WQL (default: `true`)

#### Return:

- **table**: WMI query results

#### Behavior:

- Supports execution via WMI probe when `params["wmi.type"] == 0`

- For localhost (`127.0.0.1`), uses native execution

#### Usage Example:

```lua
-- Execute with configured timeout
-- params.wmiTimeout = 10 (10 seconds)

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

Simplified query to a WMI table without a specific instance.

#### Parameters:

- **wmiobj** (string): Name of the WMI table

- **...** (strings): Fields to select (can include `namespace=...`)

#### Return:

- **any**: Single value if only one field is selected, table if multiple fields

#### Behavior:

- Automatically builds WQL using `wmi.buildwql`

- Stores result internally for use with `prev` and `lapsed`

- Supports specifying namespace via `namespace=` at the start of the fields

#### Usage Example:

```lua
-- Query operating system information
local os_name = wmi.query("Win32_OperatingSystem", "Caption")
print("Sistema Operacional:", os_name)

-- Query multiple fields
local disk_info = wmi.query("Win32_LogicalDisk", "DeviceID", "Size", "FreeSpace")
for _, disk in ipairs(disk_info) do
    local used_percent = 100 - (disk.FreeSpace / disk.Size * 100)
    print(string.format("Disco %s: %.1f%% usado", disk.DeviceID, used_percent))
end

-- Query with a specific namespace
local cluster_info = wmi.query("MSCluster_Cluster", "namespace=root\\MSCluster", "Name", "State")
```

### 6. `wmi.queryinst(...)`

WMI query for a specific instance defined in `params.InstanceId`.

#### Parameters:

- **...** (strings): Fields to select (can include `namespace=...`)

#### Return:

- **any**: Single value if only one field is selected, table if multiple fields

#### Behavior:

- Uses `params.InstanceId` to build the instance query

- Throws error if the instance is not found

- Stores result in `_mem_store` for use with `prev` and `lapsed`

#### Usage Example:

```lua
-- params.InstanceId = "Win32_Process|Name|explorer.exe"

-- Query information for the explorer.exe process
local pid = wmi.queryinst("ProcessId")
local memory = wmi.queryinst("WorkingSetSize")

print(string.format("Explorer.exe - PID: %d, Memória: %d bytes", pid, memory))

-- Query multiple fields
local process_info = wmi.queryinst("ProcessId", "WorkingSetSize", "ThreadCount", "Priority")
```

### 7. `wmi.prev(wmiobj, ...)`

Gets the previous value of a WMI query.

#### Parameters:

- **wmiobj** (string): Name of the WMI table

- **...** (strings): Fields of the original query

#### Return:

- **any**: Previously stored value

#### Behavior:

- Reconstructs the original WQL

- Looks up the value in `store.get("wmi.value." .. wql)`

- Returns a single value if the original query returned a single value

#### Usage Example:

```lua
-- Get current value
local current_memory = wmi.query("Win32_OperatingSystem", "TotalVisibleMemorySize")

-- Get previous value
local previous_memory = wmi.prev("Win32_OperatingSystem", "TotalVisibleMemorySize")

-- Calculate difference
local memory_diff = current_memory - previous_memory
print("Variação de memória:", memory_diff, "bytes")
```

### 8. `wmi.previnst(...)`

Gets the previous value of an instance WMI query.

#### Parameters:

- **...** (strings): Fields of the original query

#### Return:

- **any**: Previously stored value

#### Usage Example:

```lua
-- params.InstanceId = "Win32_Process|Name|svchost.exe"

-- Get current CPU usage
local current_cpu = wmi.queryinst("PercentProcessorTime")

-- Get previous usage
local previous_cpu = wmi.previnst("PercentProcessorTime")

-- Calculate change
local cpu_change = current_cpu - previous_cpu
print("Variação no uso de CPU:", cpu_change, "%")
```

### 9. `wmi.lapsed(wmiobj, ...)`

Gets the elapsed time since the last WMI query.

#### Parameters:

- **wmiobj** (string): Name of the WMI table

- **...** (strings): Fields of the original query

#### Return:

- **number**: Time in seconds since the last query

#### Usage Example:

```lua
-- Calculate disk throughput
local current_reads = wmi.query("Win32_PerfRawData_PerfDisk_LogicalDisk", "DiskReadBytesPerSec")
local previous_reads = wmi.prev("Win32_PerfRawData_PerfDisk_LogicalDisk", "DiskReadBytesPerSec")
local time_elapsed = wmi.lapsed("Win32_PerfRawData_PerfDisk_LogicalDisk", "DiskReadBytesPerSec")

local read_rate = (current_reads - previous_reads) / time_elapsed
print("Taxa de leitura de disco:", read_rate, "bytes/segundo")
```

### 10. `wmi.lapsedinst(...)`

Gets the elapsed time since the last instance WMI query.

#### Parameters:

- **...** (strings): Fields of the original query

#### Return:

- **number**: Time in seconds since the last query

#### Usage Example:

```lua
-- params.InstanceId = "Win32_PerfRawData_PerfDisk_LogicalDisk|Name|C:"

-- Calculate write rate for disk C:
local current_writes = wmi.queryinst("DiskWriteBytesPerSec")
local previous_writes = wmi.previnst("DiskWriteBytesPerSec")
local time_elapsed = wmi.lapsedinst("DiskWriteBytesPerSec")

local write_rate = (current_writes - previous_writes) / time_elapsed
print("Taxa de escrita no disco C:", write_rate, "bytes/segundo")
```

### 11. `wmi.diff(typ, lhs, rhs)`

Calculates the difference between two WMI values, handling counter rollover.

#### Parameters:

- **typ** (number): Counter type (32 or 64 bits)

- **lhs** (number): Current value

- **rhs** (number): Previous value

#### Return:

- **number**: Difference between the values

#### Behavior:

- Uses the same implementation as `snmp.diff`

- Handles rollover for 32-bit and 64-bit counters

- Flags `RepeatPrevValue` if the difference is negative

#### Usage Example:

```lua
-- Calculate difference for a 64-bit counter
local current_bytes = wmi.queryinst("DiskReadBytesPerSec")
local prev_bytes = wmi.previnst("DiskReadBytesPerSec")
local bytes_diff = wmi.diff(64, current_bytes, prev_bytes)

print("Bytes lidos desde última leitura:", bytes_diff)
```

## Complete Examples

### Monitoring a Specific Process:

```lua
-- Configure instance to monitor a specific process
-- params.InstanceId = "Win32_PerfRawData_PerfProc_Process|Name|chrome.exe"

-- Get current metrics
local cpu_usage = wmi.queryinst("PercentProcessorTime")
local memory_usage = wmi.queryinst("WorkingSetPrivate")
local thread_count = wmi.queryinst("ThreadCount")

-- Calculate variations
local prev_cpu = wmi.previnst("PercentProcessorTime")
local prev_memory = wmi.previnst("WorkingSetPrivate")
local time_elapsed = wmi.lapsedinst("PercentProcessorTime")

local cpu_delta = wmi.diff(32, cpu_usage, prev_cpu)
local memory_delta = memory_usage - prev_memory

print(string.format("Chrome.exe - CPU: %d%%, Memória: %d bytes, Threads: %d",
                   cpu_delta / time_elapsed, memory_delta, thread_count))
```

### Hardware Inventory with Cache:

```lua
-- Function to get hardware information with cache
local function get_hardware_info()
    local cache_key = "hardware_info_" .. params.device.address
    local cached = cache.get(cache_key)

    if cached then
        return cached
    end

    -- Collect various information
    local hardware_info = {
        os = wmi.query("Win32_OperatingSystem", "Caption", "Version", "BuildNumber"),
        cpu = wmi.query("Win32_Processor", "Name", "NumberOfCores", "MaxClockSpeed"),
        memory = wmi.query("Win32_ComputerSystem", "TotalPhysicalMemory"),
        disks = wmi.query("Win32_LogicalDisk", "DeviceID", "Size", "FreeSpace", "FileSystem")
    }

    -- Store in cache for 1 hour
    cache.put(cache_key, hardware_info, 3600)

    return hardware_info
end

-- Use cached information
local info = get_hardware_info()
print("Sistema:", info.os.Caption, info.os.Version)
print("Processador:", info.cpu.Name, "(" .. info.cpu.NumberOfCores .. " núcleos)")
print("Memória total:", info.memory / (1024*1024*1024), "GB")
```