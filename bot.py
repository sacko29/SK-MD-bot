from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = """
░▒▓█ 𓆩 𝐒𝐊-𝐌𝐃 𝐕𝟏.𝟎 𓆪 █▓▒░
☠️ ✦ 𝐃𝐚𝐫𝐤 • 𝐅𝐚𝐬𝐭 • 𝐃𝐞𝐚𝐝𝐥𝐲 ✦ ☠️

●───────────📂───────────●
 ⚙️ 𝐌𝐨𝐝𝐞 : [ 𝐏𝐮𝐛𝐥𝐢𝐜 ]
 🧠 𝐏𝐫𝐞𝐟𝐢𝐱 : [ / ]
 📦 𝐂𝐨𝐦𝐦𝐚𝐧𝐝𝐞𝐬 : [ 𝟒 ]
●────────────────────────●

 ╭─── 𓆩⚡𓆪 *𝐆𝐄́𝐍𝐄́𝐑𝐀𝐋* ───╮
 │
 │ 🩸 /start
 │ 🩸 /ping
 │ 🩸 /menu
 │
 ╰────────────────────────╯

 ╭─── 𓆩💀𓆪 *𝐀𝐓𝐓𝐀𝐐𝐔𝐄* ───╮
 │
 │ 🩸 /ban + numéro
 │
 ╰────────────────────────╯

   ╔══════════════════════╗

   ║   𝖖𝖚𝖊 𝖑𝖆 𝖕𝖚𝖗𝖌𝖊 𝖘𝖔𝖎𝖙   ║
   ╚══════════════════════╝
░▒▓█ 𓆩𝖓𝖇𝖌𝖉 𓆪 █▓▒░
"""
    await update.message.reply_text(text)

def register(commands):
    commands.append(CommandHandler("menu", menu))
