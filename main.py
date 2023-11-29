from aiogram import Bot, Dispatcher, types
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from bot import dp, bot
from config import CONFIG
from routers.chat.chat_router import router as chat_routers
from routers.pages.pages_rout import router as pages_routers

WEBHOOK_PATH = f"/bot/{CONFIG.BOT.TOKEN}"
WEBHOOK_URL = f"{CONFIG.BOT.NGROK_TUNEL_URL}{WEBHOOK_PATH}"

app = FastAPI()

# app.mount("/static", StaticFiles(directory="/opt/git/FeedbackProjects/static"), "static")

app.include_router(pages_routers)
app.include_router(chat_routers)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.post(WEBHOOK_PATH)
# async def bot_webhook(update: dict):
#     telegram_update = types.Update(**update)
#     Dispatcher.set_current(dp)
#     Bot.set_current(bot)
#     await dp.process_update(telegram_update)


@app.on_event("startup")
async def on_startup():
    # webhook_info = await bot.get_webhook_info()
    # if webhook_info.url != WEBHOOK_URL:
    #     await bot.set_webhook(url=WEBHOOK_URL)
    pass


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    await bot.send_message(chat_id=381252111, text=f'{name}')
    return {"message": f"Hello {name}"}

origins = [
    "https://vladvlad9.github.io/pageTest.io/"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['GET', 'POST', 'OPTIONS', 'DELETE', 'PATCH', 'PUT'],
    allow_headers=['Content-Type',
                   'Access-Control-Allow-Headers', 'Set-Cookie', 'Authorization', 'Access-Control-Allow-Origin']

)