---
title: "Módulo Caché"
---

El módulo **cache** proporciona un sistema de caché distribuido para scripts Lua. La caché admite operaciones de lectura/escritura con expiración automática (TTL) y mecanismos de sincronización para operaciones concurrentes.

El sistema de caché es especialmente útil para:

- Almacenar resultados de operaciones costosas (como solicitudes HTTP, consultas a bases de datos)

- Evitar llamadas redundantes a APIs externas

- Sincronizar múltiples workers que intentan acceder al mismo recurso simultáneamente

- Compartir datos entre diferentes scripts Lua en ejecución

## Funciones Disponibles

### `cache.put(key, value, ttl)`

Almacena un valor en la caché con un tiempo de vida específico.

**Parámetros**:

- `key` (string): Clave única para identificar el valor en la caché

- `value` (cualquier tipo Lua): Valor a almacenar (puede ser string, número, tabla, booleano, etc.)

- `ttl` (number): Time To Live en segundos - cuánto tiempo permanecerá el valor en la caché

**Valor de retorno**:

- `nil` en caso de éxito

- Lanza error en caso de fallo

**Ejemplo**:

```lua
-- Almacenar el resultado de una API durante 5 minutos (300 segundos)
local resultado_api = {status = "ativo", usuarios = 150}
cache.put("status_sistema", resultado_api, 300)

-- Almacenar una cadena simple durante 1 hora
cache.put("ultima_atualizacao", "2026-01-15T10:30:00Z", 3600)

-- Almacenar un número
cache.put("contador_requisicoes", 42, 60)
```

### `cache.get(key)`

Recupera un valor de la caché.

**Parámetros**:

- `key` (string): Clave del valor a recuperar

**Valor de retorno**:

- El valor almacenado si existe y no ha expirado

- `nil` si la clave no existe o el valor ha expirado

**Ejemplo**:

```lua
-- Recuperar un valor de la caché
local status = cache.get("status_sistema")

if status then
    print("Status do sistema:", status.status)
    print("Usuários ativos:", status.usuarios)
else
    print("Cache expirado ou não encontrado")
    -- Fazer uma nova requisição para obter os dados
end

-- Verificar se um valor existe
local ultima_atualizacao = cache.get("ultima_atualizacao")
if ultima_atualizacao then
    print("Última atualização:", ultima_atualizacao)
end
```

### `cache.mark_pending(key)`

Marca una clave como "pendiente". Esta función se usa para sincronizar múltiples workers que intentan calcular el mismo valor simultáneamente.

**Parámetros**:

- `key` (string): Clave a marcar como pendiente

**Valor de retorno**:

- `nil` en caso de éxito

- Lanza error en caso de fallo

**Comportamiento**:

- Cuando una clave se marca como pendiente, cualquier llamada subsecuente a `cache.get()` para esa clave bloqueará hasta que un valor sea almacenado con `cache.put()`

- El estado "pendiente" expira automáticamente después de 5 minutos (300 segundos)

- Útil para evitar que múltiples workers recalcule n el mismo valor costoso simultáneamente

**Ejemplo**:

```lua
-- Patrón típico para evitar un cache stampede
local function obter_dados_caros(chave)
    -- Primero intenta obtener del caché
    local dados = cache.get(chave)

    if dados then
        return dados
    end

    -- Si no lo encuentra, marca como pendiente
    local sucesso, erro = pcall(cache.mark_pending, chave)

    if not sucesso then
        -- Otro worker ya marcó como pendiente, espera el resultado
        dados = cache.get(chave)  -- Esta llamada se bloqueará hasta que el valor esté disponible
        if dados then
            return dados
        end
    end

    -- Este worker es responsable de calcular el valor
    -- ... cálculo costoso aquí ...
    local resultado = calcular_dados_caros()

    -- Almacena en la caché para otros workers
    cache.put(chave, resultado, 300)

    return resultado
end
```

### `cache.delete(key)`

Elimina una clave de la caché de forma inmediata.

**Parámetros**:

- `key` (string): Clave a eliminar

**Valor de retorno**:

- `nil` en caso de éxito

- Lanza error en caso de fallo

**Ejemplo**:

```lua
-- Eliminar un valor específico
cache.delete("dados_expirados")

-- Limpiar caché relacionada con un usuario
cache.delete("usuario_123_perfil")
cache.delete("usuario_123_preferencias")
cache.delete("usuario_123_historico")
```

## Información Adicional

### Sincronización de Workers

El mecanismo de "pendiente" permite que múltiples workers sincronicen el cálculo de valores costosos:

1. El primer worker marca la clave como pendiente y calcula el valor

2. Otros workers que intentan acceder a la misma clave esperan el resultado

3. Cuando el primer worker termina, almacena el valor y todos los workers lo reciben

### Tipos de datos compatibles

La caché puede almacenar cualquier tipo de valor Lua soportado por el sistema de serialización de Monsta, incluyendo:

- Cadenas

- Números

- Booleanos

- Tablas

- Valores nulos

## Consideraciones de Rendimiento

1. **Acceso rápido**: Las operaciones de caché son mucho más rápidas que recalcular valores o hacer solicitudes externas

2. **Memoria**: La caché se mantiene en memoria, por lo que valores muy grandes pueden afectar al rendimiento

3. **Concurrencia**: El sistema es thread-safe y soporta acceso concurrente de múltiples workers

4. **Red**: El caché es local al proceso, no hay sobrecarga de red

## Limitaciones

1. **Volátil**: Los datos se pierden si el proceso se reinicia

2. **Memoria limitada**: No usar para almacenar grandes volúmenes de datos

3. **Distribución**: Este es un caché local, no distribuido entre varios servidores

## Buenas Prácticas

1. **TTL adecuado**: Usa TTLs apropiados para el tipo de dato (corto para datos dinámicos, largo para datos estáticos)

2. **Claves descriptivas**: Usa nombres de clave que describan claramente el contenido

3. **Espacio de nombres**: Usa prefijos para organizar claves (ej.: `api_`, `user_`, `config_`)

4. **Fallback**: Ten siempre un fallback en caso de que la caché esté vacía o haya expirado

5. **Invalidación**: Usa `delete()` para invalidar la caché cuando los datos cambien