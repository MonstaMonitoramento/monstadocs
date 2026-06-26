---
title: "Instalando Hyper-V"
---

Tutorial con el objetivo de mostrar el procedimiento para instalar el sistema de virtualización de Microsoft, Hyper-V, en un servidor Windows.

Hyper-V es el entorno de virtualización de servidores de Microsoft y forma parte de las versiones actuales de Windows disponibles en el mercado. Para estaciones de trabajo está disponible a partir de la versión 8 (64 bits) y para servidores está disponible a partir de la versión 2008 Server (64 bits).



:::note
La versión utilizada para este tutorial es Windows 10 Pro.
:::



## Habilitar la virtualización en la BIOS del equipo

Hyper-V requiere que el hardware donde está instalado Windows tenga soporte para virtualización para funcionar. Este recurso puede venir desactivado en algunos equipos. Para habilitarlo reinicie el equipo, acceda a su BIOS (en general mediante las teclas F1 o Delete) y active la opción de virtualización del procesador según los ejemplos siguientes:

![image-1645207744580.png](../../../../../assets/images/p20_image-1645207744580.png)

![image-1645207728181.png](../../../../../assets/images/p20_image-1645207728181.png)

Guarde los cambios y reinicie el equipo.

## Instalar Hyper-V

Inicie sesión con permisos de Administrador en Windows y ejecute el siguiente programa:

```powershell
appwiz.cpl
```

Se abrirá la ventana para administrar Programas y características.

![image-1645209739713.png](../../../../../assets/images/p20_image-1645209739713.png)

- Haga clic en la opción “Activar o desactivar las características de Windows

![image-1645209850340.png](../../../../../assets/images/p20_image-1645209850340.png)

- Marque la opción “Hyper-V” y todos sus subelementos.
- Haga clic en el botón Ok.

![image-1645209878625.png](../../../../../assets/images/p20_image-1645209878625.png)

- Haga clic en el botón “Reiniciar ahora”.

Tras reiniciar Windows, Hyper-V estará disponible.

## Añadir una interfaz de red externa

Cuando se instala Hyper-V, se crea una nueva interfaz de red llamada vEthernet, como se muestra en la imagen siguiente:

![image-1645210125370.png](../../../../../assets/images/p20_image-1645210125370.png)

  
Para crear una interfaz con acceso externo, ejecute el siguiente programa:

```powershell
virtmgmt.msc
```

Se abrirá el sistema de administración de Hyper-V. Siga los pasos a continuación:

![image-1645210155993.png](../../../../../assets/images/p20_image-1645210155993.png)

- En el menú Acciones, haga clic en “Administrador de conmutador virtual”.

![image-1645210186805.png](../../../../../assets/images/p20_image-1645210186805.png)

- Haga clic en la opción “Nuevo conmutador de red virtual”;
- Seleccione la opción “Externo”;
- Haga clic en el botón “Crear conmutador virtual”.

![image-1645210218328.png](../../../../../assets/images/p20_image-1645210218328.png)

- Escriba un nombre para el nuevo conmutador;
- En “Tipo de conexión” seleccione la opción “Red Externa” y la tarjeta de red para su conmutador;
- Haga clic en el botón “Ok” para crear el conmutador.

A partir de ahora una nueva interfaz de red estará disponible en su equipo. Si es necesario, configure las direcciones IP para esta nueva interfaz.

![image-1645210258565.png](../../../../../assets/images/p20_image-1645210258565.png)

## Instalar Monsta en un servidor Linux

¿Quiere instalar Monsta en un servidor Linux? Utilice nuestro [Manual de Instalación](/es/start/instalacao/instalacao-monsta).