---
title: "Alteração das Portas de Acesso"
---

Este guia descreve o procedimento para alterar as portas de escuta da interface web do **Monsta**. Por padrão, o sistema utiliza portas específicas que podem ser customizadas via linha de comando no servidor Linux.

## Pré-requisitos

- Acesso SSH ao servidor onde o Monsta está instalado.
- Privilégios de superusuário (`root` ou `sudo`).
- Certificar-se de que as novas portas escolhidas não estão sendo utilizadas por outros serviços (ex: Apache, Nginx, Docker).

## Procedimento Passo a Passo

1. **Acesse o Terminal**: Abra a console de seu servidor.
2. **Execute o utilitário de configuração**: Utilize o binário `monkerneld` com o parâmetro `port` para definir a nova porta HTTP e a porta SSL (HTTPS).
    
```shell
/opt/monsta/bin/monkerneld port --port <porta http> 8090 --sslport <porta https>
```
    
**Exemplo**:
```shell
/opt/monsta/bin/monkerneld port --port 8090 --sslport 8443  
```      

**Parâmetros do Comando**:
- `--port`: Define a porta para conexões não criptografadas (HTTP).
- `--sslport`: Define a porta para conexões seguras (HTTPS).

:::caution[Importante: Configuração de *Firewall*]
Após a alteração, lembre-se de liberar as novas portas no *firewall* do Linux (UFW ou Firewalld) e, se aplicável, nas regras de segurança da sua infraestrutura de rede/nuvem.
:::

