# bot/send.py
import os
from nio import AsyncClient

async def inSend(text: str):
    homeserver = os.getenv("MATRIX_HOMESERVER")
    user_id = os.getenv("MATRIX_USER_ID")
    access_token = os.getenv("MATRIX_ACCESS_TOKEN")
    room_id = os.getenv("MATRIX_ROOM_ID", "!IlbFNHvoIvWRNsRSap:chat.neboer.site")

    if not homeserver or not user_id or not access_token:
        raise ValueError("缺少必要的环境变量: MATRIX_HOMESERVER, MATRIX_USER_ID, MATRIX_ACCESS_TOKEN")

    client = AsyncClient(homeserver, user_id)
    try:
        # 登录并检查响应
        response = await client.login(token=access_token)
        if not response:
            raise RuntimeError("登录失败: 未收到响应")
        if hasattr(response, 'access_token'):
            # 成功登录
            print(f"登录成功，设备ID: {response.device_id}")
        else:
            # 如果有错误字段
            error_msg = getattr(response, 'message', '未知错误')
            raise RuntimeError(f"登录失败: {error_msg}")

        # 发送消息
        await client.room_send(
            room_id,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": text}
        )
        print("消息发送成功")
    finally:
        await client.close()