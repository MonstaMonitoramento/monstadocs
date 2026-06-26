---
title: "Por que o Monsta Exibe uma Partição com 5% Menos de Espaço Utilizado?"
---

Essa diferença de 5% no espaço em disco de uma partição Linux, ao ser monitorada via [SNMP](/pt-br/tech/protocolos-coleta/snmp), é uma característica padrão dos sistemas de arquivos **Ext2, Ext3 e Ext4**. Ela não é um erro de cálculo, mas sim uma reserva de espaço intencional.

Essa reserva existe para garantir que o sistema continue funcionando de forma estável, mesmo quando o disco estiver quase totalmente cheio. Os 5% são reservados principalmente para o usuário **`root`**, o administrador do sistema.

Os principais motivos para essa reserva são para:

- **Evitar fragmentação de arquivos**: A reserva ajuda a garantir que o sistema de arquivos tenha espaço suficiente para alocar novos dados de forma contígua, o que melhora o desempenho.
- **Permitir o funcionamento do sistema**: Se o disco encher 100%, o sistema operacional pode travar ou se tornar inutilizável. Essa reserva garante que o `root` tenha espaço para, por exemplo, escrever logs, mover arquivos ou executar comandos essenciais para liberar espaço.

Em resumo, a diferença de 5% é uma característica do sistema de arquivos **Ext** projetada para proteção. Ela garante que o administrador tenha sempre uma margem para realizar operações críticas e manter a estabilidade do servidor.
