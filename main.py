import asyncio
from func import days
#计算日期
#from func import hook
#hook用于网络钩子，1.1添加日历获取、1.2添加风景
from bot import send
#调用botlib发送
async def main():
    """main：将数据格式化，交给发送端"""
    date=days.Dime()
    text=f"纳兰纪元第{date.delta}天"
    await send.inSend(text)

if __name__=="__main__":
    asyncio.run(main()) # 异步调用
    



