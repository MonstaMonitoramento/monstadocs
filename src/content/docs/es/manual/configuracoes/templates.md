---
title: "Plantillas"
sidebar:
  order: 2
---

Plantilla es el conjunto de recursos que pueden monitorizarse en un dispositivo. Cada fabricante proporciona sus propios recursos por equipo.

## Plantillas

![image-1647448202544.png](../../../../../assets/images/p61_image-1647448202544.png)

---

![image-1647448799678.png](../../../../../assets/images/p61_image-1647448799678.png)
**Importar Plantillas**: Permite seleccionar un archivo de plantilla para importar. 

---

![image-1647448005833.png](../../../../../assets/images/p61_image-1647448005833.png)
**Filtro de búsqueda**: Cuando se utiliza, muestra solo las plantillas que contienen ese texto en su nombre.

---

![image-1647448121838.png](../../../../../assets/images/p61_image-1647448121838.png)
**Nueva Plantilla**: Crea una nueva plantilla. Consulte [Crear/Editar una Plantilla](#creareditar-una-plantilla) para más información.

---

![image-1647448227188.png](../../../../../assets/images/p61_image-1647448227188.png)
**Lista de Plantillas**: Presenta una lista con todas las plantillas disponibles en el sistema.

---

![image-1739983220633.png](../../../../../assets/images/p61_image-1739983220633.png)
**Caja de Plantilla**: Presentación visual de la plantilla. Al hacer clic sobre ella, el usuario es redirigido a la pantalla de sus monitores. 

| Icono | Descripción |
| :---: | :--- |
| ![image-1647448422172.png](../../../../../assets/images/p61_image-1647448422172.png) | **Eliminar**: Elimina la plantilla seleccionada. |
| ![image-1647448460969.png](../../../../../assets/images/p61_image-1647448460969.png) | **Editar**: Edita las propiedades de la plantilla, como nombre, descripción e icono. |

### Crear/Editar una Plantilla

<a id="criareditar-um-template"></a>
![image-1647450145680.png](../../../../../assets/images/p61_image-1647450145680.png)

| Opción | Descripción |
| :---: | :--- |
| ![image-1647450183069.png](../../../../../assets/images/p61_image-1647450183069.png) | **Icono de la Plantilla**: Permite seleccionar un icono para la plantilla desde una biblioteca ya existente o a partir de una nueva imagen. |
| **Nombre** | Nombre dado a la plantilla. |
| **Descripción** | Una breve descripción sobre la plantilla. |

## Monitores

Los monitores son componentes del sistema que comprueban un recurso determinado en un dispositivo y devuelven su estado actual. Son ellos los que generan información y alertan sobre posibles anomalías.

![image-1739984216883.png](../../../../../assets/images/p61_image-1739984216883.png)

---

---

![image-1739984247217.png](../../../../../assets/images/p61_image-1739984247217.png)
**Nombre de la Plantilla**: Indica el nombre de la plantilla seleccionada.

---

![image-1739984391202.png](../../../../../assets/images/p61_image-1739984391202.png)
**Exportar**: Exporta los monitores seleccionados a un archivo.

---

![image-1739984511244.png](../../../../../assets/images/p61_image-1739984511244.png)
**Editar Plantilla**: Edita las propiedades de la plantilla, como nombre, descripción e icono.

---

![image-1647449193273.png](../../../../../assets/images/p61_image-1647449193273.png)
**Filtro de búsqueda**: Cuando se utiliza, muestra solo los monitores que contienen ese texto en su nombre.

---

![image-1647449307274.png](../../../../../assets/images/p61_image-1647449307274.png)
**Nuevo Monitor**: Crea un nuevo monitor para la plantilla seleccionada. Para más información, consulte xxxxxxx.

---

![image-1647449372287.png](../../../../../assets/images/p61_image-1647449372287.png)
**Lista de Monitores**: Presenta una lista con todos los monitores disponibles para la plantilla seleccionada. Hacer clic en un monitor permite editarlo. 

| Icono | Descripción |
| :---: | :--- |
| ![image-1647449752980.png](../../../../../assets/images/p61_image-1647449752980.png) | **Clonar**: Clona el monitor a una plantilla seleccionada. |
| ![image-1647449785056.png](../../../../../assets/images/p61_image-1647449785056.png) | **Eliminar**: Elimina el monitor seleccionado. | 


### Crear/Editar un Monitor

#### Monitor

En esta pantalla se configuran los datos básicos del monitor.

![image-1769000706570.png](../../../../../assets/images/p61_image-1769000706570.png)

| Opción | Descripción |
| :---: | :--- |
| ![image-1739984579878.png](../../../../../assets/images/p61_image-1739984579878.png) | **Icono**: Permite seleccionar un icono para la plantilla desde una biblioteca ya existente o a partir de una nueva imagen y también sirve como vista previa de cómo se mostrará el monitor en la pantalla. |
| **Nombre Corto** | Información sobre el monitor que se muestra en el icono de la pantalla de dispositivos. |
| **Nombre** | Información sobre el monitor que se muestra en la pantalla de plantillas. |
| **Descripción** | Es una breve información sobre el monitor. Este texto se mostrará al pasar el ratón sobre los monitores de un dispositivo. |
| **Intervalo de Verificación** | Selecciona el tiempo de verificación del monitor. <aside class="starlight-aside starlight-aside--caution">Si este valor es mayor de 59 segundos, cuando una métrica salga del estado normal, el intervalo de verificación pasará a ser, automáticamente, cada 1 minuto.</aside> |
| **Número de Intentos** | Número de comprobaciones que se realizarán después de que el valor del monitor supere su límite de normalidad para, posteriormente, cambiar su estado. |
| ![image-1769000749924.png](../../../../../assets/images/p61_image-1769000749924.png) | Al editar un monitor y hacer clic en este botón, el sistema permite replicar los cambios en otros dispositivos simultáneamente. Tras hacer clic, seleccione en la lista los dispositivos que deben recibir la nueva configuración. |



#### Instancias

En esta pantalla se indica el método de listado de las instancias de un recurso, por ejemplo, la lista de interfaces de red de un equipo.

![image-1739984753223.png](../../../../../assets/images/p61_image-1739984753223.png)

| Opción | Descripción |
| :---: | :--- |
| ![image-1647535774368.png](../../../../../assets/images/p61_image-1647535774368.png) | **Activar Instancias**: Activa la selección de instancias para el monitor. |
| ![image-1647535820722.png](../../../../../assets/images/p61_image-1647535820722.png) | **Método de búsqueda**: Método de búsqueda utilizado para localizar las instancias. |
| **Fijar OID** | Cuando está deshabilitado, Monsta verifica si el nombre de la instancia sigue en la misma OID. Pueden ocurrir las siguientes situaciones:<br />- **OID igual**: Monsta recoge los valores en la misma posición;<br />- **OID diferente**: Monsta descubre la nueva OID y recogerá los valores en la nueva posición;<br />Cuando está habilitado, Monsta recogerá la información siempre en la misma posición, independientemente de si la instancia cambió de OID. |
| **OIDDesc y Nombre** | Esta opción permite que el monitor identifique automáticamente múltiples componentes de un mismo dispositivo (como diferentes interfaces de red, discos o particiones). El sistema utiliza scripts de **Monsta Studio** para listar estos elementos. En los parámetros, define las propiedades deseadas (como OIDs o filtros) para extraer exactamente los datos que se mostrarán en la lista de selección. |



### Métricas

En esta pantalla se configura la forma de recolección de los recursos del dispositivo.

![image-1769002820448.png](../../../../../assets/images/p61_image-1769002820448.png)

---

![image-1647537210606.png](../../../../../assets/images/p61_image-1647537210606.png)
**Métrica**: Indica el nombre de la métrica y su posición en el gráfico. La métrica superior de la lista tiene su gráfico superpuesto por la métrica inferior. 

| Icono | Descripción |
| :---: | :--- |
![image-1647537418530.png](../../../../../assets/images/p61_image-1647537418530.png) | **Ordenación**: Alterna la posición de la métrica para mostrarse en el gráfico. | 
![image-1647537403522.png](../../../../../assets/images/p61_image-1647537403522.png) | **Eliminar**: Elimina la métrica seleccionada. | 

---

![image-1647537518634.png](../../../../../assets/images/p61_image-1647537518634.png)
**Añadir**: Añade una nueva métrica.

---

![image-1647537560886.png](../../../../../assets/images/p61_image-1647537560886.png)
**Fuente de datos para el valor**: Configura la forma de recolección de datos de la métrica. Este es el valor que se mostrará en el gráfico.

---

![image-1647538051533.png](../../../../../assets/images/p61_image-1647538051533.png)
**Fuente de datos para el valor máximo**: Método para obtener el valor máximo de la métrica. Este valor se utilizará para el cálculo del porcentaje que se empleará en los límites de alerta.

---

![image-1647538111673.png](../../../../../assets/images/p61_image-1647538111673.png)
**Color**: Color de la métrica que se presentará al acceder a su gráfico.

---

![image-1647538237011.png](../../../../../assets/images/p61_image-1647538237011.png)
**Nombre**: Nombre de la métrica que se presentará al acceder a su gráfico.

---

![image-1739986248546.png](../../../../../assets/images/p61_image-1739986248546.png)
**Unidad**: Unidad de medida de la métrica.

---

![image-1647538419774.png](../../../../../assets/images/p61_image-1647538419774.png)
**Rellenar**: Permite seleccionar si el gráfico de la métrica debe rellenarse. Si esta opción no está seleccionada, el gráfico de esta métrica mostrará solo una línea para las lecturas.

---

![image-1647538571119.png](../../../../../assets/images/p61_image-1647538571119.png)
**Tipo de valor**: Indica el tipo de valor que devuelve la métrica. La elección de esta propiedad define el tipo de gráfico que se mostrará.

---

![image-1739986284648.png](../../../../../assets/images/p61_image-1739986284648.png)
**Desactivar límites**: Desactiva los límites para la métrica. Al activar esta opción, el estado de la métrica siempre será "Normal" y nunca generará alarmas.

---

![image-1647539136617.png](../../../../../assets/images/p61_image-1647539136617.png)
**Porcentaje de límites de alerta**: En monitores que tienen un valor máximo definido, se muestra la barra porcentual. Permite visualizar y definir rápidamente los límites establecidos para los estados de la métrica.

:::note
Disponible cuando hay un valor máximo configurado.
:::

| Opción | Descripción |
| :---: | :--- |
| ![image-1647539259537.png](../../../../../assets/images/p61_image-1647539259537.png) | **Invertir**: Invierte el porcentaje de alerta. Por defecto, un valor menor se considerará mejor. |
| ![image-1647539419645.png](../../../../../assets/images/p61_image-1647539419645.png) | **Barra de porcentajes**: Permite configurar visualmente los límites de alerta. Arrastre los selectores para determinar los porcentajes de uso que activan los estados de "Advertencia" y "Crítico". |
| ![image-1647539324004.png](../../../../../assets/images/p61_image-1647539324004.png) | **Valores de los porcentajes**: Debajo de la barra porcentual, el sistema muestra el valor numérico exacto correspondiente a la posición de los marcadores. |

---

![image-1647539661996.png](../../../../../assets/images/p61_image-1647539661996.png)
**Valores de los límites de alerta**: En monitores sin un valor máximo preestablecido, el usuario tiene la libertad de indicar manualmente los valores numéricos para los estados de **Advertencia** y **Crítico**.

:::note
Disponible cuando no hay un valor máximo configurado.
:::

| Opción | Descripción |
| :---: | :--- |
| ![image-1647539740732.png](../../../../../assets/images/p61_image-1647539740732.png) | **Valor de Advertencia**: Define la condición para que la métrica entre en estado de advertencia. |
| ![image-1647539844543.png](../../../../../assets/images/p61_image-1647539844543.png) | **Valor Crítico**: Define la condición para que la métrica entre en estado crítico. |

---


![image-1739986395801.png](../../../../../assets/images/p61_image-1739986395801.png)
**Fuente de Datos**: Permite seleccionar una fuente de recolección existente y, si es necesario, completar los valores solicitados por la misma.

| Opción | Descripción |
| :---: | :--- |
| ![image-1647540152635.png](../../../../../assets/images/p61_image-1647540152635.png) | **Botón Probar**: Prueba la fuente contra un dispositivo seleccionado. |
| ![image-1647540263038.png](../../../../../assets/images/p61_image-1647540263038.png) | **Botón Eliminar**: Elimina la fuente de datos del valor seleccionado. |
| **Colector** | **Campo Colector**: Selecciona el método que se utilizará para la recolección de datos del monitor. |
| **Parámetros** | **Campo Parámetros**: Permite proporcionar los datos para los parámetros seleccionados. Parámetros con un "\*" al lado indican que su cumplimentación al añadir un monitor será obligatoria. |

---

![image-1647539918188.png](../../../../../assets/images/p61_image-1647539918188.png)
**Scripts Personalizados**: Permite seleccionar la fuente de datos de la recolección. En esta pantalla es posible utilizar scripts en el lenguaje LUA para las métricas.

| Opción | Descripción |
| :---: | :--- |
| ![image-1647540152635.png](../../../../../assets/images/p61_image-1647540152635.png) | **Botón Probar**: Prueba el script contra un dispositivo seleccionado. |
| ![image-1647540263038.png](../../../../../assets/images/p61_image-1647540263038.png) | **Botón Eliminar**: Elimina la fuente de datos del valor seleccionado. |
| **Abrir en el Editor** | **Botón Abrir en el editor**: Abre un editor avanzado de desarrollo para el script. |

---

### Parámetros

En esta pantalla es posible crear parámetros con valores predefinidos para ser utilizados por las fuentes de datos de las métricas. Esta opción es útil cuando un monitor tiene varias métricas que usan la misma información, como un usuario y contraseña para autenticación, por ejemplo.

![image-1739986497220.png](../../../../../assets/images/p61_image-1739986497220.png)

| Opción | Descripción |
| :---: | :--- |
| ![image-1739986525205.png](../../../../../assets/images/p61_image-1739986525205.png) | **Nombre**: Define un nombre para el parámetro. |
| ![image-1739986588973.png](../../../../../assets/images/p61_image-1739986588973.png) | **Tipo**: Es el tipo de información que debe recibir el parámetro. El tipo "Opción" mostrará una lista proveniente de la pestaña "Instancias". |
| ![image-1739986692649.png](../../../../../assets/images/p61_image-1739986692649.png) | **Valor predeterminado**: Define un valor predeterminado para el parámetro al crear el monitor. Esta opción no está disponible para el tipo "Opción". |
| ![image-1739986788958.png](../../../../../assets/images/p61_image-1739986788958.png) | **Descripción del campo**: Es el texto que se mostrará al usuario durante la adición de monitores a los dispositivos. |
| ![image-1647546204637.png](../../../../../assets/images/p61_image-1647546204637.png) | **Opción de Campo Obligatorio**: Exige que el parámetro tenga algún valor. No se permiten campos en blanco. |
| ![image-1647546282966.png](../../../../../assets/images/p61_image-1647546282966.png) | **Opción de Campo que se repite**: Permite al usuario insertar el mismo campo varias veces con valores diferentes. |
| ![image-1647546340415.png](../../../../../assets/images/p61_image-1647546340415.png) | **Posición**: Alterna la posición del parámetro en la lista. |
| ![image-1647546392820.png](../../../../../assets/images/p61_image-1647546392820.png) | **Botón Eliminar**: Elimina el parámetro seleccionado. |


:::caution[Importante]
Al crear o personalizar un monitor, cuando el tipo sea "Opción" y el método seleccionado sea "Scripts", el retorno deberá ser una tabla con el siguiente formato:

`local ret = { display = "Texto", instanceId = "valor" }`

- Asegúrese de que `instanceId` sea único (sin repeticiones).
- Nombre la variable como `exec.instance`. Esto posibilita el reaprovechamiento en **monitores automáticos** y la **clonación de métricas**.
:::

:::danger[Atención]
El uso obligatorio del nombre de variable `exec.instance` es un requisito previo para la automatización. Si se utiliza otro nombre, los **monitores automáticos no funcionarán correctamente** y la **clonación de métricas no estará disponible**.
:::

Ejemplo:

```lua
local opts = {
    host = "192.168.1.1",
    username = "user",
    password = "password",
    command = "ls /backup/*.sql"
}
local ret = {}

local list = string.split(ssh.exec(opts),"\n")

for i, arq in pairs(list)
do
  local name = string.split(arq,"//")[2]
  table.insert(ret,{display=name,instanceId=i})
end

return ret
```