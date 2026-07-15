---
title: Remote Module
---
The Remote module is an advanced automation tool that allows the Probe to execute commands directly on the operating system or environment where it is installed. This feature is ideal for automating incident responses, performing specific diagnostic collections, or triggering local scripts based on monitoring events.

## Available Functions

### 1. `remote.exec(command, [arg1], [arg2], ...)`

Executes a command on the remote operating system with the specified arguments.

**Parameters**:

- `command` (string): Name of the command/program to be executed
- `…` (optional, strings): Additional arguments for the command

**Return**:

- `tuple`: `(out, err)` where:
  - `out` (string or nil): Standard output of the command if successful, or `nil` if it fails
  - `err` (string or nil): Error output of the command if it fails, or `nil` if successful

**Behavior**:

1. The command is executed as the user `monsta-probe` on Windows environments and `monstasb` on Linux environments.  

   1. If the command returns exit code `0` (success):

      - `out` contains the command output
      - `err` is `nil`

   2. If the command fails (code ≠ `0`):

      - `out` is nil
      - `err` contains the command's error output (stderr)

   3. If there is an execution error (command not found, etc.):

      - `out` is `nil`
      - `err` contains the error message

**Usage Example**:

```lua
      local resp = probe.exec("ping", { "C:\\Windows\\System32\\ping.exe" }, { "127.0.0.1" })

      if resp.status == "Success" then
          print(resp.stdout)
      end
```

#### Support for Variable Arguments

Accepts any number of arguments:

```lua
-- 1 argument
process.exec("ls")

-- 2 arguments
process.exec("ls", "-la")

-- Multiple arguments
process.exec("find", ".", "-name", "*.log", "-type", "f", "-mtime", "+7")
```