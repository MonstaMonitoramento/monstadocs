---
title: "Módulo Registry"
---

El módulo **registry** proporciona un sistema de almacenamiento de datos persistente y compartido entre ejecuciones de scripts Lua. Este módulo es útil para mantener estado entre diferentes ejecuciones, compartir datos entre scripts e implementar mecanismos de caché y configuración persistente.

- Almacenamiento clave-valor persistente

- Marca de tiempo automática para cada entrada

- Seguro para uso concurrente (thread-safe)

- Datos compartidos entre todos los scripts Lua

- Persistencia entre reinicios del agente

## Funciones Disponibles

### 1. `registry.put(chave, valor)`

Almacena un valor en el registry con la clave especificada.

#### Parámetros:

- **chave** (string): Identificador único para el valor

- **valor** (qualquer tipo Lua): Valor a ser almacenado (string, número, booleano, tabla, nil)

#### Retorno:

- **nil**: La función no devuelve valor

#### Comportamiento:

1. Almacena el valor asociado a la clave

2. Registra automáticamente la marca de tiempo actual (UTC)

3. Sobrescribe cualquier valor existente con la misma clave

4. Acepta cualquier tipo de dato Lua soportado por el sistema de valores del Monagent

#### Ejemplo de Uso:

```lua
-- Almacenar valores básicos
registry.put("ultima_execucao", os.time())
registry.put("hostname", "servidor-producao")
registry.put("ativo", true)
registry.put("versao", 2.5)

-- Almacenar tablas complejas
local config = {
    timeout = 30,
    retries = 3,
    servidores = {"srv1", "srv2", "srv3"},
    limites = {cpu = 80, memoria = 90, disco = 95}
}
registry.put("configuracao_monitoramento", config)

-- Almacenar resultados de processamento
local metricas = {
    cpu_usage = 45.6,
    memory_usage = 78.3,
    disk_usage = 62.1,
    timestamp = os.time()
}
registry.put("metricas_recentes", metricas)

-- Sobrescribir valor existente
registry.put("contador", 1)
-- ... mais tarde ...
local valor, timestamp = registry.get("contador")
registry.put("contador", (valor or 0) + 1)
```

### 2. `registry.get(chave)`

Recupera un valor del registry por la clave especificada.

#### Parámetros:

- **chave** (string): Clave del valor a recuperar

#### Retorno:

- **tupla**: `(valor, timestamp)` donde:

    - **valor** (qualquer tipo ou nil): Valor almacenado, o `nil` si la clave no existe

    - **timestamp** (número ou nil): Marca de tiempo Unix (segundos) de la última actualización, o `nil` si la clave no existe

#### Comportamiento:

1. Devuelve el valor y la marca de tiempo si la clave existe

2. Devuelve `(nil, nil)` si la clave no existe

3. Preserva el tipo original del valor almacenado

4. La marca de tiempo está en segundos desde la epoch Unix (UTC)

#### Ejemplo de Uso:

```lua
-- Recuperar valor simple
local valor, timestamp = registry.get("config_timeout")
if valor then
    print("Timeout configurado:", valor, "desde", os.date("%H:%M:%S", timestamp))
else
    print("Configuração não encontrada")
end

-- Recuperar tabla
local config, ts = registry.get("configuracao_sistema")
if config then
    print("Configuração carregada:")
    for chave, valor in pairs(config) do
        print("  ", chave, "=", valor)
    end
    print("Última atualização:", os.date("%Y-%m-%d %H:%M:%S", ts))
end

-- Verificar existencia antes de usar
local dados, timestamp = registry.get("dados_processamento")
if dados then
    -- Processar dados existentes
    processar_dados(dados)
else
    -- Inicializar nuevos datos
    dados = inicializar_dados()
    registry.put("dados_processamento", dados)
end

-- Usar valor por defecto si no existe
local limite, _ = registry.get("limite_cpu")
limite = limite or 80  -- Valor por defecto 80% si no configurado
```

### 3. `registry.delete(chave)`

Elimina una entrada del registry por la clave especificada.

#### Parámetros:

- **chave** (string): Clave de la entrada a eliminar

#### Retorno:

- **nil**: La función no devuelve valor

#### Comportamiento:

1. Elimina completamente la entrada del registry

2. No hace nada si la clave no existe

3. Libera la memoria asociada a la clave

4. Operación atómica y thread-safe

#### Ejemplo de Uso:

```lua
-- Remover entrada específica
registry.delete("cache_temporario")
print("Cache temporário removido")

-- Limpiar todas las entradas de un prefijo
local function limpar_prefixo(prefixo)
    -- Nota: El registry no soporta listado directo
    -- En un caso real, necesitaría mantener una lista de claves
    log.info("Limpando entradas com prefixo:", prefixo)

    -- Exemplo com chaves conhecidas
    local chaves_conhecidas = {
        prefixo .. "_cache_dns",
        prefixo .. "_cache_http",
        prefixo .. "_metricas",
        prefixo .. "_config"
    }

    for _, chave in ipairs(chaves_conhecidas) do
        registry.delete(chave)
        log.debug("Removido:", chave)
    end
end

-- Limpar entradas expiradas
local function limpar_expirados(ttl_segundos)
    local agora = os.time()
    -- Nota: Nuevamente, sin listado directo, necesitamos una estrategia
    log.info("Limpeza de expirados não suportada diretamente")
    log.info("Use timestamps nas chaves ou mantenha lista de chaves")
end

-- Remover após uso
local function processar_e_limpar(chave)
    local dados, timestamp = registry.get(chave)

    if dados then
        -- Procesar datos
        local resultado = processar(dados)

        -- Eliminar después del procesamiento
        registry.delete(chave)
        log.info("Dados processados e removidos:", chave)

        return resultado
    else
        log.warn("Chave não encontrada:", chave)
        return nil
    end
end
```