import random
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

MENACES = [
    "☠️ Le verdict est tombé. SK-MD a parlé.",
    "🔥 La purge est en marche. Aucun recours.",
    "💀 La nuit est tombée sur {target}.",
    "⚔️ Les portes du néant s'ouvrent pour {target}.",
    "🌀 Le protocole d'effacement est activé.",
    "👁️ SK-MD a vu. SK-MD a jugé. SK-MD exécute.",
    "🌑 Silence. Puis le bruit du ban qui tombe.",
    "🔮 L'oracle a parlé : {target} sera effacé.",
]

REPONSES_BAN = [
    "🚀 Attaque lancée sur {target}. Aucune pitié.",
    "💥 {target} est en train de brûler. Adieu.",
    "🎯 Cible {target} verrouillée. Tir en cours.",
    "🔥 SK-MD entre en action. {target} est mort.",
    "🕳️ {target} va disparaître. Définitivement.",
    "🧨 Feu sur {target}. Que le chaos commence.",
    "🌪️ La tempête noire s'abat sur {target}.",
    "⚰️ {target} est dans le viseur. RIP.",
]

ERREURS = [
    "❌ Numéro manquant. Ouvre les yeux.",
    "⚠️ Utilisation : /ban + numéro (ex: /ban 0612345678)",
    "🔴 Commande incorrecte. Réessaye.",
]

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        target = context.args[0]
        menace = random.choice(MENACES).format(target=target)
        attaque = random.choice(REPONSES_BAN).format(target=target)

        await update.message.reply_text(menace)
        await update.message.reply_text("⏳ 0%... 50%... 100%")
        await update.message.reply_text(attaque)

    except IndexError:
        erreur = random.choice(ERREURS)
        await update.message.reply_text(erreur)

def register(commands):
    commands.append(CommandHandler("nom", fonction))
