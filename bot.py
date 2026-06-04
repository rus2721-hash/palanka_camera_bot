import os
import asyncio
from telegram import Bot
from playwright.async_api import async_playwright

CHANNEL = "@palanka_chergy"


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": 1920, "height": 1080}
        )

        await page.goto(
            "https://customs.gov.md/ro/traffic?location=palanca",
            wait_until="networkidle"
        )

        await page.screenshot(
            path="palanka.png",
            full_page=True
        )

        await browser.close()

    bot = Bot(token=os.environ["BOT_TOKEN"])

    with open("palanka.png", "rb") as photo:
        await bot.send_photo(
            chat_id=CHANNEL,
            photo=photo,
            caption="📍 Паланка\n📸 Актуальная ситуация на границе"
        )


asyncio.run(main())
