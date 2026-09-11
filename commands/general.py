from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "╔══════════════════════╗\n"
        "║  𝐒𝐭𝐚𝐭𝐮𝐭 : [ 𝐎𝐧𝐥𝐢𝐧𝐞 ]  ║\n"
        "║  ░▒▓█ 𓆩 𝐒𝐊-𝐌𝐃 𝐕𝟏.𝟎 𓆪 █▓▒░  ║\n"
        "╚══════════════════════╝\n"
        "░▒▓█ 𓆩 /menu 𓆪 █▓▒░"
    )

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "╔══════════════════════╗\n"
        "║  ☠️ ✦ 𝐒𝐘𝐒𝐓𝐄̀𝐌𝐄 𝐄́𝐕𝐄𝐈𝐋𝐋𝐄́ ✦ ☠️  ║\n"
        "╚══════════════════════╝"
    )

def register(commands):
    commands.append(CommandHandler("start", start))
    commands.append(CommandHandler("ping", ping))
