---
title: "WMI Error - Failed to collect information"
---

## Problem:

Monitors collect some information and then fail. The error logs report the following message: "**HRESULT Call failed with: 0x80041017**".

## Solution: 

The error **0x80041017** on Windows is related to **WMI**(*Windows Management Instrumentation*) and means **WBEM\_E\_INVALID\_QUERY**, that is, an **invalid query** was made to WMI. This error usually appears when scripts or tools try to access performance data or system information, but the query fails for some reason.

To resolve this issue you can rebuild all performance counters, including third-party ones. To do this, type the following commands in an Administrative command prompt. Press **ENTER** after each command.

- Rebuild the performance counters:

```powershell
cd c:\windows\system32
lodctr /R
cd c:\windows\sysWOW64
lodctr /R
```

- Synchronize with WMI:

```powershell
WINMGMT.EXE /RESYNCPERF
```

- Restart Log and High Performance services:

```powershell
net stop pla & net start pla
net stop winmgmt & net start winmgmt
```