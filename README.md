# Nalan-Calendar
> 一场有时差的雨，让人错过又让人相遇，也让那些曾以为过不去的雨季，最终都成了滋润生命的河流。

> _此项目献给我的初中三年_

使用requests库制作的matrix机器人
目前实现了每日日历
**欢迎**加入matrix讨论[NalanCafe/纳兰咖啡厅](chat.neboer.site/#/#N.cafe:chat.neboer.site)
也欢迎在issue提建议

## 具体实现：
### 日历
利用datetime计算和换算时间
### 发送
使用requests转发
### 定时
GithubAction运行

## 结构
```
/
|
+---bot                 有关Matrix机器人
|   \---send.py         调用requests发到Matrix Api发送
|
+---func                数据获取和计算
|   +---days.py         计算日期
|   \---hook.py         功能钩子，每个class一个功能
|
+---test                围栏脚本
|
+---main.py             主进程，调取func数据，筛选日期，格式化后发给bot
+---pyproject.toml      项目管理     
+---requirements.txt    包管理
\---README.md           介绍文件（也就是本文件(∠・ω< )⌒☆）

```

## 已完成
- [x] 1.0
 - [x] 库寻找和开发环境部署（*一个好的开始就是成功的一半*）
 - [x] 日期计算
 - [x] 日历制作
 - [x] Github Action 部署
 - [x] 初次发送
 - [x] 最终调试 
## 正在
- [ ] 1.3
 - [x] 重构后端，改异步为同步，修改发送时间
 - [x] 日历获取
 - [ ] 每次新闻（热点、风俗或者风景）



## 作者
AbyssDayStar和DeepSeek

