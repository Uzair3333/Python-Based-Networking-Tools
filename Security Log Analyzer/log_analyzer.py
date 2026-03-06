# =========================
# Security Log Analyzer
# =========================

# Reads the log file and extracts each line into a list called 'lines'
lines = []
with open('file.log', 'r') as f:
    content = f.read()
    for line in content.splitlines():
        lines.append(line)

# Extracts the IP address and Counts the number of attempts for each IP address
ip_attempts = {}
for line in lines:
    ip = line.split(' ')[0]
    if ip in ip_attempts:
        ip_attempts[ip] += 1
    else:
        ip_attempts[ip] = 1

# Detecting Suspicious IP Addresses
suspicious_ips = []
for ip, attempts in ip_attempts.items():
    if attempts > 10:  # Threshold for suspicious activity
        suspicious_ips.append(ip)

# =========================
# User-Friendly Output
# =========================

print("\n" + "="*40)
print("SECURITY LOG ANALYSIS REPORT")
print("="*40 + "\n")

print(f"Total log entries analyzed: {len(lines)}")
print(f"Unique IP addresses found: {len(ip_attempts)}\n")

print("Activity Summary:")
for ip, count in ip_attempts.items():
    print(f"- {ip} → {count} requests")

print("\nSuspicious Activity:")
if suspicious_ips:
    for ip in suspicious_ips:
        print(f"⚠ {ip} made {ip_attempts[ip]} requests → Possible scanning or attack behavior")
else:
    print("None detected")

print("\nAnalysis Complete.")
print("="*40 + "\n")