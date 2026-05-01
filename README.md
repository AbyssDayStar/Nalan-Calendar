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
+---test                [不定]调试脚本
|
+---main.py             主进程，调取func数据，格式化后发给bot
+---mise.toml           mise环境规划
+---requirements.txt    包管理
\---README.md           介绍文件（也就是本文件(∠・ω< )⌒☆）

```

## 规划
**当前**
- [x] 库寻找和开发环境部署（*一个好的开始就是成功的一半*）
- [x] 日期计算
- [x] 日历制作
- [ ] 初次发送
- [ ] Github Action 部署
- [ ] 最终调试 
---
**想的有些远了**
- [ ] 基本网络获取完成
- [ ] 网络数据格式化和调试
- [ ] 上游自搭建，一些人文关怀和小巧思

## 作者
AbyssDayStar和DeepSeek

