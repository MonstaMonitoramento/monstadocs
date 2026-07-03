---
title: Visualización de Monitores
sidebar:
  order: 7
---
## Monitores

Los monitores son información existente en un equipo, como CPU, memoria, disco, etc. Cada equipo dispone de recursos exclusivos que pueden ser monitorizados. Los colores de los monitores varían según su estado.

![image-1739972140083.png](../../../../../assets/images/p113_image-1739972140083.png)

---

![image-1646943045253.png](../../../../../assets/images/p113_image-1646943045253.png)
**Gráfico en tiempo real**: Muestra el gráfico actualizando sus datos en el intervalo de tiempo seleccionado. 

:::caution
Intervalos menores que el tiempo de actualización de los datos del equipo pueden generar gráficos con información incorrecta, tales como lecturas en cero o picos por encima del máximo permitido por el equipo.
:::

---

![image-1732626960803.png](../../../../../assets/images/p113_image-1732626960803.png) 
 **Periodo de Muestreo**: Personaliza el periodo del gráfico a generar. 

---

 ![image-1646943186232.png](../../../../../assets/images/p113_image-1646943186232.png) 
 **Propiedades del Gráfico**: Abre la pantalla con las propiedades del gráfico mostrado. 


| Ícone | Descrição |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| ![image-1732627382742.png](../../../../../assets/images/p113_image-1732627382742.png) | **Título**: Nombre que aparecerá en la parte superior del gráfico. |
| ![image-1646943518875.png](../../../../../assets/images/p113_image-1646943518875.png) | **Límites por lectura**: Cuando está activado, rellena todo el gráfico según el estado del periodo durante las lecturas. |
| ![image-1646943561235.png](../../../../../assets/images/p113_image-1646943561235.png) | **Mostrar marcadores de estado**: Cuando hay un cambio de estado en el periodo de tiempo presentado, Monsta añade una marca para visualizar cuándo y a qué estado se produjo el cambio. |
| ![image-1732627513437.png](../../../../../assets/images/p113_image-1732627513437.png) | **Ocultar valores**: Elimina los valores informados de la parte inferior de la presentación del gráfico. |
| ![image-1732627598700.png](../../../../../assets/images/p113_image-1732627598700.png) | **Ocultar leyenda**: Elimina la leyenda de la presentación del gráfico. |
| ![image-1732627665080.png](../../../../../assets/images/p113_image-1732627665080.png) | **Mostrar solo variación**: Renderiza el gráfico únicamente con sus variaciones para una mejor visualización de los cambios. |
| ![image-1732627792522.png](../../../../../assets/images/p113_image-1732627792522.png) | **Color de la leyenda**: Personaliza el color del texto de las leyendas en la parte inferior del gráfico. |
| ![image-1732627851295.png](../../../../../assets/images/p113_image-1732627851295.png) | **Color de fondo**: Personaliza el color de fondo del gráfico. |
| ![image-1732627906990.png](../../../../../assets/images/p113_image-1732627906990.png) | **Tamaño de la fuente de la leyenda**: Personaliza el tamaño de la leyenda en la parte inferior del gráfico. |
| ![image-1732627963075.png](../../../../../assets/images/p113_image-1732627963075.png) | **Ancho de la línea**: Personaliza el ancho de la línea renderizada en el gráfico. |
| ![image-1646943757386.png](../../../../../assets/images/p113_image-1646943757386.png) | **Mostrar indicador de percentil**: Añade al gráfico el percentil seleccionado. |
| **Agrupar Dados por Tempo** | **Agrupar los datos por tiempo**: Cuando hay un periodo de tiempo mayor a dos días, Monsta agrupa los datos y genera una media de la información automáticamente para presentarla en el gráfico. En esta propiedad es posible elegir el intervalo que utilizará este agrupamiento o simplemente desactivar esta opción. |


---



![image.png](../../../../../assets/images/image.png)

**Activar monitorización**: Este botón permite habilitar o pausar la recopilación de datos y la visualización de gráficos para el activo seleccionado. Cuando el monitor está **desactivado**, la recopilación se interrumpe inmediatamente, cesando el procesamiento de métricas y el envío de alertas asociadas, sin eliminar el historial de datos ya almacenado.

---

![image.png](../../../../../assets/images/image-2.png)

**Clonar monitor**: Utilice esta funcionalidad para replicar el monitor. Al accionar este botón, se abrirá una lista para seleccionar el dispositivo de destino, heredando todas las métricas, umbrales de alerta y parámetros de verificación configurados.  

---

![image.png](../../../../../assets/images/image-1.png)

 **Valor de la métrica**: Indica el nombre de la métrica, el valor de la lectura actual y si el resultado es mayor, menor o igual a la lectura anterior.

---

![image-1732628094300.png](../../../../../assets/images/p113_image-1732628094300.png) 
**Métricas**: Muestra la información sobre cada recurso individual monitorizado. 

