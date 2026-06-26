---
title: "Módulo TCP"
---

Este módulo proporciona funcionalidades para conexiones TCP y TCP+TLS desde scripts Lua. Ofrece soporte para comunicación con sockets crudos, lectura/escritura de cadenas, JSON y paquetes JSON con tamaño prefijado.

El módulo **tcp** permite:

- Conexiones TCP simples con timeout configurable

- Conexiones TLS

- Lectura y escritura de cadenas simples

- Lectura y escritura de JSON

- Lectura y escritura de paquetes JSON con tamaño prefijado (para comunicación binaria segura)

- Resolución DNS automática para conexiones TLS

## Funciones Disponibles

### `tcp.connect(host, port, [timeout_secs])`

Establece una conexión TCP simple con un servidor remoto.

**Parámetros**:

- `host` (string): Dirección del host o IP del servidor

- `port` (number): Puerto TCP para la conexión

- `timeout_secs` (number, opcional): Timeout en segundos (por defecto: 5)

**Valor de retorno**:

- Objeto `Connection` que puede usarse para lectura/escritura

- Lanza error en caso de fallo o timeout

**Ejemplo**:

```lua
-- Conectar a un servidor en el puerto 8080 con timeout de 10 segundos
local conn = tcp.connect("servidor.exemplo.com", 8080, 10)

-- Conectar con timeout predeterminado (5 segundos)
local conn2 = tcp.connect("192.168.1.100", 3000)
```

### `tcp.connect_tls(host, port, [timeout_secs])`

Establece una conexión TLS (SSL) con un servidor remoto.

**Parámetros**:

- `host` (string): Dirección del host del servidor

- `port` (number): Puerto TLS para la conexión

- `timeout_secs` (number, opcional): Timeout en segundos (por defecto: 5)

**Valor de retorno**:

- Objeto `TlsConnection` que puede usarse para lectura/escritura

- Lanza error en caso de fallo o timeout

**Ejemplo**:

```lua
-- Conectar vía TLS en el puerto 443
local conn = tcp.connect_tls("api.exemplo.com", 443)

-- Conectar con timeout personalizado
local conn2 = tcp.connect_tls("servidor-seguro.com", 8443, 15)
```

### `tcp.send(data)`

Envía datos a través de la última conexión TCP abierta con la función `connect()`. Esta función se mantiene para compatibilidad con versiones anteriores. Para mayor claridad y control, prefiera la forma `local conn = connect("host", porta)` y use los métodos del objeto de conexión retornado (ej: `conn:write_json_packet()`).

**Parámetros**:

- `data` (string): Datos a enviar

**Valor de retorno**:

- `nil` en caso de éxito

- Lanza error si no hay conexión activa

**Nota**: Esta función usa la última conexión TCP abierta con la función `connect()`. Es útil para scripts simples que mantienen una única conexión.

**Ejemplo**:

```lua
-- Primeiro estabelece uma conexão
local conn = tcp.connect("servidor.exemplo.com", 8080)

-- Envia dados
send("GET / HTTP/1.1\r\nHost: servidor.exemplo.com\r\n\r\n")
```

### `tcp.recv()`

Recibe datos de la última conexión TCP abierta con la función `connect()` y almacenada en el registro Lua. Esta función se mantiene para compatibilidad con versiones anteriores. Para mayor claridad y control, prefiera la forma `local conn = connect("host", porta)` y use los métodos del objeto de conexión retornado (ej: `conn:read_str()` o `conn:read_json_packet()`).

**Parámetros**:

- Ninguno

**Valor de retorno**:

- `string` con los datos recibidos

- Lanza error si no hay conexión activa

**Nota**:

- Esta función usa la última conexión TCP abierta con la función `connect()`. Es útil para scripts simples que mantienen una única conexión.

- Lee hasta 8192 bytes por llamada. Para lectura completa, puede ser necesario llamar múltiples veces.

**Ejemplo**:

```lua
-- Recebe resposta
local resposta = tcp.recv()
print("Resposta recebida:", resposta)
```

## Métodos de los Objetos Connection

Los objetos retornados por `connect()` y `connect_tls()` poseen los siguientes métodos:

### `conn:read_str()`

Lee una cadena completa del socket hasta EOF.

