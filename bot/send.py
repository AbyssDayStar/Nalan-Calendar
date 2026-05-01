# bot/send.py
import os
from nio import AsyncClient

async def inSend(text: str):
    homeserver = os.getenv("MATRIX_HOMESERVER", "https://chat.neboer.site")
    user_id = os.getenv("MATRIX_USER_ID", "@stp_bot:chat.neboer.site")
    access_token = os.getenv("MATRIX_ACCESS_TOKEN", "syt_c3RwX2JvdA_ksVTBlhSLMMsaLwxfnBr_3RSdhT")
    room_id = os.getenv("MATRIX_ROOM_ID", "!IlbFNHvoIvWRNsRSap:chat.neboer.site")

    client = AsyncClient(homeserver, user_id)
    try:
        # 使用 access token 登录
        await client.login(token=access_token)
        # 发送消息
        await client.room_send(
            room_id,
            message_type="m.room.message",
            content={"msgtype": "m.text", "body": text}
        )
    finally:
        await client.close()