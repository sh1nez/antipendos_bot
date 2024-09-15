import logging
import aiogram
import asyncio
import tomllib
import re
import random
import translators as trans
data = tomllib.load(open("config.toml", "rb"))
hohol = data["hohol"]
token = data["token"]
pendos = data["pendos"]


dp = aiogram.Dispatcher()


async def main() -> None:
    bot = aiogram.Bot(token=token)
    await dp.start_polling(bot)

pivo = ["AgACAgIAAxkBAAMwZudNzW67VdGxX4lOX3VCqiiBg-cAAmrmMRusfEFL2HbDgbrslggBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAAM1ZudOS1hfXVy8OkTrQApumF-wBucAAm3mMRusfEFL1WRRGjogTuQBAAMCAAN4AAM2BA",
        "AgACAgIAAxkBAAM2ZudOog5unr2TOfKf2d0ST6zwIuUAAnDmMRusfEFLNlOZLK3KBvIBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAAM3ZudOxcMjFNf_QIcWuqDnKg654qoAAnPmMRusfEFLsb5AIyL24P8BAAMCAANzAAM2BA",
        "AgACAgIAAxkBAAM4ZudO6SFleyPGjwFo1JehBvEBzisAAnXmMRusfEFLqvUWTQ7vIAkBAAMCAANtAAM2BA",
        "AgACAgIAAxkBAAM5ZudPEYWkEvVdzfBWB4J9cSrd0N8AAnbmMRusfEFLU2M-B0i6EykBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAAM6ZudPUs1308rxOsezK7qxTcmJCdYAAnfmMRusfEFL5uapx2N2dfIBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAAM7ZudPfHMbZHVl37Aq12iu-aFsoqcAAnjmMRusfEFL2KA92wppyuEBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAAM8ZudPmLTho5s-x-9_zPKUXsVYP68AAnnmMRusfEFLb6VGtU_afa8BAAMCAAN4AAM2BA"
        ]
komp = ["AgACAgIAAxkBAAM9ZudQXFpqRLQPoxkxgCv41AM7KjQAAnvmMRusfEFLxLVJngRCJZoBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAANAZudQpoQlcf7Sb0pZbYIWGv02-LkAAnzmMRusfEFLFZut-X1dfIIBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAANBZudQwASudQABPjiqntYWu6T8vFwfAAJ95jEbrHxBSwtYKs9ndBfTAQADAgADcwADNgQ",
        "AgACAgIAAxkBAANCZudQ9Chs3ihnV0qAbyfWKfla9R0AAoDmMRusfEFLuuGJ5lPl9cUBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAANDZudRQOmIOI2LSbNUUC_8C8I55mcAAoLmMRusfEFLw71PAn-vdncBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAANEZudRhGKyR_SY22GhkPse9I1n3XQAAofmMRusfEFL3rSNdo3NIDIBAAMCAANzAAM2BA",
        "AgACAgIAAxkBAANFZudRqtr_O5HqqSDdUfCA1Oykp3QAAojmMRusfEFLPxo2Ldl3yOABAAMCAANzAAM2BA",
        "AgACAgIAAxkBAANGZudR3Hg_n4dORvt-rJAgTDTOWUUAAonmMRusfEFLvRW2BVPcXrMBAAMCAANzAAM2BA" <
        "AgACAgIAAxkBAANHZudR_Nb_QPGvPLDP0ThYsZnbfEIAAovmMRusfEFL4NL6hUWVLAEBAAMCAANzAAM2BA",
        ]


@dp.message()
async def filter(message: aiogram.types.Message):
    if message.from_user.id == hohol and message.text:
        if "компик" in message.text and ("сид" in message.text
                                         or " за " in message.text
                                         or "сиж" in message.text):
            await message.reply_photo(komp[random.randint(0, len(komp)-1)])
        elif "пиво" in message.text or "пива" in message.text:
            await message.reply_photo(pivo[random.randint(0, len(pivo)-1)])
    if message.from_user.id in pendos:
        # tmp1 = len(re.compile(r'[a-zA-Z.,!?;:\'\" ]').findall(message.text))
        tmp2 = len(re.compile(r'[а-яА-Я ]').findall(message.text))
        # if tmp1 > len(message.text) * 0.9:
        ru = trans.translate_text(message.text, "yandex", to_language="ru")
        logging.info(f"said: {message.text}, trans: {ru}")
        # nick = message.from_user.full_name
        if ru == message.text and len(message.text) * 0.5 > tmp2:
            await message.answer("Богдаун пытался что-то сказать, но у него не получилось")
        else:
            await message.answer(f"Богдаун сказал: {ru}")
        await message.delete()
    # message.content_type == aiogram.types.ContentType.VIDEO:


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.WARNING,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            # logging.StreamHandler()  # Вывод в консоль
            logging.FileHandler('log.txt'),
        ]
    )
    asyncio.run(main())
