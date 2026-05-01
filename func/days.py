from datetime import date,timedelta,datetime
from zoneinfo import ZoneInfo

class Dime:
    """计算日期"""
    def __init__(self):
        self.now = datetime.now(ZoneInfo("Asia/Shanghai")).date()
        self.delta = (self.now-date(2025,7,31)).days + 1
    


