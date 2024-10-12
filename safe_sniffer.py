from scapy.all import sniff, IP, TCP, UDP, ICMP

def packet_callback(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        print(f"\nIP Packet:")
        print(f"Source: {src_ip}, Destination: {dst_ip}")

        if TCP in packet:
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            print(f"TCP - Source Port: {src_port}, Destination Port: {dst_port}")
        elif UDP in packet:
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            print(f"UDP - Source Port: {src_port}, Destination Port: {dst_port}")
        elif ICMP in packet:
            icmp_type = packet[ICMP].type
            icmp_code = packet[ICMP].code
            print(f"ICMP - Type: {icmp_type}, Code: {icmp_code}")

def main(interface):
    print(f"Sniffing on interface: {interface}")
    print("Capturing only IP packets. Press Ctrl+C to stop.")

    try:
        # Start sniffing packets
        sniff(iface=interface, prn=packet_callback, store=0)
    except KeyboardInterrupt:
        print("\nPacket capture stopped.")
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Make sure you're running this script with sudo.")

if __name__ == "__main__":
    interface = input("Enter the network interface to sniff (e.g., en0 for Wi-Fi): ")
    main(interface)
