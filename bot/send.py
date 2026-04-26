import simplematrixbotlib as botlib
#制作机器人并转发到matrix群
async def inSend(days:int,now:int,news:str):
    creds=botlib.Creds("https://chat.neboer.site","stp_bot","Stp@Ie110920111029")
    bot=botlib.Bot(creds)
    # 登录机器人


