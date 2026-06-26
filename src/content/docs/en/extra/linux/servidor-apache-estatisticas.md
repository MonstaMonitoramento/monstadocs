---
title: "Apache Server Statistics (Linux)"
---

This tutorial aims to enable a basic configuration of the Apache HTTP Server for monitoring. Depending on the Apache configuration or the operating system where it is installed, the information below may not work.

## Enabling the mod\_stats module

Apache HTTP Server usage statistics are available through the mod\_stats module, which generally comes with most installations but is not enabled.  
  
Logged in as root, edit the Apache configuration file. To find the location of this file, run the command below:

```shell
httpd -V | grep 'SERVER_CONFIG_FILE'
```

The following result will be displayed:

`-D SERVER_CONFIG_FILE="/etc/httpd/conf/httpd.conf"`

Based on this information, the Apache configuration file is located at `/etc/httpd/conf/httpd.conf`. Add the lines below to the file (as a suggestion, you can add them at the end of the file):

```vim
<Location /server-status>  
SetHandler server-status  
Order Deny,Allow  
Deny from all  
</Location>  
ExtendedStatus On
```

The above settings allow any host to query the statistics on your Apache server. To restrict queries to the Monsta IP, add the line below before the `</Location>`

`Allow from IP_do_Monsta`

Restart Apache with the command:

```shell
httpd -k restart
```

With these settings, Apache statistics can already be monitored through Monsta's "Apache – HTTP Server" template.