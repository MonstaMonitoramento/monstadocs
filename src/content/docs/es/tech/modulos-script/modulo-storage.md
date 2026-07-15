---
title: Módulo de almacenamiento
---
El módulo Storage realiza un análisis continuo de la integridad y el rendimiento de discos duros (HDs) y unidades de estado sólido (SSDs), recopilando información S.M.A.R.T. para identificar señales de desgaste, fallos inminentes y degradación del dispositivo

## Funciones Disponibles

### 1. `storage.list_devices()`

Lista todos los dispositivos de almacenamiento detectados en el sistema.

**Retorno**:  
Array de *string*s con las rutas de los dispositivos

`{ "/dev/sda", "/dev/sdb" }`

**Exemplo**:

```lua
local devices = storage.list_devices()

for _, dev in ipairs(devices) do
    print(dev)
end
```

### 2. `storage.info(path)`

Devuelve información general del disco.

**Parámetros**:

`path` (*string*): Ruta del dispositivo (ej.: `"/dev/sda"`)

**Retorno**:

`Table` con los campos:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `device_model` | *string* | Modelo del disco |
| `model_family` | *string* | Familia del modelo (solo ATA) |
| `serial_number` | *string* | Número de serie |
| `firmware_version` | *string* | Versión del firmware |
| `user_capacity` | *string* | Capacidad total |
| `rotation_rate` | *string* | RPM (solo ATA) |
| `form_factor` | *string* | Factor de forma (solo ATA) |
| `interface` | *string* | Velocidad de la interfaz (solo ATA) |
| `protocol` | *string* | "ATA", "NVMe" o "SCSI" |
| `smart_support` | *table* | Información de soporte S.M.A.R.T. |
| `logical_block_size` | *number* | Tamaño del bloque lógico |
| `physical_block_size` | *number* | Tamaño del bloque físico |
| `nvme_version` | *string* | Versión NVMe (solo NVMe) |

**Exemplo de uso**:

```lua
local info = storage.info("/dev/sda")
print(info.device_model, info.serial_number)
```

### 3. `storage.health(path)`

Devuelve el estado general de salud del disco (S.M.A.R.T. *overall-health*).

**Parámetros**:

`path` (*string*): Ruta del dispositivo

**Retorno**:

`Table` con los campos:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `passed` | *boolean* | true si el disco pasó la prueba S.M.A.R.T. |
| `status` | *string* | "PASSED" o "FAILED" |
| `message` | *string* | Mensaje descriptivo del estado |

**Exemplo de uso**:

```lua
local h = storage.health("/dev/sda")
if h.passed then
    print("Disco saudavel")
else
    print("FALHA: " .. h.message)
end
```

### 4. `storage.attributes(path)`

Devuelve todos los atributos S.M.A.R.T. del disco.

**Parámetros**:

`path` (*string*): Ruta del dispositivo

**Retorno**:

Array de objetos, cada uno con los campos:

| Campo | Tipo | Descripción |
| --- | --- | --- |
| `id` | *number* | ID del atributo |
| `name` | *string* | Nombre del atributo (ex: "Temperature_Celsius") |
| `value` | *number* | Valor normalizado |
| `worst` | *number* | Peor valor registrado |
| `thresh` | *number* | Umbral de fallo |
| `raw` | *number* | Valor bruto (*raw*) |
| `when_failed` | *string* | Indicación de fallo |
| `flags` | *string* | *Flags* del atributo |

**Exemplo de uso**:

```lua
local attrs = storage.attributes("/dev/sda")
for _, a in ipairs(attrs) do
    print(a.id, a.name, a.raw)
end
```

### 5. `storage.attribute(path, attr_name)`

Devuelve un atributo S.M.A.R.T. específico por su nombre.

**Parámetros**:

| Parâmetro | Tipo | Descrição |
| --- | --- | --- |
| `path` | *string* | Ruta del dispositivo |
| `attr_name` | *string* | Nombre del atributo (ex: "Temperature_Celsius") |

**Retorno**:

El objeto del atributo si se encuentra, `nil` en caso contrario

**Exemplo de uso**:

```lua
local attr = storage.attribute("/dev/sda", "Power_On_Hours")
if attr then
    print("Horas ligadas:", attr.raw)
end
```

### 6. `storage.temperature(path)`

Devuelve la temperatura actual del disco en Celsius.

**Parámetros**:

`path` (*string*): Ruta del dispositivo

**Retorno**:

Temperatura en grados Celsius, o `nil` si no está disponible

**Exemplo de uso**:

```lua
local temp = storage.temperature("/dev/sda")
if temp then
    print("Temperatura:", temp, "C")
end
```

### 7. `storage.error_log(path)`

Devuelve un resumen del registro de errores del disco.

**Parámetros**:

`path` (*string*):   Ruta del dispositivo

**Retorno**:

`Table` ou `nil` con los campos (varía según el protocolo):

| | Campo | Tipo | Descripción |
| :---: | --- | --- | --- |
| ATA | | | |
| | `count` | *number* | Cantidad de errores registrados |
| | `logged_errors` | *number* | Errores registrados en el log |
| NVMe | | | |
| | `size` | *number* | Tamaño del registro |
| | `read` | *number* | Entradas leídas |
| | `unread` | *number* | Entradas no leídas |

**Exemplo de uso**:

```lua
local log = storage.error_log("/dev/nvme0")
if log then
    print("Erros nao lidos:", log.unread)
end
```

### 8. `storage.self_test(path)`

Devuelve el resultado del último *self-test* del disco.

**Parámetros**:

`path` (*string*):   Ruta del dispositivo

**Retorno**:

`Table` ou `nil` con los campos (varía según el protocolo):

| Campo | Descripción |
| --- | --- |
| `ATA` | Devuelve la última prueba de la tabla de *self-tests* |
| `NVMe` | `current_self_test_operation` (*string*): Operación actual |

**Exemplo de uso**:

```lua
local test = storage.self_test("/dev/sda")
if test then
    print("Status:", test.status)
end
```