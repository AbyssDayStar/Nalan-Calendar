# bot/send.py
import asyncio
import os

class MatrixCommander:
    """封装 matrix-commander 命令行工具，使用 Access Token 认证"""
    def __init__(self, homeserver: str, username: str, token: str):
        self.homeserver = homeserver
        self.username = username
        self.token = token

    async def send(self, room_id: str, text: str):
        """发送消息到指定房间"""
        cmd = [
            "matrix-commander",
            "--homeserver", self.homeserver,
            "--user", self.username,
            "--token", self.token,
            "--room", room_id,
            "--message", text,
        ]
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        _, stderr = await proc.communicate()
        if proc.returncode != 0:
            raise RuntimeError(f"发送失败: {stderr.decode().strip()}")

_mc = None

async def inSend(text: str):
    global _mc
    if _mc is None:
        homeserver = os.environ.get("MATRIX_HOMESERVER", "https://chat.neboer.site")
        username = os.environ.get("MATRIX_USERNAME", "stp_bot")
        token = os.environ.get("MATRIX_ACCESS_TOKEN","syt_c3RwX2JvdA_mFzGxwnTTdcanJGOzAOC_1v1YYf")
        if not token:
            raise ValueError("未找到 MATRIX_ACCESS_TOKEN 环境变量，请设置 Access Token")
        _mc = MatrixCommander(homeserver, username, token)
    room_id = os.environ.get("MATRIX_ROOM_ID", "!IlbFNHvoIvWRNsRSap:chat.neboer.site")
    await _mc.send(room_id, text)