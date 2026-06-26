---
title: Sincronizando a Hora em Servidores Linux
sidebar:
  order: 11
---
A maneira mais recomendada para servidores é usar **NTP** para garantir que a hora seja sempre precisa e sincronizada com fontes externas. Vamos abordar abaixo o método recomendado para efetuar essa configuração.

## Utilizando o `chrony` (Recomendado para Sincronização Mais Precisa)

O `chrony` é frequentemente usado em máquinas virtuais ou ambientes com tempo de rede variável. É comum em RHEL/CentOS 7+ e algumas instalações Ubuntu e Debian.

1. **Instale `chrony` (se necessário)**:

   * **Debian/Ubuntu**: `sudo apt update && sudo apt install chrony`
   * **RHEL/CentOS/Fedora**: `sudo dnf install chrony` ou `sudo yum install chrony`
2. **Inicie e Habilite o Serviço**:

   ```shell
   sudo systemctl enable --now chronyd  
   # ou chrony para Debian/Ubuntu
   ```
3. **Verifique a Sincronização**:

   ```shell
   chronyc tracking
   ```
   Procure por um **`Reference ID`** e um **`Stratum`** diferente de zero. O **`System time`** mostrará o offset.
  

---

## Definir Fuso Horário

Primeiro, defina o **fuso horário** correto, pois isso afeta o relógio do sistema.

1. **Liste os Fusos Horários**:

   ```shell
   timedatectl list-timezones | grep 'America/Sao_Paulo'
   ```
   (Substitua pelo fuso horário desejado)

2. **Defina o Fuso Horário**: 

   ```shell
   sudo timedatectl set-timezone 'America/Sao_Paulo'
   ```
3. **Verifique se a hora está correta**:
   ```shell
   date
   ```
   
## Sincronizar Relógio do Hardware (CMOS/BIOS)

O servidor Linux mantém dois relógios: o **Relógio do Sistema** (software) e o **Relógio do Hardware/BIOS** (CMOS, bateria mantida). Depois de corrigir o relógio do sistema, sincronize-o com o relógio do hardware para que a hora permaneça correta após uma reinicialização.

```shell
sudo hwclock -w  # Escreve a hora do Sistema (soft) para o Hardware (hard)
```
