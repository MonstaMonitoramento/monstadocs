---
title: "Módulo WS"
---

El módulo **ws** proporciona funcionalidades para comunicación bidireccional en tiempo real a través del protocolo WebSocket. Este módulo es útil para scripts que necesiten conectarse a servicios que utilizan WebSockets.

**Características principales**:

- Conexión WebSocket asíncrona

- Envío y recepción de mensajes de texto

- Soporte para URLs seguras (wss://) y no seguras (ws://)

- Timeout implícito basado en el sistema

**Protocolo WebSocket**:

- Protocolo de comunicación full-duplex sobre una única conexión TCP

- Ideal para aplicaciones en tiempo real

- Soportado por la mayoría de los navegadores y servidores modernos

- Menor overhead en comparación con el polling HTTP

## Funciones disponibles

### 1. `ws.send_recv(url, dados)`

Establece una conexión WebSocket, envía un mensaje y espera una respuesta.

#### Parámetros:

- **url** (string): URL del servidor WebSocket (ej: "ws://exemplo.com/socket", "wss://exemplo.com/ws")

- **dados** (string): Mensaje de texto que se enviará al servidor

#### Retorno:

- **string**: Respuesta de texto recibida del servidor WebSocket

#### Comportamiento:

1. Establece conexión WebSocket con el servidor especificado

2. Envía el mensaje de texto proporcionado

3. Espera una respuesta del servidor

4. Devuelve el primer mensaje de texto recibido

5. Cierra la conexión después de recibir la respuesta

6. Lanza un error si recibe un mensaje binario o si no hay respuesta

#### Errores comunes:

- `"ws binary messages not supported"` - Servidor envió mensaje binario (no soportado)

- `"no response from web socket"` - Servidor no respondió

- Errores de conexión (servidor fuera de línea, URL inválida, etc.)

#### Ejemplo de uso:

```lua
-- Conexión básica con servidor WebSocket
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

-- Com tratamento de erro
local function enviar_com_tratamento(url, dados)
    local ok, resposta = pcall(ws.send_recv, url, dados)
    if ok then
        return resposta
    else
        log.error("Erro no WebSocket:", resposta)
        return nil
    end
end

-- Testar múltiplos servidores
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

## Información adicional

### Conexión segura (wss://):

```lua
-- O módulo suporta tanto ws:// quanto wss://
local conexoes = {
    "ws://localhost:8080/ws",      -- Não seguro (HTTP)
    "wss://servidor.com/ws",       -- Seguro (HTTPS)
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

### Solo mensajes de texto:

```lua
-- O módulo só suporta mensagens de texto
-- Mensagens binárias retornam erro

local function enviar_dados_seguros(url, dados)
    -- Converter dados para JSON (texto)
    local dados_json = json.encode(dados)

    local resposta = ws.send_recv(url, dados_json)

    -- Parsear resposta JSON
    return json.decode(resposta)
end

-- Exemplo com dados complexos
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