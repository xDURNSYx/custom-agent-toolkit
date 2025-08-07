
import os
import requests
from dotenv import load_dotenv
load_dotenv()

def update_notion_page(page_id, content):
    url = f"https://api.notion.com/v1/pages/{page_id}"
    headers = {
        "Authorization": f"Bearer {os.getenv('NOTION_TOKEN')}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    data = {
        "properties": {
            "Content": {
                "rich_text": [{"text": {"content": content}}]
            }
        }
    }
    res = requests.patch(url, headers=headers, json=data)
    return res.json()
