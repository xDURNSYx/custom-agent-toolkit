
from flask import Flask, request, jsonify
import os
from utils.notion import update_notion_page
from utils.telegram import send_telegram_message

app = Flask(__name__)

@app.route('/notion/update', methods=['POST'])
def notion_update():
    data = request.json
    result = update_notion_page(data['page_id'], data['content'])
    return jsonify(result)

@app.route('/telegram/send', methods=['POST'])
def telegram_send():
    data = request.json
    result = send_telegram_message(data['chat_id'], data['message'])
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
