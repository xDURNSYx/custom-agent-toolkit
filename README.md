
# Custom GPT Agent Toolkit

This toolkit connects OpenAI Agent Mode to custom tools like Notion and Telegram via API.

## Setup Instructions

1. Install requirements:
   ```bash
   pip install flask requests python-dotenv
   ```

2. Create a `.env` file with:
   ```
   NOTION_TOKEN=your_notion_secret
   TELEGRAM_BOT_TOKEN=your_bot_token
   ```

3. Run the server:
   ```bash
   python server.py
   ```

4. Point your `manifest.json` and `openapi.yaml` to your live endpoint.

5. Deploy on Replit, Render, or AWS for public access.

## Tools

- `/notion/update`: Update a Notion page
- `/telegram/send`: Send a Telegram message
