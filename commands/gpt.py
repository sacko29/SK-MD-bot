import os
from openai import OpenAI
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler, MessageHandler, filters

# --- CLIENT OPENAI ---
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# --- FONCTION QUI APPELLE OPENAI ---
def ask_openai(prompt):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Tu es un assistant utile et concis."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=1000
    )
    return response.choices[0].message.content

# --- COMMANDE /gpt ---
async def gpt(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        context.user_data["waiting_for_gpt"] = True
        await update.message.reply_text(
            "🧠 *Je suis à l'écoute.*\n\n"
            "Pose ta question.",
            parse_mode="Markdown"
        )
        return

    prompt = " ".join(context.args)
    await update.message.reply_text("⏳ *Réflexion...*", parse_mode="Markdown")

    try:
        answer = ask_openai(prompt)
        if len(answer) > 4000:
            answer = answer[:4000] + "..."
        await update.message.reply_text(f"🤖 *OpenAI :*\n\n{answer}", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Erreur : {str(e)}")

# --- RÉCEPTION DE LA QUESTION ---
async def gpt_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.user_data.get("waiting_for_gpt"):
        return

    context.user_data["waiting_for_gpt"] = False
    prompt = update.message.text

    await update.message.reply_text("⏳ *Réflexion...*", parse_mode="Markdown")

    try:
        answer = ask_openai(prompt)
        if len(answer) > 4000:
            answer = answer[:4000] + "..."
        await update.message.reply_text(f"🤖 *OpenAI :*\n\n{answer}", parse_mode="Markdown")
    except Exception as e:
        await update.message.reply_text(f"❌ Erreur : {str(e)}")

# --- ENREGISTREMENT ---
def register(commands):
    commands.append(CommandHandler("gpt", gpt))
    commands.append(MessageHandler(filters.TEXT & ~filters.COMMAND, gpt_message))
