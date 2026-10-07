#import requests as web
#from func import days
import celestial_calendar as celestial
from datetime import date, timedelta
#原来的想法：大概1.3或1.4会加装格言，1.6或1.7加装ntfy获取新闻，2.0或2.1加装天气。目前先这样
#1.1添加日历获取、1.2添加风景
#格言：先随机调用一言的api(https://hitokoto.cn)和网易云评论的api，之后可能会自己做仓库
#新闻：github部署TrendRadar，发送到ntfy，然后requests收取
#天气：正在构思，希望在2.3或2.4为天气加上描述词
#基本上为class调用，然后回复。

class Word:
    pass

class News:
    pass

class Weather:
    pass

class MyCalendar:
    @staticmethod
    def to_beijing_date(civil):
    # 当天已过秒数 + 8 小时
        seconds = civil.fraction * 86400 + 8 * 3600
        days_to_add = int(seconds // 86400)
        utc_date = date(civil.year, civil.month, civil.day)
        return utc_date + timedelta(days=days_to_add)
    
    JIEQI_CN = [
        "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
        "立夏", "小满", "芒种", "夏至", "小暑", "大暑",
        "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
        "立冬", "小雪", "大雪", "冬至", "小寒", "大寒",
    ]
    holidays = {
        (12, 25): "圣诞节",
        (1, 1): "元旦",
        (10, 1): "国庆节",
        (7, 31): "咖啡厅生日",
    }
    festival = {
        (1,1):"春节",
        (7,7):"七夕节",
        (8,15):"中秋节",
    }  

    def __init__(self,today:date):
        #初始化
        self.data=celestial.GregorianDate.from_date(today)
        self.yindata=celestial.gregorian_to_lunar(celestial.LunarAlgorithm.ALGO3, self.data)
        self.luck = False
        self.luckqi = False
        self.luckri = False
        self.luckyi = False
        self.nowjieqi = None
        self.nowjieri = None
        self.nowjieyi = None

        #节气判断
        for jieqi in celestial.Jieqi:
            moment = celestial.jieqi_moment(today.year, jieqi)
            beijing_date = self.to_beijing_date(moment.moment_ut1)
            if beijing_date == today:
                    self.luckqi = True
                    self.luck = True
                    self.nowjieqi = self.JIEQI_CN[jieqi.value]
                    break
        #节日判断
        # 公历           
        jiemd = (today.month, today.day)
        if name := self.holidays.get(jiemd):
            self.luckri = self.luck = True
            self.nowjieri = name
        #阴历
        if not self.yindata.is_leap:
            yinmd=(self.yindata.month,self.yindata.day)
            if name := self.festival.get(yinmd):
                self.luckyi=self.luck=True
                self.nowjieyi=name



class scenery:
    pass
