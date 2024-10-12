# MyPacketSniffer

## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Prerequisites](#prerequisites)
4. [Installation](#installation)
5. [Usage](#usage)
6. [Output Explanation](#output-explanation)
7. [Use Cases](#use-cases)
8. [Legal and Ethical Considerations](#legal-and-ethical-considerations)
9. [Security Considerations](#security-considerations)
10. [Limitations](#limitations)

## Introduction

This is a simple yet powerful packet sniffer implemented in Python using the Scapy library. It's designed to capture and display basic information about IP packets traversing a specified network interface. This tool is intended for educational purposes, network troubleshooting, and authorized security analysis.

## Features

- Captures IPv4 packets in real-time
- Identifies and displays source and destination IP addresses
- Recognizes and shows details for TCP, UDP, and ICMP protocols
- Displays source and destination ports for TCP and UDP packets
- Shows ICMP type and code for ICMP packets
- User-friendly interface allowing selection of network interface

## Prerequisites

- Python 3.x
- Scapy library

## Installation

1. Ensure Python 3.x is installed on your system.
2. Install Scapy:
   ```
   pip install scapy
   ```
3. Save the provided script to a file, e.g., `packet_sniffer.py`.

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script with administrator/root privileges:
   ```
   sudo python3 packet_sniffer.py
   ```
4. When prompted, enter the name of the network interface you want to monitor (e.g., 'en0' for Wi-Fi on macOS, 'eth0' for Ethernet on Linux).
5. The script will start capturing packets. Let it run as long as you need.
6. To stop the capture, press Ctrl+C.

## Output Explanation

The sniffer outputs information in the following format:

```
IP Packet:
Source: [Source IP], Destination: [Destination IP]
[Protocol] - Source Port: [Port], Destination Port: [Port]
```

- For TCP and UDP, it shows the source and destination ports.
- For ICMP, it displays the type and code instead of ports.

## Use Cases

1. Network Troubleshooting: Identify connectivity issues or unusual traffic patterns.
2. Security Analysis: Detect potential unauthorized access attempts or suspicious traffic.
3. Educational Tool: Learn about network protocols and traffic flows.
4. Performance Monitoring: Observe network usage patterns.

## Legal and Ethical Considerations

1. Only use this tool on networks you own or have explicit permission to analyze.
2. Do not use this sniffer to intercept or analyze traffic on public networks or systems you do not own.
3. Be aware of and comply with all relevant laws and regulations in your jurisdiction regarding network monitoring and data privacy.
4. If used in a professional environment, ensure compliance with organizational policies and obtain necessary approvals.

## Security Considerations

1. This script requires root/administrator privileges to run, which can pose security risks if misused.
2. The tool can potentially capture sensitive information. Handle any captured data with extreme care.
3. Be aware that your packet sniffing activities might be detected by security software or network administrators.

## Limitations

1. This sniffer only captures and displays packet header information, not payload data.
2. It may not capture all packets in high-traffic environments due to processing speed limitations.
3. The script does not decrypt encrypted traffic; only metadata is visible for such packets.
4. Some security software or firewalls may interfere with or block the sniffer's operation.

Remember: This tool is for educational and authorized use only. Always prioritize ethical considerations, privacy, and security in your network analysis activities. Unauthorized packet sniffing may be illegal and unethical.
