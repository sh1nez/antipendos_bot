import asyncio
import sys
from datetime import datetime

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import Router
from aiogram.types import FSInputFile

CAPITAL_BEGIN = 65
CAPITAL_END = 90

lower_begin = 97
lower_end = 122

TOKEN = sys.argv[1]

VIDEO_PATH = 'gif/higurashi.mp4'

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

dp = Dispatcher()
router = Router(name=__name__)
dp.include_router(router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer("Привет, этот бот создан чтобы унижать пендосов")

@dp.message()
async def message_handler(message: Message) -> None:
    if message.text:
        contains_lowercase = any(lower_begin <= ord(char) <= lower_end for char in message.text)
        if contains_lowercase:
            await message.delete()
            video = FSInputFile(VIDEO_PATH)
            sent_message = await bot.send_video(chat_id=message.chat.id, video=video, duration=10)
            user_id = message.from_user.id
            username = message.from_user.username or "No username"
            current_time = datetime.now().strftime("%m/%d/%Y %H:%M:%S")  # MM/DD/YYYY Format
            log_message = f"{current_time}: Deleted message from user {username} (ID: {user_id}) in chat {message.chat.id}\n"

            with open('log.txt', 'a', encoding='utf-8') as log_file:
                log_file.write(log_message)

            await asyncio.sleep(10)
            await bot.delete_message(chat_id=sent_message.chat.id, message_id=sent_message.message_id)

async def main() -> None:
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
