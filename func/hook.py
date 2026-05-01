import requests as web
#大概1.3或1.4会加装格言，1.6或1.7加装ntfy获取新闻，2.0或2.1加装天气。目前先这样
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
