---
title: "Módulo SNMP"
---

El módulo **snmp** proporciona una interfaz completa para el monitoreo y la gestión de dispositivos de red a través del protocolo SNMP (Simple Network Management Protocol). Este módulo es útil para la recopilación de métricas de routers, switches, servidores, impresoras y cualquier dispositivo que soporte SNMP.

- Soporte para SNMP v1, v2c y v3

- Operaciones GET, GET BULK y WALK

- Autenticación y cifrado SNMP v3

- Configuración flexible de timeout y reintentos

- Retorno seguro con manejo de errores

**Protocolos soportados**:

- **SNMP v1**: Protocolo básico con comunidad pública/privada

- **SNMP v2c**: Mejoras de rendimiento con operaciones BULK

- **SNMP v3**: Seguridad avanzada con autenticación y cifrado

## Configuración SNMP

Todas las funciones SNMP requieren un objeto de configuración que define los parámetros de conexión. La configuración es una tabla Lua con los siguientes campos:

### Campos de Configuración Básicos:

| Campo                    | Tipo     | Padrão          | Descripción                             |
| --- | --- | :---: | --- |
| `address`                | string   | **obrigatório** | Endereço IP ou hostname do dispositivo |
| `snmpVersion`            | número   | 1               | Versão SNMP (1=v1, 2=v2c, 3=v3)        |
| `snmpPort`               | número   | 161             | Porta SNMP                             |
| `snmpCommunity`          | string   | nil             | Comunidade SNMP (v1/v2c)               |
| `snmpTimeout`            | número   | 5               | Timeout em segundos                    |
| `snmpRetryCount`         | número   | 3               | Número de retentativas                 |
| `snmpMaxBulkItems`       | número   | nil             | Máximo de itens por operação BULK      |
| `snmpExponentialBackoff` | booleano | false           | Habilitar backoff exponencial          |

### Campos para SNMP v3:

| Campo               | Tipo   | Descripción                                                    |
| --- | --- | --- |
| `snmpSecurityLevel` | string | Nível de segurança: "NoAuthNoPriv", "AuthNoPriv", "AuthPriv" |
| `snmpAuthProtocol`  | string | Protocolo de autenticação: "MD5", "SHA1"                     |
| `snmpAuthUser`      | string | Usuário de autenticação                                      |
| `snmpAuthPassword`  | string | Senha de autenticação                                        |
| `snmpPrivProtocol`  | string | Protocolo de criptografia: "DES", "AES"                      |
| `snmpPrivPassword`  | string | Senha de criptografia                                        |

### Configuração via Tabela `params`:

O ambiente Lua inclui uma tabela predefinida chamada `params` que contém os detalhes do dispositivo atual. Esta tabela puede ser usada directamente como configuración SNMP, ya que ya posee los campos necesarios en el formato esperado.

**Exemplo de uso direto**:

```lua
-- Usar la tabla device directamente como configuración
local sys_descr = snmp.getex(device, "1.3.6.1.2.1.1.1.0")
print("Descrição do dispositivo:", sys_descr)

-- Versión que no lanza error
local valor, erro = snmp.get_safe(device, "1.3.6.1.2.1.1.3.0")
if not erro then
    print("Uptime do dispositivo:", valor)
end
```

**Combinando com configurações adicionais**:

```lua
-- Crear configuración basada en device con ajustes
local config = {
    address = device.address,
    snmpVersion = device.snmpVersion,
    snmpCommunity = device.snmpCommunity,
    snmpTimeout = device.snmpTimeout or 5,  -- Usar el valor predeterminado si no está definido
    snmpRetryCount = 2,  -- Sobrescribir valor predeterminado
    snmpMaxBulkItems = 50  -- Agregar configuración adicional
}

-- Usar para operación BULK
local oids = {"1.3.6.1.2.1.1.1.0", "1.3.6.1.2.1.1.3.0"}
local resultados = snmp.get_bulk(config, oids)
```

### Ejemplos de Configuración:

```lua
-- Configuração básica SNMP v2c
local config_v2c = {
    address = "192.168.1.1",
    snmpVersion = 2,
    snmpCommunity = "public",
    snmpTimeout = 3,
    snmpRetryCount = 2
}

-- Configuração SNMP v3 com autenticação e criptografia
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

-- Configuração para dispositivo com porta não padrão
local config_custom_port = {
    address = "switch.piso1.local",
    snmpVersion = 2,
    snmpCommunity = "internal",
    snmpPort = 8161,  -- Puerto personalizado
    snmpTimeout = 10  -- Timeout mayor para red lenta
}
```

## Funções Disponíveis

### 1. `snmp.getex(config, oid)`

Realiza una consulta SNMP GET para un OID específico.

#### Parâmetros:

- **config** (tabela): Configuração SNMP (ver seção acima)

