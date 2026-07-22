---
title: Scripting con LUA
sidebar:
  order: 1
---
El Monsta le permite crear lógicas personalizadas de recolección de datos, procesamiento de métricas y reglas complejas de alertas utilizando el lenguaje de programación **Lua**. 

Si las plantillas estándar o las expresiones nativas no son suficientes para su necesidad (como el parseo de cadenas complejas, cálculos matemáticos avanzados o bucles), el motor de scripting en Lua ofrece total flexibilidad para extender la plataforma.

---

## ¿Por qué Lua?

Lua es un lenguaje de scripting brasileño, ampliamente utilizado en la industria tecnológica (especialmente en videojuegos y sistemas embebidos) por tres motivos principales:

- **Extrema Velocidad**: Es uno de los lenguajes de scripting más rápidos del mundo, garantizando que sus scripts se ejecuten en milisegundos sin sobrecargar el servidor de Monsta.
- **Ligereza**: El intérprete ocupa muy poco espacio en memoria, permitiendo ejecuciones simultáneas a gran escala.
- **Sintaxis Simple**: Es muy fácil de leer y aprender, incluso para quienes tienen poca experiencia en programación.

---

## Guía rápida de sintaxis de Lua

Para ayudarle a empezar a crear sus primeros scripts en Monsta, aquí están los conceptos fundamentales del lenguaje:

### Variables y tipos de datos

En Lua, no necesita definir el tipo de la variable antes (tipado dinámico). Use siempre la palabra clave `local` para garantizar que la variable exista solo dentro de ese script (evitando conflictos de memoria).

```lua
local nome_dispositivo = "Servidor Core" -- Cadena
local latencia = 45                     -- Número
local ativo = true                      -- Booleano
```

### Estructuras condicionales (`if` / `else`)

La sintaxis utiliza las palabras clave then, elseif y cierra el bloque obligatoriamente con un end.

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

-- Ejemplo de Dicionário (Chave/Valor)
local dados_coleta = {
    ip = "192.168.1.50",
    status = "Online",
    portas_abertas = 4
}
```

:::caution[¡Atención con los índices!]
A diferencia de la mayoría de los lenguajes de programación (como **JavaScript** o **Python**) donde las listas comienzan en el índice `0`, en Lua las tablas empiezan en el índice `1`.
Por lo tanto, `sensores[1]` devolverá "Ping".
:::

## ¿Cómo interactúa Monsta con el script?

Generalmente, Monsta inyecta variables globales o tablas predefinidas dentro de su script (conteniendo los datos recolectados del dispositivo) y espera que su script devuelva un valor específico (como un número, texto o booleano) usando el comando `return`.

```lua
-- Ejemplo de una consulta de SNMP
local load_linux = snmp.get("1.3.6.1.4.1.2021.10.1.3.2.0") -- Função do Monsta
return load_linux
```

El `return` también puede definir el estado de la métrica. Para devolver un estado, el return debe devolver un diccionario que contenga `value` (valor a devolver) y `status` (una *string* con valores predefinidos).

Los valores aceptados para `status` son:


| status | Color | Estado de la métrica |
| ---------------- | -------- | ----------------- |
| "MetricOk" | Verde | Normal |
| "MetricWarning" | Naranja | Advertencia |
| "MetricCritical" | Rojo | Crítico |


```lua
-- Ejemplo de una consulta de SNMP con tratamiento del status
local volt = snmp.get("1.3.6.1.2.1.33.1.3.3.1.3.1.0")

if volt > 230 then
   -- Si la tensión es mayor, entra en estado Advertencia
   return { value=volt, status="MetricWarning" }
elseif volt < 100 then
   -- Si la tensión es menor, entra en estado Crítico
   return { value=volt, status="MetricCritical" }
else
   -- Si no, el estado será Normal
   return { value=volt, status="MetricOk" }
end
```

:::caution[¡Atención!]

Cuando el status se define dentro del script, no es posible configurar el estado de alerta a través de las configuraciones del monitor, ya que el script definirá esta información. 

:::

## Recursos y manuales completos

Para profundizar en el lenguaje, consulte la [documentación oficial de la lengua Lua](https://lua.org/docs.html).

Monsta cuenta con funciones propias que se utilizan en los scripts. Para conocer los módulos internos específicos que Monsta pone a disposición (funciones de red, manipulación de cadenas y conexión), consulte los próximos artículos de esta sección (**Módulos de script con Lua**).