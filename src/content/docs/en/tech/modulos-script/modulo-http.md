---
title: "HTTP Module"
---

This module provides functions to perform HTTP requests from Lua scripts. The functions return a table with the request results.

## Available Functions

### `http.request(method, url, body, headers, options)`

Generic function to perform HTTP requests with any method.

**Parameters**:

- `method` (string): HTTP method (GET, POST, PUT, DELETE, PATCH, HEAD)

- `url` (string): Endpoint URL

- `body` (string, optional): Request body

- `headers` (table, optional): HTTP headers as key-value pairs

- `options` (table, optional): Additional request options

**Available options**:

- `verify` (boolean): Verify SSL certificates (default: true)

- `charset` (string): Charset for decoding the response (default: "utf-8")

**Security Warning**:

Disabling SSL verification (`verify = false`) exposes the connection to "man-in-the-middle" attacks and should be used **only** in controlled development or testing environments. Never use this option in production with real servers or sensitive data.

**Return value**:

Returns a table with:

- `status` (number): HTTP status code

- `body` (string): Response body

**Example**:

```lua
local resultado = http.request("POST", "https://api.exemplo.com/dados",
    '{"nome": "teste", "valor": 123}',
    {["Content-Type"] = "application/json"},
    {verify = true, charset = "utf-8"}
)

print("Status:", resultado.status)
print("Resposta:", resultado.body)
```

### `http.get(url, body, headers, options)`

Performs an HTTP GET request.

**Parameters**:

- `url` (string): Endpoint URL

- `body` (string, optional): Request body (rare for GET, but supported)

- `headers` (table, optional): HTTP headers

- `options` (table, optional): Additional options

**Example**:

```lua
local resultado = http.get("https://api.exemplo.com/usuarios/1",
    nil,
    {["Authorization"] = "Bearer token123"},
    {verify = true}
)

if resultado.status == 200 then
    print("Dados recebidos:", resultado.body)
else
    print("Erro:", resultado.status)
end
```

### `http.post(url, body, headers, options)`

Performs an HTTP POST request.

**Parameters**:

- `url` (string): Endpoint URL

- `body` (string): Request body (usually JSON or form data)

- `headers` (table, optional): HTTP headers

- `options` (table, optional): Additional options

**Example**:

```lua
local dados_json = '{"nome": "Novo Usuário", "email": "usuario@exemplo.com"}'

local resultado = http.post("https://api.exemplo.com/usuarios",
    dados_json,
    {
        ["Content-Type"] = "application/json",
        ["Authorization"] = "Bearer token123"
    }
)

if resultado.status == 201 then
    print("Usuário criado com sucesso!")
    print("Resposta:", resultado.body)
else
    print("Falha ao criar usuário. Status:", resultado.status)
end
```

### `http.put(url, body, headers, options)`

Performs an HTTP PUT request to update resources.

**Parameters**:

- `url` (string): Endpoint URL

- `body` (string): Request body with updated data

- `headers` (table, optional): HTTP headers

- `options` (table, optional): Additional options

**Example**:

```lua
local dados_atualizados = '{"nome": "Usuário Atualizado", "ativo": true}'

local resultado = http.put("https://api.exemplo.com/usuarios/1",
    dados_atualizados,
    {
        ["Content-Type"] = "application/json",
        ["Authorization"] = "Bearer token123"
    }
)

if resultado.status == 200 then
    print("Usuário atualizado com sucesso!")
else
    print("Falha na atualização. Status:", resultado.status)
end
```

### `http.delete(url, body, headers, options)`

Performs an HTTP DELETE request to remove resources.

**Parameters**:

- `url` (string): Endpoint URL

- `body` (string, optional): Request body (optional for DELETE)

- `headers` (table, optional): HTTP headers

- `options` (table, optional): Additional options

**Example**:

```lua
local resultado = http.delete("https://api.exemplo.com/usuarios/1",
    nil,
    {["Authorization"] = "Bearer token123"}
)

if resultado.status == 204 then
    print("Usuário removido com sucesso!")
else
    print("Falha ao remover usuário. Status:", resultado.status)
end
```

### `http.head(url, body, headers, options)`

Performs an HTTP HEAD request to obtain headers only.

**Parameters**:

- `url` (string): Endpoint URL

- `body` (string, optional): Request body

- `headers` (table, optional): HTTP headers

- `options` (table, optional): Additional options

**Example**:

```lua
local resultado = http.head("https://api.exemplo.com/usuarios/1",
    nil,
    {["Authorization"] = "Bearer token123"}
)

print("Status da verificação:", resultado.status)
-- The HEAD response usually has no body
```

## Additional Information

### Automatic URL

If the URL does not contain a scheme (like `http://` or `https://`), the system automatically adds `http://` as a prefix.

```lua
-- These two calls are equivalent:
local r1 = http.get("api.exemplo.com/dados")
local r2 = http.get("http://api.exemplo.com/dados")
```

### SSL Verification

By default, SSL certificate verification is enabled. To disable (useful in development/testing environments):

**Attention**: Disabling SSL verification (`verify = false`) exposes the connection to "man-in-the-middle" attacks and should be used **only** in controlled development or testing environments. Never use this option in production with real servers or sensitive data.

```lua
local resultado = get("https://servidor-local.com",
    nil,
    nil,
    {verify = false}
)
```

### Charsets

It is possible to specify a different charset to decode the response:

```lua
local resultado = get("https://api.exemplo.com/dados",
    nil,
    nil,
    {charset = "iso-8859-1"}
)
```

## Usage Example

```lua
-- API monitoring example
function verificar_saude_api()
    local resultado = http.get("https://api.exemplo.com/health",
        nil,
        {["User-Agent"] = "MonstaAgent/1.0"}
    )

    if resultado.status == 200 then
        local dados = resultado.body
        -- Process JSON response if necessary
        print("API está saudável")
        return true
    else
        print("API com problemas. Status:", resultado.status)
        return false
    end
end
```

## Important Notes

:::note
1. **Timeout**: The default timeout is the global timeout configured for Lua scripts in the system.

2. **Performance**: Use persistent connections when making multiple requests to the same server.

3. **Security**: Never disable SSL verification in production without necessity.
:::