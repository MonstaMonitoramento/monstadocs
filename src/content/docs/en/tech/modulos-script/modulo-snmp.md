---
title: "SNMP Module"
---

The **snmp** module provides a complete interface for monitoring and managing network devices via the SNMP (Simple Network Management Protocol). This module is useful for collecting metrics from routers, switches, servers, printers, and any device that supports SNMP.

- Support for SNMP v1, v2c and v3

- GET, GET BULK and WALK operations

- SNMP v3 authentication and encryption

- Flexible configuration for timeout and retries

- Safe returns with error handling

**Supported protocols**:

- **SNMP v1**: Basic protocol with public/private community

- **SNMP v2c**: Performance improvements with BULK operations

- **SNMP v3**: Advanced security with authentication and encryption

## SNMP Configuration

All SNMP functions require a configuration object that defines the connection parameters. The configuration is a Lua table with the following fields:

### Basic Configuration Fields:

| Campo                    | Tipo     | Padrão          | Descrição                              |
| --- | --- | :---: | --- |
| `address`                | string   | **obrigatório** | IP address or hostname of the device   |
| `snmpVersion`            | número   | 1               | SNMP version (1=v1, 2=v2c, 3=v3)       |
| `snmpPort`               | número   | 161             | SNMP port                              |
| `snmpCommunity`          | string   | nil             | SNMP community (v1/v2c)                |
| `snmpTimeout`            | número   | 5               | Timeout in seconds                     |
| `snmpRetryCount`         | número   | 3               | Number of retries                      |
| `snmpMaxBulkItems`       | número   | nil             | Maximum items per BULK operation       |
| `snmpExponentialBackoff` | booleano | false           | Enable exponential backoff             |

### Fields for SNMP v3:

| Campo               | Tipo   | Descrição                                                    |
| --- | --- | --- |
| `snmpSecurityLevel` | string | Security level: "NoAuthNoPriv", "AuthNoPriv", "AuthPriv"     |
| `snmpAuthProtocol`  | string | Authentication protocol: "MD5", "SHA1"                      |
| `snmpAuthUser`      | string | Authentication user                                         |
| `snmpAuthPassword`  | string | Authentication password                                     |
| `snmpPrivProtocol`  | string | Privacy protocol: "DES", "AES"                              |
| `snmpPrivPassword`  | string | Privacy password                                            |

### Configuration via `params` Table:

The Lua environment includes a predefined table called `params` that contains the details of the current device. This table can be used directly as SNMP configuration, as it already contains the necessary fields in the expected format.

**Direct usage example**:

```lua
-- Use the device table directly as configuration
local sys_descr = snmp.getex(device, "1.3.6.1.2.1.1.1.0")
print("Descrição do dispositivo:", sys_descr)

-- Version that does not raise an error
local valor, erro = snmp.get_safe(device, "1.3.6.1.2.1.1.3.0")
if not erro then
    print("Uptime do dispositivo:", valor)
end
```

**Combining with additional settings**:

```lua
-- Create configuration based on device with adjustments
local config = {
    address = device.address,
    snmpVersion = device.snmpVersion,
    snmpCommunity = device.snmpCommunity,
    snmpTimeout = device.snmpTimeout or 5,  -- Use default if not defined
    snmpRetryCount = 2,  -- Override default value
    snmpMaxBulkItems = 50  -- Add extra configuration
}

-- Use for BULK operation
local oids = {"1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.3.0"}
local resultados = snmp.get_bulk(config, oids)
```

### Configuration Examples:

```lua
-- Basic SNMP v2c configuration
local config_v2c = {
    address = "192.168.1.1",
    snmpVersion = 2,
    snmpCommunity = "public",
    snmpTimeout = 3,
    snmpRetryCount = 2
}

-- SNMP v3 configuration with authentication and encryption
local config_v3 = {
    address = "10.0.0.254",
    snmpVersion = 3,
    snmpSecurityLevel = "AuthPriv",
    snmpAuthProtocol = "SHA1",
    snmpAuthUser = "monitor",
    snmpAuthPassword = "senha123",
    snmpPrivProtocol = "AES",
    snmpPrivPassword = "chave456",
    snmpTimeout = 5
}

-- Configuration for device with non-standard port
local config_custom_port = {
    address = "switch.piso1.local",
    snmpVersion = 2,
    snmpCommunity = "internal",
    snmpPort = 8161,  -- Custom port
    snmpTimeout = 10  -- Larger timeout for slow network
}
```

