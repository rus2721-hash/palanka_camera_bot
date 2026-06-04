import os
import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

CHANNEL = "@palanka_chergy"

async def main():
async with async_playwright() as p:
browser = await p.chromium.launch(
args=["--autoplay-policy=no-user-gesture-required"]
)

    page = await browser.new_page(
        viewport={"width": 1280, "height": 900}
    )

    await page.goto(
        "https://border.gov.md/camere-web/palanca-intrare",
        wait_until="domcontentloaded",
        timeout=60000
    )

    # Ждём загрузку страницы
    await page.wait_for_timeout(8000)

    # Клик примерно по центру видеоплеера
    await page.mouse.click(640, 360)

    # Ждём запуск видео
    await page.wait_for_timeout(10000)

    # Скриншот области камеры
    await page.screenshot(
        path="palanka.png",
        clip={
            "x": 200,
            "y": 250,
            "width": 900,
            "height": 520
        }
    )

    await browser.close()

bot = Bot(token=os.environ["BOT_TOKEN"])

with open("palanka.png", "rb") as photo:
    await bot.send_photo(
        chat_id=CHANNEL,
        photo=photo,
        caption="📍 Паланка (в'їзд в Молдову)\n📸 Актуальна ситуація на кордоні"
    )

asyncio.run(main())
