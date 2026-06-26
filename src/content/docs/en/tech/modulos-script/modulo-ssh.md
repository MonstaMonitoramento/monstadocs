---
title: "SSH Module"
---

The **ssh** module provides functions to execute remote commands on servers via the Secure Shell (SSH) protocol. It offers two main approaches: single command execution and persistent connections for multiple commands. The module supports password authentication and includes automatic DNS resolution.

## Available Functions

### 1. `ssh.exec(opts)`

Executes a remote command over SSH asynchronously and returns the command output.

**Parameters**:

- `opts` (table): Connection and execution options containing:

    - `host` (string): Server address (hostname or IP)

    - `username` (string): Username for authentication

    - `password` (string): Password for authentication

    - `command` (string): Command to be executed on the remote server

    - `port` (number, optional, default: 22): SSH port

    - `timeout` (number, optional, default: 60): Timeout in seconds for the connection

**Returns**:

- `string`: Standard output (stdout) of the executed command

**Exceptions**:

- Throws an error if any required parameter is missing

- Throws an error if the SSH connection fails

- Throws an error if the command fails on the remote server

- Throws a "connection timeout" error if the timeout is exceeded

**Examples**:

```lua
-- Basic command execution
local opts = {
    host = "servidor.exemplo.com",
    username = "admin",
    password = "senha123",
    command = "uname -a",
    port = 22,
    timeout = 30
}

local success, output = pcall(function()
    return ssh.exec(opts)
end)

if success then
    print("Saída do comando: " .. output)
else
    print("Erro SSH: " .. output)
end

-- Verificar uso de disco
local disk_opts = {
    host = "192.168.1.100",
    username = "monitor",
    password = "monitor_pass",
    command = "df -h /"
}

local disk_usage = ssh.exec(disk_opts)

-- Verificar serviços em execução
local service_opts = {
    host = "app-server",
    username = "root",
    password = "root_password",
    command = "systemctl list-units --type=service --state=running"
}

local services = ssh.exec(service_opts)
```

### 2. `ssh.connect(opts)`

Establishes a persistent SSH connection and returns a client object that can execute multiple commands.

**Note**: This function uses default values from the `params` table when parameters are not provided.

**Parameters**:

- `opts` (table): Connection options containing:

    - `host` (string): Server address (hostname or IP)

    - `username` (string): Username for authentication

    - `password` (string): Password for authentication

    - `port` (number, optional, default: 22): SSH port

    - `timeout` (number, optional, default: `params.sshTimeout` or 60): Timeout in seconds for the connection

**Returns**:

- `SshClient`: SSH client object with an `exec()` method to run commands

**Exceptions**:

- Throws an error if any required parameter is missing

- Throws an error if the SSH connection fails

- Throws a "connection timeout" error if the timeout is exceeded

**Examples**:

```lua
-- Criar conexão persistente
local connect_opts = {
    host = "banco-de-dados.exemplo.com",
    username = "dba",
    password = "dba_password",
    port = 2222,
    timeout = 45
}

local success, client = pcall(function()
    return ssh.connect(connect_opts)
end)

if not success then
    print("Falha na conexão SSH: " .. client)
    return
end

-- Executar múltiplos comandos na mesma conexão
local cmd1_output = client:exec("pg_isready")
local cmd2_output = client:exec("psql -c 'SELECT version();'")
local cmd3_output = client:exec("df -h /var/lib/postgresql")

print("PostgreSQL status: " .. cmd1_output)
print("Versão PostgreSQL: " .. cmd2_output)
print("Espaço em disco: " .. cmd3_output)
```

### 3. `SshClient:exec(command)`

Method of the client object returned by `ssh.connect()` to execute commands on the established connection.

**Parameters**:

- `command` (string): Command to be executed on the remote server

**Returns**:

- `string`: Standard output (stdout) of the executed command

**Exceptions**:

- Throws an error if the underlying connection fails

- Throws an error if the command fails on the remote server

**Examples**:

```lua
-- Usage with multiple related commands
-- Example using explicit values
local client = ssh.connect({
    host = "monitor-server",
    username = "metrics",
    password = "metrics_pass"
})

-- Exemplo usando valores do params configurado no dispositivo
-- params.sshUsername = "admin"
-- params.sshPassword = "admin123"
-- params.address = "servidor.local"
-- params.sshPort = 22
-- params.sshTimeout = 30

local client_simplificado = ssh.connect({})
-- Equivalente a: ssh.connect({
--     host = "servidor.local",
--     username = "admin",
--     password = "admin123",
--     port = 22,
--     timeout = 30
-- })

-- Exemplo misto (alguns valores explícitos, outros do params)
local client_misto = ssh.connect({
    host = "backup-server",
    port = 2222
})
-- Usa: host = "backup-server", port = 2222
-- Usa do params: username = "admin", password = "admin123", timeout = 30

-- Coletar métricas do sistema
local uptime = client:exec("uptime")
local memory = client:exec("free -m")
local cpu = client:exec("top -bn1 | grep 'Cpu(s)'")
local disk = client:exec("iostat -x 1 1")

-- Processar resultados
print("Uptime: " .. uptime)
print("Memória: " .. memory)
print("CPU: " .. cpu)
print("Disk I/O: " .. disk)
```

## Additional Information

### 1. **Automatic DNS Resolution**

- Hostnames are automatically resolved to IP addresses

- Uses Monsta's internal DNS module

- Supports both IPv4 and IPv6

### 2. **Persistent Connections**

- SSH connections can be reused for multiple commands

- Reduces authentication overhead for sequential commands

- Improves performance for batch operations

### 3. **Configurable Timeout**

- Default timeout of 60 seconds for connections

- Configurable per connection via the `timeout` parameter

- Prevents hung/stuck connections

## Limitations

### 1. **Password-Only Authentication**

- Does not support public key (SSH key) authentication

### 2. **Performance**

- SSH connections have significant overhead

- Not recommended for very frequent commands (use local agents)