- **oid** (string): OID a ser consultado (formato numérico ou nomeado)

#### Retorno:

- **valor**: Valor retornado pelo dispositivo SNMP (número, string, etc.)

#### Erros:

- Lança erro se o OID não existir ou houver falha na comunicação

#### Exemplo de Uso:

```lua
-- Consultar sysDescr (descripción del sistema)
local config = {
    address = "192.168.1.1",
    snmpVersion = 2,
    snmpCommunity = "public"
}

local sys_descr = snmp.getex(config, "1.3.6.1.2.1.1.1.0")
-- o usando OID nombrado
local sys_descr = snmp.getex(config, ".1.3.6.1.2.1.1.1.0")

print("Descrição do sistema:", sys_descr)
-- Ejemplo de salida: "Cisco IOS Software, C3750 Software (C3750-IPSERVICESK9-M), Version 12.2(55)SE10, RELEASE SOFTWARE (fc2)"

-- Consultar uptime del sistema
local sys_uptime = snmp.getex(config, "1.3.6.1.2.1.1.3.0")
print("Uptime:", sys_uptime, "centésimos de segundo")

-- Consultar nombre del host
local sys_name = snmp.getex(config, "1.3.6.1.2.1.1.5.0")
print("Nome do host:", sys_name)

-- Consultar ubicación
local sys_location = snmp.getex(config, "1.3.6.1.2.1.1.6.0")
print("Localização:", sys_location)
```

### 2. `snmp.get_safe(config, oid)`

Versión segura de `getex` que no lanza excepciones, retornando el error como segundo valor.

#### Parâmetros:

- **config** (tabela): Configuração SNMP

- **oid** (string): OID a ser consultado

#### Retorno:

- **tuple**: `(valor, erro)` donde:

    - **valor** (qualquer tipo ou nil): Valor retornado se bem-sucedido

    - **erro** (string ou nil): Mensagem de error se falhar, nil se bem-sucedido

#### Exemplo de Uso:

```lua
local config = {
    address = "192.168.1.1",
    snmpVersion = 2,
    snmpCommunity = "public"
}

-- Consulta segura que no rompe el script en caso de error
local valor, erro = snmp.get_safe(config, "1.3.6.1.2.1.1.1.0")

if erro then
    log.error("Falha na consulta SNMP:", erro)
    -- Tomar acción alternativa
else
    print("Valor obtido:", valor)
end

-- Consultar múltiplos OIDs com tratamento de erro individual
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

Realiza operación SNMP GET BULK para múltiples OIDs a la vez (SNMP v2c/v3).

#### Parâmetros:

- **config** (tabela): Configuração SNMP (deve ser v2 ou v3)

- **oids** (array de strings): Lista de OIDs para consulta

#### Retorno:

- **tabela**: Mapa OID → valor para todos los OIDs consultados

#### Comportamiento:

- Más eficiente que múltiples llamadas `getex` para muchos OIDs

- Soportado solo en SNMP v2c y v3

- Usa `snmpMaxBulkItems` de la configuración para limitar tamaño

#### Exemplo de Uso:

```lua
local config = {
    address = "192.168.1.1",
    snmpVersion = 2,  -- Deve ser v2 ou v3 para GET BULK
    snmpCommunity = "public",
    snmpMaxBulkItems = 50  -- Limitar a 50 OIDs por operación
}

-- Consultar múltiplas informações do sistema de uma vez
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

-- Consultar información de múltiples interfaces
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

Versión simplificada de `snmp.getex` que usa automáticamente la configuración del dispositivo actual (`params`).

#### Parâmetros:

- **oid** (string): OID a ser consultado

#### Retorno:

- **valor**: Valor retornado pelo dispositivo SNMP

#### Comportamiento:

- Usa `params` como configuração

- Lança erro se o OID não existir ou houver falha na comunicação

#### Exemplo de Uso:

```lua
-- Consulta simplificada usando la configuración del dispositivo actual
local sys_descr = snmp.get("1.3.6.1.2.1.1.1.0")
print("Descrição do sistema:", sys_descr)

-- Consultar múltiplos OIDs
local uptime = snmp.get("1.3.6.1.2.1.1.3.0")
local hostname = snmp.get("1.3.6.1.2.1.1.5.0")

print("Uptime:", uptime, "Hostname:", hostname)
```

### 5. `snmp.walk(oid, cache_ttl, enforce_ordering)`

Realiza una operación SNMP WALK con soporte de caché y ordenamiento.

#### Parâmetros:

- **oid** (string): OID base para el walk

- **cache_ttl** (número, opcional): Tiempo de vida del caché en segundos

- **enforce_ordering** (booleano, opcional): Forzar ordenación de los resultados (orden natural)

#### Comportamiento del cache:

- Usa caché cuando `cache_ttl` es especificado

#### Exemplo de Uso:

