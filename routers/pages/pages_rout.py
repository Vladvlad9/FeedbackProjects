from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates


router = APIRouter(
    prefix='/pages',
    tags=['Фронтенд']
)

templates = Jinja2Templates(directory='./templates')


@router.get('/chat')
def get_chat(request: Request):
    return templates.TemplateResponse(name='chat.html',
                                      context={
                                          "request": request
                                      })
