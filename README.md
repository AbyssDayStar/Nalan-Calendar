# Nalan-Calendar
> 给时光以生命，而不是给生命以时光

使用simplematrixbot库制作的matrix机器人
实现了每日日历和新闻转发
**欢迎**加入matrix讨论[NalanCafe/纳兰咖啡厅](chat.neboer.site/#/#N.cafe:chat.neboer.site)
也欢迎在issue提建议

## 具体实现：
### 日历
利用datetime计算和换算时间
### 发送
使用simplematrixbot转发
### 定时
GithubAction运行

## 结构
```
/
|
+---bot                 有关Matrix机器人
|   \---send.py         调用simplematrixbot发送
|
+---func                数据获取和计算
|   +---days.py         计算日期（本来就是日历对吧）
|   \---hook.py         [规划中]网络钩子，用于api获取，之后会拆成几个部分
|
+---test                [规划中]调试脚本
|
+---main.py             主进程，调取func数据，格式化后发给bot
+---mise.toml           mise环境规划
+---requirements.txt    包管理
\---README.md           介绍文件（也就是本文件(∠・ω< )⌒☆）

```

## 规划
**当前**
- [x] v0.5  库寻找和开发环境部署（*一个好的开始就是成功的一半*）
- [ ] v0.6  日期计算
- [ ] v0.7  日期格式化
- [ ] v0.8  bot制作和初次发送
- [ ] v0.9  Github Action 部署
- [ ] v1.0  最终调试
---
**想的有些远了**
- [ ] v2.0  基本网络获取完成
- [ ] v2.5  网络数据格式化和调试
- [ ] v3.*  上游自搭建，一些人文关怀和小巧思
- [ ] v4.*  小修小补

## 作者
AbyssDayStar和DeepSeek

