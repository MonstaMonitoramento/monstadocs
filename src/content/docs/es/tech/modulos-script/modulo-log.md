---
title: "Módulo de registro"
---

El módulo **log** proporciona funciones de logging para scripts Lua, permitiendo el registro de mensajes con diferentes niveles de severidad. Este módulo es útil para depuración, monitorización y auditoría de scripts en producción.

**Características principales**:

- 5 niveles de log: debug, info, warn, error

- Identificación por contexto de ejecución

- Formateo automático de valores Lua

- Soporte para múltiples argumentos con separación por tabulación en la salida

## Funciones Disponibles

### 1. `log.set_ident(identificador)`

Define un identificador para los logs generados por el script actual.

#### Parámetros:

- **identificador** (string): Identificador único para el contexto de ejecución

#### Retorno:

- **nil**: La función no devuelve valor

#### Comportamiento:

- El identificador se almacena internamente y persiste durante toda la ejecución del script

- Todos los mensajes de log posteriores incluirán este identificador

- Útil para distinguir registros de diferentes scripts o instancias

#### Ejemplo de uso:

```lua
-- Establecer identificador para un script específico
log.set_ident("monitoramento-cpu")

-- Ahora todos los logs incluirán "[monitoramento-cpu]"
log.info("Iniciando monitoramento")
-- Salida: [lua] [monitoramento-cpu] Iniciando monitoramento

-- En otro script o contexto
log.set_ident("backup-automatico")
log.info("Iniciando backup")
-- Salida: [lua] [backup-automatico] Iniciando backup
```

### 2. `log.debug(...)`

Registra mensajes de nivel DEBUG para información detallada de depuración.

#### Parámetros:

- **...** (múltiples valores): Valores a registrar, separados por tabulación

#### Retorno:

- **nil**: La función no devuelve valor

#### Ejemplo de uso:

```lua
-- Registro de valores de variables para depuración
local temperatura = 45.6
local uso_memoria = 78.3
log.debug("Variáveis de sistema:", "Temp:", temperatura, "Mem:", uso_memoria)
-- Salida: [lua] [ident] Variáveis de sistema:	Temp:	45.6	Mem:	78.3

-- Depuración del flujo de ejecución
log.debug("Entrando na função processar_dados")
log.debug("Parâmetros recebidos:", parametros)
log.debug("Configuração atual:", config)

-- Depuración de estructuras complejas
local dados = {
    usuario = "admin",
    acao = "login",
    timestamp = os.time()
}
log.debug("Dados da requisição:", dados)
```

### 3. `log.info(...)`

Registra mensajes de nivel INFO para información general sobre la ejecución.

#### Parámetros:

- **...** (múltiples valores): Valores a registrar, separados por tabulación

#### Retorno:

- **nil**: La función no devuelve valor

### 4. `log.warn(...)`

Registra mensajes de nivel WARN para situaciones que requieren atención pero no son errores.

#### Parámetros:

- **...** (múltiples valores): Valores a registrar, separados por tabulación

#### Retorno:

- **nil**: La función no devuelve valor

### 5. `log.error(...)`

Registra mensajes de nivel ERROR para situaciones de error que requieren intervención.

#### Parámetros:

- **...** (múltiples valores): Valores a registrar, separados por tabulación

#### Retorno:

- **nil**: La función no devuelve valor