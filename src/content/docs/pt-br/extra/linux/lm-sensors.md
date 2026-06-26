---
title: "LM Sensors - Linux"
---

![image-1740052992811.png](../../../../../assets/images/p17_image-1740052992811.png)

Tutorial com objetivo de ativar o pacote LM Sensors em distribuições Linux para monitoramento através do Monsta.



:::note
Existem diversas distribuições Linux, cada qual com suas particularidades. As informações a seguir podem não funcionar em sua distribuição.
:::



## Instalar e configurar o pacote LM Sensors

Logado como root, na tela do servidor Linux que será monitorado digite o comando abaixo:  
• Para distribuições que utilizam o yum:

```shell
yum install lm_sensors
```

• Para distribuições que utilizam o apt-get

```shell
apt-get install lm_sensors
```

Após instalado o pacote, digite o comando abaixo para detectar os sensores existentes em seu servidor e gravar o arquivo de configuração do lm-sensors:

```shell
sensors-detect --auto
```

Após finalizada a detecção dos sensores, você poderá exibir na console os itens disponíveis e suas medições através do comando sensors, conforme exemplo abaixo:

```shell
sensors
```



> coretemp-isa-0000  
> Adapter: ISA adapter  
> Physical id 0: +25.0°C (high = +82.0°C, crit = +102.0°C)  
> Core 0: +23.0°C (high = +82.0°C, crit = +102.0°C)  
> Core 1: +23.0°C (high = +82.0°C, crit = +102.0°C)  
> it8728-isa-0a30  
> Adapter: ISA adapter  
> in0: +0.91 V (min = +2.40 V, max = +0.24 V)  
> in1: +1.49 V (min = +1.68 V, max = +2.59 V)  
> in2: +2.94 V (min = +0.04 V, max = +0.18 V)  
> +3.3V: +3.43 V (min = +4.75 V, max = +3.17 V)  
> in4: +2.08 V (min = +1.73 V, max = +0.22 V)  
> in5: +1.06 V (min = +1.58 V, max = +0.01 V)  
> in6: +2.23 V (min = +0.22 V, max = +1.34 V)  
> 3VSB: +3.26 V (min = +0.05 V, max = +0.91 V)  
> Vbat: +3.19 V  
> fan1: 1165 RPM (min = 22 RPM)  
> fan3: 0 RPM (min = 249 RPM)  
> fan4: 0 RPM (min = -1 RPM)  
> fan5: 0 RPM (min = -1 RPM)  
> temp1: +14.0°C (low = -1.0°C, high = +127.0°C) sensor = thermal diode  
> temp2: -128.0°C (low = -1.0°C, high = +127.0°C) sensor = disabled  
> temp3: -78.0°C (low = -1.0°C, high = +127.0°C) sensor = Intel PECI  
> intrusion0: ALARM



## Instalar o serviço SNMP

Consulte nosso tutorial em [Configurando o SNMP no Linux](/pt-br/extra/linux/snmp-linux).

## Monsta

Para monitorar os sensores no Monsta, durante a criação do dispositivo adicione o template “LM Sensors” conforme exemplo abaixo. Com isso, ao inserir um monitor no Monsta serão mostrados os monitores referentes ao LM Sensors também.

![image-1645205747750.png](../../../../../assets/images/p17_image-1645205747750.png)
