var bot = (TelegramBotClient)ctx["bot"];
var commands = (Dictionary<string, Func<string, dynamic, Task>>)ctx["commands"];

commands["/hello"] = async (args, msg) =>
{
    await bot.SendMessage(msg.Chat.Id, "Hello from a script module!");
};
