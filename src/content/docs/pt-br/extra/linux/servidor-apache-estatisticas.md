---
title: "Estatísticas para Servidor Apache (Linux)"
---

Tutorial tem como objetivo ativar uma configuração básica do Servidor Apache HTTP para monitorar. Dependendo das configurações do Apache ou do sistema operacional onde o mesmo se encontra instalado, as informações abaixo poderão não funcionar.

## Habilitando o módulo mod_stats

As estatísticas de uso do Servidor Apache HTTP estão disponíveis através do módulo mod\_stats, que em geral, já vem na maioria as instalações mas não está habilitado.  
  
Logado como root, edite o arquivo de configuração do Apache. Para saber a localização deste arquivo, digite o comando abaixo:

```shell
httpd -V | grep 'SERVER_CONFIG_FILE'
```

O seguinte resultado será exibido:

`-D SERVER_CONFIG_FILE="/etc/httpd/conf/httpd.conf"`

Com base nessas informações, o arquivo de configuração do apache se encontra em `/etc/httpd/conf/httpd.conf`. Adicione as linhas abaixo no arquivo (como sugestão, você pode adicionar ao final do arquivo):

```vim
<Location /server-status>  
SetHandler server-status  
Order Deny,Allow  
Deny from all  
</Location>  
ExtendedStatus On
```

As configurações acima permitem que qualquer host pesquise pelas estatísticas em seu servidor Apache. Para restringir as consultas ao IP do Monsta, adicione a linha abaixo antes do `</Location>`

`Allow from IP_do_Monsta`

Reinicie o Apache com o comando:

```shell
httpd -k restart
```

Com estas configurações, as estatísticas do Apache já podem ser monitoradas através do template “Apache – Servidor HTTP” do Monsta.
