---
title: Módulo Storage
---
O módulo Storage realiza uma análise contínua da integridade e do desempenho de discos rígidos (HDs) e unidades de estado sólido (SSDs), coletando informações S.M.A.R.T. para identificar sinais de desgaste, falhas iminentes e degradação do dispositivo

## Funções Disponíveis

### 1. `storage.list_devices()`

Lista todos os dispositivos de armazenamento detectados no sistema.

**Retorno**:  
Array de strings com os caminhos dos dispositivos

`{ "/dev/sda", "/dev/sdb" }`

**Exemplo**:

```lua
local devices = storage.list_devices()

for _, dev in ipairs(devices) do
    print(dev)
end
```

### 2. `storage.info(path)`

Retorna informações gerais do disco.

**Parâmetros**:

`path` (string): Caminho do dispositivo (ex: `"/dev/sda"`)

**Retorno**:

Table com os campos:

> device_model (string): Modelo do disco  
> model_family (string): Familia do modelo (apenas ATA)  
> serial_number (string): Numero de serie  
> firmware_version (string): Versao do firmware  
> user_capacity (string): Capacidade total  
> rotation_rate (string): RPM (apenas ATA)  
> form_factor (string): Formato fisico (apenas ATA)  
> interface (string): Velocidade da interface (apenas ATA)  
> protocol (string): "ATA", "NVMe" ou "SCSI"  
> smart_support (table): Informacoes de suporte SMART  
> logical_block_size (number): Tamanho do bloco logico    
> physical_block_size (number): Tamanho do bloco fisico    
> nvme_version (string): Versao NVMe (apenas NVMe)

**Exemplo de uso**:

```lua
local info = storage.info("/dev/sda")
print(info.device_model, info.serial_number)
```

### 3. `storage.health(path)`

Retorna o status geral de saude do disco (SMART *overall-health*).

**Parâmetros**:

`path` (string):   Caminho do dispositivo

**Retorno**:

Table com os campos:

```text
    passed (boolean):  true se o disco passou no teste SMART  
    status (string):   "PASSED" ou "FAILED"  
    message (string):   Mensagem descritiva do status
```

**Exemplo de uso**:

```lua
local h = storage.health("/dev/sda")
if h.passed then
    print("Disco saudavel")
else
    print("FALHA: " .. h.message)
end
```

### 4. `storage.attributes(path)`

Retorna todos os atributos SMART do disco.

**Parâmetros**:

`path` (string): Caminho do dispositivo

**Retorno**:

Array de objetos, cada um com os campos:

```text
    id (number):   ID do atributo  
    name (string):   Nome do atributo (ex: "Temperature_Celsius")  
    value (number):   Valor normalizado  
    worst (number):   Pior valor ja registrado  
    thresh (number):   Limite de falha  
    raw (number):   Valor bruto (raw)  
    when_failed (string):   Indicacao de falha  
    flags (string):   Flags do atributo
```

**Exemplo de uso**:

```lua
local attrs = storage.attributes("/dev/sda")
for _, a in ipairs(attrs) do
    print(a.id, a.name, a.raw)
end
```

### 5. `storage.attribute(path, attr_name)`

Retorna um atributo SMART especifico pelo nome.

**Parâmetros**:

```text
  path      : string   Caminho do dispositivo  
  attr_name : string   Nome do atributo (ex: "Temperature_Celsius")
```

**Retorno**:

O objeto do atributo se encontrado, nil caso contrario

**Exemplo de uso**:

```lua
local attr = storage.attribute("/dev/sda", "Power_On_Hours")
if attr then
    print("Horas ligadas:", attr.raw)
end
```

### 6. `storage.temperature(path)`

Retorna a temperatura atual do disco em Celsius.

**Parâmetros**:

`path` (string): Caminho do dispositivo

**Retorno**:

Temperatura em graus Celsius, ou `nil` se indisponível

**Exemplo de uso**:

```lua
local temp = storage.temperature("/dev/sda")
if temp then
    print("Temperatura:", temp, "C")
end
```

### 7. `storage.error_log(path)`

Retorna um resumo do log de erros do disco.

**Parâmetros**:

`path` (string):   Caminho do dispositivo

**Retorno**:

Table ou nil com os campos (varia por protocolo):

```text
    ATA:  
      count (number):   Quantidade de erros registrados  
      logged_errors (number):   Erros logados

    NVMe:  
      size (number):   Tamanho do log  
      read (number):   Entradas lidas  
      unread (number):   Entradas nao lidas
```

**Exemplo de uso**:

```lua
local log = storage.error_log("/dev/nvme0")
if log then
    print("Erros nao lidos:", log.unread)
end
```

### 8. `storage.self_test(path)`

Retorna o resultado do ultimo *self-test* do disco.

**Parâmetros**:

`path` (string):   Caminho do dispositivo

**Retorno**:

Table ou nil com os campos (varia por protocolo):

```text
    ATA: retorna o ultimo teste da tabela de self-tests

    NVMe:  
            current_self_test_operation : string   Operacao atual
```

**Exemplo de uso**:

```lua
local test = storage.self_test("/dev/sda")
if test then
    print("Status:", test.status)
end
```

