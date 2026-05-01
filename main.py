import asyncio
from func import days
#计算日期
#from func import hook
#hook用于网络钩子，大概1.3或1.4会加装格言，1.6或1.7加装ntfy获取新闻，2.0或2.1加装天气。目前先这样
from bot import send
#调用botlib发送
async def main():
    """main：将数据格式化，交给发送端"""
    date=days.Dime()
    text=f"纳兰纪元第{date.delta}天"
    await send.inSend(text)

if __name__=="__main__":
    asyncio.run(main())
    



