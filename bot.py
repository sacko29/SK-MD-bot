import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram.ext import Application

from commands import load_commands

TOKEN = os.environ.get("TOKEN")

# --- SERVEUR HTTP POUR RENDER ---
class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"SK-MD is alive")
    def log_message(self, format, *args):
        pass

def run_health_server():
    port = int(os.environ.get("PORT", 10000))
    server = HTTPServer(("0.0.0.0", port), HealthHandler)
    server.serve_forever()

threading.Thread(target=run_health_server, daemon=True).start()

# --- CHARGEMENT AUTOMATIQUE DES COMMANDES ---
app = Application.builder().token(TOKEN).build()

for handler in load_commands():
    app.add_handler(handler)

print(
    "●──────── 𓆩 𝐒𝐊-𝐌𝐃 𓆪 ────────●\n"
    "  ☠️ 𝐒𝐘𝐒𝐓𝐄̀𝐌𝐄 𝐄́𝐕𝐄𝐈𝐋𝐋𝐄́\n"
    "  🩸 𝐉𝐞 𝐬𝐮𝐢𝐬 𝐚̀ 𝐯𝐨𝐬 𝐨𝐫𝐝𝐫𝐞𝐬.\n"
    "●──────────────────────────●\n"
    "░▒▓"
)
