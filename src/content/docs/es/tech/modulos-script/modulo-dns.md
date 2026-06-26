---
title: "Módulo DNS"
---

El módulo **DNS** proporciona funciones para probar el rendimiento y la disponibilidad de servidores DNS. Este módulo es útil para el monitoreo de la infraestructura DNS, el diagnóstico de problemas de resolución de nombres y la medición de la latencia en consultas DNS.

## Funciones Disponibles

### 1. `dns.ping(server, domain)`

Realiza una consulta DNS a un servidor específico y mide el tiempo de respuesta (RTT - Round Trip Time).

#### Parámetros:

- **server** (string): Dirección del servidor DNS a probar (puede ser IP o nombre de dominio)

- **domain** (string): Dominio que se consultará en el servidor DNS

#### Retorno:

- **número**: Tiempo de respuesta en milisegundos (latencia DNS)

#### Comportamiento:

1. Resuelve la dirección del servidor DNS (si es un nombre de dominio)

2. Se conecta al servidor DNS en el puerto 53 (UDP)

3. Realiza una consulta de tipo A para el dominio especificado

4. Mide el tiempo entre el envío de la consulta y la recepción de la respuesta

5. Devuelve el tiempo en milisegundos

#### Ejemplo de Uso:

```lua
-- Probar la latencia del DNS de Google
local latencia = dns.ping("8.8.8.8", "google.com")
-- latencia = 25 (ejemplo: 25 milisegundos)

-- Probar DNS público de Cloudflare
local latencia_cf = dns.ping("1.1.1.1", "github.com")
-- latencia_cf = 30 (ejemplo)

-- Probar servidor DNS por nombre
local latencia_local = dns.ping("dns.local", "servidor.producao")
-- Prueba el servidor DNS interno "dns.local"

-- Comparar múltiples servidores DNS
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

## Información Adicional

### Resolución Automática del Servidor DNS

La función `dns.ping` resuelve automáticamente el nombre del servidor DNS si se proporciona como dominio:

```lua
-- Funciona con IP
dns.ping("8.8.8.8", "google.com")

-- Funciona con nombre de dominio (se resolverá primero)
dns.ping("dns.google", "exemplo.com")
dns.ping("one.one.one.one", "exemplo.com")  -- DNS de Cloudflare
```

### Consulta de Tipo A

La función siempre realiza consultas de tipo A (IPv4).

### Protocolo UDP

Las consultas se realizan vía UDP en el puerto 53, que es el protocolo estándar para consultas DNS.

## Ejemplo de uso

### Prueba de Propagación DNS

```lua
-- Comprobar si un dominio se resuelve correctamente en diferentes servidores
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