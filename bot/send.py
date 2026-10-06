# bot/send.py
import os
import requests
import uuid

def inSend(text: str):
    '''使用requests转发到官方API发送（同步版本）'''
    homeserver = os.getenv("MATRIX_HOMESERVER")
    access_token = os.getenv("MATRIX_ACCESS_TOKEN")
    room_id = os.getenv("MATRIX_ROOM_ID")

    if not all([homeserver, access_token, room_id]):
        raise ValueError("未找到 MATRIX_HOMESERVER、MATRIX_ACCESS_TOKEN 或 MATRIX_ROOM_ID 环境变量")

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
    
    try:
        response = requests.put(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status() # 如果状态码不是200，自动抛出HTTPError
        print("消息发送成功")
    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"发送失败: {e}")
