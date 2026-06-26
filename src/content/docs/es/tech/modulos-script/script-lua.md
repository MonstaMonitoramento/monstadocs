---
title: "Scripting con LUA"
sidebar:
  order: 1
---

El Monsta te permite crear lógicas personalizadas de recolección de datos, procesamiento de métricas y reglas complejas de alertas utilizando el lenguaje de programación **Lua**. 

Si las plantillas predeterminadas o las expresiones nativas no son suficientes para tu necesidad (como parsing de cadenas complejas, cálculos matemáticos avanzados o bucles), el motor de scripting en Lua ofrece total flexibilidad para extender la plataforma.

---

## ¿Por qué Lua?

Lua es un lenguaje de scripting brasileño, ampliamente utilizado en la industria tecnológica (especialmente en videojuegos y sistemas embebidos) por tres motivos principales:

* **Extrema Velocidad**: Es uno de los lenguajes de scripting más rápidos del mundo, garantizando que tus scripts se ejecuten en milisegundos sin sobrecargar el servidor de Monsta.
* **Ligereza**: El intérprete ocupa muy poco espacio en memoria, permitiendo ejecuciones simultáneas a gran escala.
* **Sintaxis Simple**: Es muy fácil de leer y aprender, incluso para quienes tienen poca experiencia en programación.

---

## Guía Rápida de Sintaxis de Lua

Para ayudarte a comenzar a crear tus primeros scripts en Monsta, aquí están los conceptos fundamentales del lenguaje:

### Variables y Tipos de Datos
En Lua, no necesitas definir el tipo de la variable antes (tipado dinámico). Usa siempre la palabra clave `local` para garantizar que la variable exista solo dentro de ese script (evitando conflictos de memoria).

```lua
local nome_dispositivo = "Servidor Core" -- Cadena
local latencia = 45                     -- Número
local ativo = true                      -- Booleano
```

### Estructuras Condicionales (`if` / `else`)
La sintaxis usa las palabras clave then, elseif y cierra obligatoriamente el bloque con un end.

```lua
if latencia > 100 then
    print("Alerta: Latência Alta!")
elseif latencia > 50 then
    print("Aviso: Latência Moderada.")
else
    print("Status: OK.")
end
```

### Tablas (Diccionarios y Arrays)
Las tablas son la única estructura de datos compleja en Lua. Sirven tanto como listas indexadas como objetos con clave y valor.

```lua
-- Ejemplo de Array/Lista
local sensores = {"Ping", "CPU", "Memória"}

-- Ejemplo de Diccionario (Clave/Valor)
local dados_coleta = {
    ip = "192.168.1.50",
    status = "Online",
    portas_abertas = 4
}
```
:::caution[¡Atención con los índices!]
A diferencia de la mayoría de los lenguajes de programación (como **JavaScript** o **Python**) donde las listas comienzan en el índice `0`, en Lua las tablas comienzan en el índice `1`.
Por lo tanto, `sensores[1]` devolverá "Ping".
:::

## ¿Cómo interactúa Monsta con el Script?
Generalmente, Monsta inyecta variables globales o tablas predefinidas dentro de tu script (conteniendo los datos recolectados del dispositivo) y espera que tu script devuelva un valor específico (como un número, texto o booleano) usando el comando return.

```lua
-- Ejemplo de una consulta SNMP
local load_linux = snmp.get("1.3.6.1.4.1.2021.10.1.3.2.0") -- Función de Monsta
return load_linux
```

## Recursos y Manuales Completos
Para profundizar en el lenguaje, consulta la [documentación oficial del lenguaje Lua](https://lua.org/docs.html).

Monsta tiene funciones propias que se utilizan en los scripts. Para conocer los módulos internos específicos que Monsta pone a disposición (funciones de red, manipulación de cadenas y conexión), consulta los próximos artículos de esta sección (**Módulos de Script con Lua**).