## Available Functions

### 1. `snmp.getex(config, oid)`

Performs an SNMP GET query for a specific OID.

#### Parameters:

- **config** (table): SNMP configuration (see section above)

- **oid** (string): OID to query (numeric or named format)

#### Return:

- **value**: Value returned by the SNMP device (number, string, etc.)

#### Errors:

- Raises an error if the OID does not exist or there is a communication failure

#### Example Usage:

```lua
-- Query sysDescr (system description)
local config = {
    address = "192.168.1.1",
    snmpVersion = 2,
    snmpCommunity = "public"
}

local sys_descr = snmp.getex(config, "1.3.6.1.2.1.1.1.0")
-- or using named OID
local sys_descr = snmp.getex(config, ".1.3.6.1.2.1.1.1.0")

print("Descrição do sistema:", sys_descr)
-- Example output: "Cisco IOS Software, C3750 Software (C3750-IPSERVICESK9-M), Version 12.2(55)SE10, RELEASE SOFTWARE (fc2)"

-- Query system uptime
local sys_uptime = snmp.getex(config, "1.3.6.1.2.1.1.3.0")
print("Uptime:", sys_uptime, "centésimos de segundo")

-- Query host name
local sys_name = snmp.getex(config, "1.3.6.1.2.1.1.5.0")
print("Nome do host:", sys_name)

-- Query location
local sys_location = snmp.getex(config, "1.3.6.1.2.1.1.6.0")
print("Localização:", sys_location)
```

### 2. `snmp.get_safe(config, oid)`

Safe version of `getex` that does not throw exceptions, returning an error as the second value.

#### Parameters:

- **config** (table): SNMP configuration

- **oid** (string): OID to query

#### Return:

- **tuple**: `(value, error)` where:

    - **value** (any type or nil): Value returned if successful

    - **error** (string or nil): Error message if failed, nil if successful

#### Example Usage:

```lua
local config = {
    address = "192.168.1.1",
    snmpVersion = 2,
    snmpCommunity = "public"
}

-- Safe query that doesn't break the script in case of error
local valor, erro = snmp.get_safe(config, "1.3.6.1.2.1.1.1.0")

if erro then
    log.error("Falha na consulta SNMP:", erro)
    -- Take alternative action
else
    print("Valor obtido:", valor)
end

-- Query multiple OIDs with individual error handling
local oids = {
    "1.3.6.1.2.1.1.1.0",  -- sysDescr
    "1.3.6.1.2.1.1.3.0",  -- sysUpTime
    "1.3.6.1.2.1.1.5.0",  -- sysName
    "1.3.6.1.2.1.1.6.0"   -- sysLocation
}

local resultados = {}
for _, oid in ipairs(oids) do
    local valor, erro = snmp.get_safe(config, oid)
    if erro then
        log.warn("Falha no OID", oid, ":", erro)
        resultados[oid] = {erro = erro}
    else
        resultados[oid] = {valor = valor}
    end
end
```

### 3. `snmp.get_bulk(config, oids)`

Performs an SNMP GET BULK operation for multiple OIDs at once (SNMP v2c/v3).

#### Parameters:

- **config** (table): SNMP configuration (must be v2 or v3)

- **oids** (array of strings): List of OIDs to query

#### Return:

- **table**: Map OID → value for all queried OIDs

#### Behavior:

- More efficient than multiple `getex` calls for many OIDs

- Supported only in SNMP v2c and v3

- Uses `snmpMaxBulkItems` from the configuration to limit size

#### Example Usage:

