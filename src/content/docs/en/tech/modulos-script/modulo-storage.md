---
title: Storage Module
---
The Storage module performs continuous analysis of the integrity and performance of hard disk drives (HDDs) and solid-state drives (SSDs), collecting S.M.A.R.T. information to identify signs of wear, imminent failures and device degradation

## Available Functions

### 1. `storage.list_devices()`

Lists all storage devices detected on the system.

**Return**:  
Array of *strings* with the device paths

`{ "/dev/sda", "/dev/sdb" }`

**Example**:

```lua
local devices = storage.list_devices()

for _, dev in ipairs(devices) do
    print(dev)
end
```

### 2. `storage.info(path)`

Returns general disk information.

**Parameters**:

`path` (*string*): Device path (e.g. `"/dev/sda"`)

**Return**:

`Table` with the fields:

| Field | Type | Description |
| --- | --- | --- |
| `device_model` | *string* | Disk model |
| `model_family` | *string* | Model family (ATA only) |
| `serial_number` | *string* | Serial number |
| `firmware_version` | *string* | Firmware version |
| `user_capacity` | *string* | Total capacity |
| `rotation_rate` | *string* | RPM (ATA only) |
| `form_factor` | *string* | Physical form factor (ATA only) |
| `interface` | *string* | Interface speed (ATA only) |
| `protocol` | *string* | "ATA", "NVMe" or "SCSI" |
| `smart_support` | *table* | S.M.A.R.T. support information |
| `logical_block_size` | *number* | Logical block size |
| `physical_block_size` | *number* | Physical block size |
| `nvme_version` | *string* | NVMe version (NVMe only) |

**Example usage**:

```lua
local info = storage.info("/dev/sda")
print(info.device_model, info.serial_number)
```

### 3. `storage.health(path)`

Returns the disk's overall health status (S.M.A.R.T. *overall-health*).

**Parameters**:

`path` (*string*): Device path

**Return**:

`Table` with the fields:

| Field | Type | Description |
| --- | --- | --- |
| `passed` | *boolean* | true if the disk passed the S.M.A.R.T. test |
| `status` | *string* | "PASSED" or "FAILED" |
| `message` | *string* | Descriptive status message |

**Example usage**:

```lua
local h = storage.health("/dev/sda")
if h.passed then
    print("Disco saudavel")
else
    print("FALHA: " .. h.message)
end
```

### 4. `storage.attributes(path)`

Returns all the disk's S.M.A.R.T. attributes.

**Parameters**:

`path` (*string*): Device path

**Return**:

Array of objects, each with the fields:

| Field | Type | Description |
| --- | --- | --- |
| `id` | *number* | Attribute ID |
| `name` | *string* | Attribute name (e.g.: "Temperature_Celsius") |
| `value` | *number* | Normalized value |
| `worst` | *number* | Worst value recorded |
| `thresh` | *number* | Failure threshold |
| `raw` | *number* | Raw value (*raw*) |
| `when_failed` | *string* | Failure indication |
| `flags` | *string* | Attribute flags |

**Example usage**:

```lua
local attrs = storage.attributes("/dev/sda")
for _, a in ipairs(attrs) do
    print(a.id, a.name, a.raw)
end
```

### 5. `storage.attribute(path, attr_name)`

Returns a specific S.M.A.R.T. attribute by name.

**Parameters**:

| Parameter | Type | Description |
| --- | --- | --- |
| `path` | *string* | Device path |
| `attr_name` | *string* | Attribute name (e.g.: "Temperature_Celsius") |

**Return**:

The attribute object if found, `nil` otherwise

**Example usage**:

```lua
local attr = storage.attribute("/dev/sda", "Power_On_Hours")
if attr then
    print("Horas ligadas:", attr.raw)
end
```

### 6. `storage.temperature(path)`

Returns the current disk temperature in Celsius.

**Parameters**:

`path` (*string*): Device path

**Return**:

Temperature in degrees Celsius, or `nil` if unavailable

**Example usage**:

```lua
local temp = storage.temperature("/dev/sda")
if temp then
    print("Temperatura:", temp, "C")
end
```

### 7. `storage.error_log(path)`

Returns a summary of the disk's error log.

**Parameters**:

`path` (*string*):   Device path

**Return**:

`Table` or `nil` with the fields (varies by protocol):

| | Field | Type | Description |
| :---: | --- | --- | --- |
| ATA | | | |
| | `count` | *number* | Number of recorded errors |
| | `logged_errors` | *number* | Logged errors |
| NVMe | | | |
| | `size` | *number* | Log size |
| | `read` | *number* | Entries read |
| | `unread` | *number* | Unread entries |

**Example usage**:

```lua
local log = storage.error_log("/dev/nvme0")
if log then
    print("Erros nao lidos:", log.unread)
end
```

### 8. `storage.self_test(path)`

Returns the result of the last disk self-test.

**Parameters**:

`path` (*string*):   Device path

**Return**:

`Table` or `nil` with the fields (varies by protocol):

| Field | Description |
| --- | --- |
| `ATA` | Returns the latest test from the self-tests table |
| `NVMe` | `current_self_test_operation` (*string*): Current operation |

**Example usage**:

```lua
local test = storage.self_test("/dev/sda")
if test then
    print("Status:", test.status)
end
```