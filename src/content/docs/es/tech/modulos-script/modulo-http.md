---
title: "Módulo HTTP"
---

Este módulo proporciona funciones para realizar solicitudes HTTP desde scripts Lua. Las funciones devuelven una tabla con los resultados de la solicitud.

## Funciones Disponibles

### `http.request(method, url, body, headers, options)`

Función genérica para realizar solicitudes HTTP con cualquier método.

**Parámetros**:

- `method` (string): Método HTTP (GET, POST, PUT, DELETE, PATCH, HEAD)

- `url` (string): URL del endpoint

- `body` (string, opcional): Cuerpo de la solicitud

- `headers` (tabela, opcional): Encabezados HTTP como pares clave-valor

- `options` (tabela, opcional): Opciones adicionales de la solicitud

**Opciones disponibles**:

- `verify` (boolean): Verificar certificados SSL (predeterminado: true)

- `charset` (string): Charset para decodificación de la respuesta (predeterminado: "utf-8")

**Aviso de Seguridad**:

Deshabilitar la verificación SSL (`verify = false`) expone la conexión a ataques "man-in-the-middle" y debe usarse **solo** en entornos de desarrollo o prueba controlados. Nunca utilice esta opción en producción con servidores reales o con datos sensibles.

**Valor de retorno**:

Devuelve una tabla con:

- `status` (number): Código de estado HTTP

- `body` (string): Cuerpo de la respuesta

**Ejemplo**:

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

Realiza una solicitud HTTP GET.

**Parámetros**:

- `url` (string): URL del endpoint

- `body` (string, opcional): Cuerpo de la solicitud (raro para GET, pero soportado)

- `headers` (tabela, opcional): Encabezados HTTP

- `options` (tabela, opcional): Opciones adicionales

**Ejemplo**:

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

Realiza una solicitud HTTP POST.

**Parámetros**:

- `url` (string): URL del endpoint

- `body` (string): Cuerpo de la solicitud (generalmente JSON o datos de formulario)

- `headers` (tabela, opcional): Encabezados HTTP

- `options` (tabela, opcional): Opciones adicionales

**Ejemplo**:

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

Realiza una solicitud HTTP PUT para actualizar recursos.

**Parámetros**:

- `url` (string): URL del endpoint

- `body` (string): Cuerpo de la solicitud con datos actualizados

- `headers` (tabela, opcional): Encabezados HTTP

- `options` (tabela, opcional): Opciones adicionales

**Ejemplo**:

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

Realiza una solicitud HTTP DELETE para eliminar recursos.

**Parámetros**:

- `url` (string): URL del endpoint

- `body` (string, opcional): Cuerpo de la solicitud (opcional para DELETE)

- `headers` (tabela, opcional): Encabezados HTTP

- `options` (tabela, opcional): Opciones adicionales

**Ejemplo**:

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

Realiza una solicitud HTTP HEAD para obtener solo encabezados.

**Parámetros**:

- `url` (string): URL del endpoint

- `body` (string, opcional): Cuerpo de la solicitud

- `headers` (tabela, opcional): Encabezados HTTP

- `options` (tabela, opcional): Opciones adicionales

**Ejemplo**:

```lua
local resultado = http.head("https://api.exemplo.com/usuarios/1",
    nil,
    {["Authorization"] = "Bearer token123"}
)

print("Status da verificação:", resultado.status)
-- La respuesta HEAD generalmente no tiene cuerpo
```

## Información Adicional

### URL Automática

Si la URL no contiene un esquema (como `http://` o `https://`), el sistema automáticamente añade `http://` como prefijo.

```lua
-- Estas dos llamadas son equivalentes:
local r1 = http.get("api.exemplo.com/dados")
local r2 = http.get("http://api.exemplo.com/dados")
```

### Verificación SSL

Por defecto, la verificación de certificados SSL está habilitada. Para deshabilitar (útil en entornos de desarrollo/prueba):

**Atención**: Deshabilitar la verificación SSL (`verify = false`) expone la conexión a ataques "man-in-the-middle" y debe usarse **solo** en entornos de desarrollo o prueba controlados. Nunca utilice esta opción en producción con servidores reales o con datos sensibles.

```lua
local resultado = get("https://servidor-local.com",
    nil,
    nil,
    {verify = false}
)
```

### Charsets

Es posible especificar un charset diferente para decodificar la respuesta:

```lua
local resultado = get("https://api.exemplo.com/dados",
    nil,
    nil,
    {charset = "iso-8859-1"}
)
```

## Ejemplo de Uso

```lua
-- Ejemplo de monitorización de API
function verificar_saude_api()
    local resultado = http.get("https://api.exemplo.com/health",
        nil,
        {["User-Agent"] = "MonstaAgent/1.0"}
    )

    if resultado.status == 200 then
        local dados = resultado.body
        -- Procesar respuesta JSON si es necesario
        print("API está saudável")
        return true
    else
        print("API com problemas. Status:", resultado.status)
        return false
    end
end
```

## Notas Importantes

:::note
1. **Timeout**: El timeout predeterminado es el timeout global configurado para scripts Lua en el sistema.

2. **Rendimiento**: Use conexiones persistentes cuando realice múltiples solicitudes al mismo servidor.

3. **Seguridad**: Nunca desactive la verificación SSL en producción sin necesidad.
:::