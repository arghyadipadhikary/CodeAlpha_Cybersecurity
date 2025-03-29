from scapy.all import sniff, IP, TCP, UDP # type: ignore
import pandas as pd # type: ignore
import time

# Function to process packets
def packet_callback(packet):        
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        proto = packet[IP].proto

        alert = None
        if packet.haslayer(TCP) and packet[TCP].flags == 2:  # SYN flag to request connection
            alert = "Possible Port Scan Detected!"
        elif packet.haslayer(UDP) and len(packet) < 8:
            alert = "Suspicious UDP Packet!"

        log_entry = {
            "Timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "Source IP": src_ip,
            "Destination IP": dst_ip,
            "Protocol": "TCP" if proto == 6 else "UDP" if proto == 17 else "Other",
            "Alert": alert if alert else "No Threat"
        }

        df = pd.DataFrame([log_entry])
        print(df)

# Sniff network packets
print("Starting Network Intrusion Detection System...")
sniff(filter="ip", prn=packet_callback, store=False)
