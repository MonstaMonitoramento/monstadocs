---
title: "Módulo Process"
---

El módulo **process** proporciona una función para ejecutar comandos del sistema operativo desde scripts Lua. Esta función es útil para la automatización de tareas administrativas, la recopilación de información del sistema y la integración con herramientas externas.

- Ejecución de comandos con usuario no privilegiado

- Captura de stdout y stderr por separado

- Retorno estructurado con éxito/error

- Soporte de argumentos variables

**Nota de seguridad**: Todos los comandos se ejecutan con el usuario `monstasb` para garantizar seguridad y control de permisos.

## Funciones Disponibles

### 1. `process.exec(command, [arg1], [arg2], ...)`

Ejecuta un comando del sistema operativo con los argumentos especificados.

#### Parámetros:

- **command** (string): Nombre del comando/programa a ejecutar

- **...** (opcional, strings): Argumentos adicionales para el comando

#### Retorno:

- **tuple**: `(out, err)` donde:

    - **out** (string o nil): Salida estándar del comando si tiene éxito, o `nil` si falla

    - **err** (string o nil): Salida de error del comando si falla, o `nil` si tiene éxito

#### Comportamiento:

1. El comando se ejecuta con el usuario `monstasb`

2. Si el comando devuelve código de salida 0 (éxito):

    - `out` contiene la salida del comando

    - `err` es `nil`

3. Si el comando falla (código ≠ 0):

    - `out` es nil

    - `err` contiene la salida de error (stderr) del comando

4. Si hay un error en la ejecución (comando no encontrado, etc.):

    - `out` es `nil`

    - `err` contiene el mensaje de error

#### Ejemplo de Uso:

```lua
-- Ejecutar comando simple
local saida, erro = process.exec("ls", "-la", "/tmp")
if saida then
    print("Conteúdo de /tmp:")
    print(saida)
else
    print("Erro:", erro)
end

-- Ejecutar comando con múltiples argumentos
local saida, erro = process.exec("df", "-h")
if saida then
    -- Processar saída do df
    local linhas = string.split(saida, "\n")
    for _, linha in ipairs(linhas) do
        print("Linha:", linha)
    end
end

-- Verificar si un servicio está en ejecución
local saida, erro = process.exec("systemctl", "is-active", "nginx")
if saida then
    local status = string.trim(saida)
    if status == "active" then
        print("Nginx está ativo")
    else
        print("Nginx não está ativo:", status)
    end
else
    print("Erro ao verificar Nginx:", erro)
end

-- Recopilar información del sistema
local comandos = {
    {"uname", "-a"},
    {"uptime"},
    {"free", "-h"},
    {"df", "-h", "/"}
}

for _, cmd_args in ipairs(comandos) do
    local comando = table.remove(cmd_args, 1)
    local saida, erro = process.exec(comando, table.unpack(cmd_args))
    if saida then
        print("=== " .. comando .. " ===")
        print(saida)
    end
end
```

## Información Adicional

### Ejecución con Usuario Específico

Todos los comandos se ejecutan con el usuario `monstasb`:

```lua
-- Seguridad: los comandos no se ejecutan como root
process.exec("whoami")  -- Retornará "monstasb", no "root"
```

### Soporte de Argumentos Variables

Acepta cualquier número de argumentos:

```lua
-- 1 argumento
process.exec("ls")

-- 2 argumentos
process.exec("ls", "-la")

-- Múltiples argumentos
process.exec("find", ".", "-name", "*.log", "-type", "f", "-mtime", "+7")
```