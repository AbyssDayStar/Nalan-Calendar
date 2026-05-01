# bot/send.py
import os
import requests
import uuid
from func import days
import asyncio

async def inSend(text: str):
    # 使用正确的 homeserver 地址（带端口）
    #homeserver = os.getenv("MATRIX_HOMESERVER", "https://matrix.neboer.site:8448").rstrip('/')
    #access_token = os.getenv("MATRIX_ACCESS_TOKEN", "syt_c3RwX2JvdA_ksVTBlhSLMMsaLwxfnBr_3RSdhT")
    #room_id = os.getenv("MATRIX_ROOM_ID", "!IlbFNHvoIvWRNsRSap:chat.neboer.site")  # 房间 ID 可能不变

    homeserver = "https://matrix.neboer.site:8448/"
    access_token = "syt_c3RwX2JvdA_ksVTBlhSLMMsaLwxfnBr_3RSdhT"
    room_id = "!IlbFNHvoIvWRNsRSap:chat.neboer.site"

    if not access_token:
        raise ValueError("未找到 MATRIX_ACCESS_TOKEN 环境变量")

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "msgtype": "m.text",
        "body": text,
    }

    txn_id = str(uuid.uuid4())
    url = f"{homeserver}/_matrix/client/v3/rooms/{room_id}/send/m.room.message/{txn_id}"
    response = requests.put(url, json=payload, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f"发送失败 (HTTP {response.status_code}): {response.text}")

    print("消息发送成功")