```lua
local config = {
    address = "192.168.1.1",
    snmpVersion = 2,  -- Must be v2 or v3 for GET BULK
    snmpCommunity = "public",
    snmpMaxBulkItems = 50  -- Limit to 50 OIDs per operation
}

-- Query multiple system information at once
local oids = {
    "1.3.6.1.2.1.1.1.0",  -- sysDescr
    "1.3.6.1.2.1.1.3.0",  -- sysUpTime
    "1.3.6.1.2.1.1.5.0",  -- sysName
    "1.3.6.1.2.1.1.6.0",  -- sysLocation
    "1.3.6.1.2.1.1.7.0"   -- sysServices
}

local resultados = snmp.get_bulk(config, oids)

for oid, valor in pairs(resultados) do
    print("OID:", oid, "=", valor)
end

-- Query information for multiple interfaces
local function obter_info_interfaces(config, indices)
    local oids = {}
    for _, idx in ipairs(indices) do
        table.insert(oids, "1.3.6.1.2.1.2.2.1.2." .. idx)   -- ifDescr
        table.insert(oids, "1.3.6.1.2.1.2.2.1.3." .. idx)   -- ifType
        table.insert(oids, "1.3.6.1.2.1.2.2.1.5." .. idx)
    end
    return snmp.get_bulk(config, oids)
end
```

### 4. `snmp.get(oid)`

Simplified version of `snmp.getex` that automatically uses the current device configuration (`params`).

#### Parameters:

- **oid** (string): OID to query

#### Return:

- **value**: Value returned by the SNMP device

#### Behavior:

- Uses `params` as configuration

- Raises an error if the OID does not exist or there is a communication failure

#### Example Usage:

```lua
-- Simplified query using current device configuration
local sys_descr = snmp.get("1.3.6.1.2.1.1.1.0")
print("Descrição do sistema:", sys_descr)

-- Query multiple OIDs
local uptime = snmp.get("1.3.6.1.2.1.1.3.0")
local hostname = snmp.get("1.3.6.1.2.1.1.5.0")

print("Uptime:", uptime, "Hostname:", hostname)
```

### 5. `snmp.walk(oid, cache_ttl, enforce_ordering)`

Performs an SNMP WALK operation with support for caching and ordering.

#### Parameters:

- **oid** (string): Base OID for the walk

- **cache_ttl** (number, optional): Cache time-to-live in seconds

- **enforce_ordering** (boolean, optional): Enforce natural ordering of results

#### Cache behavior:

- Uses cache when `cache_ttl` is specified

#### Example Usage:

```lua
-- Walk with 30-second cache
local interfaces = snmp.walk("1.3.6.1.2.1.2.2.1.2", 30)
for oid, ifname in pairs(interfaces) do
    print("Interface", oid, ":", ifname)
end

-- Walk with enforced ordering (no cache)
local ordered_interfaces = snmp.walk("1.3.6.1.2.1.2.2.1.2", nil, true)
print("Total de interfaces:", #ordered_interfaces)
```

#### Ordering Behavior:

The `enforce_ordering` parameter controls how results are structured:

- **When `false` (default)**: Results are returned as a Lua table where each OID is a key mapping to its value. This structure is efficient for random access, but it **loses the natural ordering** of OIDs, since Lua tables do not preserve insertion order of keys.

- **When `true`**: Results are returned as a **list of pairs** (table of tables), where each element is a table containing 2 elements. This structure preserves the natural order of the OIDs as returned by the SNMP device.

**Example of difference**:

```lua
-- With enforce_ordering = false (default)
local resultado_tabela = snmp.walk("1.3.6.1.2.1.2.2.1.2", nil, false)
-- Structure: { ["1.3.6.1.2.1.2.2.1.2.1"] = "eth0", ["1.3.6.1.2.1.2.2.1.2.2"] = "eth1" }
-- The order of keys is not guaranteed

-- With enforce_ordering = true
local resultado_lista = snmp.walk("1.3.6.1.2.1.2.2.1.2", nil, true)
-- Structure: { {"1.3.6.1.2.1.2.2.1.2.1", "eth0"},
--              {"1.3.6.1.2.1.2.2.1.2.2", "eth1"} }
-- The order of elements is preserved
```

When to use each mode:

- Use `enforce_ordering = false` when you only need to access values by specific OID and order does not matter.

