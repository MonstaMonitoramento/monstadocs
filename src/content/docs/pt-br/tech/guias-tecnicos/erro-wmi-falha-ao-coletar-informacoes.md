---
title: "Erro WMI - Falha ao coletar informações"
---

## Problema:

Os monitores coletam algumas informações e depois falham. Os logs de erro reportam a seguinte mensagem: "**HRESULT Call failed with: 0x80041017**".

## Solução: 

O erro **0x80041017** no Windows está relacionado ao **WMI**(*Windows Management Instrumentation*) e significa **WBEM\_E\_INVALID\_QUERY**, ou seja, uma **consulta inválida** foi feita ao WMI. Esse erro costuma aparecer quando scripts ou ferramentas tentam acessar dados de desempenho ou informações do sistema, mas a consulta falha por algum motivo.

Para resolver esse problema você pode recompilar todos os contadores de desempenho, inclusive de terceiros. Para fazer isso, digite os comandos a seguir em um prompt de comando Administrativo. Pressione **ENTER** após cada comando.

- Reconstruir os contadores:

```powershell
cd c:\windows\system32
lodctr /R
cd c:\windows\sysWOW64
lodctr /R
```

- Sincronizar com o WMI:

```powershell
WINMGMT.EXE /RESYNCPERF
```

- Reiniciar serviços de Log e Alto Desempenho:

```powershell
net stop pla & net start pla
net stop winmgmt & net start winmgmt
```