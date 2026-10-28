---
title: "TCP Module"
---

This module provides functionality for TCP and TCP+TLS connections from Lua scripts. It supports communication with raw sockets, reading/writing strings, JSON, and length-prefixed JSON packets.

The **tcp** module allows:

- Simple TCP connections with configurable timeout

- TLS connections

- Reading and writing simple strings

- Reading and writing JSON

- Reading and writing length-prefixed JSON packets (for safe binary communication)

- Automatic DNS resolution for TLS connections

## Available Functions

### `tcp.connect(host, port, [timeout_secs])`

Establishes a simple TCP connection to a remote server.

**Parameters**:

- `host` (string): Hostname or IP address of the server

- `port` (number): TCP port to connect to

- `timeout_secs` (number, optional): Timeout in seconds (default: 5)

**Return value**:

- `Connection` object that can be used for reading/writing

- Throws an error on failure or timeout

**Example**:

```lua
-- Conectar a um servidor na porta 8080 com timeout de 10 segundos
local conn = tcp.connect("servidor.exemplo.com", 8080, 10)

-- Conectar com timeout padrão (5 segundos)
local conn2 = tcp.connect("192.168.1.100", 3000)
```

### `tcp.connect_tls(host, port, [timeout_secs])`

Establishes a TLS (SSL) connection to a remote server.

**Parameters**:

- `host` (string): Hostname of the server

- `port` (number): TLS port to connect to

- `timeout_secs` (number, optional): Timeout in seconds (default: 5)

**Return value**:

- `TlsConnection` object that can be used for reading/writing

- Throws an error on failure or timeout

**Example**:

```lua
-- Conectar via TLS na porta 443
local conn = tcp.connect_tls("api.exemplo.com", 443)

-- Conectar com timeout personalizado
local conn2 = tcp.connect_tls("servidor-seguro.com", 8443, 15)
```

### `tcp.send(data)`

Sends data over the last TCP connection opened with the `connect()` function. This function is kept for backward compatibility. For clearer control, prefer the form `local conn = connect("host", port)` and use the methods of the returned connection object (e.g., `conn:write_json_packet()`).

**Parameters**:

- `data` (string): Data to send

**Return value**:

- `nil` on success

- Throws an error if there is no active connection

**Note**: This function uses the last TCP connection opened with `connect()`. It is useful for simple scripts that maintain a single connection.

**Example**:

```lua
-- Primeiro estabelece uma conexão
local conn = tcp.connect("servidor.exemplo.com", 8080)

-- Envia dados
send("GET / HTTP/1.1\r\nHost: servidor.exemplo.com\r\n\r\n")
```

### `tcp.recv()`

Receives data from the last TCP connection opened with `connect()` and stored in the Lua registry. This function is kept for backward compatibility. For clearer control, prefer the form `local conn = connect("host", port)` and use the methods of the returned connection object (e.g., `conn:read_str()` or `conn:read_json_packet()`).

**Parameters**:

- None

**Return value**:

- `string` with the received data

- Throws an error if there is no active connection

**Note**:

- This function uses the last TCP connection opened with `connect()`. It is useful for simple scripts that maintain a single connection.

- Reads up to 8192 bytes per call. For complete reads, multiple calls may be necessary.

**Example**:

```lua
-- Recebe resposta
local resposta = tcp.recv()
print("Resposta recebida:", resposta)
```

## Connection Object Methods

Objects returned by `connect()` and `connect_tls()` provide the following methods:

### `conn:read_str()`

Reads a complete string from the socket until EOF.

**Return value**:

- `string` with the read data

- Throws an error on read failure

**Example**:

```lua
local conn = tcp.connect("servidor.exemplo.com", 8080)
local dados = conn:read_str()
print("Dados recebidos:", dados)
```

### `conn:read_json()`

Reads a string from the socket and interprets it as JSON.

**Return value**:

- Lua value decoded from JSON

- Throws an error if the data is not valid JSON

**Example**:

```lua
local conn = tcp.connect("api.exemplo.com", 3000)
local dados_json = conn:read_json()

-- Acessar dados decodificados
print("Status:", dados_json.status)
print("Mensagem:", dados_json.message)
```

