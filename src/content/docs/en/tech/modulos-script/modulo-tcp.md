---
title: "TCP Module"
---

This module provides functionality for TCP and TCP+TLS connections from Lua scripts. It supports communication with raw sockets, reading/writing strings, JSON and size-prefixed JSON packets.

The **tcp** module provides:

- Simple TCP connections with configurable timeout

- TLS connections

- Reading and writing simple strings

- Reading and writing JSON

- Reading and writing size-prefixed JSON packets (for safe binary communication)

- Automatic DNS resolution for TLS connections

## Available Functions

### `tcp.connect(host, port, [timeout_secs])`

Establishes a simple TCP connection to a remote server.

**Parameters**:

- `host` (string): Host address or server IP

- `port` (number): TCP port to connect to

- `timeout_secs` (number, optional): Timeout in seconds (default: 5)

**Return value**:

- A `Connection` object that can be used for reading/writing

- Throws an error on failure or timeout

**Example**:

```lua
-- Connect to a server on port 8080 with a 10-second timeout
local conn = tcp.connect("servidor.exemplo.com", 8080, 10)

-- Connect with default timeout (5 seconds)
local conn2 = tcp.connect("192.168.1.100", 3000)
```

### `tcp.connect_tls(host, port, [timeout_secs])`

Establishes a TLS (SSL) connection to a remote server.

**Parameters**:

- `host` (string): Server host address

- `port` (number): TLS port to connect to

- `timeout_secs` (number, optional): Timeout in seconds (default: 5)

**Return value**:

- A `TlsConnection` object that can be used for reading/writing

- Throws an error on failure or timeout

**Example**:

```lua
-- Connect via TLS on port 443
local conn = tcp.connect_tls("api.exemplo.com", 443)

-- Connect with custom timeout
local conn2 = tcp.connect_tls("servidor-seguro.com", 8443, 15)
```

### `tcp.send(data)`

Sends data over the last TCP connection opened with the `connect()` function. This function is kept for backward compatibility. For greater clarity and control, prefer the form `local conn = connect("host", porta)` and use the methods of the returned connection object (eg: `conn:write_json_packet()`).

**Parameters**:

- `data` (string): Data to send

**Return value**:

- `nil` on success

- Throws an error if there is no active connection

**Note**: This function uses the last TCP connection opened with the `connect()` function. It is useful for simple scripts that maintain a single connection.

**Example**:

```lua
-- Primeiro estabelece uma conexão
local conn = tcp.connect("servidor.exemplo.com", 8080)

-- Envia dados
send("GET / HTTP/1.1\r\nHost: servidor.exemplo.com\r\n\r\n")
```

### `tcp.recv()`

Receives data from the last TCP connection opened with the `connect()` function and stored in the Lua registry. This function is kept for backward compatibility. For greater clarity and control, prefer the form `local conn = connect("host", porta)` and use the methods of the returned connection object (eg: `conn:read_str()` or `conn:read_json_packet()`).

**Parameters**:

- None

**Return value**:

- `string` with the received data

- Throws an error if there is no active connection

**Note**:

- This function uses the last TCP connection opened with the `connect()` function. It is useful for simple scripts that maintain a single connection.

- Reads up to 8192 bytes per call. For full reads, it may be necessary to call multiple times.

**Example**:

```lua
-- Recebe resposta
local resposta = tcp.recv()
print("Resposta recebida:", resposta)
```

## Connection Object Methods

The objects returned by `connect()` and `connect_tls()` have the following methods:

### `conn:read_str()`

Reads a complete string from the socket until EOF.

**Return value**:

- `string` with the data read

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

- Lua value decoded from the JSON

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

Reads a size-prefixed JSON packet (binary format).

**Packet format**:

1. 4 bytes (uint32): Size of the JSON data

2. N bytes: Serialized JSON data

**Size limit**: 512 KB (512,000 bytes)

**Return value**:

- Lua value decoded from the JSON

- Throws an error if the packet is too large or the JSON is invalid

**Example**:

```lua
local conn = tcp.connect("servidor-binario.com", 9000)
local pacote = conn:read_json_packet()
print("Pacote recebido:", pacote)
```

### `conn:write_json_packet(packet)`

Writes a size-prefixed JSON packet (binary format).

**Parameters**:

- `packet` (any Lua value): Data to be serialized as JSON

**Return value**:

- `nil` on success

- Throws an error on serialization or write failure

**Example**:

```lua
local conn = connect("servidor-binario.com", 9000)

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

The `connect_tls()` function automatically resolves the host name to an IP address before establishing the connection.

### Maximum Packet Size

Size-prefixed JSON packets have a 512 KB limit to prevent denial-of-service attacks.

## Usage Examples

### Simple HTTP Communication

```lua
function fazer_requisicao_http(host, porta, caminho)
    local conn = connect(host, porta, 10)

    -- Send HTTP request
    local requisicao = string.format(
        "GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n",
        caminho, host
    )

    -- Use the send method (connection is in the registry)
    send(requisicao)

    -- Read response
    local resposta = recv()

    -- Extract response body (simplified)
    local corpo = resposta:match("\r\n\r\n(.+)$")

    return corpo
end
```

### JSON API Client

```lua
function consultar_api_json(endpoint, dados)
    local conn = connect_tls("api.exemplo.com", 443)

    -- Send data as a JSON packet
    conn:write_json_packet({
        endpoint = endpoint,
        dados = dados,
        timestamp = os.time()
    })

    -- Wait for response
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
    local sucesso, conn = pcall(connect, host, porta, 5)

    if sucesso then
        local tempo_resposta = os.time() - inicio

        -- Test basic communication
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
        erro = conn  -- conn contains the error message when pcall fails
    }
end
```

### Bidirectional Communication

```lua
function chat_client(host, porta)
    local conn = connect(host, porta)

    -- Thread to receive messages
    local function receber_mensagens()
        while true do
            local mensagem = conn:read_json_packet()
            print("Recebido:", mensagem.texto)
        end
    end

    -- Thread to send messages (simplified)
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
    -- This is a simplification for demonstration
end
```