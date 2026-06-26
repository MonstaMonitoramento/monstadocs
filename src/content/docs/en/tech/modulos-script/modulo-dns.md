---
title: "DNS Module"
---

The **DNS** module provides functions to test the performance and availability of DNS servers. This module is useful for monitoring DNS infrastructure, diagnosing name resolution issues, and measuring latency in DNS queries.

## Available Functions

### 1. `dns.ping(server, domain)`

Performs a DNS query to a specific server and measures the response time (RTT - Round Trip Time).

#### Parameters:

- **server** (string): Address of the DNS server to test (can be an IP or domain name)

- **domain** (string): Domain to be queried on the DNS server

#### Return:

- **number**: Response time in milliseconds (DNS latency)

#### Behavior:

1. Resolves the DNS server address (if it's a domain name)

2. Connects to the DNS server on port 53 (UDP)

3. Performs an A-type query for the specified domain

4. Measures the time between sending the query and receiving the response

5. Returns the time in milliseconds

#### Usage Example:

```lua
-- Test DNS latency of Google DNS
local latencia = dns.ping("8.8.8.8", "google.com")
-- latencia = 25 (example: 25 milliseconds)

-- Test Cloudflare public DNS
local latencia_cf = dns.ping("1.1.1.1", "github.com")
-- latencia_cf = 30 (example)

-- Test DNS server by name
local latencia_local = dns.ping("dns.local", "servidor.producao")
-- Tests the internal DNS server "dns.local"

-- Compare multiple DNS servers
local servidores_dns = {
    {nome = "Google DNS", endereco = "8.8.8.8"},
    {nome = "Cloudflare", endereco = "1.1.1.1"},
    {nome = "Quad9", endereco = "9.9.9.9"},
    {nome = "DNS Local", endereco = "192.168.1.1"}
}

for _, dns in ipairs(servidores_dns) do
    local latencia = dns.ping(dns.endereco, "exemplo.com")
    print(dns.nome .. ": " .. latencia .. "ms")
end
```

## Additional Information

### Automatic DNS Server Resolution

The function `dns.ping` automatically resolves the DNS server name if provided as a domain:

```lua
-- Works with IP
dns.ping("8.8.8.8", "google.com")

-- Works with domain name (will be resolved first)
dns.ping("dns.google", "exemplo.com")
dns.ping("one.one.one.one", "exemplo.com")  -- Cloudflare DNS
```

### A-Type Query

The function always performs A-type queries (IPv4).

### UDP Protocol

Queries are performed via UDP on port 53, which is the standard protocol for DNS queries.

## Example Usage

### DNS Propagation Test

```lua
-- Check if a domain is resolving correctly across different servers
local function testar_propagacao_dns(dominio, ip_esperado)
    local servidores = {
        "8.8.8.8",      -- Google
        "1.1.1.1",      -- Cloudflare
        "9.9.9.9",      -- Quad9
        "208.67.222.222", -- OpenDNS
        "64.6.64.6",    -- Verisign
    }

    local resultados = {}
    for _, server in ipairs(servidores) do
        local ok, latencia = pcall(dns.ping, server, dominio)

        resultados[server] = {
            latencia = ok and latencia or nil,
            acessivel = ok,
            erro = not ok and latencia or nil
        }
    end

    return resultados
end
```