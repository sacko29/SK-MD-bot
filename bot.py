import os
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

from telegram.ext import Application, CommandHandler

# Import des commandes
from commands.general import start, ping
from commands.menu import menu

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

# --- ENREGISTREMENT DES COMMANDES ---
app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("menu", menu))

print("🤖 SK-MD tourne...")
app.run_polling()app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("menu", menu))

print("🤖 SK-MD tourne...")
app.run_polling()