**Valor de retorno**:

- `string` con los datos leídos

- Lanza error en caso de fallo de lectura

**Ejemplo**:

```lua
local conn = tcp.connect("servidor.exemplo.com", 8080)
local dados = conn:read_str()
print("Dados recebidos:", dados)
```

### `conn:read_json()`

Lee una cadena del socket e interpreta su contenido como JSON.

**Valor de retorno**:

- Valor Lua decodificado desde el JSON

- Lanza error si los datos no son JSON válido

**Ejemplo**:

```lua
local conn = tcp.connect("api.exemplo.com", 3000)
local dados_json = conn:read_json()

-- Acceder a los datos decodificados
print("Status:", dados_json.status)
print("Mensagem:", dados_json.message)
```

### `conn:read_json_packet()`

Lee un paquete JSON con tamaño prefijado (formato binario).

**Formato del paquete**:

1. 4 bytes (uint32): Tamaño de los datos JSON

2. N bytes: Datos JSON serializados

**Límite de tamaño**: 512KB (512.000 bytes)

**Valor de retorno**:

- Valor Lua decodificado desde el JSON

- Lanza error si el paquete es demasiado grande o JSON inválido

**Ejemplo**:

```lua
local conn = tcp.connect("servidor-binario.com", 9000)
local pacote = conn:read_json_packet()
print("Pacote recebido:", pacote)
```

### `conn:write_json_packet(packet)`

Escribe un paquete JSON con tamaño prefijado (formato binario).

**Parámetros**:

- `packet` (cualquier valor Lua): Datos a serializar como JSON

**Valor de retorno**:

- `nil` en caso de éxito

- Lanza error en caso de fallo de serialización o escritura

**Ejemplo**:

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

## Información Adicional

### Timeout Configurable

Todas las funciones de conexión aceptan timeout personalizado. Si no se especifica, usan 5 segundos por defecto.

### Resolución DNS Automática

La función `connect_tls()` resuelve automáticamente el nombre del host a una dirección IP antes de establecer la conexión.

### Tamaño Máximo de Paquete

Los paquetes JSON con tamaño prefijado tienen un límite de 512KB para prevenir ataques de denegación de servicio.

## Ejemplos de Uso

### Comunicación HTTP Simple

```lua
function fazer_requisicao_http(host, porta, caminho)
    local conn = connect(host, porta, 10)

    -- Enviar petición HTTP
    local requisicao = string.format(
        "GET %s HTTP/1.1\r\nHost: %s\r\nConnection: close\r\n\r\n",
        caminho, host
    )

    -- Usar el método send (la conexión está en el registro)
    send(requisicao)

    -- Leer respuesta
    local resposta = recv()

    -- Extraer cuerpo de la respuesta (simplificado)
    local corpo = resposta:match("\r\n\r\n(.+)$")

    return corpo
end
```

### Cliente de API JSON

```lua
function consultar_api_json(endpoint, dados)
    local conn = connect_tls("api.exemplo.com", 443)

    -- Enviar datos como paquete JSON
    conn:write_json_packet({
        endpoint = endpoint,
        dados = dados,
        timestamp = os.time()
    })

    -- Esperar respuesta
    local resposta = conn:read_json_packet()

    return resposta
end

-- Ejemplo de uso
local resultado = consultar_api_json("/usuarios", {id = 123})
if resultado.success then
    print("Usuário:", resultado.usuario.nome)
end
```

### Monitorización de Servicio TCP

```lua
function verificar_servico_tcp(host, porta)
    local inicio = os.time()
    local sucesso, conn = pcall(connect, host, porta, 5)

    if sucesso then
        local tempo_resposta = os.time() - inicio

        -- Probar comunicación básica
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
        erro = conn  -- conn contiene el mensaje de error cuando pcall falla
    }
end
```

### Comunicación Bidireccional

```lua
function chat_client(host, porta)
    local conn = connect(host, porta)

    -- Hilo para recibir mensajes
    local function receber_mensagens()
        while true do
            local mensagem = conn:read_json_packet()
            print("Recebido:", mensagem.texto)
        end
    end

    -- Hilo para enviar mensajes (simplificado)
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

    -- En un entorno real, esto se haría con corutinas
    -- Esta es una simplificación para demostración
end
```