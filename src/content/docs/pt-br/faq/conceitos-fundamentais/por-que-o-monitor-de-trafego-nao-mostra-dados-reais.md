---
title: "Por que o monitor de tráfego não mostra dados reais?"
---

Ao monitorar o tráfego de rede via SNMP, nos deparamos com monitores de **32 bits** e **64 bits.** A principal diferença entre eles está na capacidade máxima de contagem.

## Monitor de Tráfego

Esse monitor utiliza uma variável de 32 bits que pode armazenar um valor máximo de 4 Gigabytes trafegados. Em um link de rede de alta velocidade, por exemplo, um link de 1 Gbps, essa contagem pode ser atingida em 32 segundos.

- **Ocorrência de rollover**: Quando essa variável ultrapassa o valor máximo, o contador retorna a zero. Essa característica é conhecida no Monsta como `rollover`.
- **Problema ocasionado**: Esse "estouro" de contador pode levar a gráficos de monitoramento como quedas abruptas, reportar velocidades incorretas ou menores que o total trafegado na interface de rede monitorada, dificultando a análise e o cálculo correto do tráfego. Com isso, o valor real do tráfego é perdido, pois dependendo da frequência com que a coleta do monitor ocorre, um rollover pode ocorrer sem ser detectado.

![image-1756919458783.png](../../../../../assets/images/p120_image-1756919458783.png)  
Exemplo de um monitor de tráfego 32 bits em um link de 1gbps com frequência de 5 minutos.

## Monitor de Tráfego (64 bits)

Esse monitor pode armazenar um valor máximo de 18 Exabytes. Esse número é tão grande que um `rollover` em links de alta velocidade é praticamente impossível de ocorrer. Por exemplo, um link de 100 Gbps levaria aproximadamente 46 anos para preencher toda a variável.

- **Maior precisão e confiabilidade**: Com o contador de 64 bits, você garante que a contagem do tráfego seja contínua e precisa, sem interrupções.
- **Análise de longo prazo**: Permite uma análise de tráfego mais precisa e confiável em períodos longos, já que o valor acumulado não é perdido.

![image-1756919778342.png](../../../../../assets/images/p120_image-1756919778342.png)

O mesmo tráfego em um monitor de 64 bits.

## Conclusão

Para gráficos reais, utilize sempre os monitores de 64 bits que possuem uma melhor precisão na medição. Entretanto, caso o equipamento que você pretende monitorar disponibilize apenas o tráfego em 32 bits, diminua a frequência da coleta de dados para um valor que se ajuste velocidade da interface de rede monitorada.
