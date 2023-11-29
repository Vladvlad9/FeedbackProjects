from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import ParseMode, Message

from config import CONFIG
from crud import CRUDUsers
from schemas import UserSchema

bot = Bot(token=CONFIG.BOT.TOKEN, parse_mode=ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands='start')
async def start_handler(message: Message):
    getUser = await CRUDUsers.get_user()
    if getUser:
        await message.answer('Добро пожаловать в бот обратной связи')
    else:
        pass
        # await CRUDUsers.add(user=UserSchema(user_id=int(message.from_user.id)))
        await message.answer('Для продолжения необходимо пройти регистрацию')
    pass


@dp.message_handler()
async def get_msg(message: Message):
    # getUser = await CRUDUsers.get(user_id=int(message.from_user.id))
    # a = message.text
    # if getUser:
    #     await CRUDMessage.add(get_message=MessagingSchemas(user_id=getUser.id,
    #                                                        message=message.text,
    #                                                        is_processed=False
    #                                                        ))
    #     await message.reply(text="Ожидайте ответа")
    pass
