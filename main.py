from func import days
#计算日期
from func import hook
#hook用于网络钩子，1.3添加日历获取，1.5添加风景
from bot import send
#调用botlib发送
def format_message(dime, calen):
    text = f"纳兰纪元第{dime.delta}天"

    if calen.luck:
        text+="，今天是"
    names = []
    if calen.luckri:
        names.append(calen.nowjieri)
    if calen.luckyi:
        names.append(calen.nowjieyi)
    if names:
        text += "、".join(names) + "🎉"
        if calen.luckqi:
            text+=","
    if calen.luckqi:
        text += f"{calen.nowjieqi}日"

    return text


if __name__ == "__main__":
    dime = days.Dime()
    calen = hook.MyCalendar(dime.today)

    if dime.delta % 10 == 0 or calen.luck:
        send.inSend(format_message(dime, calen))



