from fastapi import APIRouter, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
import httpx

# from bot import bot
from config import CONFIG

router = APIRouter(
    prefix='/pages',
    tags=['Фронтенд']
)

templates = Jinja2Templates(directory='./templates')


@router.get("/stats", name="stats")
async def get_stats(request: Request):
    stats_data = {"data": [12, 19, 3, 5, 2, 3]}  # Пример данных
    return templates.TemplateResponse("stat.html", {"request": request, "stats": stats_data})


@router.get("/form", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse('test.html', context={'request': request})


@router.post("/send_message/")
async def send_message(message: str = Form(...)):
    # await bot.send_message(chat_id=381252111, text=f'{message}')
    pass
    telegram_bot_token = CONFIG.BOT.TOKEN
    chat_id = CONFIG.BOT.ADMINS[0]
    url = f"https://api.telegram.org/bot{telegram_bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': message
    }
    async with httpx.AsyncClient() as client:
        await client.post(url, data=payload)
    return {"message": "Сообщение отправлено"}
