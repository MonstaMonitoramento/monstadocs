---
title: "Process Module"
---

The **process** module provides a function to execute operating system commands from Lua scripts. This function is useful for automation of administrative tasks, gathering system information, and integration with external tools.

- Execution of commands with a non-privileged user

- Capture stdout and stderr separately

- Structured return with success/error

- Support for variable arguments

**Security note**: All commands are executed as the `monstasb` user to ensure security and permission control.

## Available Functions

### 1. `process.exec(command, [arg1], [arg2], ...)`

Executes an operating system command with the specified arguments.

#### Parameters:

- **command** (string): Name of the command/program to execute

- **...** (optional, strings): Additional arguments for the command

#### Return:

- **tuple**: `(out, err)` where:

    - **out** (string or nil): Standard output of the command if successful, or `nil` if it fails

    - **err** (string or nil): Error output of the command if it fails, or `nil` if successful

#### Behavior:

1. The command is executed as the `monstasb` user

2. If the command returns exit code 0 (success):

    - `out` contains the command output

    - `err` is `nil`

3. If the command fails (code ≠ 0):

    - `out` is nil

    - `err` contains the command's error output (stderr)

4. If there is an execution error (command not found, etc.):

    - `out` is `nil`

    - `err` contains the error message

#### Example Usage:

```lua
-- Execute simple command
local saida, erro = process.exec("ls", "-la", "/tmp")
if saida then
    print("Conteúdo de /tmp:")
    print(saida)
else
    print("Erro:", erro)
end

-- Execute command with multiple arguments
local saida, erro = process.exec("df", "-h")
if saida then
    -- Process df output
    local linhas = string.split(saida, "\n")
    for _, linha in ipairs(linhas) do
        print("Linha:", linha)
    end
end

-- Check if a service is running
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

-- Collect system information
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

## Additional Information

### Execution as a Specific User

All commands are executed as the `monstasb` user:

```lua
-- Security: commands are not executed as root
process.exec("whoami")  -- Will return "monstasb", not "root"
```

### Support for Variable Arguments

Accepts any number of arguments:

```lua
-- 1 argument
process.exec("ls")

-- 2 arguments
process.exec("ls", "-la")

-- Multiple arguments
process.exec("find", ".", "-name", "*.log", "-type", "f", "-mtime", "+7")
```