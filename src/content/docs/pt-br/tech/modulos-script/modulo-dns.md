---
title: "Módulo DNS"
---

O módulo **DNS** fornece funções para testar a performance e disponibilidade de servidores DNS. Este módulo é útil para monitoramento de infraestrutura de DNS, diagnóstico de problemas de resolução de nomes e medição de latência em consultas DNS.

## Funções Disponíveis

### 1. `dns.ping(server, domain)`

Realiza uma consulta DNS a um servidor específico e mede o tempo de resposta (RTT - Round Trip Time).

#### Parâmetros:

- **server** (string): Endereço do servidor DNS a testar (pode ser IP ou nome de domínio)

- **domain** (string): Domínio a ser consultado no servidor DNS

#### Retorno:

- **número**: Tempo de resposta em milissegundos (latência DNS)

#### Comportamento:

1. Resolve o endereço do servidor DNS (se for um nome de domínio)

2. Conecta ao servidor DNS na porta 53 (UDP)

3. Realiza uma consulta do tipo A para o domínio especificado

4. Mede o tempo entre o envio da consulta e o recebimento da resposta

5. Retorna o tempo em milissegundos

#### Exemplo de Uso:

```lua
-- Testar latência do DNS do Google
local latencia = dns.ping("8.8.8.8", "google.com")
-- latencia = 25 (exemplo: 25 milissegundos)

-- Testar DNS público do Cloudflare
local latencia_cf = dns.ping("1.1.1.1", "github.com")
-- latencia_cf = 30 (exemplo)

-- Testar servidor DNS por nome
local latencia_local = dns.ping("dns.local", "servidor.producao")
-- Testa o servidor DNS interno "dns.local"

-- Comparar múltiplos servidores DNS
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

## Informações Adicionais

### Resolução Automática do Servidor DNS

A função `dns.ping` resolve automaticamente o nome do servidor DNS se fornecido como domínio:

```lua
-- Funciona com IP
dns.ping("8.8.8.8", "google.com")

-- Funciona com nome de domínio (será resolvido primeiro)
dns.ping("dns.google", "exemplo.com")
dns.ping("one.one.one.one", "exemplo.com")  -- Cloudflare DNS
```

### Consulta do Tipo A

A função sempre realiza consultas do tipo A (IPv4).

### Protocolo UDP

As consultas são realizadas via UDP na porta 53, que é o protocolo padrão para consultas DNS.

## Exemplo de uso

### Teste de Propagação DNS

```lua
-- Verificar se um domínio está resolvendo corretamente em diferentes servidores
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