```lua
-- Walk con caché de 30 segundos
local interfaces = snmp.walk("1.3.6.1.2.1.2.2.1.2", 30)
for oid, ifname in pairs(interfaces) do
    print("Interface", oid, ":", ifname)
end

-- Walk con ordenación forzada (sin caché)
local ordered_interfaces = snmp.walk("1.3.6.1.2.1.2.2.1.2", nil, true)
print("Total de interfaces:", #ordered_interfaces)
```

#### Comportamiento de Ordenação:

El parámetro `enforce_ordering` controla cómo se estructuran los resultados:

- **Cuando `false` (padrão)**: Los resultados se retornan como una tabla Lua donde cada OID es una clave que mapea a su valor. Esta estructura es eficiente para acceso aleatorio, pero **pierde la ordenación natural** de los OIDs, ya que las tablas Lua no preservan el orden de inserción de las claves.

- **Cuando `true`**: Los resultados se retornan como una **lista de pares** (tabla de tablas), donde cada elemento es una tabla conteniendo 2 elementos. Esta estructura preserva el orden natural de los OIDs tal como son retornados por el dispositivo SNMP.

**Exemplo de diferença**:

```lua
-- Com enforce_ordering = false (padrão)
local resultado_tabela = snmp.walk("1.3.6.1.2.1.2.2.1.2", nil, false)
-- Estrutura: { ["1.3.6.1.2.1.2.2.1.2.1"] = "eth0", ["1.3.6.1.2.1.2.2.1.2.2"] = "eth1" }
-- A ordem das chaves não é garantida

-- Com enforce_ordering = true
local resultado_lista = snmp.walk("1.3.6.1.2.1.2.2.1.2", nil, true)
-- Estrutura: { {"1.3.6.1.2.1.2.2.1.2.1", "eth0"},
--              {"1.3.6.1.2.1.2.2.1.2.2", "eth1"} }
-- A ordem dos elementos é preservada
```

**Quando usar cada modo**:

- Use `enforce_ordering = false` cuando solo necesita acceder valores por OID específico y el orden no importa.

- Use `enforce_ordering = true` cuando necesita procesar los resultados en el mismo orden en que fueron retornados por el dispositivo, como para:

    - Generar reportes ordenados

    - Procesar secuencias de índices consecutivos

    - Mantener correspondencia con otras listas ordenadas

#### Retorno:

- **tabela**: Mapa OID → valor para todos os OIDs encontrados

### 6. `snmp.walkex(device, oid, cache_ttl)`

Función extendida de walk con sistema de caché avanzado y prevención de ejecuciones concurrentes.

#### Parâmetros:

- **device** (tabela): Configuração do dispositivo

- **oid** (string): OID base para el walk

- **cache_ttl** (número, opcional): Tiempo de vida del caché en segundos

#### Retorno:

- **tabela**: Mapa OID → valor para todos los OIDs encontrados

#### Comportamiento:

- Implementa caché global compartido entre ejecuciones

- Previene ejecuciones concurrentes del mismo walk

- Usa `registry` para coordinar ejecuciones simultáneas

#### Exemplo de Uso:

```lua
-- Walk extendido con caché de 60 segundos
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

Cuenta el número de ítems retornados por un walk.

#### Parâmetros:

- **oid** (string): OID base para contar

#### Retorno:

- **número**: Cantidad de ítems encontrados

#### Exemplo de Uso:

```lua
-- Contar número de interfaces
local num_interfaces = snmp.count("1.3.6.1.2.1.2.2.1.2")
print("Número de interfaces:", num_interfaces)

-- Contar número de procesos
local num_processes = snmp.count("1.3.6.1.2.1.25.4.2.1.2")
print("Número de processos:", num_processes)
```

### 8. `snmp.diff(typ, lhs, rhs)`

Calcula la diferencia entre dos valores, manejando rollover de contadores.

#### Parâmetros:

- **typ** (número): Tipo do contador (32 ou 64 bits)

- **lhs** (número): Valor atual

- **rhs** (número): Valor anterior

#### Retorno:

- **número**: Diferença entre os valores

#### Comportamiento:

- Trata rollover de contadores de 32 y 64 bits

- Señala `RepeatPrevValue` si la diferencia es negativa

#### Exemplo de Uso:

```lua
-- Calcular diferencia para contador de 32 bits
local current_bytes = snmp.get("1.3.6.1.2.1.2.2.1.10.1")  -- ifInOctets.1
local prev_bytes = prev("1.3.6.1.2.1.2.2.1.10.1")
local bytes_diff = snmp.diff(32, current_bytes, prev_bytes)

