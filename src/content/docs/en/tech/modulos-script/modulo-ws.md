---
title: "WS Module"
---

The **ws** module provides functionality for real-time bidirectional communication over the WebSocket protocol. This module is useful for scripts that need to connect to services using WebSockets.

**Key features**:

- Asynchronous WebSocket connection

- Sending and receiving text messages

- Support for secure (wss://) and non-secure (ws://) URLs

- Implicit timeout based on the system

**WebSocket Protocol**:

- Full-duplex communication protocol over a single TCP connection

- Ideal for real-time applications

- Supported by most modern browsers and servers

- Lower overhead compared to HTTP polling

## Available Functions

### 1. `ws.send_recv(url, dados)`

Establishes a WebSocket connection, sends a message and waits for a response.

#### Parameters:

- **url** (string): WebSocket server URL (ex: "ws://exemplo.com/socket", "wss://exemplo.com/ws")

- **dados** (string): Text message to send to the server

#### Return:

- **string**: Text response received from the WebSocket server

#### Behavior:

1. Establishes a WebSocket connection to the specified server

2. Sends the provided text message

3. Waits for a response from the server

4. Returns the first text message received

5. Closes the connection after receiving the response

6. Throws an error if a binary message is received or if there is no response

#### Common Errors:

- `"ws binary messages not supported"` - Server sent a binary message (not supported)

- `"no response from web socket"` - Server did not respond

- Connection errors (server offline, invalid URL, etc.)

#### Usage Example:

```lua
-- Basic connection to WebSocket server
local url = "ws://echo.websocket.org"
local mensagem = "Olá, WebSocket!"
local resposta = ws.send_recv(url, mensagem)
print("Resposta do servidor:", resposta)
-- Saída: "Olá, WebSocket!" (servidor echo)

-- Conexão segura (wss://)
local url_segura = "wss://servidor.producao.com/ws"
local dados = json.encode({acao = "ping", timestamp = now()})
local resposta = ws.send_recv(url_segura, dados)
print("Resposta segura:", resposta)

-- With error handling
local function enviar_com_tratamento(url, dados)
    local ok, resposta = pcall(ws.send_recv, url, dados)
    if ok then
        return resposta
    else
        log.error("Erro no WebSocket:", resposta)
        return nil
    end
end

-- Test multiple servers
local servidores = {
    "ws://servidor1.com/ws",
    "ws://servidor2.com/socket",
    "ws://backup.servidor.com/ws"
}

for _, servidor in ipairs(servidores) do
    local resposta = enviar_com_tratamento(servidor, "ping")
    if resposta then
        print("Servidor", servidor, "respondendo")
        break
    end
end
```

## Additional Information

### Secure Connection (wss://):

```lua
-- The module supports both ws:// and wss://
local conexoes = {
    "ws://localhost:8080/ws",      -- Not secure (HTTP)
    "wss://servidor.com/ws",       -- Secure (HTTPS)
    "ws://192.168.1.100:3000/ws",  -- Local network
}

for _, url in ipairs(conexoes) do
    local ok, resposta = pcall(ws.send_recv, url, "ping")
    if ok then
        print("Conexão bem-sucedida:", url)
    else
        print("Falha na conexão:", url, "-", resposta)
    end
end
```

### Text Messages Only:

```lua
-- The module only supports text messages
-- Binary messages return an error

local function enviar_dados_seguros(url, dados)
    -- Convert data to JSON (text)
    local dados_json = json.encode(dados)

    local resposta = ws.send_recv(url, dados_json)

    -- Parse JSON response
    return json.decode(resposta)
end

-- Example with complex data
local dados_complexos = {
    usuarios = {
        {id = 1, nome = "Alice", ativo = true},
        {id = 2, nome = "Bob", ativo = false}
    },
    metricas = {
        cpu = 45.6,
        memoria = 78.3,
        timestamp = now()
    }
}

local resposta = enviar_dados_seguros("wss://api.empresa.com/ws", dados_complexos)
```