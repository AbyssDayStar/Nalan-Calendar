import simplematrixbotlib as botlib

async def inSend(text:str):
    """制作机器人并转发到matrix群"""
    creds=botlib.Creds("https://chat.neboer.site","stp_bot","Stp@Ie110920111029")
    bot=botlib.Bot(creds)
    # 登录机器人
    ROOM_ID="!IlbFNHvoIvWRNsRSap:chat.neboer.site"

    await bot.async_client.login(creds.password, device_name="Github")
    await bot.async_client.sync(timeout=30000, full_state=True)  # 同步一次，获取房间信息
    await bot.api.send_text_message(ROOM_ID,text)
    await bot.async_client.close()
    

