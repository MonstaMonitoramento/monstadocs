---
title: "Exemplos de Templates de Mensagem de Alerta"
---

Os alertas enviados pelo Monsta podem ser personalizados através dos Templates de Mensagem, disponível em Grupo de Alertas > Template de Mensagem. Este artigo demonstra alguns exemplos de personalização para melhorar as mensagens de alerta, afim de se adaptar à sua necessidade. Para entender o funcionamento dos Templates de Mensagem e como funcionam as variáveis disponíveis, veja o artigo sobre os [Alertas](/pt-br/manual/grupos-alertas/alertas#templates-de-mensagem) do Monsta.

## Utilizando variáveis de acordo com o alerta

Algumas variáveis são relacionadas ao dispositivo e outras ao monitor. Por exemplo, a variável `{{nomemetrica}}` está relacionada com um monitor. Sendo assim, ao utilizar essa variável em um alerta de dispositivo, ela será enviada vazia no alerta. Porém, é possível diferenciar no mesmo template qual será a mensagem para um alerta de dispositivo ou monitor. O código a seguir é um exemplo que utiliza esse recurso.

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Estado: {{monitor.estado}}
Dispositivo: {{dispositivo.nome}}
Monitor: {{monitor.nomecurto}}
{{nomemetrica}} ({{nomeinstancia}}): {{valor}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{/if}}
```

O que está entre `{{#if alertadispositivo}}` e o `{{else}}` refere-se à mensagem para um alerta gerado por um dispositivo (quando ele fica offline, por exemplo). O que está entre `{{else}}` e `{{/if}}` refere-se à mensagem para um alerta gerado por um monitor (quando um monitor atinge uma métrica de alerta, por exemplo). Vale citar que o campo "`>Subject:`" refere-se ao "assunto", quando o alerta é enviado por e-mail. Os alertas por Telegram e SMS não vão possuir essa informação.

O código de exemplo vai gerar os alertas a seguir (exemplos recebidos no Telegram).
- Alerta gerado por um Dispositivo que retornou do status crítico:

:::tip[Alerta]
Estado: Normal  
Dispositivo: Impressora  
IP: 192.168.10.10  
Horario: 01/01/2026 - 14:50:18
:::

- Alerta gerado por um Monitor sem instância que entrou em status crítico:

:::tip[Alerta]
Estado: Crítico  
Dispositivo: Servidor Firewall  
Monitor: Carga (Load Average)  
Carga (): 3  
IP: 192.168.10.1  
Horario: 01/01/2026 - 11:55:06
:::



- Alerta gerado por um Monitor com instância que entrou em status crítico:



:::tip[Alerta]
Estado: Crítico  
Dispositivo: Servidor de E-mails  
Monitor: Partição /home  
Partição (/home): 500 GB  
IP: 192.168.10.2  
Horario: 01/01/2026 - 12:33:46
:::



Caso não fosse utilizada a personalização para dispositivo e monitor (utilizando as configurações da mensagem dos alertas de monitor para ambos), a mensagem de alerta de um dispositivo ficaria assim:

- Alerta gerado por um Dispositivo com com as variáveis de monitores.



:::tip[Alerta]
Estado: Normal  
Dispositivo: Impressora  
Monitor:   
 (): False  
IP: 192.168.10.10  
Horario: 01/01/2026 - 14:50:18
:::



A personalização permite que a mensagem fique melhor estruturada.

## Personalizando com informações fixas

Além de utilizar as variáveis, você também pode adicionar informações que não são alteradas de acordo com o alerta, como nome da empresa, setor, responsável, número de suporte... Esses dados podem ser úteis caso você receba alertas de mais de um Monsta (para identificar de onde veio o alerta) ou até mesmo para alertas que são enviados para gerentes, fornecedores ou terceiros. Como é possível criar vários templates de mensagem, você pode criar um [Grupo de Alertas](/pt-br/manual/grupos-alertas/alertas#grupos) para um fornecedor de suprimentos de impressora que receberá um e-mail quando o toner da sua impressora estiver em status crítico. Basta configurar o template no grupo de alertas e adicionar o grupo de alertas no monitor específico.

Por exemplo:

- Template para fornecedor de suprimentos para a impressora, que pode ser utilizado exclusivamente em monitores de impressora

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Alerta da empresa Monsta
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Alerta da empresa Monsta
Nossa impressora ({{dispositivo.nome}}) está alertando que {{nomemetrica}} ({{nomeinstancia}}) está em estado {{monitor.estado}} ({{valor}}).
Por favor, envie um orçamento para suporteti@empresa.com.br
Horário: {{dataehora}}
{{/if}}
```

- Alerta gerado por um Monitor da impressora em status crítico:



:::tip[Alerta]
Alerta da empresa Monsta  
Nossa impressora (Impressora XYZ) está alertando que Toner (Toner) está em estado Crítico (10 %).  
Por favor, envie um orçamento para <suporteti@empresa.com.br> para substituição.  
Horário: 01/01/2026 - 12:33:46
:::



Exemplo da configuração do grupo de alertas, para que o destinatário receba apenas o alerta de crítico de monitores:

![image-1773337531514.png](../../../../../assets/images/p173_image-1773337531514.png)

Configuração do monitor Toner, utilizado no exemplo:

![image-1773337636144.png](../../../../../assets/images/p173_image-1773337636144.png)

Veja outro exemplo, para o caso de ter mais de um servidor Monsta e desejar identificar de qual deles veio o alerta.

- Template Monsta 1

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Monsta Matriz - Alerta Dispositivo
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Monsta Matriz - Alerta Monitor
Estado: {{monitor.estado}}
Dispositivo: {{dispositivo.nome}}
Monitor: {{monitor.nomecurto}}
{{nomemetrica}} ({{nomeinstancia}}): {{valor}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{/if}}
```

- Alerta gerado por um Dispositivo que retornou do status crítico:



:::tip[Alerta]
Monsta Matriz - Alerta Dispositivo  
Estado: Normal  
Dispositivo: Impressora  
IP: 192.168.10.10  
Horario: 01/01/2026 - 14:50:18
:::



- Alerta gerado por um Monitor com instância que entrou em status crítico:



:::tip[Alerta]
Monsta Matriz - Alerta Monitor  
Estado: Crítico  
Dispositivo: Servidor de E-mails  
Monitor: Partição /home  
Partição (/home): 500 GB  
IP: 192.168.10.2  
Horario: 01/01/2026 - 12:33:46
:::



- Template Monsta 2

```
{{#if alertadispositivo}}
> Subject: {{dispositivo.estado}}: Dispositivo {{dispositivo.nome}}.
Monsta Filial - Alerta Dispositivo
Estado: {{dispositivo.estado}}
Dispositivo: {{dispositivo.nome}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{else}}
> Subject: {{monitor.estado}}: Monitor {{dispositivo.nome}}/{{monitor.nome}}.
Monsta Filial - Alerta Monitor
Estado: {{monitor.estado}}
Dispositivo: {{dispositivo.nome}}
Monitor: {{monitor.nomecurto}}
{{nomemetrica}} ({{nomeinstancia}}): {{valor}}
IP: {{dispositivo.endereco}}
Horário: {{dataehora}}
{{/if}}
```

- Alerta gerado por um Dispositivo que retornou do status crítico:



:::tip[Alerta]
Monsta Filial - Alerta Dispositivo  
Estado: Normal  
Dispositivo: Impressora  
IP: 192.168.11.10  
Horario: 01/01/2026 - 14:50:18
:::



- Alerta gerado por um Monitor com instância que entrou em status crítico:



:::tip[Alerta]
Monsta Filial - Alerta Monitor  
Estado: Crítico  
Dispositivo: Servidor Firewall  
Monitor: Partição /home  
Partição (/home): 500 GB  
IP: 192.168.11.2  
Horario: 01/01/2026 - 12:33:46
:::



## Conclusão

Há inúmeras formas de personalizar as mensagens de alerta do Monsta. Utilize esses exemplos para explorar ideias que se adaptem ao seu cenário. Qualquer dúvida adicional, entre em contato com o nosso suporte.
