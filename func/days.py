from datetime import date,datetime
from zoneinfo import ZoneInfo

class Dime:
    """计算日期"""
    def __init__(self):
        self.today = datetime.now(ZoneInfo("Asia/Shanghai")).date()
        self.delta = (self.today-date(2025,7,31)).days + 1
    


