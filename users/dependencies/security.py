import hashlib
import hmac
import time

from fastapi import Request, HTTPException, status


class VerifyFiefSignature:
    def __init__(self, secret: str):
        self.secret = secret

    async def __call__(self, request: Request):
        timestamp = request.headers.get("X-Fief-Webhook-Timestamp")
        signature = request.headers.get("X-Fief-Webhook-Signature")

        if not timestamp or not signature:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing webhook headers"
            )

        if int(time.time()) - int(timestamp) > 5 * 60:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Webhook timestamp expired"
            )

        body_bytes = await request.body()
        payload = body_bytes.decode("utf-8")

        message = f"{timestamp}.{payload}"
        computed_hash = hmac.new(
            self.secret.encode("utf-8"),
            msg=message.encode("utf-8"),
            digestmod=hashlib.sha256,
        )
        computed_signature = computed_hash.hexdigest()

        if not hmac.compare_digest(signature, computed_signature):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid webhook signature"
            )
