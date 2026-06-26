---
title: "Monitorando a Qualidade do Link de Internet: Inversão dos Limites de Alerta"
---

Ao monitorar a velocidade ou o desempenho do seu link de internet (como o *throughput*), você quer ser alertado quando a velocidade **cair abaixo de um valor aceitável**.

Os monitores de tráfego no Monsta, por padrão, assumem que **quanto mais alto o valor, pior é o problema.** Mas você pode inverter essa lógica para monitorar o seu link para trabalhar com: **quanto mais baixo o valor, pior é o problema**.

Utilize a funcionalidade **Inverter Limites** para aplicar essa lógica:

## Invertendo a Lógica

Para garantir que você receba alertas quando a velocidade cair abaixo do mínimo aceitável, siga estes passos:

- Clique sobre o monitor de tráfego;
- Clique no botão "Editar";
- Clique sobre o botão "Inverter Limites"  
    ![image-1765802497808.png](../../../../../assets/images/p144_image-1765802497808.png)
- Ajuste as barras de percentual para escolher os limites no qual você deseja ser alertado.

No exemplo da imagem acima, o monitor está ajustado para alertar sobre um link de 1G nas seguintes situações:



| Campo | Exemplo de Valor | Objetivo |
| --- | --- | --- |
| **Limite Crítico** | 2% | O Monsta enviará alerta de estado crítico se o tráfego ficar **abaixo ou igual** a 20 Mbps. |
| **Limite de Aviso** | 8% | O Monsta enviará alerta de de aviso se o tráfego ficar **entre** 80 Mbps e **acima** de 20Mbps. |



Após definir seus limites, clique no botão **Salvar para gravar suas alterações**.