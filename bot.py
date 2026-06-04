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
    "https://border.gov.md/camere-web/palanca-intrare"
)

# Ждём загрузку страницы
await page.wait_for_timeout(5000)

# Нажимаем кнопку Play
await page.click("button")

# Ждём запуск видео
await page.wait_for_timeout(8000)

# Скриншот
await page.screenshot(
    path="palanka2.png",
    full_page=True
)

        await browser.close()

    bot = Bot(token=os.environ["BOT_TOKEN"])

    with open("palanka.png", "rb") as photo:
        await bot.send_photo(
            chat_id=CHANNEL,
            photo=photo,
            caption="📍 Паланка в Україну\n📸 Актуальна черга на кордоні"
        )


asyncio.run(main())
