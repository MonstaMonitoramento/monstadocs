---
title: "Monsta Studio"
sidebar:
  order: 5
---

O Monsta Studio gerencia os mecanismos de coletas, alertas e ações do Monsta. As fontes disponibilizadas neste local estarão disponíveis para os dispositivos, monitores e grupos de alerta.

## Pantalla inicial

![image-1739987060103.png](../../../../../assets/images/p62_image-1739987060103.png)

---

![image-1739987089441.png](../../../../../assets/images/p62_image-1739987089441.png)
Listado de las fuentes disponibles y su ubicación en Monsta. 

| Item | Descrição |
| :---: | :--- |
| Métricas | Son las fuentes utilizadas en las recopilaciones de datos de los monitores. |
| Instancias | Son las fuentes utilizadas en la pestaña "Instancias" durante la creación o edición de los monitores. |
| Tiempo de actividad | Son las fuentes utilizadas para comprobar el uptime durante la creación o edición del dispositivo. |
| ![image-1739987364857.png](../../../../../assets/images/p62_image-1739987364857.png) | Categoría de la fuente. Utilizada para una mejor organización de la lista. |
| ![image-1647622602480.png](../../../../../assets/images/p62_image-1647622602480.png) | Añade una nueva fuente de datos dentro de la ubicación seleccionada. | 

## Editor de fuentes

En esta pantalla se crean o personalizan las fuentes de datos.

![image-1739987456748.png](../../../../../assets/images/p62_image-1739987456748.png)

#### Detalles

![image-1647623122977.png](../../../../../assets/images/p62_image-1647623122977.png)
Muestra la pantalla para la edición de información de la fuente, como nombres y parámetros.

| Opção / Ícone | Descrição |
| :---: | :--- |
| ![image-1739987483509.png](../../../../../assets/images/p62_image-1739987483509.png) | Selecciona un icono para la fuente en destaque. |
| **Nome** | Indica un nombre para la fuente. Ese nombre es el que se mostrará en los listados de fuentes disponibles. |
| **Descrição** | Breve comentario sobre lo que hace la fuente. |
| **Categoria** | Indica en cuál categoría se encuentra la fuente. |
| **Tipo de Retorno** | Tipo de valor retornado al final de la ejecución de la fuente. Puede ser un número, una cadena, un texto, una tabla, entre otros. |
| **Parâmetros** | Son variables configuradas para ser utilizadas por el código fuente de la programación. Es posible configurar un valor predeterminado para cada variable, así como el usuario puede modificarla durante su ejecución. |
| ![image-1739987532048.png](../../../../../assets/images/p62_image-1739987532048.png) | Nombre de la variable. |
| ![image-1739987551030.png](../../../../../assets/images/p62_image-1739987551030.png) | Tipo de valor de la variable. |
| ![image-1739987627316.png](../../../../../assets/images/p62_image-1739987627316.png) | Define un valor predeterminado para la variable. |
| ![image-1739987708487.png](../../../../../assets/images/p62_image-1739987708487.png) | Un comentario sobre la variable. Esta información aparecerá cuando el ratón esté sobre el campo de valor durante la ejecución. |
| ![image-1647624115398.png](../../../../../assets/images/p62_image-1647624115398.png) | Si está marcado, la variable deberá rellenarse obligatoriamente. |
| ![image-1647624151382.png](../../../../../assets/images/p62_image-1647624151382.png) | Si está marcado, la variable podrá ser duplicada por el usuario. |
| ![image-1647624197215.png](../../../../../assets/images/p62_image-1647624197215.png) | Posición de visualización de la variable en la lista. |
| ![image-1647624227451.png](../../../../../assets/images/p62_image-1647624227451.png) | Elimina la variable seleccionada. |

#### Código

![image-1647624338287.png](../../../../../assets/images/p62_image-1647624338287.png)
En esta opción se mostrará el editor de código de Monsta. El lenguaje de programación soportado será LUA ([https://www.lua.org](https://www.lua.org/)). Para más información sobre comandos y funciones, consulte [Scripting con LUA](/es/tech/modulos-script/script-lua) o [https://www.lua.org/manual/](https://www.lua.org/manual/). |

| Opção / Ícone | Descrição |
| :---: | :--- |
| ![image-1647625589954.png](../../../../../assets/images/p62_image-1647625589954.png) | Guarda la edición de código actual. |
| ![image-1647625628655.png](../../../../../assets/images/p62_image-1647625628655.png) | Exporta la fuente en cuestión a un archivo. |
| ![image-1647625699048.png](../../../../../assets/images/p62_image-1647625699048.png) | Elimina la fuente en cuestión. Este proceso solo está permitido si la misma no está en uso. |
| ![image-1647625745603.png](../../../../../assets/images/p62_image-1647625745603.png) | Código de identificación de la fuente para búsquedas. |
| ![image-1647625807586.png](../../../../../assets/images/p62_image-1647625807586.png) | Muestra las salidas y el retorno del script cuando se ejecuta. |
| ![image-1647625896651.png](../../../../../assets/images/p62_image-1647625896651.png) | Configura la fuente y el tamaño de los caracteres en el editor de scripts. |
| ![image-1647625957430.png](../../../../../assets/images/p62_image-1647625957430.png) | Indica el tipo de lenguaje utilizado por el script. |
| ![image-1739988046784.png](../../../../../assets/images/p62_image-1739988046784.png) | Selecciona el dispositivo en el que se ejecutará la prueba del script. |
| ![image-1739988315966.png](../../../../../assets/images/p62_image-1739988315966.png) | Permite introducir valores en los parámetros cuando existan. |
| ![image-1647625532238.png](../../../../../assets/images/p62_image-1647625532238.png) | Editor de código de Monsta. |
| ![image-1647626507459.png](../../../../../assets/images/p62_image-1647626507459.png) | Ejecuta el script con fines de prueba. |