---
title: "Como atualizar o Monsta da v4 para a v5?"
---

A **versão 5 (v5)** do Monsta representa uma reformulação completa do núcleo do sistema (*core*), oferecendo novas funcionalidades e maior eficiência em comparação com a versão anterior (v4).

## Por que atualizar?

O suporte à v4 foi **descontinuado** com o lançamento da v5. Manter o Monsta desatualizado pode causar problemas críticos de compatibilidade e operação:

- **Validação da Licença**: A v4 não é compatível com o novo modelo de assinaturas. Para aplicar ou renovar a licença, é obrigatório possuir o Monsta na v5.
- **Importação de Templates**: Novos templates solicitados ao suporte são sempre fornecidos na **última versão oficial**. Templates da v5 **não podem ser importados** na v4, devido à incompatibilidade de arquivos.

É fundamental atualizar seu Monsta para a v5 para garantir a continuidade e a validade do seu monitoramento.

Se o seu Monsta não exibir a nova atualização em **Configuração &gt; Atualização**, pode ter ocorrido um erro que impede a detecção. Siga os passos abaixo para tentar resolver o problema.

## (Opcional) Backup completo

O processo de atualização é **seguro** e não afeta o banco de dados do histórico de monitoramento (gráficos). No entanto, para máxima garantia de preservação de dados, recomendamos um **backup completo**. O backup na nuvem salva apenas as configurações do Monsta.

## Opções de Backup Completo

1. **Máquina Virtual (VM)**: Se o Monsta estiver instalado em um Linux dentro de uma VM, o método mais simples é criar uma cópia (clone) completa da máquina virtual.
2. **Servidor Físico ou Backup Manual**: Se não for possível clonar a VM ou se a instalação estiver em um servidor físico, siga estes passos: 
    1. Verifique a versão do seu Monsta em **Configuração &gt; Sobre o Monsta**
    2. Pare o Monsta:   
        **\#v4.1.18 ou inferior**  
        `service monsta stop`  
        **\#4.1.19**  
        `systemctl stop monsta-com.*`
    3. Com o Monsta parado, copie as pastas: `/var/monsta` e `/opt/monsta`

## Verificando os logs

Um problema conhecido que pode bloquear a atualização é uma falha na rotação de logs do Linux, resultando em um acúmulo excessivo de arquivos de log do `monstadb` que sobrecarrega o servidor.

1. Acesse o diretório de logs do Monsta:  
    `cd /var/log/monsta`
2. Verifique a quantidade de logs do `monstadb`:  
    \- Execute o comando para contar os arquivos de log do monstadb. Se houver **centenas/milhares** de arquivos, a correção é necessária. Nota: Você pode também utilizar o comando `ls -la` para ver os arquivos do diretório.  
    `ls -la monstadb.log* | wc -l`
3. Pare o serviço do Monsta (use o comando adequado conforme a versão, como descrito no item 2.2 da seção de Backup completo.)
4. Exclua os arquivos do `monstadb.log`:  
    `rm -f monstadb.log.*`  
    `rm -f monstadb.log-*`  
    Nota: se ocorrer o erro "lista de argumentos muito longa" no comando `rm -f monstadb.log.*`, use o comando a seguir:  
    `printf '%s\0' monstadb.log.* | xargs -0 rm -v`
5. Utilize o `ls -la` para verificar se os arquivos foram removidos
6. Inicie novamente o Monsta  
    **\#v4.1.18 ou inferior**  
    `service monsta start`
    
    **\#V4.1.19**  
    `systemctl start monsta-com.nginx`  
    `systemctl start monsta-com.monstadb`  
    `systemctl start monsta-com.monstad`  
    `systemctl start monsta-com.moncored`  
    `systemctl start monsta-com.monagentd`  
    `systemctl start monsta-com.monstaupd`

## Atualizando

Após iniciar os serviços, acesse a interface web do Monsta e verifique se a atualização está disponível. Dependendo de sua versão atual (ex: 4.1.16 ou 4.1.18), o Monsta pode primeiro atualizar para a 4.1.19 (o que causará uma reinicialização) e, em seguida, permitir a atualização final para a v5.

Acompanhe o progresso em tempo real pelo log:

`tail -f /var/log/monstaupd.log`

(use `Ctrl + C` para parar o comando `tail`)

:::tip
Durante a atualização, a tela da interface web pode **não se atualizar automaticamente**. Após alguns minutos, tente acessar novamente o endereço do seu Monsta para visualizar a tela de login.
:::

## Não há problemas nos logs e mesmo assim não aparece a atualização

Se a correção dos logs não resolver e a atualização para a v5 não aparecer, por favor, entre em contato com o **suporte** técnico. Nossos especialistas poderão analisar a causa-raiz. **Será solicitado acesso à interface web e ao Linux do seu Monsta** para que a equipe possa diagnosticar e resolver o problema diretamente.

