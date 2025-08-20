# Simple Configuration System

# Server IP (tuple - cannot be changed)
server_ip = ("192.168.1.1",)

# Allowed IPs (list - can be updated)
allowed_ips = ["192.168.1.100", "192.168.1.101"]

# Show original config
print("Server IP:", server_ip[0])
print("Allowed IPs:", allowed_ips)

# Update allowed IPs
allowed_ips.append("192.168.1.102")
allowed_ips.append("192.168.1.103")

# Show updated config
print("\nUpdated Configuration:")
print("Server IP:", server_ip[0])   # unchanged
print("Allowed IPs:", allowed_ips)
