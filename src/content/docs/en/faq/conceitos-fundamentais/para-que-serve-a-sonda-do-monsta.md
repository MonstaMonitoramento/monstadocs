---
title: "What is the Monsta Probe used for?"
---

The "Monsta Probe" refers to a monitoring tool developed by Monsta Tecnologia for Windows operating systems. It is passive, meaning it waits for requests from Monsta on a specific port and returns information over the same connection.

In summary, the Monsta Probe is used for:

- **Monitoring Windows system performance in real time**: Tracks CPU, RAM, hard disk and network usage, allowing identification of bottlenecks and resource optimization.
- **Visualizing important data**: Integrates the collected metrics with the Monsta platform to create customized, detailed dashboards.
- **Diagnosing problems remotely**: Provides valuable information to resolve incidents quickly and efficiently, even without physical access to the machine.

Technically, the probe collects crucial metrics through the API libraries provided by Microsoft for WMI (Windows Management Instrumentation).

The probe can be installed via a graphical installer (`MonstaProbe.exe`) or via the command line to automate network installation.

To install our Probe, use our tutorial [Probe: Windows Monitoring](/en/start/instalacao/sonda-windows).