---

![image-1647016828331.png](../../../../../assets/images/p113_image-1647016828331.png) 
**Editar**: Modifica las propiedades del monitor seleccionado. 

---

![image-1647016882068.png](../../../../../assets/images/p113_image-1647016882068.png) 
**Eliminar**: Elimina el monitor seleccionado. 

---

![image-1647016926788.png](../../../../../assets/images/p113_image-1647016926788.png) 
**Publicar**: Crea un enlace para publicar el gráfico sin necesidad de autenticación. Para más información, consulte [Publicar un Monitor](#publicar-um-monitor)

---

![image-1647017067003.png](../../../../../assets/images/p113_image-1647017067003.png) 
**Número de intentos**: Indica la cantidad de intentos del monitor antes de salir del estado normal. 

---

![image-1732628125264.png](../../../../../assets/images/p113_image-1732628125264.png) 
**Información del monitor**: Muestra la fecha de la última verificación, la fecha de la próxima verificación, el último cambio de estado y la fecha del último alerta enviado. 

---

![image-1732628187732.png](../../../../../assets/images/p113_image-1732628187732.png) 
**Porcentaje**: Muestra el porcentaje de recurso utilizado por la métrica seleccionada cuando hay un valor máximo informado. 

---

![image-1756124792478.png](../../../../../assets/images/p113_S2vimage-1756124792478.png) 
**Exportar / Calcular Área**: El gráfico de recopilaciones de información ofrece tres opciones principales para interactuar con los datos visualizados:

- **Exportar como imagen**: En la esquina superior derecha del gráfico, haga clic en el icono de "Download" o "Exportar" para guardar el gráfico como un archivo de imagen. Esto le permite usar la imagen en informes, presentaciones o compartirla fácilmente.
- **Exportar datos**: Puede exportar los datos brutos en formatos de hoja de cálculo para análisis posteriores. Los formatos disponibles son CSV y XLS.
- **Informe de consumo**: Para un análisis más detallado, puede calcular el área bajo la curva del gráfico. Esta función es ideal para obtener valores acumulados o totales a lo largo del periodo seleccionado. Haga clic en la opción "Relatório de Consumo" y el resultado se mostrará en un cuadro de texto, listo para copiarse o utilizarse en sus cálculos.

### Publicar um Monitor

La publicación de un monitor permite al usuario crear un enlace para acceso en internet sin la necesidad de usuario y contraseña.

![image-1647023048029.png](../../../../../assets/images/p113_image-1647023048029.png)

- **Publicar**: Habilita la creación del enlace para el monitor seleccionado.
- **Período**: Permite elegir el tiempo de publicación del gráfico. Por seguridad, no se permiten periodos mayores a un mes.
- **Pantalla completa**: Cuando está activado, utiliza toda la pantalla para mostrar el gráfico.
- **Ancho y Alto**: Define las dimensiones del gráfico en píxeles.
- **Código HTML**: Este código es generado por Monsta para el monitor seleccionado y puede utilizarse para publicar el gráfico en un panel de terceros.

### Editar/Customizar um Monitor

La edición de un monitor permite personalizar información importante sobre su comportamiento, como la frecuencia de las recopilaciones, límites de alerta y su script de cómo obtener la información.

![image-1739972270800.png](../../../../../assets/images/p113_image-1739972270800.png)

#### Detalhes

![image-1739972288968.png](../../../../../assets/images/p113_image-1739972288968.png)
**Ícone**: Permite seleccionar el icono que se mostrará en pantalla. 

---

![image-1739972320658.png](../../../../../assets/images/p113_image-1739972320658.png)
**Nome curto**: Es el texto que aparecerá en el icono del monitor. 

---

![image-1739972336891.png](../../../../../assets/images/p113_image-1739972336891.png)
**Nome**: Es el texto que se mostrará en la parte superior del gráfico del monitor. 

---

![image-1739972366625.png](../../../../../assets/images/p113_image-1739972366625.png)
**Métricas**: Son los recursos cuyos datos serán recopilados para el gráfico. 

---

![image-1732629430867.png](../../../../../assets/images/p113_image-1732629430867.png)
**Cor**: Selecciona el color que será renderizado por la métrica en el gráfico. 

---

![image-1732629288328.png](../../../../../assets/images/p113_image-1732629288328.png)
**Nome da métrica**: Es el nombre que se mostrará en la leyenda del indicador de la lectura actual. 

---

![image-1739972396801.png](../../../../../assets/images/p113_image-1739972396801.png)
**Legenda**: Es el nombre que se mostrará en la leyenda del gráfico y en el indicador de valor actual referente a la métrica seleccionada. 

---

![image-1732629728817.png](../../../../../assets/images/p113_image-1732629728817.png)
**Instâncias**: Permite cambiar la instancia actual de la métrica. 

---

![image-1647108824415.png](../../../../../assets/images/p113_image-1647108824415.png)
**Clonar**: Permite añadir una nueva métrica al mismo monitor. 

---

![image-1732629952003.png](../../../../../assets/images/p113_image-1732629952003.png)
**Desativar Limites**: Cuando está marcado, desactiva el envío de alertas para el monitor en edición. La métrica seleccionada será considerada siempre en estado normal. 

---

![image-1732630014138.png](../../../../../assets/images/p113_image-1732630014138.png)
**Fixar OID**: Cuando está desmarcada, Monsta verificará si el nombre de la instancia monitorizada sigue en la misma OID y en caso de cambio, la nueva posición será localizada automáticamente. Cuando esta opción está marcada, Monsta recopilará datos siempre de la misma OID, independientemente del nombre de la instancia. 

---

![image-1647109347088.png](../../../../../assets/images/p113_image-1647109347088.png)
**Inversão da Lógica de Limite (Threshold Inversion)**: Esta opción permite que usted cambie la **lógica de alerta** de un monitor. Use esta funcionalidad para métricas donde un **valor bajo** indica un problema (p. ej.: la velocidad de una interfaz de red no debe bajar de cierto nivel) o donde necesite monitorizar rangos específicos de valores. 

---

![image-1647109503541.png](../../../../../assets/images/p113_image-1647109503541.png)
![image-1647109809636.png](../../../../../assets/images/p113_image-1647109809636.png)
**Porcentaje para alertas**: Permite seleccionar en qué valores la métrica entrará en estado de alerta. Cuando hay un valor máximo definido, la configuración de las alertas será en porcentaje; de lo contrario, los límites se informan textualmente. 

---

![image-1647110437143.png](../../../../../assets/images/p113_image-1647110437143.png)
**Intervalo de verificación**: Permite seleccionar la frecuencia con la que se ejecutará el monitor. 

---

![image-1647110506456.png](../../../../../assets/images/p113_image-1647110506456.png)
**Número de intentos**: Permite seleccionar cuántas veces se debe comprobar el monitor antes de salir de su estado normal. Cuando un monitor vuelve al estado normal antes de alcanzar este límite, ese contador se reinicia. | 

---

#### Grupos de alerta

![image-1732630557678.png](../../../../../assets/images/p113_image-1732630557678.png)
**Notificar grupo de alerta**: Cuando está activado, envía alertas a los grupos seleccionados; de lo contrario, Monsta no enviará alertas aunque el monitor cambie de estado.

---

![image-1732630665348.png](../../../../../assets/images/p113_image-1732630665348.png)
**Herdado do dispositivo**: Son los grupos de alerta definidos en la edición del dispositivo. Una vez que son heredados, no es posible eliminarlos del monitor, solo desactivarlos.

---

![image-1732630758350.png](../../../../../assets/images/p113_image-1732630758350.png)
**Adicionar Grupo de Alerta**: Añade grupos que recibirán las alertas cuando el monitor cambie de estado. Para más información consulte [Alertas](/es/manual/grupos-alertas/alertas).

---

![image-1647111288941.png](../../../../../assets/images/p113_image-1647111288941.png)
**Remover Grupo de Alerta**: Elimina el grupo de alerta seleccionado.

---

#### Sons de Alerta

![image-1732630990555.png](../../../../../assets/images/p113_image-1732630990555.png)
Permite añadir sonidos de alerta personalizados para cada estado del monitor.

---

#### Log de Erros

![image-1732631123766.png](../../../../../assets/images/p113_image-1732631123766.png)
Informa de las últimas fallas que ocurrieron con la recopilación del monitor. Este registro es útil para conocer el motivo por el cual alguna recopilación no se está realizando con éxito.

#### Avançado

![image-1647113062837.png](../../../../../assets/images/p113_image-1647113062837.png)

##### Métricas

![image-1732638791772.png](../../../../../assets/images/p113_image-1732638791772.png)
Métricas: Permite cambiar el orden de visualización de la métrica, eliminarla o editarla. Para más información sobre cómo editar una métrica consulte [Métricas](/es/manual/configuracoes/templates#métricas). 

---

![image-1732638931351.png](../../../../../assets/images/p113_image-1732638931351.png) 
Fuente de datos para el valor: Es el método que Monsta utilizará para recopilar información para esta métrica. Para más información, consulte [Métricas](/es/manual/configuracoes/templates#métricas). 

---

![image-1732639055201.png](../../../../../assets/images/p113_image-1732639055201.png)
Fuente de datos para el valor máximo: Utilizado cuando el monitor posee un valor máximo límite. Para más información, consulte [Métricas](/es/manual/configuracoes/templates#métricas). 

---

##### Parámetros

En esta pestaña se indicarán los parámetros utilizados por el monitor seleccionado y sus respectivos valores empleados.