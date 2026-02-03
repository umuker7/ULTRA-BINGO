# ULTRA-BINGO

Simple FastAPI backend + minimal frontend for sending an "Open Bingo" link to a Telegram chat.

Quick start (mobile-friendly):
1. In the repo on GitHub (open in your mobile browser), open the page and use "Request desktop site" to access Settings → Secrets and add BOT_TOKEN and CHAT_ID as repository secrets.
2. On a machine (or cloud runner) run the backend with:
   uvicorn backend.main:app --host 0.0.0.0 --port 8000 --reload
3. Expose the running server with ngrok (ngrok http 8000) and copy the HTTPS URL.
4. POST {"url":"https://your.app.link"} to /send_button to send a Telegram message with the link.

Notes:
- Do NOT store BOT_TOKEN in the repository files. Use .env locally or GitHub Secrets for CI/deploy.
- If you need, I can help set up Actions or a small deploy workflow.