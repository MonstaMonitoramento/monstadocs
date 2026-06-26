---
title: "WMI (Windows Management Instrumentation)"
sidebar:
  order: 1
---

# What is WMI?

Windows Management Instrumentation (WMI) is a core infrastructure for managing data and operations on Windows operating systems. It is Microsoft's implementation of WBEM (Web-Based Enterprise Management) and provides a standardized interface for administrators and applications to monitor, control, and configure many aspects of the Windows environment, from hardware and software information to the state of system services and processes. This ability to "instrument" the system enables automation of administrative tasks and facilitates centralized diagnosis and troubleshooting.

## Objectives and Features

WMI is designed to provide:

- **Centralized Management**: A uniform way to access configuration and status information of Windows systems.
- **Automation**: The ability to create scripts and applications that monitor events, perform queries, and make changes automatically.
- **Monitoring**: Real-time retrieval of data about processes, services, hardware, network, and other system components.
- **Interaction with System Elements**: Operations for reading and modifying system data, including executing methods and scripts for maintenance and configuration.

With this approach, WMI serves as a powerful tool for system administrators, solution integrators, and developers who need to monitor and manage IT environments.

## History and Evolution

WMI was introduced by Microsoft to standardize access to system management information. Since its first version on Windows NT and its evolution from Windows 2000, WMI has become an integral part of Microsoft's management strategies. Its development is based on the Common Information Model (CIM), a standard that unifies the way devices and services are represented in heterogeneous environments.

Historically, WMI has evolved to offer better performance, new features, and greater integration with other management technologies, enabling a wider range of administrative and monitoring actions.

MI (Management Infrastructure): The next generation of WMI, known as MI (Management Infrastructure), offers additional features and benefits for the creation and development of WMI providers and clients.

## WMI Architecture

The WMI architecture is robust and built on several components that work together to provide its functionalities.

### Main Components

- **WMI Service (winmgmt)**: The central service that acts as the "orchestrator" of WMI. It manages client requests, distributes queries, and coordinates communication with data providers.
- **CIM Repository (Common Information Model)**: This repository contains a standardized representation of system data. CIM classes serve as templates for the information that WMI exposes, ensuring consistency and interoperability with other management systems.
- **WMI Clients**: Applications or scripts that perform queries and commands via WMI. Examples include the command prompt (using `wmic`), PowerShell scripts, and applications developed in various languages that use the WMI APIs.

### WMI Providers

Providers are components that "translate" requests made via WMI into specific hardware or software commands. Each provider is responsible for an area of the system (for example, process management, network information, storage devices) and collects the necessary data to respond to client queries.

### CIM Repository and Data Modeling

The CIM model defines a hierarchical and standardized structure to represent system data. Through it, WMI organizes information into classes—for example, `Win32_Process` for running processes, `Win32_OperatingSystem` for operating system information, among others. This standardization facilitates creating coherent queries and integrating with other management tools.

### WMI Query Language (WQL)

WMI uses the WMI Query Language (WQL), which is similar to SQL but adapted for system information management. With WQL, you can perform queries such as:

```sql
SELECT * FROM Win32_Process WHERE Name = 'notepad.exe'
```

This query returns information about processes whose name is "notepad.exe". In addition, WQL allows the creation of event-monitoring queries. For example, you can define a query that triggers an action whenever a new process is started or a service is stopped.

## Using WMI

Access via Command-Line Tools and Scripts

- **WMIC (Windows Management Instrumentation Command-line)**: A command-line tool that allows execution of queries, extraction of information, and invocation of methods via WMI. Example:    
    ```powershell
    wmic process list brief
    
    ```
- **PowerShell**: Cmdlets such as `Get-WmiObject` (in older versions) and `Get-CimInstance` (in newer versions) allow access to WMI data. Example with PowerShell:
    
    ```powershell
    Get-WmiObject -Query "SELECT * FROM Win32_OperatingSystem"
    ```
- **VBScript, C#, Python (using libraries like pywin32)**: Various programming languages can interact with WMI, making it accessible for custom scripts that automate administrative tasks.

## How Monsta collects the resources provided by WMI

Monsta has a custom-developed probe that accesses the WMI APIs directly to collect the information requested by the monitoring platform. The probe is installed directly on the server or workstation you want to monitor and its operation is passive, meaning it receives requests on a port, processes the information, and returns it over the same connection.

To download and install the probe on your servers/workstations, use our tutorial [Probe: Windows Monitoring](/en/start/instalacao/sonda-windows) to monitor your Microsoft environment.