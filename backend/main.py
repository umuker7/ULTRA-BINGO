import os
import requests
from fastapi import FastAPI
from pydantic import BaseModel

BOT_TOKEN = os.getenv("BOT_TOKEN", "REPLACE_WITH_YOUR_TOKEN")
CHAT_ID = os.getenv("CHAT_ID", "REPLACE_WITH_CHAT_ID")

app = FastAPI()

class ButtonPayload(BaseModel):
    url: str

@app.post("/send_button")
async def send_button(payload: ButtonPayload):
    """Send a simple message with an Open button link to the configured CHAT_ID."""
    text = f"Open Bingo: {payload.url}"
    resp = requests.post(f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage", data={
        "chat_id": CHAT_ID,
        "text": text,
        "disable_web_page_preview": False
    })
    try:
        return {"ok": resp.ok, "status_code": resp.status_code, "response": resp.json()}
    except ValueError:
        return {"ok": resp.ok, "status_code": resp.status_code, "response_text": resp.text}

@app.get("/")
async def root():
    return {"msg": "ULTRA-BINGO backend"}