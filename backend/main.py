from fastapi import FastAPI, Request
import os
import requests

app = FastAPI()

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.get("/")
async def root():
    return {"status": "ok"}

@app.post("/send_button")
async def send_button(req: Request):
    data = await req.json()
    url = data.get("url")
    if not url:
        return {"error": "missing url"}
    if not BOT_TOKEN or not CHAT_ID:
        return {"error": "missing BOT_TOKEN or CHAT_ID"}
    text = f"Open Bingo: {url}"
    resp = requests.get(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        params={"chat_id": CHAT_ID, "text": text}
    )
    try:
        return {"telegram": resp.json()}
    except ValueError:
        return {"telegram_status": resp.status_code, "response_text": resp.text}