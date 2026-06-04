import os
import asyncio
from telegram import Bot

CHANNEL = "@palanka_chergy"

async def main():
    bot = Bot(token=os.environ["BOT_TOKEN"])

    await bot.send_message(
        chat_id=CHANNEL,
        text="📸 Тестовое сообщение от CamPalanka Bot"
    )

asyncio.run(main())
