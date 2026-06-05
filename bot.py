import os
import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

CHANNEL = "@palanka_chergy"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1280, "height": 900}
        )

        await page.goto(
    "https://customs.gov.md/ro/traffic?location=palanca",
    wait_until="domcontentloaded",
    timeout=120000
)

        # Ждём загрузку камеры
        await page.wait_for_timeout(10000)

        # Скриншот видимой части страницы
        await page.screenshot(
    path="palanka.png",
    clip={
        "x": 250,
        "y": 150,
        "width": 1100,
        "height": 650
    }
        )

        await browser.close()

    bot = Bot(token=os.environ["BOT_TOKEN"])

    with open("palanka.png", "rb") as photo:
        await bot.send_photo(
            chat_id=CHANNEL,
            photo=photo,
            caption="📍 Паланка в Україну"
        )


asyncio.run(main())