- Use `enforce_ordering = true` when you need to process results in the same order returned by the device, such as:

    - Generating ordered reports

    - Processing sequences of consecutive indices

    - Maintaining correspondence with other ordered lists

#### Return:

- **table**: Map OID → value for all found OIDs

### 6. `snmp.walkex(device, oid, cache_ttl)`

Extended walk function with advanced cache system and prevention of concurrent executions.

#### Parameters:

- **device** (table): Device configuration

- **oid** (string): Base OID for the walk

- **cache_ttl** (number, optional): Cache time-to-live in seconds

#### Return:

- **table**: Map OID → value for all found OIDs

#### Behavior:

- Implements a global cache shared between executions

- Prevents concurrent executions of the same walk

- Uses `registry` to coordinate simultaneous executions

#### Example Usage:

```lua
-- Extended walk with 60-second cache
local device_config = {
    address = "192.168.1.1",
    snmpVersion = 2,
    snmpCommunity = "public"
}

local sys_oids = snmp.walkex(device_config, "1.3.6.1.2.1.1", 60)
for oid, value in pairs(sys_oids) do
    print("OID:", oid, "Valor:", value)
end
```

### 7. `snmp.count(oid)`

Counts the number of items returned by a walk.

#### Parameters:

- **oid** (string): Base OID to count

#### Return:

- **number**: Number of items found

#### Example Usage:

```lua
-- Count number of interfaces
local num_interfaces = snmp.count("1.3.6.1.2.1.2.2.1.2")
print("Número de interfaces:", num_interfaces)

-- Count number of processes
local num_processes = snmp.count("1.3.6.1.2.1.25.4.2.1.2")
print("Número de processos:", num_processes)
```

### 8. `snmp.diff(typ, lhs, rhs)`

Calculates the difference between two values, handling counter rollover.

#### Parameters:

- **typ** (number): Counter type (32 or 64 bits)

- **lhs** (number): Current value

- **rhs** (number): Previous value

#### Return:

- **number**: Difference between the values

#### Behavior:

- Handles rollover for 32- and 64-bit counters

- Signals `RepeatPrevValue` if the difference is negative

#### Example Usage:

```lua
-- Calculate difference for 32-bit counter
local current_bytes = snmp.get("1.3.6.1.2.1.2.2.1.10.1")  -- ifInOctets.1
local prev_bytes = prev("1.3.6.1.2.1.2.2.1.10.1")
local bytes_diff = snmp.diff(32, current_bytes, prev_bytes)

print("Bytes recebidos desde última leitura:", bytes_diff)
```

### 9. `inst(oid)`

Dynamically resolves instance OIDs based on the instance name.

#### Parameters:

- **oid** (string): Base OID (without instance index)

#### Return:

- **string**: Full OID with instance index

#### Behavior:

- Uses `params.InstanceName` and `params.snmpOIDDesc` for resolution

- Supports instance caching

- Raises an error if the instance is not found

#### Example Usage:

```lua
-- Resolve OID for specific instance
-- params.InstanceName = "eth0"
-- params.snmpOIDDesc = "1.3.6.1.2.1.2.2.1.2"  -- ifDescr

local if_in_octets_oid = inst("1.3.6.1.2.1.2.2.1.10")  -- ifInOctets
print("OID resolvido:", if_in_octets_oid)
-- Output: "1.3.6.1.2.1.2.2.1.10.1" (if eth0 is index 1)

-- Query using resolved OID
local bytes_in = snmp.get(if_in_octets_oid)
print("Bytes recebidos na interface eth0:", bytes_in)
```

### 10. `prev(oid)`

Gets the previous value of an OID stored.

#### Parameters:

- **oid** (string): OID to get previous value for

#### Return:

- **any type**: Previously stored value, or 0 if none exists

#### Behavior:

- Looks up value in `store.get("snmp.value." .. oid)`

- Returns 0 if no stored value is found

#### Example Usage:

```lua
-- Get previous value for rate calculation
local current_value = snmp.get("1.3.6.1.2.1.2.2.1.16.1")  -- ifOutOctets.1
local previous_value = prev("1.3.6.1.2.1.2.2.1.16.1")

local bytes_out_diff = current_value - previous_value
print("Bytes enviados desde última leitura:", bytes_out_diff)
```

