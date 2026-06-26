---
title: "WMI (Instrumentación de Administración de Windows)"
sidebar:
  order: 1
---

# ¿Qué es WMI?

El *Windows Management Instrumentation* (**WMI**) es una infraestructura central para la gestión de datos y operaciones en sistemas operativos Windows. Es la implementación de WBEM (Gestión Empresarial Basada en la Web) de Microsoft y proporciona una interfaz estandarizada para que administradores y aplicaciones puedan supervisar, controlar y configurar diversos aspectos del entorno Windows, desde información de hardware y software hasta el estado de los servicios y procesos del sistema. Esta capacidad de “instrumentar” el sistema permite la automatización de tareas administrativas y facilita el diagnóstico y la resolución de problemas de forma centralizada.

## Objetivos y Funcionalidades

WMI fue diseñado para proporcionar:

- **Gestión Centralizada**: Una manera uniforme de acceder a la información de configuración y estado de los sistemas Windows.
- **Automatización**: Capacidad para crear scripts y aplicaciones que supervisan eventos, realizan consultas y efectúan cambios de forma automatizada.
- **Monitorización**: Obtención en tiempo real de datos sobre procesos, servicios, hardware, red y otros componentes del sistema.
- **Interacción con los Elementos del Sistema**: Operaciones de lectura y modificación de datos del sistema, incluyendo la ejecución de métodos y scripts para mantenimiento y configuración.

Con este enfoque, WMI sirve como una herramienta poderosa para administradores de sistemas, integradores de soluciones y desarrolladores que necesitan supervisar y gestionar entornos de TI.

## Historia y Evolución

WMI fue introducido por Microsoft con la intención de estandarizar el acceso a la información de gestión del sistema. Desde su primera versión en Windows NT y su evolución a partir de Windows 2000, WMI se convirtió en parte integrante de las estrategias de gestión de Microsoft. Su desarrollo se basa en el Common Information Model (CIM), un estándar que unifica la forma de representar dispositivos y servicios en entornos heterogéneos.

Históricamente, WMI ha evolucionado para ofrecer mejor rendimiento, nuevas funcionalidades y mayor integración con otras tecnologías de gestión, permitiendo una mayor amplitud de acciones administrativas y de monitorización.

**MI (Infraestructura de Gestión)**: La próxima generación de WMI, conocida como MI (Infraestructura de Gestión), ofrece recursos y beneficios adicionales para la creación y desarrollo de proveedores y clientes WMI.

## Arquitectura del WMI

La arquitectura de WMI es robusta y está construida sobre varios componentes que trabajan de forma integrada para proporcionar sus funcionalidades.

### Componentes principales

- **WMI Service (winmgmt)**: Es el servicio central que actúa como el “orquestador” de WMI. Gestiona las solicitudes de los clientes, distribuye consultas y coordina la comunicación con los proveedores de datos.
- **Repositorio CIM (Common Information Model)**: Este repositorio contiene una representación estandarizada de los datos del sistema. Las clases CIM sirven como modelos para la información que WMI expone, garantizando consistencia e interoperabilidad con otros sistemas de gestión.
- **Clientes WMI**: Son las aplicaciones o scripts que realizan consultas y comandos vía WMI. Ejemplos incluyen el símbolo del sistema (usando `wmic`), scripts en PowerShell y aplicaciones desarrolladas en varios lenguajes que utilicen las APIs de WMI.

### WMI Providers

Los *Proveedores* son componentes que “traducen” las solicitudes hechas vía WMI a comandos específicos del hardware o software. Cada proveedor es responsable de un área del sistema (por ejemplo, gestión de procesos, información de red, dispositivos de almacenamiento) y recopila los datos necesarios para responder a las consultas de los clientes.

### Repositorio CIM y el Modelado de Datos

El modelo CIM define una estructura jerárquica y estandarizada para representar los datos del sistema. A través de él, WMI organiza la información en clases – por ejemplo, `Win32_Process` para procesos en ejecución, `Win32_OperatingSystem` para información del sistema operativo, entre otras. Esta estandarización facilita la creación de consultas coherentes y la integración con otras herramientas de gestión.

### WMI Query Language (WQL)

WMI utiliza la WMI Query Language (WQL), que es similar al lenguaje SQL, pero adaptada para la gestión de información del sistema. Con WQL, es posible realizar consultas como:

```sql
SELECT * FROM Win32_Process WHERE Name = 'notepad.exe'
```

Esta consulta devuelve información sobre procesos cuyo nombre es “notepad.exe”. Además, WQL permite la creación de consultas para la monitorización de eventos. Por ejemplo, se puede definir una consulta que desencadene una acción siempre que se inicie un nuevo proceso o se detenga un servicio.

## Uso de WMI

Acceso mediante herramientas de línea de comandos y scripts

- **WMIC (Windows Management Instrumentation Command-line)**: Herramienta de línea de comandos que permite ejecutar consultas, extraer información y ejecutar métodos vía WMI. Ejemplo:    
    ```powershell
    wmic process list brief
    
    ```
- **PowerShell**: Cmdlets como `Get-WmiObject` (en versiones anteriores) y `Get-CimInstance` (en las versiones más recientes) permiten el acceso a los datos de WMI. Ejemplo con PowerShell:
    
    ```powershell
    Get-WmiObject -Query "SELECT * FROM Win32_OperatingSystem"
    ```
- **VBScript, C#, Python (usando bibliotecas como pywin32)**: Diversos lenguajes de programación pueden interactuar con WMI, lo que lo hace accesible para scripts personalizados que automatizan tareas administrativas.

## Cómo Monsta recopila los recursos proporcionados por WMI

Monsta cuenta con una sonda de desarrollo propio que accede directamente a las APIs de WMI para recopilar la información solicitada por la plataforma de monitorización. La sonda se instala directamente en el servidor o estación de trabajo que se desea monitorizar y su funcionamiento es pasivo; es decir, recibe solicitudes por un puerto, procesa la información y la devuelve por la misma conexión.

Para descargar e instalar la sonda en sus servidores/estaciones, utilice nuestro tutorial [Sonda: Monitorización de Windows](/es/start/instalacao/sonda-windows) para monitorizar su entorno Microsoft.