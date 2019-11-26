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
line_bot_api = LineBotApi('WM+ZVOFIkFQzuGyG0k1xHhI+ooDnlVztTlZCYzeO1WwkmUMmZ63CUdgbeVBSELFI4ajG5d5EmZbibragX2r+Gyb7FcUFkiLwA1bRKQwnAzct8IoO2IR+GaJct5KBkjUEM+GTfqvdi04W2uq0/iwq0gdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('2239701cf5f673cbbf96f61e504b8366')

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
    app.run(host='0.0.0.0', port=80)
