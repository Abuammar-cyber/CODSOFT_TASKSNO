from scapy.all import sniff, IP


def analyze_packet(packet):
    if IP in packet:
        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        protocol = packet[IP].proto

        print("\n" + "=" * 50)
        print("NETWORK PACKET")
        print("=" * 50)
        print("Source IP      :", source_ip)
        print("Destination IP :", destination_ip)
        print("Protocol       :", protocol)
        print("Packet Data    :", packet.summary())


print("Network Packet Analyzer")
print("Capturing packets... Press Ctrl+C to stop.")

sniff(prn=analyze_packet, store=False)