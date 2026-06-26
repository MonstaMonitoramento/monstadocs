---
title: "Monsta Studio"
sidebar:
  order: 5
---

Monsta Studio manages Monsta's collection engines, alerts and actions. The sources made available here will be available to devices, monitors and alert groups.

## Home Screen

![image-1739987060103.png](../../../../../assets/images/p62_image-1739987060103.png)

---

![image-1739987089441.png](../../../../../assets/images/p62_image-1739987089441.png)
Listing of available sources and their location in Monsta.

| Item | Descrição |
| :---: | :--- |
| Métricas | These are the sources used in monitor data collections. |
| Instâncias | These are the sources used in the "Instances" tab when creating or editing monitors. |
| Uptime | These are the sources used to check uptime when creating or editing the device. |
| ![image-1739987364857.png](../../../../../assets/images/p62_image-1739987364857.png) | Source category. Used for better organization of the list. |
| ![image-1647622602480.png](../../../../../assets/images/p62_image-1647622602480.png) | Adds a new data source within the selected location. | 

## Source Editor

On this screen data sources are created or customized.

![image-1739987456748.png](../../../../../assets/images/p62_image-1739987456748.png)

#### Details

![image-1647623122977.png](../../../../../assets/images/p62_image-1647623122977.png)
Displays the screen for editing source information, such as names and parameters.

| Opção / Ícone | Descrição |
| :---: | :--- |
| ![image-1739987483509.png](../../../../../assets/images/p62_image-1739987483509.png) | Selects an icon for the highlighted source. |
| **Nome** | Specifies a name for the source. This name is what will be shown in the available sources listings. |
| **Descrição** | Brief comment about what the source does. |
| **Categoria** | Indicates which category the source belongs to. |
| **Tipo de Retorno** | Type of value returned at the end of the source execution. It can be a number, a string, a text, a table, among others. |
| **Parâmetros** | Variables configured to be used by the source code. It is possible to set a default value for each variable, and the user can change it during execution. |
| ![image-1739987532048.png](../../../../../assets/images/p62_image-1739987532048.png) | Variable name. |
| ![image-1739987551030.png](../../../../../assets/images/p62_image-1739987551030.png) | Variable value type. |
| ![image-1739987627316.png](../../../../../assets/images/p62_image-1739987627316.png) | Sets a default value for the variable. |
| ![image-1739987708487.png](../../../../../assets/images/p62_image-1739987708487.png) | A comment about the variable. This information will appear when hovering over the value field during execution. |
| ![image-1647624115398.png](../../../../../assets/images/p62_image-1647624115398.png) | If checked, the variable must be filled in (required). |
| ![image-1647624151382.png](../../../../../assets/images/p62_image-1647624151382.png) | If checked the variable can be duplicated by the user. |
| ![image-1647624197215.png](../../../../../assets/images/p62_image-1647624197215.png) | Display position of the variable in the list. |
| ![image-1647624227451.png](../../../../../assets/images/p62_image-1647624227451.png) | Removes the selected variable. |

#### Code

![image-1647624338287.png](../../../../../assets/images/p62_image-1647624338287.png)
This option presents Monsta's code editor. The supported programming language is LUA ([https://www.lua.org](https://www.lua.org/)). For more information on commands and functions, consult [Scripting with LUA](/en/tech/modulos-script/script-lua) or [https://www.lua.org/manual/](https://www.lua.org/manual/). |

| Opção / Ícone | Descrição |
| :---: | :--- |
| ![image-1647625589954.png](../../../../../assets/images/p62_image-1647625589954.png) | Saves the current code edit. |
| ![image-1647625628655.png](../../../../../assets/images/p62_image-1647625628655.png) | Exports the highlighted source to a file. |
| ![image-1647625699048.png](../../../../../assets/images/p62_image-1647625699048.png) | Removes the highlighted source. This process is only allowed if it is not in use. |
| ![image-1647625745603.png](../../../../../assets/images/p62_image-1647625745603.png) | Source identification code for searches. |
| ![image-1647625807586.png](../../../../../assets/images/p62_image-1647625807586.png) | Displays the script outputs and return when executed. |
| ![image-1647625896651.png](../../../../../assets/images/p62_image-1647625896651.png) | Configures font and character size in the script editor. |
| ![image-1647625957430.png](../../../../../assets/images/p62_image-1647625957430.png) | Specifies the type of language used by the script. |
| ![image-1739988046784.png](../../../../../assets/images/p62_image-1739988046784.png) | Selects the device on which the script test will be executed. |
| ![image-1739988315966.png](../../../../../assets/images/p62_image-1739988315966.png) | Allows entering values for parameters when present. |
| ![image-1647625532238.png](../../../../../assets/images/p62_image-1647625532238.png) | Monsta's code editor. |
| ![image-1647626507459.png](../../../../../assets/images/p62_image-1647626507459.png) | Executes the script for testing purposes. |