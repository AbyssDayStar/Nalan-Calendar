# bot/send.py
import asyncio
import os

class MatrixCommander:
    def __init__(self, homeserver: str, username: str, token: str,password:str):
        self.homeserver = homeserver
        self.username = username
        self.token = token
        self.password = password

    async def send(self, room_id: str, text: str):
        cmd = [
            "matrix-commander",
            "--homeserver", self.homeserver,
            "--user", self.username,
            "--access-token", self.token,   
            "--room", room_id,
            "--message", text,
            "-password", self.password,
            "--login", "password",
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
        password = os.environ.get("MATRIX_PASSWORD", "Stp@Ie110920111029")
        if not token:
            raise ValueError("未找到 MATRIX_ACCESS_TOKEN 环境变量")
        if not password:
            raise ValueError("未找到 MATRIX_PASSWORD 环境变量")
        _mc = MatrixCommander(homeserver, username, token,password)
    room_id = os.environ.get("MATRIX_ROOM_ID", "!IlbFNHvoIvWRNsRSap:chat.neboer.site")
    await _mc.send(room_id, text)