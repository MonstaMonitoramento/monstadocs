---
title: "Ping Module"
---

The **ping** module provides functions to test network connectivity via ICMP, TCP and DNS. This module is useful for availability monitoring, network troubleshooting and latency measurement in production environments.

**Key features**:

- ICMP ping support (IPv4 and IPv6)

- TCP port testing

- Flexible parameter configuration

- Automatic DNS resolution

- Configurable timeout

## Available Functions

### 1. `ping.up([host], [count], [data_size], [timeout], [interval_ms])`

Checks if a host is reachable via ICMP ping.

#### Parameters:

- **host** (optional, string): Host address or domain name (e.g., "google.com", "192.168.1.1")

- **count** (optional, number, default: `params.icmpUpNumPackets` or 3): Number of ping attempts

- **data_size** (optional, number, default: 24): Size of the data packet in bytes

- **timeout** (optional, number, default: `params.icmpUpTimeout` or 2): Timeout in seconds for each attempt

- **interval_ms** (optional, number, default: `params.icmpUpInterval` or 100): Interval between attempts in milliseconds

- If `host` is not provided, uses `params.address`

- If `count` is not provided, uses `params.icmpUpNumPackets`

- If `timeout` is not provided, uses `params.icmpUpTimeout`

- If `interval_ms` is not provided, uses `params.icmpUpInterval`

#### Return:

- **boolean**: `true` if at least one ping succeeded, `false` otherwise

#### Usage Example:

```lua
-- Check if a host is reachable
local acessivel = ping.up("google.com")
-- acessivel = true (if it responds to ping)

-- Check with custom parameters
local resultado = ping.up("servidor.local", 5, 32, 5, 200)
-- 5 attempts, 32-byte packets, 5s timeout, 200ms interval

-- Test IPv6 address
local ipv6_ok = ping.up("2001:4860:4860::8888")
-- Tests IPv6 connectivity with Google DNS

-- Check multiple hosts
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

Measures ICMP ping latency to a host.

#### Parameters:

- **host** (optional,string): Host address or domain name

- **count** (optional, number, default: `params.icmpTimeNumPackets` or 3): Number of ping attempts

- **data_size** (optional, number, default: 24): Size of the data packet in bytes

- **timeout** (optional, number, default: `params.icmpTimeTimeout` or 2): Timeout in seconds for each attempt

- **interval_ms** (optional, number, default: `params.icmpTimeInterval` or 100): Interval between attempts in milliseconds

- If `host` is not provided, uses `params.address`

- If `count` is not provided, uses `params.icmpTimeNumPackets`

- If `timeout` is not provided, uses `params.icmpTimeTimeout`

- If `interval_ms` is not provided, uses `params.icmpTimeInterval`

#### Return:

- **tuple**: `(latency, error)` where:

    - **latency** (number or nil): Average latency in milliseconds, or `nil` on failure

    - **error** (string or nil): Error message, or `nil` if successful

#### Usage Example:

```lua
-- Measure basic latency
local latencia, erro = ping.send("google.com")
-- latencia = 25.3 (example), erro = nil

-- Measure with custom parameters
local latencia, erro = ping.send("servidor.remoto", 10, 64, 5, 500)
-- 10 attempts, 64-byte packets, 5s timeout, 500ms interval

-- Handle result
local latencia, erro = ping.send("host.inacessivel")
if latencia then
    print("Latência: " .. latencia .. "ms")
else
    print("Erro: " .. erro)
    -- erro = "ping failed" or a specific message
end

-- Compare latency between multiple hosts
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

Tests connectivity to a specific TCP port.

#### Parameters:

- **host** (string): Host address or domain name

- **port** (number): TCP port number to test

- **count** (optional, number, default: 3): Number of connection attempts

- **timeout** (optional, number, default: 2): Timeout in seconds for each attempt

#### Return:

- **tuple**: `(latency, error)` where:

    - **latency** (number or nil): Average connection latency in milliseconds, or `nil` on failure

    - **error** (string or nil): Error message, or `nil` if successful

#### Usage Example:

```lua
-- Test default HTTP port
local latencia, erro = ping.port("google.com", 80)
-- latencia = 45.2 (example), erro = nil

-- Test HTTPS port
local latencia, erro = ping.port("google.com", 443)
if latencia then
    print("HTTPS acessível com latência: " .. latencia .. "ms")
else
    print("HTTPS inacessível: " .. erro)
end

-- Test multiple ports
local portas = {22, 80, 443, 3306, 5432}
for _, porta in ipairs(portas) do
    local latencia, erro = ping.port("servidor.local", porta, 2, 3)
    if latencia then
        print("Porta " .. porta .. " aberta (" .. latencia .. "ms)")
    else
        print("Porta " .. porta .. " fechada ou inacessível")
    end
end

-- Check specific service
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

## Additional Information

### Automatic DNS Resolution

All functions perform DNS resolution automatically:

```lua
-- Works with domain names
ping.up("google.com")
ping.send("api.github.com")
ping.port("servidor.local", 443)

-- Works with IP addresses
ping.up("8.8.8.8")
ping.send("192.168.1.1")
ping.port("10.0.0.5", 22)
```

### IPv4 and IPv6 Support

The module automatically detects the address type:

```lua
-- IPv4
ping.up("8.8.8.8")

-- IPv6
ping.up("2001:4860:4860::8888")

-- Domain name (resolved to IPv4 or IPv6)
ping.up("google.com")
```

### Configurable Timeout

Each function allows configuring an individual timeout:

```lua
-- Short timeout for local networks
ping.up("router.local", 3, 24, 1)  -- 1 second

-- Long timeout for high-latency networks
ping.up("servidor.remoto", 3, 24, 10)  -- 10 seconds

-- Port-specific timeout
ping.port("database.remoto", 5432, 3, 5)  -- 5 seconds
```