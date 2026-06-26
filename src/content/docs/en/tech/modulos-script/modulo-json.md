---
title: "JSON Module"
---

The **json** module provides functions to convert between Lua data and JSON (JavaScript Object Notation) format. It is useful for communication with web APIs, configuration storage, data serialization, and interoperability with other systems.

## Available Functions

### 1. `json.encode(value)`

Encodes a Lua value into a JSON string.

**Parameters**:

- `value` (any type): Value to be encoded to JSON.

**Return**:

- `string`: JSON representation of the value

**Exceptions**:

- Throws an error if the value contains circular references

- Throws an error if the table has mixed-type keys

- Throws an error if some data type cannot be serialized

**Examples**:

```lua
-- Encode basic values
local json_null = json.encode(nil)           -- "null"
local json_bool = json.encode(true)          -- "true"
local json_num = json.encode(42.5)           -- "42.5"
local json_str = json.encode("Hello\nWorld") -- "\"Hello\\nWorld\""

-- Encode array (table with sequential numeric indices)
local array = {"apple", "banana", "orange"}
local json_array = json.encode(array)
-- Result: "[\"apple\",\"banana\",\"orange\"]"

-- Encode object (table with string keys)
local person = {
    name = "João Silva",
    age = 30,
    active = true,
    tags = {"developer", "backend"},
    address = {
        street = "Rua das Flores, 123",
        city = "São Paulo"
    }
}
local json_person = json.encode(person)
-- Result: {"name":"João Silva","age":30,"active":true,"tags":["developer","backend"],"address":{"street":"Rua das Flores, 123","city":"São Paulo"}}

-- Encode monitoring data
local metrics = {
    timestamp = os.time(),
    hostname = "server-01",
    cpu_usage = 45.7,
    memory_mb = 2048,
    services = {"nginx", "postgresql", "redis"},
    status = "healthy"
}
local json_metrics = json.encode(metrics)

-- Encode list of events
local events = {
    {
        id = 1,
        type = "login",
        user = "admin",
        timestamp = "2024-01-15T10:30:00Z"
    },
    {
        id = 2,
        type = "logout",
        user = "user1",
        timestamp = "2024-01-15T11:45:00Z"
    }
}
local json_events = json.encode(events)
```

### 2. `json.decode(string)`

Decodes a JSON string into a Lua value asynchronously.

**Parameters**:

- `string` (string): JSON string to be decoded

**Return**:

- `any`: Decoded object as a Lua value (most often a table):

**Exceptions**:

- Throws an error if the string is not valid JSON

- Throws an error if there is excessive nesting depth

- Throws an error if numbers are too large or too small

**Examples**:

```lua
-- Decode basic values
local null_val = json.decode("null")           -- nil
local bool_val = json.decode("true")           -- true
local num_val = json.decode("42.5")            -- 42.5
local str_val = json.decode("\"Hello\"")       -- "Hello"

-- Decode JSON array
local json_array = "[\"apple\", \"banana\", \"orange\"]"
local array = json.decode(json_array)
-- Result: {"apple", "banana", "orange"}
print(array[1])  -- "apple"
print(array[2])  -- "banana"
print(#array)    -- 3

-- Decode JSON object
local json_person = [[
{
    "name": "Maria Santos",
    "age": 28,
    "active": true,
    "skills": ["Python", "Lua", "JavaScript"],
    "metadata": {
        "department": "Engineering",
        "level": "Senior"
    }
}
]]
local person = json.decode(json_person)
-- Result: table with keys name, age, active, skills, metadata
print(person.name)                    -- "Maria Santos"
print(person.age)                     -- 28
print(person.skills[1])               -- "Python"
print(person.metadata.department)     -- "Engineering"

-- Decode API response
local api_response = [[
{
    "status": "success",
    "data": {
        "users": [
            {"id": 1, "name": "Alice", "email": "alice@example.com"},
            {"id": 2, "name": "Bob", "email": "bob@example.com"}
        ],
        "total": 2,
        "page": 1
    },
    "timestamp": "2024-01-15T12:00:00Z"
}
]]
local response = json.decode(api_response)
if response.status == "success" then
    for _, user in ipairs(response.data.users) do
        print("Usuário: " .. user.name .. " (" .. user.email .. ")")
    end
    print("Total: " .. response.data.total)
end

-- Decode configurations
local config_json = [[
{
    "server": {
        "host": "0.0.0.0",
        "port": 8080,
        "timeout": 30
    },
    "database": {
        "host": "localhost",
        "name": "monagent",
        "pool_size": 10
    },
    "logging": {
        "level": "info",
        "file": "/var/log/monagent.log"
    }
}
]]
local config = json.decode(config_json)
local server_host = config.server.host          -- "0.0.0.0"
local db_pool = config.database.pool_size       -- 10
local log_level = config.logging.level          -- "info"
```