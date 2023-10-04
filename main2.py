from fastapi import FastAPI, HTTPException
from telethon import TelegramClient
import asyncio

app = FastAPI()

@app.post("/start_auth")
async def start_auth(api_id: int, api_hash: str, phone: str):
    try:
        client = TelegramClient(phone, api_id, api_hash)
        await client.connect()
        if not await client.is_user_authorized():
            await client.send_code_request(phone)
            return {"message": "Введите код от TG"}
        return {"message": "Авторизован"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/verify_code")
async def verify_code(api_id: int, api_hash: str, phone: str, code: str):
    try:
        client = TelegramClient(phone, api_id, api_hash)
        await client.connect()
        await client.sign_in(phone, code)
        return {"message": "Авторизован"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))