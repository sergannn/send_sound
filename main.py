import asyncio
from http.client import HTTPException
from telethon import TelegramClient, events, sync
from fastapi import FastAPI

app = FastAPI()
api_id =   21433623 #25151470
api_hash =  '4862f5339c133e3d738d830c7f4250fc' #'a8589726dfdebd7c1eed521c29de88e6'
target_username='me'

@app.get("/")
async def send_telegram_message(api_id: str, api_hash: str, target_username: str):
    try:
        # Создаем экземпляр TelegramClient с переданными параметрами
        client = TelegramClient('session_name', api_id, api_hash)
        
        await client.start()
        await client.send_message("me", 'Hello from FastAPI and Telethon!')
        await client.disconnect()
        
        return {"message": "Message sent successfully!"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

client = TelegramClient('anon', api_id, api_hash)

async def main():
    # You can send messages to yourself...
    await client.send_message('kirR951', 'Hello, myself!')
    # ...to some chat ID
    #await client.send_message(-100123456, 'Hello, group!')
    # ...to your contacts
    #await client.send_message('+34600123123', 'Hello, friend!')
    # ...or even to any username
    #await client.send_message('TelethonChat', 'Hello, Telethon!')

#with client:
#    client.loop.run_until_complete(main())

#send_telegram_message(api_id, api_hash, target_username)

    
