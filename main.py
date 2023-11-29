from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from bot import dp, bot
from config import CONFIG

WEBHOOK_PATH = f"/bot/{CONFIG.BOT.TOKEN}"
WEBHOOK_URL = f"{CONFIG.BOT.NGROK_TUNEL_URL}{WEBHOOK_PATH}"

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post(WEBHOOK_PATH)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("startup")
async def on_startup():
    webhook_info = await bot.get_webhook_info()
    if webhook_info.url != WEBHOOK_URL:
        await bot.set_webhook(url=WEBHOOK_URL)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    await bot.send_message(chat_id=381252111, text=f'{name}')
    return {"message": f"Hello {name}"}

