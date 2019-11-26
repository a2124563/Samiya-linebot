from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *


#======這裡是呼叫的檔案內容=====
from message import *
from new import *
from Function import *
#======這裡是呼叫的檔案內容=====

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('Gzext05rwnI6KcctcQoPrTFjezmvdZU5WkZA+UAkNy0BWkpeLiMeSj9LA/uXOw+6Uf6/9Y5kqAEgelvVhpn6BR0Do8MfXHeTZw0YML3crcU+k4z2fRGL6svdxzTaCNcRWLDqw3hyq6+8E3753YGJTQdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('89316a887919c3f1f87b4339e0cea6ca')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = TextSendMessage(text=event.message.text)
    line_bot_api.reply_message(event.reply_token, message)

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
