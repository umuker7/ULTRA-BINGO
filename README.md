# ULTRA-BINGO

Minimal repository for the ULTRA BINGO mini-app.

Setup (local):

1. Create a virtual environment and install dependencies:

   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -r requirements.txt

2. Set environment variables (do NOT commit real tokens):

   export BOT_TOKEN="<your bot token>"
   export CHAT_ID="<your chat id>"

3. Run the backend:

   uvicorn backend.main:app --reload --host 0.0.0.0 --port 8000

4. (Optional) Use ngrok for telegram testing:

   ngrok http 8000

5. Send a POST /send_button to send a Telegram message with a link to the app:

   curl -X POST http://localhost:8000/send_button -H "Content-Type: application/json" -d '{"url":"https://example.com"}'

Security:
- Keep BOT_TOKEN and CHAT_ID in environment variables or GitHub Secrets. Do NOT publish them in this repository.
