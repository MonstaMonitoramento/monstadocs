---
title: Módulo Remote
---
O módulo Remote é uma ferramenta avançada de automação que permite que a Sonda execute comandos diretamente no sistema operacional ou no ambiente onde ela está instalada. Este recurso é ideal para automatizar respostas a incidentes, realizar coletas de diagnóstico específicas ou disparar scripts locais baseados em eventos do monitoramento.

## Funções Disponíveis

### 1. `remote.exec(command, [arg1], [arg2], ...)`

Executa um comando do sistema operacional remoto com os argumentos especificados.

### Parâmetros:

- **command** (string): Nome do comando/programa a ser executado
- **…** (opcional, strings): Argumentos adicionais para o comando

### Retorno:

- **tuple**: `(out, err)` onde:
  - **out** (string ou nil): Saída padrão do comando se bem-sucedido, ou `nil` se falhar
  - **err** (string ou nil): Saída de erro do comando se falhar, ou `nil` se bem-sucedido

### Comportamento:

1. O comando é executado com o usuário `monsta-probe` em ambientes Windows e `monstasb` em ambientes Linux.  

2. Se o comando retornar código de saída 0 (sucesso):
  - `out` contém a saída do comando
  - `err` é `nil`
3. Se o comando falhar (código ≠ 0):
  - `out` é nil
  - `err` contém a saída de erro (stderr) do comando
4. Se houver erro na execução (comando não encontrado, etc.):
  - `out` é `nil`
  - `err` contém a mensagem de erro

### Exemplo de Uso:

```
      local resp = probe.exec("ping", { "C:\\Windows\\System32\\ping.exe" }, { "127.0.0.1" })

      if resp.status == "Success" then
          print(resp.stdout)
      end
```

### Suporte a Argumentos Variáveis

Aceita qualquer número de argumentos:

```
-- 1 argumento
process.exec("ls")

-- 2 argumentos
process.exec("ls", "-la")

-- Múltiplos argumentos
process.exec("find", ".", "-name", "*.log", "-type", "f", "-mtime", "+7")
```



&nbsp;