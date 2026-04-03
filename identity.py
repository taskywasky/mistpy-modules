from telegram.ext import CommandHandler

from telegram import Bot

passedCtx = None

def run(ctx):
    global passedCtx
    print(f"[identify module] ctx keys: {list(ctx.keys())}")  # see what's available
    passedCtx = ctx
    ctx["app"].add_handler(CommandHandler("identify", identify))

async def identify(update, context):
    print(f"[identify] Received command from chat_id: {update.effective_chat.id}, username: {update.message.from_user.username}")

    if not passedCtx["auth"].CheckAuth(update.effective_chat.id):
        print(f"Unauthorized access attempt by {update.message.from_user.username}")
        return

    if not context.args:
        await update.message.reply_text("Usage: /identify <client_id>")
        return
    
    if context.args[0] != passedCtx["info"].ReturnClientID():
        print("Not the same client ID")
        return
    IDENTIFIERS = passedCtx["info"].GetUniqueIdentifiers()
    response = f"Current identifiers:\nMachine Name: {IDENTIFIERS['MachineName']}\nOS: {IDENTIFIERS['OS']} {IDENTIFIERS['OSVersion']} ({IDENTIFIERS['Architecture']})\nProcessor: {IDENTIFIERS['Processor']}\nUsername: {IDENTIFIERS['Username']}"
    await update.message.reply_text(response)