### `conn:read_json_packet()`

Reads a length-prefixed JSON packet (binary format).

**Packet format**:

1. 4 bytes (uint32): Size of the JSON data

2. N bytes: Serialized JSON data

**Size limit**: 512KB (512,000 bytes)

**Return value**:

- Lua value decoded from JSON

- Throws an error if the packet is too large or the JSON is invalid

**Example**:

```lua
local conn = tcp.connect("servidor-binario.com", 9000)
local pacote = conn:read_json_packet()
print("Pacote recebido:", pacote)
```

### `conn:write_json_packet(packet)`

Writes a length-prefixed JSON packet (binary format).

**Parameters**:

- `packet` (any Lua value): Data to be serialized as JSON

**Return value**:

- `nil` on success

- Throws an error on serialization or write failure

**Example**:

```lua
local conn = tcp.connect("servidor-binario.com", 9000)

-- Enviar um pacote JSON
local dados = {
    comando = "atualizar",
    id = 123,
    valores = {10, 20, 30}
}
conn:write_json_packet(dados)
```

## Additional Information

### Configurable Timeout

All connection functions accept a custom timeout. If not specified, 5 seconds is used by default.

### Automatic DNS Resolution

The `connect_tls()` function automatically resolves the hostname to an IP address before establishing the connection.

### Maximum Packet Size

Length-prefixed JSON packets have a 512KB limit to prevent denial-of-service attacks.

## Usage Examples

### Simple HTTP Communication

```lua
function fazer_requisicao_http(host, porta, caminho)
    local conn = tcp.connect(host, porta, 10)

    -- Enviar requisição HTTP
    local requisicao = string.format(
        "GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n",
        caminho, host
    )

    -- Usar o método send (conexão está no registro)
    tcp.send(requisicao)

    -- Ler resposta
    local resposta = tcp.recv()

    -- Extrair corpo da resposta (simplificado)
    local corpo = resposta:match("\r\n\r\n(.+)$")

    return corpo
end
```

### JSON API Client

```lua
function consultar_api_json(endpoint, dados)
    local conn = tcp.connect_tls("api.exemplo.com", 443)

    -- Enviar dados como pacote JSON
    conn:write_json_packet({
        endpoint = endpoint,
        dados = dados,
        timestamp = os.time()
    })

    -- Aguardar resposta
    local resposta = conn:read_json_packet()

    return resposta
end

-- Exemplo de uso
local resultado = consultar_api_json("/usuarios", {id = 123})
if resultado.success then
    print("Usuário:", resultado.usuario.nome)
end
```

### TCP Service Monitoring

```lua
function verificar_servico_tcp(host, porta)
    local inicio = os.time()
    -- with_coroutine aceita a função e seus argumentos, retornando (result, err)
    local conn, err = with_coroutine(tcp.connect, host, porta, 5)

    if not err and conn then
        local tempo_resposta = os.time() - inicio

        -- Testar comunicação básica
        conn:write_json_packet({ping = true})
        local resposta = conn:read_json_packet()

        if resposta and resposta.pong then
            return {
                status = "online",
                tempo_resposta = tempo_resposta,
                versao = resposta.versao
            }
        end
    end

    return {
        status = "offline",
        erro = err  -- err contém a mensagem de erro quando with_coroutine falha
    }
end
```

### Bidirectional Communication

```lua
function chat_client(host, porta)
    local conn = tcp.connect(host, porta)

    -- Thread para receber mensagens
    local function receber_mensagens()
        while true do
            local mensagem = conn:read_json_packet()
            print("Recebido:", mensagem.texto)
        end
    end

    -- Thread para enviar mensagens (simplificado)
    local function enviar_mensagens()
        while true do
            io.write("Digite mensagem: ")
            local texto = io.read()
            if texto == "sair" then break end

            conn:write_json_packet({
                tipo = "mensagem",
                texto = texto,
                timestamp = os.time()
            })
        end
    end

    -- Em um ambiente real, isso seria feito com corrotinas
    -- Esta é uma simplificação para demonstração
end
```