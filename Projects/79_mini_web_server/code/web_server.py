from http.server import HTTPServer, BaseHTTPRequestHandler
import socket, datetime

def get_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except Exception:
        return "localhost"

class PiHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        html = f"""
<!DOCTYPE html>
<html>
<head>
    <title>My Raspberry Pi!</title>
    <style>
        body {{ font-family: Arial, sans-serif; background: #1a1a2e; color: #eee;
               display: flex; justify-content: center; align-items: center;
               min-height: 100vh; margin: 0; }}
        .card {{ background: #16213e; padding: 40px; border-radius: 15px;
                 text-align: center; max-width: 500px; }}
        h1 {{ color: #e94560; }}
        .time {{ color: #0f3460; background: #e94560; padding: 10px;
                 border-radius: 8px; font-size: 1.2em; }}
    </style>
    <meta http-equiv="refresh" content="5">
</head>
<body>
    <div class="card">
        <h1>🍓 Hello from Raspberry Pi!</h1>
        <p>Your Pi is serving this webpage!</p>
        <div class="time">⏰ {now}</div>
        <p>This page refreshes every 5 seconds.</p>
        <p>Path requested: {self.path}</p>
    </div>
</body>
</html>"""
        self.wfile.write(html.encode())
    
    def log_message(self, format, *args):
        print(f"Visitor: {self.address_string()} — {args[0]}")

ip = get_ip()
PORT = 8080
print(f"Starting web server on port {PORT}")
print(f"Open in browser: http://{ip}:{PORT}")
print("Press Ctrl+C to stop.")

server = HTTPServer(("", PORT), PiHandler)
try:
    server.serve_forever()
except KeyboardInterrupt:
    print("\nServer stopped.")
