---
title: "Módulo SSH"
---

El módulo **ssh** proporciona funciones para ejecutar comandos remotos en servidores a través del protocolo Secure Shell (SSH). Ofrece dos enfoques principales: ejecución única de comandos y conexiones persistentes para múltiples comandos. El módulo soporta autenticación por contraseña e incluye resolución DNS automática.

## Funciones disponibles

### 1. `ssh.exec(opts)`

Ejecuta un comando remoto vía SSH de forma asíncrona y devuelve la salida del comando.

**Parámetros**:

- `opts` (tabla): Opciones de conexión y ejecución que contienen:

    - `host` (string): Dirección del servidor (hostname o IP)

    - `username` (string): Nombre de usuario para la autenticación

    - `password` (string): Contraseña para la autenticación

    - `command` (string): Comando a ejecutar en el servidor remoto

    - `port` (número opcional, por defecto: 22): Puerto SSH

    - `timeout` (número opcional, por defecto: 60): Tiempo de espera en segundos para la conexión

**Retorno**:

- `string`: Salida estándar (stdout) del comando ejecutado

**Excepciones**:

- Lanza error si falta algún parámetro obligatorio

- Lanza error si la conexión SSH falla

- Lanza error si el comando falla en el servidor remoto

- Lanza error "connection timeout" si se excede el tiempo límite

**Ejemplos**:

```lua
-- Ejecución básica de comando
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

-- Comprobar uso de disco
local disk_opts = {
    host = "192.168.1.100",
    username = "monitor",
    password = "monitor_pass",
    command = "df -h /"
}

local disk_usage = ssh.exec(disk_opts)

-- Verificar servicios en ejecución
local service_opts = {
    host = "app-server",
    username = "root",
    password = "root_password",
    command = "systemctl list-units --type=service --state=running"
}

local services = ssh.exec(service_opts)
```

### 2. `ssh.connect(opts)`

Establece una conexión SSH persistente y devuelve un objeto cliente que puede ejecutar múltiples comandos.

**Nota**: Esta función usa valores predeterminados de la tabla `params` cuando no se proporcionan los parámetros.

**Parámetros**:

- `opts` (tabla): Opciones de conexión que contienen:

    - `host` (string): Dirección del servidor (hostname o IP)

    - `username` (string): Nombre de usuario para la autenticación

    - `password` (string): Contraseña para la autenticación

    - `port` (número opcional, por defecto: 22): Puerto SSH

    - `timeout` (número opcional, por defecto: `params.sshTimeout` o 60): Tiempo de espera en segundos para la conexión

**Retorno**:

- `SshClient`: Objeto cliente SSH con el método `exec()` para ejecutar comandos

**Excepciones**:

- Lanza error si falta algún parámetro obligatorio

- Lanza error si la conexión SSH falla

- Lanza error "connection timeout" si se excede el tiempo límite

**Ejemplos**:

```lua
-- Crear conexión persistente
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

-- Ejecutar múltiples comandos en la misma conexión
local cmd1_output = client:exec("pg_isready")
local cmd2_output = client:exec("psql -c 'SELECT version();'")
local cmd3_output = client:exec("df -h /var/lib/postgresql")

print("PostgreSQL status: " .. cmd1_output)
print("Versão PostgreSQL: " .. cmd2_output)
print("Espaço em disco: " .. cmd3_output)
```

### 3. `SshClient:exec(command)`

Método del objeto cliente devuelto por `ssh.connect()` para ejecutar comandos en la conexión establecida.

**Parámetros**:

- `command` (string): Comando a ejecutar en el servidor remoto

**Retorno**:

- `string`: Salida estándar (stdout) del comando ejecutado

**Excepciones**:

- Lanza error si la conexión subyacente falla

- Lanza error si el comando falla en el servidor remoto

**Ejemplos**:

```lua
-- Uso con múltiples comandos relacionados
-- Ejemplo usando valores explícitos
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

-- Ejemplo mixto (algunos valores explícitos, otros de params)
local client_misto = ssh.connect({
    host = "backup-server",
    port = 2222
})
-- Usa: host = "backup-server", port = 2222
-- Usa do params: username = "admin", password = "admin123", timeout = 30

-- Recopilar métricas del sistema
local uptime = client:exec("uptime")
local memory = client:exec("free -m")
local cpu = client:exec("top -bn1 | grep 'Cpu(s)'")
local disk = client:exec("iostat -x 1 1")

-- Procesar resultados
print("Uptime: " .. uptime)
print("Memória: " .. memory)
print("CPU: " .. cpu)
print("Disk I/O: " .. disk)
```

## Información adicional

### 1. **Resolución DNS automática**

- Los hostnames se resuelven automáticamente a direcciones IP

- Usa el módulo DNS interno de Monsta

- Soporta tanto IPv4 como IPv6

### 2. **Conexiones persistentes**

- Las conexiones SSH pueden reutilizarse para múltiples comandos

- Reduce el overhead de autenticación para comandos secuenciales

- Mejora el rendimiento en operaciones por lotes

### 3. **Tiempo de espera configurable**

- Tiempo de espera por defecto de 60 segundos para las conexiones

- Configurable por conexión mediante el parámetro `timeout`

- Prevención contra conexiones bloqueadas

## Limitaciones

### 1. **Autenticación solo por contraseña**

- No soporta autenticación por clave pública (SSH key)

### 2. **Rendimiento**

- Las conexiones SSH tienen un overhead significativo

- No recomendado para comandos muy frecuentes (usar agentes locales)