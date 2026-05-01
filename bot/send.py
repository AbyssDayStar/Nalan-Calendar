# bot/send.py
import os
import requests
import uuid
from func import days
import asyncio

async def inSend(text: str):
    '''使用requests转发到官方API发送'''
    homeserver = os.getenv("MATRIX_HOMESERVER") # 从环境变量获取 服务器地址
    access_token = os.getenv("MATRIX_ACCESS_TOKEN") # 从环境变量获取 token
    room_id = os.getenv("MATRIX_ROOM_ID")  # 从环境变量获取 房间地址

    if not access_token:
        raise ValueError("未找到 MATRIX_ACCESS_TOKEN 环境变量") # 环境变量检查

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    } # 设置请求头
    payload = {
        "msgtype": "m.text",
        "body": text,
    } # 设置发送类型

    txn_id = str(uuid.uuid4()) # 标识符，防止重复发送
    url = f"{homeserver}/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txn_id}" # 拼接请求url
    response = requests.put(url, json=payload, headers=headers) # put发送
    if response.status_code != 200:
        raise RuntimeError(f"发送失败 (HTTP {response.status_code}): {response.text}") # 错误输出

    print("消息发送成功") # 输出