print("Bytes recebidos desde última leitura:", bytes_diff)
```

### 9. `inst(oid)`

Resuelve dinámicamente OIDs de instancias basado en el nombre de la instancia.

#### Parâmetros:

- **oid** (string): OID base (sin índice de instancia)

#### Retorno:

- **string**: OID completo con índice de instancia

#### Comportamiento:

- Usa `params.InstanceName` e `params.snmpOIDDesc` para resolución

- Soporta caché de instancias

- Lança erro se a instância não for encontrada

#### Exemplo de Uso:

```lua
-- Resolver OID para instância específica
-- params.InstanceName = "eth0"
-- params.snmpOIDDesc = "1.3.6.1.2.1.2.2.1.2"  -- ifDescr

local if_in_octets_oid = inst("1.3.6.1.2.1.2.2.1.10")  -- ifInOctets
print("OID resolvido:", if_in_octets_oid)
-- Saída: "1.3.6.1.2.1.2.2.1.10.1" (se eth0 for índice 1)

-- Consultar usando OID resolvido
local bytes_in = snmp.get(if_in_octets_oid)
print("Bytes recebidos na interface eth0:", bytes_in)
```

### 10. `prev(oid)`

Obtiene el valor anterior de un OID almacenado.

#### Parâmetros:

- **oid** (string): OID para obtener valor anterior

#### Retorno:

- **qualquer tipo**: Valor anterior almacenado, o 0 se no existir

#### Comportamiento:

- Busca valor en `store.get("snmp.value." .. oid)`

- Retorna 0 si no encuentra valor almacenado

#### Exemplo de Uso:

```lua
-- Obtener valor anterior para cálculo de tasa
local current_value = snmp.get("1.3.6.1.2.1.2.2.1.16.1")  -- ifOutOctets.1
local previous_value = prev("1.3.6.1.2.1.2.2.1.16.1")

local bytes_out_diff = current_value - previous_value
print("Bytes enviados desde última leitura:", bytes_out_diff)
```

### 11. `lapsed(oid)`

Obtiene el tiempo transcurrido desde la última lectura de un OID.

#### Parâmetros:

- **oid** (string): OID para verificar tiempo transcurrido

#### Retorno:

- **número**: Tiempo en segundos desde la última lectura, o 1 si no hay registro

#### Exemplo de Uso:

```lua
-- Calcular tasa por segundo
local current_counter = snmp.get("1.3.6.1.2.1.2.2.1.10.1")  -- ifInOctets.1
local previous_counter = prev("1.3.6.1.2.1.2.2.1.10.1")
local time_elapsed = lapsed("1.3.6.1.2.1.2.2.1.10.1")

local bytes_per_second = (current_counter - previous_counter) / time_elapsed
print("Taxa de recebimento:", bytes_per_second, "bytes/segundo")
```

## Exemplos Completos

### Monitoramento de Interface de Rede:

```lua
-- Resolver OID da interface eth0
local if_index_oid = inst("1.3.6.1.2.1.2.2.1.1")  -- ifIndex
local if_descr_oid = inst("1.3.6.1.2.1.2.2.1.2")  -- ifDescr

-- Obtener información de la interfaz
local interface_index = snmp.get(if_index_oid)
local interface_name = snmp.get(if_descr_oid)

print("Monitorando interface:", interface_name, "(índice", interface_index, ")")

-- Recopilar estadísticas
local in_octets = snmp.get(inst("1.3.6.1.2.1.2.2.1.10"))  -- ifInOctets
local out_octets = snmp.get(inst("1.3.6.1.2.1.2.2.1.16")) -- ifOutOctets
local in_errors = snmp.get(inst("1.3.6.1.2.1.2.2.1.14"))  -- ifInErrors
local out_errors = snmp.get(inst("1.3.6.1.2.1.2.2.1.20")) -- ifOutErrors

-- Calcular diferencias desde la última lectura
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

### Inventário de Interfaces com Walk:

```lua
-- Listar todas las interfaces con walk
local interfaces = snmp.walk("1.3.6.1.2.1.2.2.1.2", 300)  -- ifDescr com cache de 5 minutos

print("=== Inventário de Interfaces ===")
for oid, ifname in pairs(interfaces) do
    -- Extraer índice de la interfaz del OID
    local index = string.match(oid, "(%d+)$")

    -- Obtener tipo y estado de la interfaz
    local iftype = snmp.get("1.3.6.1.2.1.2.2.1.3." .. index)   -- ifType
    local ifstatus = snmp.get("1.3.6.1.2.1.2.2.1.8." .. index)  -- ifOperStatus

    local status_text = "DOWN"
    if ifstatus == 1 then status_text = "UP" end

    print(string.format("Interface %s: %s (Tipo: %d, Status: %s)",
                       index, ifname, iftype, status_text))
end

print("Total de interfaces:", snmp.count("1.3.6.1.2.1.2.2.1.2"))
```

### Monitoramento de Uso de CPU com Múltiplas Instâncias:

```lua
-- Usar walk para obter todas as CPUs
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