---
title: "QUIC Protocol"
sidebar:
  order: 4
---

# QUIC Protocol: The Future of Internet Communications

The Quick UDP Internet Connections (QUIC) is a transport protocol developed by Google and standardized by the IETF (Internet Engineering Task Force). It was created to speed up the performance of web-based applications, offering the advantages of TCP with the speed of UDP, plus built-in encrypted security.

Originally designed to replace TCP for HTTP/3 traffic, QUIC is core to the Monsta Agent architecture due to its high efficiency and resilience on WANs.

## Basic Operation

QUIC is a transport protocol that runs **over UDP** (User Datagram Protocol), not over TCP.

| **Characteristic** | **Detail** |
| --- | --- |
| **Transport** | Uses **UDP** (User Datagram Protocol). |
| **Security** | **TLS 1.3** encryption integrated into the protocol. |
| **Application** | Provides the connection between the Monsta Agent and the Monsta Server, ensuring speed and security. |

## Main Technical Advantages

QUIC addresses historical bottlenecks of TCP and TLS, and is the primary reason for its adoption in critical communications like those of the Monsta Agent:

#### A. Zero RTT (Round Trip Time) or 1-RTT Connection Setup

- **TCP + TLS**: Establishing a TCP connection and negotiating TLS (the handshake) requires multiple packet exchanges.
- **QUIC**: It combines connection establishment and TLS negotiation into a single step. On subsequent connections (Zero RTT), it can send encrypted data on the very first message, **eliminating the initial handshake latency**.

#### B. Elimination of Head-of-Line Blocking

In TCP, if a packet is lost in a data stream, the entire subsequent stream (even if data has arrived) must wait for retransmission of the lost packet.

- **QUIC**: It allows **multiple independent streams** within the same connection. If a packet is lost on one stream, only that stream is paused, while other streams continue transmitting and processing data without interruption. This is important for simultaneous metric collections by the agent.

#### C. Tolerance to Network Changes (Connection Migration)

TCP identifies a connection by the IP/port pair. If a client's IP address changes (e.g., switching from Wi‑Fi to 4G), the TCP connection is terminated.

- **QUIC**: The connection is identified by a **Unique Connection ID**. If the Monsta Agent changes networks (and thus its IP), the QUIC connection can remain active and traffic resumes instantly, without needing to reestablish the tunnel and the TLS handshake.

## QUIC and Security (TLS 1.3)

Security is native to QUIC. TLS 1.3 encryption is **mandatory and integrated** from the start of the connection.

- **Integrity**: The protocol encrypts most headers, not just the payload, preventing intermediaries (like proxies) from inspecting or manipulating communication between the Agent and the Monsta Server.

## Application Summary

| **QUIC Feature** | **Benefit for Monsta** |
| --- | --- |
| **Zero RTT / 1-RTT** | Faster communications and real-time alert delivery. |
| **Multiple Streams** | Ensures that loss of a single metric packet does not delay delivery of all other metrics and commands. |
| **Connection ID** | Uninterrupted connection even if the Remote Agent's IP changes temporarily. |
| **Integrated TLS 1.3** | Maximum security and end-to-end encryption without additional configuration. |