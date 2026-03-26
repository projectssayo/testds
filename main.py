from fastapi import FastAPI
from .playwright_test import run_test

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "FastAPI + Playwright running!"}

@app.get("/test")
async def test_playwright():
    title = await run_test()
    return {"news_site_title": title}
