---
title: "Reset da senha do usuário admin"
---

Para resetar a senha do usuário admin no Monsta é necessário logar-se no Linux com um usuário que tenha permissões de root e digitar o comando abaixo:

```shell
/opt/monsta/bin/monagent -c /opt/monsta/etc/monkerneld.ini reset-admin
```

:::note
Após esse procedimento, será possível logar no Monsta com o **usuário** `admin` e **senha** `admin`.
:::
