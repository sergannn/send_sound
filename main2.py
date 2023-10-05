from fastapi import FastAPI, HTTPException
from telethon import TelegramClient
import asyncio

app = FastAPI()

@app.post("/start_auth")
async def start_auth(api_id: int, api_hash: str, phone: str):
    try:
        client = TelegramClient(phone, api_id, api_hash,system_version="4.16.30-vxSER")
        await client.connect()
        if not await client.is_user_authorized():
            result = await client.send_code_request(phone, force_sms=True)
            phone_code_hash = result.phone_code_hash
            return {"message": "Введите код от TG", "phone_code_hash": phone_code_hash}
        await client.send_message('me', 'Hello, myself!')
        return {"message": "Авторизован"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/verify_code")
async def verify_code(api_id: int, api_hash: str, phone: str, code: str, phone_code_hash: str):
    try:
        client = TelegramClient(phone, api_id, api_hash,system_version="4.16.30-vxSER")
        await client.connect()
        await client.sign_in(phone, code, phone_code_hash=phone_code_hash)
        await client.send_message('me', 'Hello, myself!')
        return {"message": "Авторизован"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
