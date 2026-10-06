#import requests as web
from func import days,datetime, timedelta
import celestial_calendar as celestial
from datetime import date
#原来的想法：大概1.3或1.4会加装格言，1.6或1.7加装ntfy获取新闻，2.0或2.1加装天气。目前先这样
#1.1添加日历获取、1.2添加风景
#格言：先随机调用一言的api(https://hitokoto.cn)和网易云评论的api，之后可能会自己做仓库
#新闻：github部署TrendRadar，发送到ntfy，然后requests收取
#天气：正在构思，希望在2.3或2.4为天气加上描述词
#基本上为class调用，然后回复。

nowday=days.Dime()

class Word:
    pass

class News:
    pass

class Weather:
    pass

class calendar:
    def __init__(self):
        self.data=celestial.GregorianDate.from_date(nowday.today)
        self.yindata=celestial.gregorian_to_lunar(celestial.LunarAlgorithm.ALGO3, self.data)
        self.luck = False
        self.luckqi = False
        self.luckri = False
        self.luckyi = False

        self.nowjieqi = None
        self.nowjieri = None
        self.nowjieyi = None
        JIEQI_CN = [
            "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
            "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
            "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
            "立冬", "小雪", "大雪", "冬至", "小寒", "大寒",
        ]  
        for jieqi in celestial.Jieqi:
            moment = celestial.jieqi_moment(nowday.today.year, jieqi)
    
            ut1 = moment.moment_ut1
            # 构造 UT1 的 datetime 对象
            ut1_dt = datetime(ut1.year, ut1.month, ut1.day) + timedelta(days=ut1.day_fraction)
            # 转为北京时间
            bj_dt = ut1_dt + timedelta(hours=8)
    
            if (bj_dt.year == nowday.today.year and
                bj_dt.month == nowday.today.month and
                bj_dt.day == nowday.today.day):
                    self.luckqi = True
                    self.luck = True
                    self.nowjieqi = JIEQI_CN[jieqi.value]
                    break
            
        d = nowday.today

        if (d.month, d.day) == (12, 25):
            self.luckri = True
            self.luck = True
            self.nowjieri = "圣诞节"
        elif (d.month, d.day) == (1, 1):
            self.luckri = True
            self.luck = True
            self.nowjieri = "元旦"
        elif (d.month, d.day) == (10, 1):
            self.luckri = True
            self.luck = True
            self.nowjieri = "国庆节"
        elif (d.month, d.day) == (7, 31):
            self.luckri = True
            self.luck = True
            self.nowjieri = "咖啡厅生日"
        match (self.yindata.month, self.yindata.day):
            case (1, 1):
                self.luckyi=True
                self.luck=True
                self.nowjieyi="春节"
            case (7, 7):
                self.luckyi=True
                self.luck=True
                self.nowjieyi="七夕节"
            case (8, 15):
                self.luckyi=True
                self.luck=True
                self.nowjieyi="中秋节"



class scenery:
    pass
