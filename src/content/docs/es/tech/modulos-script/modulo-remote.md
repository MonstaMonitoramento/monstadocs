---
title: Módulo Remoto
---
El módulo Remote es una herramienta avanzada de automatización que permite que la Sonda ejecute comandos directamente en el sistema operativo o en el entorno donde está instalada. Este recurso es ideal para automatizar respuestas a incidentes, realizar recopilaciones de diagnóstico específicas o disparar scripts locales basados en eventos del monitoreo.

## Funciones Disponibles

### 1. `remote.exec(command, [arg1], [arg2], ...)`

Ejecuta un comando del sistema operativo remoto con los argumentos especificados.

**Parámetros**:

- `command` (string): Nombre del comando/programa a ejecutar
- `…` (opcional, strings): Argumentos adicionales para el comando

**Retorno**:

- `tuple`: `(out, err)` donde:
  - `out` (string o nil): Salida estándar del comando si tiene éxito, o `nil` si falla
  - `err` (string o nil): Salida de error del comando si falla, o `nil` si tiene éxito

**Comportamiento**:

1. El comando se ejecuta con el usuario `monsta-probe` en entornos Windows y `monstasb` en entornos Linux.  

   1. Si el comando devuelve código de salida `0` (éxito):

      - `out` contiene la salida del comando
      - `err` es `nil`

   2. Si el comando falla (código ≠ `0`):

      - `out` es nil
      - `err` contiene la salida de error (stderr) del comando

   3. Si hay un error en la ejecución (comando no encontrado, etc.):

      - `out` es `nil`
      - `err` contiene el mensaje de error

**Ejemplo de uso**:

```lua
      local resp = probe.exec("ping", { "C:\\Windows\\System32\\ping.exe" }, { "127.0.0.1" })

      if resp.status == "Success" then
          print(resp.stdout)
      end
```

#### Soporte de argumentos variables

Acepta cualquier número de argumentos:

```lua
-- 1 argumento
process.exec("ls")

-- 2 argumentos
process.exec("ls", "-la")

-- Múltiples argumentos
process.exec("find", ".", "-name", "*.log", "-type", "f", "-mtime", "+7")
```