---
title: "¿Es posible utilizar el particionado predeterminado de Linux para Monsta?"
description: Conozca las recomendaciones de particionado de Linux para instalar Monsta y descubra cuándo el esquema de particionado predeterminado es adecuado.
sidebar:
  order: 2
---

El particionado predeterminado, aunque conveniente, no está optimizado para el perfil de uso y las necesidades de crecimiento del software Monsta. Recomendamos siempre el **particionado manual** para garantizar la asignación correcta de espacio y la flexibilidad futura.

A continuación, explicamos los principales motivos por los cuales el particionado predeterminado no es ideal.

---

## 1. 🏡 Asignación ineficiente para `/home`

Muchos asistentes de instalación de distribuciones Linux están configurados para uso personal (escritorios) y, por tanto, tienden a asignar un **espacio considerable y generoso para la partición `/home`**.

- **Problema**: Monsta es un sistema de software que no depende del directorio `/home` para su funcionamiento principal ni para el almacenamiento de datos de gran volumen. El espacio asignado a `/home` terminará siendo **subutilizado**, mientras que otras áreas cruciales pueden quedarse con poco espacio.
- **Recomendación**: Priorizar el espacio para los directorios donde los datos del sistema y de Monsta realmente residen.

## 2. 🗃️ Partición `/var` subdimensionada o ausente

La partición `/var` es de **importancia crítica** para Monsta, ya que es el lugar predeterminado donde se almacenan las bases de datos y los *registros* del sistema.

- **Problema**: Algunos particionadores automáticos pueden **no crear una partición separada para `/var`** o asignarle un volumen muy pequeño. Con el uso intensivo de bases de datos por parte de Monsta, esta partición puede agotar rápidamente su espacio, lo que provoca fallos operativos y pérdida en el almacenamiento de datos.
- **Recomendación**: Crear la partición `/var` por separado y garantizar que tenga el **mayor volumen de espacio** asignado, considerando el crecimiento de los datos a lo largo del tiempo.

## 3. 📉 Falta de flexibilidad con LVM

Muchos sistemas predeterminados pueden no configurar las particiones utilizando el **Logical Volume Manager (LVM)**.

- **Problema**: El LVM es una capa de abstracción que permite la gestión y manipulación flexible de los volúmenes de disco. **Sin LVM**, será imposible, o extremadamente difícil, **aumentar el tamaño** de una partición (como `/var`) si empieza a quedarse sin espacio en el futuro, lo que exige detener el sistema y, potencialmente, migrar datos.
- **Recomendación**: Utilizar **LVM** al crear las particiones, especialmente para `/var` y `/`, para garantizar la capacidad de **expansión futura** sin *tiempo de inactividad* complejo.
