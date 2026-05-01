# bot/send.py
import asyncio
import os

class MatrixCommander:
    """封装 matrix-commander 命令行工具，提供直观的 send 方法"""
    def __init__(self, homeserver: str, username: str, password: str):
        self.homeserver = homeserver
        self.username = username
        self.password = password

    async def send(self, room_id: str, text: str):
        """发送消息到指定房间"""
        cmd = [
            "matrix-commander",
            "--homeserver", self.homeserver,
            "--user", self.username,
            "--password", self.password,
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

# 全局单例（从环境变量初始化）
_mc = None

async def inSend(text: str):
    global _mc
    if _mc is None:
        homeserver = os.environ.get("MATRIX_HOMESERVER", "https://chat.neboer.site")
        username = os.environ.get("MATRIX_USERNAME", "stp_bot")
        password = os.environ.get("MATRIX_PASSWORD", "Stp@Ie110920111029")
        if not password:
            raise ValueError("未找到 MATRIX_PASSWORD 环境变量")
        _mc = MatrixCommander(homeserver, username, password)
    room_id = os.environ.get("MATRIX_ROOM_ID","!IlbFNHvoIvWRNsRSap:chat.neboer.site")
    await _mc.send(room_id, text)