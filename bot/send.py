# bot/send.py
import os
import sys
import uuid
import logging
import requests

logger = logging.getLogger(__name__)


def inSend(text: str) -> bool:
    """使用 requests 转发到官方 API 发送。

    成功返回 True。
    失败时记录日志、打印 GitHub Actions 错误注释，并抛出 RuntimeError。
    """
    homeserver = os.getenv("MATRIX_HOMESERVER")
    access_token = os.getenv("MATRIX_ACCESS_TOKEN")
    room_id = os.getenv("MATRIX_ROOM_ID")

    # 显式检查，且打印到底缺哪个（不打印值）
    missing = [
        name for name, val in [
            ("MATRIX_HOMESERVER", homeserver),
            ("MATRIX_ACCESS_TOKEN", access_token),
            ("MATRIX_ROOM_ID", room_id),
        ] if not val
    ]
    if missing:
        msg = f"缺少环境变量: {', '.join(missing)}"
        logger.error(msg)
        print(f"::error title=Matrix 配置缺失::{msg}")
        raise RuntimeError(msg)

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
    }
    payload = {
        "msgtype": "m.text",
        "body": text,
    }

    txn_id = str(uuid.uuid4())
    # room_id 里可能带 ! 和 :，需要 URL 编码；这里最简单是交给 requests 处理路径
    # 如果 room_id 形如 !abc:example.com，直接拼进 URL 会有问题，见下方说明
    url = (
        f"{homeserver}/_matrix/client/v3/rooms/"
        f"{requests.utils.quote(room_id, safe='')}"
        f"/send/m.room.message/{txn_id}"
    )

    logger.info("发送到 room=%s, txn=%s", room_id, txn_id)

    try:
        response = requests.put(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        # 把 HTTP 状态码和响应体也带出来，排查关键
        detail = ""
        resp = getattr(e, "response", None)
        if resp is not None:
            detail = f" status={resp.status_code} body={resp.text[:500]}"
        msg = f"发送失败: {e}{detail}"
        logger.error(msg)
        print(f"::error title=Matrix 发送失败::{msg}")
        raise RuntimeError(msg) from e

    # 校验 Matrix 返回里有没有 event_id
    try:
        data = response.json()
    except ValueError:
        data = {}
    event_id = data.get("event_id")
    if not event_id:
        msg = f"发送接口返回 2xx 但没有 event_id: {response.text[:500]}"
        logger.error(msg)
        print(f"::error title=Matrix 返回异常::{msg}")
        raise RuntimeError(msg)

    logger.info("消息发送成功 event_id=%s", event_id)
    return True