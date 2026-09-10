from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import random
import time
import os
from http.server import HTTPServer, BaseHTTPRequestHandler
import threading

# --- PETIT SERVEUR HTTP POUR RENDER ---
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

TOKEN = "8766153141:AAFMCq2AqAE5Ak1z-fNN3ao4YdYPcLiW1cc"  # Remplace par ton vrai token

MENACES = [
    "☠️ Le verdict est tombé. SK-MD a parlé.",
    "🔥 La purge est en marche.",
    "💀 La nuit est tombée sur {target}.",
]

REPONSES_BAN = [
    "🚀 Attaque lancée sur {target}. Aucune pitié.",
    "💥 {target} est en train de brûler.",
]

async def start(update, context):
    await update.message.reply_text("🔥 SK-MD est en ligne. Envoie /menu.")

async def ping(update, context):
    await update.message.reply_text("🏓 Pong !")

async def menu(update, context):
    text = """
╭──────────────────╮
│  🔥 SK-MD V1.0   │
│  ✦ Dark • Fast • Deadly
├──────────────────┤
│  /start  /ping  /ban
╰──────────────────╯
"""
    await update.message.reply_text(text)

async def ban(update, context):
    try:
        target = context.args[0]
        menace = random.choice(MENACES).format(target=target)
        attaque = random.choice(REPONSES_BAN).format(target=target)
        await update.message.reply_text(menace)
        await update.message.reply_text("⏳ 0%... 50%... 100%")
        time.sleep(1)
        await update.message.reply_text(attaque)
    except IndexError:
        await update.message.reply_text("❌ Utilisation : /ban + numéro")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("menu", menu))
app.add_handler(CommandHandler("ban", ban))

print("🤖 SK-MD tourne...")
app.run_polling()
