from scapy.all import IP, ICMP, sr1

# Set the destination IP address
dst_ip = "172.29.8.1"

# Create an ICMP echo request packet
packet = IP(dst=dst_ip) / ICMP()

# Send the packet and receive the response
reply = sr1(packet, timeout=2)

# Check if we received a response and print the result
if reply is not None:
    print(f"Received ICMP reply from {reply.src}")
else:
    print(f"No response received from {dst_ip}")
