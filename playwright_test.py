from playwright.async_api import async_playwright

async def run_test():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            locale='en-US', 
            timezone_id='America/Los_Angeles'
        )
        await page.goto("https://news.ycombinator.com/")
        title = await page.title()
        await browser.close()
        return title
