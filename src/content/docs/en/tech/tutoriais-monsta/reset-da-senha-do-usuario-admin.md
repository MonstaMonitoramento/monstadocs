---
title: "Reset the admin user's password"
---

To reset the admin user's password in Monsta you must log in to Linux with a user that has root permissions and run the command below:

```shell
/opt/monsta/bin/monagent -c /opt/monsta/etc/monkerneld.ini reset-admin
```

:::note
After this procedure, you will be able to log in to Monsta with the **user** `admin` and **password** `admin`.
:::