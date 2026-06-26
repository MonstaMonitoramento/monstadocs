---
title: "Grupo de Dispositivos"
sidebar:
  order: 4
---

Monsta permite crear grupos en los que se pueden registrar dispositivos de forma individual. Los dispositivos registrados en un grupo heredan sus configuraciones, tales como usuarios, contraseñas, datos SNMP, y estas se superponen a las configuraciones globales.

Los grupos de dispositivos se utilizan para optimizar tareas rutinarias, como configuraciones, disponer para un usuario cuáles dispositivos tiene acceso o para una visualización rápida del estado general de sus dispositivos registrados.

![image-1739988728084.png](../../../../../assets/images/p65_image-1739988728084.png)

---

![image-1647884450145.png](../../../../../assets/images/p65_image-1647884450145.png)
**Nuevo grupo de dispositivos**: Crea un nuevo grupo.

---

![image-1739988753787.png](../../../../../assets/images/p65_image-1739988753787.png)
**Buscar grupos**: Filtra los grupos de acuerdo con el texto informado.

---

![image-1739988818350.png](../../../../../assets/images/p65_image-1739988818350.png)
**Caja del grupo**: Presenta el nombre del grupo y una visualización rápida sobre la cantidad de dispositivos registrados y sus estados. 

| Ícone | Descrição |
| :---: | :--- |
| ![image-1739988847442.png](../../../../../assets/images/p65_image-1739988847442.png) | Indica el total de dispositivos registrados en el grupo por estado. |
| ![image-1739988866136.png](../../../../../assets/images/p65_image-1739988866136.png) | Indica el nombre del grupo. |
| ![image-1647884315767.png](../../../../../assets/images/p65_image-1647884315767.png) | Asigna acciones que serán heredadas por el grupo. Para más información, consulte [Opciones Globales](/es/manual/dispositivos/opcoes#opciones-globales-de-dispositivos). |
| ![image-1647884360825.png](../../../../../assets/images/p65_image-1647884360825.png) | Añade un nuevo dispositivo al grupo seleccionado. |
| ![image-1647884405279.png](../../../../../assets/images/p65_image-1647884405279.png) | Abre la pantalla de edición del grupo. |



## Agregar/Editar un grupo de dispositivos

![image-1739988994615.png](../../../../../assets/images/p65_image-1739988994615.png)

### Detalles

Información básica sobre el grupo. 

| Opção | Descrição |
| :---: | :--- |
| ![image-1739989016556.png](../../../../../assets/images/p65_image-1739989016556.png) | Permite seleccionar un icono para el grupo. |
| **Nome do grupo de dispositivos** | Permite introducir un nombre para el grupo en edición. |
| **Descrição** | Un breve comentario sobre el grupo en edición. |

### Miembros
Son los dispositivos que forman parte del grupo.


| Ícone | Descrição |
| :---: | :--- |
| ![image-1739989077427.png](../../../../../assets/images/p65_image-1739989077427.png) | Listado de miembros del grupo. |
| ![image-1739989114437.png](../../../../../assets/images/p65_image-1739989114437.png) | Añade o elimina miembros seleccionados. |
| ![image-1739989148209.png](../../../../../assets/images/p65_image-1739989148209.png) | Añade o elimina todos los miembros. |

### Recopilación
Son las configuraciones de los principales métodos de búsqueda que serán heredadas por los dispositivos que forman parte del grupo. Para más información, consulte [Recopilación](/es/manual/dispositivos/novo-dispositivo#coleta).

### Sonidos de alerta
Configura los sonidos de alerta que serán heredados por los dispositivos miembros de este grupo. Para más información, consulte [Sonidos de alerta](/es/manual/dispositivos/novo-dispositivo#grupos-de-alerta).

### Sensibilidad
Define el comportamiento del tiempo de actividad (uptime) de los dispositivos miembros de este grupo. Para más información, consulte [Sensibilidad](/es/manual/dispositivos/opcoes#sensibilidade).