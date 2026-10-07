from func import days,hook
from datetime import date,timedelta,datetime
from zoneinfo import ZoneInfo
import pytest
def test_daytime():
    d = days.Dime()

    # 1. 时区正确性：today 应该是北京时间当天
    expected_today = datetime.now(ZoneInfo("Asia/Shanghai")).date()
    assert d.today == expected_today

    # 2. 基准日硬编码，作为回归护栏
    # 如果谁把 2025-07-31 改成别的，或把 +1 去掉，这里会挂
    assert d.delta == (expected_today - date(2025, 7, 31)).days + 1

    # 3. 基本约束：基准日之后 delta 至少为 1
    assert d.delta >= 1

    # 4. 类型
    assert isinstance(d.today, date)
    assert isinstance(d.delta, int)

def test_mycalendar_cases():
    """测试 MyCalendar 在正常、边界情况下的行为。"""

    # ---------- 1. 正常：公历节日（日期固定，可精确断言） ----------
    for d, name in [
        (date(2026, 1, 1),  "元旦"),
        (date(2026, 10, 1), "国庆节"),
        (date(2026, 12, 25),"圣诞节"),
        (date(2026, 7, 31), "咖啡厅生日"),
    ]:
        c = hook.MyCalendar(d)
        assert c.luckri is True, f"{d} 应是公历节日"
        assert c.luck is True,   f"{d} luck 应为 True"
        assert c.nowjieri == name, f"{d} 节日名应为 {name}，实际 {c.nowjieri}"

    # ---------- 2. 边界：非公历节日不应误报 ----------
    for d in [date(2026, 6, 15), date(2026, 11, 2)]:
        c = hook.MyCalendar(d)
        assert c.luckri is False, f"{d} 不应是公历节日"
        assert c.nowjieri is None, f"{d} nowjieri 应为 None"

    # ---------- 3. 边界：跨年相邻日，公历节日不应互相污染 ----------
    # 2026-12-31 与 2027-01-01 紧邻，1/1 是元旦，12/31 不是
    c_end = hook.MyCalendar(date(2026, 12, 31))
    c_new = hook.MyCalendar(date(2027, 1, 1))
    assert c_end.nowjieri is None
    assert c_new.nowjieri == "元旦"

    # ---------- 4. 全年扫描：结构性检查节气与农历节日 ----------
    jieqi_names = []
    lunar_names = []
    d = date(2026, 1, 1)
    end = date(2026, 12, 31)
    while d <= end:
        c = hook.MyCalendar(d)
        if c.luckqi:
            jieqi_names.append(c.nowjieqi)
        if c.luckyi:
            lunar_names.append(c.nowjieyi)
        d += timedelta(days=1)

    # 节气：名字必须在 JIEQI_CN 里，且一年内不重复
    assert len(jieqi_names) == len(set(jieqi_names)), \
        f"节气出现重名: {jieqi_names}"
    assert set(jieqi_names).issubset(set(hook.MyCalendar.JIEQI_CN)), \
        f"出现未知节气名: {jieqi_names}"
    # 公历一年内节气必然为24个
    assert len(jieqi_names) == 24, \
        f"节气数量异常: {len(jieqi_names)}"

    # 农历节日：春节、七夕、中秋各 1 次
    assert sorted(lunar_names) == sorted(["春节", "七夕节", "中秋节"]), \
        f"农历节日异常: {lunar_names}"

    # ---------- 5. 一致性：luck 应是三个分标志的“或” ----------
    d = date(2026, 1, 1)
    while d <= end:
        c = hook.MyCalendar(d)
        assert c.luck == (c.luckqi or c.luckri or c.luckyi), \
            f"{d} luck 与分标志不一致"
        d += timedelta(days=1)

@pytest.mark.skip(reason="exploration only, run manually")
def test_explore_year_2026():
    d = date(2026, 1, 1)
    end = date(2026, 12, 31)
    while d <= end:
        c = hook.MyCalendar(d)
        marks = []
        if c.luckqi:
            marks.append(f"节气:{c.nowjieqi}")
        if c.luckri:
            marks.append(f"公历:{c.nowjieri}")
        if c.luckyi:
            marks.append(f"农历:{c.nowjieyi}")
        if marks:
            print(d, "|", ", ".join(marks))
        d += timedelta(days=1)