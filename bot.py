import os
import threading
import traceback
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

print("🔍 Démarrage SK-MD...")

try:
    print("⏳ Chargement des commandes...")
    handlers = load_commands()
    print(f"✅ {len(handlers)} commandes chargées.")

    print("⏳ Connexion à Telegram...")
    app = Application.builder().token(TOKEN).build()

    for handler in handlers:
        app.add_handler(handler)

    print("🤖 SK-MD tourne... que la purge soit !")
    app.run_polling()

except Exception as e:
    print("=" * 50)
    print("❌ ERREUR FATALE :")
    print("=" * 50)
    traceback.print_exc()
    print("=" * 50)
