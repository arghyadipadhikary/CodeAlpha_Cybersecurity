from scapy.all import sniff, IP, TCP, UDP, Raw #type:ignore

# Function to process captured packets
def packet_callback(packet):
    print("\n=== Packet Captured ===")

    if IP in packet:
        print(f"Source IP: {packet[IP].src}")
        print(f"Destination IP: {packet[IP].dst}")
        print(f"Protocol: {packet[IP].proto}")

        if TCP in packet:
            print(f"TCP Packet | Src Port: {packet[TCP].sport} | Dst Port: {packet[TCP].dport}")
        elif UDP in packet:
            print(f"UDP Packet | Src Port: {packet[UDP].sport} | Dst Port: {packet[UDP].dport}")

        if Raw in packet:
            print(f"Raw Data: {packet[Raw].load}")

# Start sniffing
print("Starting Network Sniffer...")
sniff(filter="ip", prn=packet_callback, store=False)
