---
title: "Módulo Ping"
---

El módulo **ping** proporciona funciones para probar la conectividad de red mediante ICMP, TCP y DNS. Este módulo es útil para el monitoreo de disponibilidad, diagnóstico de problemas de red y medición de latencia en entornos de producción.

**Características principales**:

- Soporte para ping ICMP (IPv4 y IPv6)

- Pruebas de puerto TCP

- Configuración flexible de parámetros

- Resolución DNS automática

- Timeout configurable

## Funciones Disponibles

### 1. `ping.up([host], [count], [data_size], [timeout], [interval_ms])`

Comprueba si un host es accesible mediante ping ICMP.

#### Parámetros:

- **host** (opcional, string): Dirección del host o nombre de dominio (ej: "google.com", "192.168.1.1")

- **count** (opcional, número, por defecto: `params.icmpUpNumPackets` o 3): Número de intentos de ping

- **data_size** (opcional, número, por defecto: 24): Tamaño del paquete de datos en bytes

- **timeout** (opcional, número, por defecto: `params.icmpUpTimeout` o 2): Timeout en segundos para cada intento

- **interval_ms** (opcional, número, por defecto: `params.icmpUpInterval` o 100): Intervalo entre intentos en milisegundos

- Si `host` no se proporciona, usa `params.address`

- Si `count` no se proporciona, usa `params.icmpUpNumPackets`

- Si `timeout` no se proporciona, usa `params.icmpUpTimeout`

- Si `interval_ms` no se proporciona, usa `params.icmpUpInterval`

#### Retorno:

- **boolean**: `true` si al menos un ping fue exitoso, `false` en caso contrario

#### Ejemplo de Uso:

```lua
-- Comprobar si un host es accesible
local acessivel = ping.up("google.com")
-- acessivel = true (si responde al ping)

-- Comprobar con parámetros personalizados
local resultado = ping.up("servidor.local", 5, 32, 5, 200)
-- 5 intentos, paquetes de 32 bytes, timeout de 5s, intervalo de 200ms

-- Probar dirección IPv6
local ipv6_ok = ping.up("2001:4860:4860::8888")
-- Prueba conectividad IPv6 con Google DNS

-- Comprobar múltiples hosts
local hosts = {"router.local", "192.168.1.1", "8.8.8.8"}
for _, host in ipairs(hosts) do
    if ping.up(host) then
        print(host .. " está online")
    else
        print(host .. " está offline")
    end
end
```

### 2. `ping.send([host], [count], [data_size], [timeout], [interval_ms])`

Mide la latencia de ping ICMP hacia un host.

#### Parámetros:

- **host** (opcional,string): Dirección del host o nombre de dominio

- **count** (opcional, número, por defecto: `params.icmpTimeNumPackets` o 3): Número de intentos de ping

- **data_size** (opcional, número, por defecto: 24): Tamaño del paquete de datos en bytes

- **timeout** (opcional, número, por defecto: `params.icmpTimeTimeout` o 2): Timeout en segundos para cada intento

- **interval_ms** (opcional, número, por defecto: `params.icmpTimeInterval` o 100): Intervalo entre intentos en milisegundos

- Si `host` no se proporciona, usa `params.address`

- Si `count` no se proporciona, usa `params.icmpTimeNumPackets`

- Si `timeout` no se proporciona, usa `params.icmpTimeTimeout`

- Si `interval_ms` no se proporciona, usa `params.icmpTimeInterval`

#### Retorno:

- **tuple**: `(latencia, erro)` donde:

    - **latencia** (número o nil): Latencia media en milisegundos, o `nil` si falla

    - **erro** (string o nil): Mensaje de error, o `nil` si tiene éxito

#### Ejemplo de Uso:

```lua
-- Medir latencia básica
local latencia, erro = ping.send("google.com")
-- latencia = 25.3 (ejemplo), erro = nil

-- Medir con parámetros personalizados
local latencia, erro = ping.send("servidor.remoto", 10, 64, 5, 500)
-- 10 intentos, paquetes de 64 bytes, timeout 5s, intervalo 500ms

-- Manejar resultado
local latencia, erro = ping.send("host.inacessivel")
if latencia then
    print("Latência: " .. latencia .. "ms")
else
    print("Erro: " .. erro)
    -- erro = "ping failed" o mensaje específico
end

-- Comparar latencia entre múltiples hosts
local hosts = {
    "dns.google",
    "cloudflare-dns.com",
    "quad9.net"
}

for _, host in ipairs(hosts) do
    local latencia, erro = ping.send(host, 5)
    if latencia then
        print(host .. ": " .. string.format("%.2f", latencia) .. "ms")
    end
end
```

### 3. `ping.port(host, port, [count], [timeout])`

Prueba la conectividad a un puerto TCP específico.

#### Parámetros:

- **host** (string): Dirección del host o nombre de dominio

- **port** (número): Número del puerto TCP a probar

- **count** (opcional, número, por defecto: 3): Número de intentos de conexión

- **timeout** (opcional, número, por defecto: 2): Timeout en segundos para cada intento

#### Retorno:

- **tuple**: `(latencia, erro)` donde:

    - **latencia** (número o nil): Latencia media de conexión en milisegundos, o `nil` si falla

    - **erro** (string o nil): Mensaje de error, o `nil` si tiene éxito

#### Ejemplo de Uso:

```lua
-- Probar puerto HTTP por defecto
local latencia, erro = ping.port("google.com", 80)
-- latencia = 45.2 (ejemplo), erro = nil

-- Probar puerto HTTPS
local latencia, erro = ping.port("google.com", 443)
if latencia then
    print("HTTPS acessível com latência: " .. latencia .. "ms")
else
    print("HTTPS inacessível: " .. erro)
end

-- Probar múltiples puertos
local portas = {22, 80, 443, 3306, 5432}
for _, porta in ipairs(portas) do
    local latencia, erro = ping.port("servidor.local", porta, 2, 3)
    if latencia then
        print("Porta " .. porta .. " aberta (" .. latencia .. "ms)")
    else
        print("Porta " .. porta .. " fechada ou inacessível")
    end
end

-- Verificar servicio específico
local function verificar_servico(host, porta, nome_servico)
    local latencia, erro = ping.port(host, porta)
    if latencia then
        log.info(nome_servico .. " OK (" .. latencia .. "ms)")
        return true
    else
        log.error(nome_servico .. " FALHA: " .. erro)
        return false
    end
end
```

## Información Adicional

### Resolución DNS Automática

Todas las funciones realizan resolución DNS automáticamente:

```lua
-- Funciona con nombres de dominio
ping.up("google.com")
ping.send("api.github.com")
ping.port("servidor.local", 443)

-- Funciona con direcciones IP
ping.up("8.8.8.8")
ping.send("192.168.1.1")
ping.port("10.0.0.5", 22)
```

### Soporte para IPv4 e IPv6

El módulo detecta automáticamente el tipo de dirección:

```lua
-- IPv4
ping.up("8.8.8.8")

-- IPv6
ping.up("2001:4860:4860::8888")

-- Nombre de dominio (resuelto a IPv4 o IPv6)
ping.up("google.com")
```

### Timeout Configurable

Cada función permite configurar el timeout de forma individual:

```lua
-- Timeout corto para redes locales
ping.up("router.local", 3, 24, 1)  -- 1 segundo

-- Timeout largo para redes con alta latencia
ping.up("servidor.remoto", 3, 24, 10)  -- 10 segundos

-- Timeout específico por puerto
ping.port("database.remoto", 5432, 3, 5)  -- 5 segundos
```