### 11. `lapsed(oid)`

Gets the elapsed time since the last read of an OID.

#### Parameters:

- **oid** (string): OID to check elapsed time for

#### Return:

- **number**: Time in seconds since last read, or 1 if no record exists

#### Example Usage:

```lua
-- Calculate rate per second
local current_counter = snmp.get("1.3.6.1.2.1.2.2.1.10.1")  -- ifInOctets.1
local previous_counter = prev("1.3.6.1.2.1.2.2.1.10.1")
local time_elapsed = lapsed("1.3.6.1.2.1.2.2.1.10.1")

local bytes_per_second = (current_counter - previous_counter) / time_elapsed
print("Taxa de recebimento:", bytes_per_second, "bytes/segundo")
```

## Complete Examples

### Network Interface Monitoring:

```lua
-- Resolve OID of eth0 interface
local if_index_oid = inst("1.3.6.1.2.1.2.2.1.1")  -- ifIndex
local if_descr_oid = inst("1.3.6.1.2.1.2.2.1.2")  -- ifDescr

-- Get interface information
local interface_index = snmp.get(if_index_oid)
local interface_name = snmp.get(if_descr_oid)

print("Monitorando interface:", interface_name, "(índice", interface_index, ")")

-- Collect statistics
local in_octets = snmp.get(inst("1.3.6.1.2.1.2.2.1.10"))  -- ifInOctets
local out_octets = snmp.get(inst("1.3.6.1.2.1.2.2.1.16")) -- ifOutOctets
local in_errors = snmp.get(inst("1.3.6.1.2.1.2.2.1.14"))  -- ifInErrors
local out_errors = snmp.get(inst("1.3.6.1.2.1.2.2.1.20")) -- ifOutErrors

-- Calculate differences since last read
local time_elapsed = lapsed(inst("1.3.6.1.2.1.2.2.1.10"))
local prev_in = prev(inst("1.3.6.1.2.1.2.2.1.10"))
local prev_out = prev(inst("1.3.6.1.2.1.2.2.1.16"))

local in_rate = (in_octets - prev_in) / time_elapsed
local out_rate = (out_octets - prev_out) / time_elapsed

print("Taxa de entrada:", in_rate, "bytes/seg")
print("Taxa de saída:", out_rate, "bytes/seg")
print("Erros de entrada:", in_errors)
print("Erros de saída:", out_errors)
```

### Interface Inventory with Walk:

```lua
-- List all interfaces with walk
local interfaces = snmp.walk("1.3.6.1.2.1.2.2.1.2", 300)  -- ifDescr with 5-minute cache

print("=== Inventário de Interfaces ===")
for oid, ifname in pairs(interfaces) do
    -- Extract interface index from OID
    local index = string.match(oid, "(%d+)$")

    -- Get type and status of the interface
    local iftype = snmp.get("1.3.6.1.2.1.2.2.1.3." .. index)   -- ifType
    local ifstatus = snmp.get("1.3.6.1.2.1.2.2.1.8." .. index)  -- ifOperStatus

    local status_text = "DOWN"
    if ifstatus == 1 then status_text = "UP" end

    print(string.format("Interface %s: %s (Tipo: %d, Status: %s)",
                       index, ifname, iftype, status_text))
end

print("Total de interfaces:", snmp.count("1.3.6.1.2.1.2.2.1.2"))
```

### CPU Usage Monitoring with Multiple Instances:

```lua
-- Use walk to get all CPUs
local cpu_oids = snmp.walk("1.3.6.1.2.1.25.3.3.1.2", 30)  -- hrProcessorLoad

local total_load = 0
local cpu_count = 0

for oid, load in pairs(cpu_oids) do
    cpu_count = cpu_count + 1
    total_load = total_load + load

    local cpu_index = string.match(oid, "(%d+)$")
    print(string.format("CPU %d: %d%%", cpu_index, load))
end

if cpu_count > 0 then
    local avg_load = total_load / cpu_count
    print(string.format("Média de uso de CPU: %.1f%%", avg_load))
end
```