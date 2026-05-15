import socket, subprocess, os

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception: return "Unable to determine"

print("Network Info Display")
print("====================")
hostname = socket.gethostname()
local_ip = get_ip()
print(f"Hostname:  {hostname}")
print(f"Local IP:  {local_ip}")
try:
    full_hostname = socket.getfqdn()
    print(f"Full name: {full_hostname}")
except Exception: pass

try:
    external = subprocess.run(["curl", "-s", "--max-time", "3", "https://api.ipify.org"],
                               capture_output=True, text=True, timeout=5)
    if external.returncode == 0:
        print(f"External IP: {external.stdout.strip()}")
except Exception:
    print("External IP: (no internet connection)")

print("\nTip: Your local IP is what other devices on your network use to talk to you!")
print(f"Share files by running python3 -m http.server and visiting http://{local_ip}:8000")
