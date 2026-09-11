import random
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes, CommandHandler, CallbackQueryHandler
from data.motifs import MOTIFS

# --- TEXTES DARK ---
MENACES = [
    "☠️ *Le verdict est tombé.* SK-MD a parlé.",
    "🔥 *La purge est en marche.* Aucun recours.",
    "💀 *La nuit est tombée* sur `{target}`.",
    "⚔️ *Les portes du néant* s'ouvrent pour `{target}`.",
    "🌀 *Le protocole d'effacement* est activé.",
    "👁️ *SK-MD a vu.* SK-MD a jugé. SK-MD exécute.",
    "🌑 *Silence.* Puis le bruit du ban qui tombe.",
    "🔮 *L'oracle a parlé* : `{target}` sera effacé.",
    "🩸 *Le sang coule.* La purge commence.",
    "⚰️ *Ton heure est venue.* `{target}`.",
]

REPONSES_BAN = [
    "🚀 *Attaque lancée* sur `{target}`. Aucune pitié.",
    "💥 `{target}` *est en train de brûler.* Adieu.",
    "🎯 *Cible* `{target}` *verrouillée.* Tir en cours.",
    "🔥 *SK-MD entre en action.* `{target}` est mort.",
    "🕳️ `{target}` *va disparaître.* Définitivement.",
    "🧨 *Feu sur* `{target}`. Que le chaos commence.",
    "🌪️ *La tempête noire* s'abat sur `{target}`.",
    "⚰️ `{target}` *est dans le viseur.* RIP.",
    "☠️ *Un de moins.* `{target}` est effacé.",
    "🩸 *Le protocole est terminé.* `{target}` n'est plus.",
]

ERREURS = [
    "❌ *Numéro manquant.* Ouvre les yeux.",
    "⚠️ *Utilisation :* `/ban + numéro` (ex: `/ban 0612345678`)",
    "🔴 *Commande incorrecte.* Réessaye.",
    "💀 *Tu as oublié la cible.* Réfléchis.",
]

async def ban(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        target = context.args[0]
        context.user_data["target"] = target

        keyboard = []
        for key, motif in MOTIFS.items():
            keyboard.append([
                InlineKeyboardButton(
                    f"{motif['emoji']} {motif['nom']}",
                    callback_data=f"motif_{key}"
                )
            ])

        reply_markup = InlineKeyboardMarkup(keyboard)

        await update.message.reply_text(
            f"╔══════════════════════╗\n"
            f"║  ☠️ *𝐏𝐑𝐎𝐓𝐎𝐂𝐎𝐋𝐄 𝐃'𝐄́𝐋𝐈𝐌𝐈𝐍𝐀𝐓𝐈𝐎𝐍* ☠️\n"
            f"╚══════════════════════╝\n\n"
            f"🎯 *Cible verrouillée :* `{target}`\n\n"
            f"🔮 *Choisis le motif du signalement :*",
            reply_markup=reply_markup,
            parse_mode="Markdown"
        )

    except IndexError:
        await update.message.reply_text(
            random.choice(ERREURS),
            parse_mode="Markdown"
        )

async def motif_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    motif_key = query.data.split("_")[1]
    motif = MOTIFS.get(motif_key)
    target = context.user_data.get("target", "inconnu")

    if not motif:
        await query.edit_message_text("❌ Motif invalide.")
        return

    keyboard = []
    for i, msg in enumerate(motif["messages"], 1):
        keyboard.append([
            InlineKeyboardButton(
                f"📩 𝐌𝐞𝐬𝐬𝐚𝐠𝐞 {i}",
                callback_data=f"msg_{motif_key}_{i-1}"
            )
        ])

    reply_markup = InlineKeyboardMarkup(keyboard)

    await query.edit_message_text(
        f"╔══════════════════════╗\n"
        f"║  {motif['emoji']} *{motif['nom'].upper()}* {motif['emoji']}\n"
        f"╚══════════════════════╝\n\n"
        f"🎯 *Cible :* `{target}`\n"
        f"🩸 *Description :* _{motif['description']}_\n\n"
        f"📜 *Choisis le message à envoyer :*",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

async def message_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    parts = query.data.split("_")
    motif_key = parts[1]
    msg_index = int(parts[2])

    motif = MOTIFS.get(motif_key)
    target = context.user_data.get("target", "inconnu")
    message = motif["messages"][msg_index]

    menace = random.choice(MENACES).format(target=target)
    attaque = random.choice(REPONSES_BAN).format(target=target)

    await query.edit_message_text(
        f"{menace}\n\n"
        f"╭──────────────────────╮\n"
        f"│ ⏳ 𝐄𝐍 𝐂𝐎𝐔𝐑𝐒...       │\n"
        f"│ ██████░░░░ 50%       │\n"
        f"│ ██████████ 100%      │\n"
        f"╰──────────────────────╯\n\n"
        f"{attaque}\n\n"
        f"╔══════════════════════╗\n"
        f"║  📋 *𝐑𝐀𝐏𝐏𝐎𝐑𝐓 𝐃'𝐀𝐓𝐓𝐀𝐐𝐔𝐄*\n"
        f"╚══════════════════════╝\n"
        f"🎯 *Cible :* `{target}`\n"
        f"{motif['emoji']} *Motif :* {motif['nom']}\n"
        f"📩 *Message :* _{message[:100]}_\n\n"
        f"✅ *Signalements simulés envoyés.*\n"
        f"💀 *Que la purge soit.*",
        parse_mode="Markdown"
    )

def register(commands):
    commands.append(CommandHandler("ban", ban))
    commands.append(CallbackQueryHandler(motif_callback, pattern=r"^motif_"))
    commands.append(CallbackQueryHandler(message_callback, pattern=r"^msg_"))
