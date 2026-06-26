---
title: "É possível utilizar o particionamento padrão do Linux para o Monsta?"
sidebar:
  order: 2
---

:::caution[Atenção]
Nossa recomendação é enfaticamente que NÃO seja utilizado o particionamento padrão/automático do Linux para a instalação do Monsta.
:::

O particionamento padrão, embora conveniente, não é otimizado para o perfil de uso e as necessidades de crescimento do software Monsta. Recomendamos sempre o **particionamento manual** para garantir a alocação correta de espaço e a flexibilidade futura.

A seguir, explicamos os principais motivos pelos quais o particionamento padrão não é ideal.

---

## 1. 🏡 Alocação Ineficiente para `/home`

  
Muitos assistentes de instalação de distribuições Linux são configurados para uso pessoal (desktops) e, por isso, tendem a alocar um **espaço considerável e generoso para a partição `/home`**.

- **Problema**: O Monsta é um sistema de software que não depende do diretório `/home` para seu funcionamento principal ou armazenamento de dados de alto volume. O espaço alocado para `/home` acabará sendo **subutilizado**, enquanto outras áreas cruciais podem ficar com pouco espaço.
- **Recomendação**: Priorizar o espaço para diretórios onde os dados do sistema e do Monsta realmente residem.

## 2. 🗃️ Partição `/var` Subdimensionada ou Ausente

  
A partição `/var` é de **importância crítica** para o Monsta, pois é o local padrão onde os bancos de dados e *logs* do sistema são armazenados.

- **Problema**: Alguns particionadores automáticos podem **não criar uma partição separada para `/var`** ou alocar um volume muito pequeno para ela. Com a utilização intensiva de bancos de dados pelo Monsta, essa partição pode esgotar rapidamente seu espaço, levando a falhas operacionais e de armazenamento de dados.
- **Recomendação**: Criar a partição `/var` separadamente e garantir que ela tenha o **maior volume de espaço** alocado, considerando o crescimento dos dados ao longo do tempo.

## 3. 📉 Falta de Flexibilidade com LVM

  
Muitos sistemas padrão podem não configurar as partições utilizando o **Logical Volume Manager (LVM)**.

- **Problema**: O LVM é uma camada de abstração que permite o gerenciamento e a manipulação flexível dos volumes de disco. **Sem o LVM**, será impossível, ou extremamente difícil, **aumentar o tamanho** de uma partição (como `/var`) se ela começar a ficar sem espaço no futuro, exigindo a parada do sistema e, potencialmente, a migração de dados.
- **Recomendação**: Utilizar o **LVM** ao criar as partições, especialmente para `/var`e `/` para garantir a capacidade de **expansão futura** sem *downtime* complexo.

---

:::tip
Para garantir a **performance**, **estabilidade** e **capacidade de expansão** do seu sistema, recomendamos que seja realizado um **particionamento manual** seguindo as diretrizes específicas de instalação que priorizam o espaço para as partições `/var`, `/` e que utilizem LVM.
:::