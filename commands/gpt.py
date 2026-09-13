import os
import requests
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler

# --- CLÉS API (à mettre dans Render → Environment) ---
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY")

# --- FONCTION OPENAI ---
def ask_openai(prompt):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "gpt-4o-mini",  # ou gpt-3.5-turbo
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# --- FONCTION DEEPSEEK ---
def ask_deepseek(prompt):
    url = "https://api.deepseek.com/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "deepseek-chat",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 1000
    }
    response = requests.post(url, headers=headers, json=data)
    return response.json()["choices"][0]["message"]["content"]

# --- COMMANDE /gpt ---
async def gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text(
            "❌ Utilisation : `/gpt <ta question>`\n"
            "Exemple : `/gpt Explique-moi la photosynthèse`",
            parse_mode="Markdown"
        )
        return

    prompt = " ".join(context.args)

    # Menu de choix
    keyboard = [
        [
            InlineKeyboardButton("OpenAI (GPT-4o)", callback_data=f"gpt_openai_{prompt[:50]}"),
            InlineKeyboardButton("DeepSeek", callback_data=f"gpt_deepseek_{prompt[:50]}")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        f"🧠 *Question :* {prompt[:100]}...\n\n"
        f"🔮 *Choisis ton modèle :*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# --- GESTION DU CHOIX DU MODÈLE ---
async def gpt_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = query.data.split("_", 2)
    model = data[1]
    prompt = data[2]

    await query.edit_message_text(f"⏳ *{model.upper()} réfléchit...*", parse_mode="Markdown")

    try:
        if model == "openai":
            response = ask_openai(prompt)
        else:
            response = ask_deepseek(prompt)

        # Limiter la réponse à 4000 caractères
        if len(response) > 4000:
            response = response[:4000] + "..."

        await query.edit_message_text(
            f"🤖 *{model.upper()} :*\n\n{response}",
            parse_mode="Markdown"
        )
    except Exception as e:
        await query.edit_message_text(f"❌ Erreur : {str(e)}")

# --- ENREGISTREMENT ---
def register(commands):
    commands.append(CommandHandler("gpt", gpt))
    commands.append(CallbackQueryHandler(gpt_callback, pattern=r"^gpt_"))
