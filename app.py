import os
from flask import Flask, request, make_response
from wechatpy import parse_message, create_reply
from wechatpy.utils import check_signature
import openai

# Load credentials from environment variables
TOKEN = os.getenv("WECHAT_TOKEN")
AES_KEY = os.getenv("WECHAT_ENCODING_AES_KEY")
APP_ID = os.getenv("WECHAT_APP_ID")
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route("/wechat", methods=["GET", "POST"])
def wechat():
    signature = request.args.get("signature", "")
    timestamp = request.args.get("timestamp", "")
    nonce = request.args.get("nonce", "")
    echostr = request.args.get("echostr", "")
    try:
        check_signature(TOKEN, signature, timestamp, nonce)
    except:
        return "Invalid signature", 403
    if request.method == "GET":
        return echostr
    msg = parse_message(request.data, safe_mode=True,
                        crypto={'token': TOKEN, 'aes_key': AES_KEY, 'app_id': APP_ID})
    if msg.type == "text":
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": msg.content}]
        )
        reply_content = response.choices[0].message.content
        reply = create_reply(reply_content, msg, safe_mode=True,
                             crypto={'token': TOKEN, 'aes_key': AES_KEY, 'app_id': APP_ID})
        return make_response(reply.render())
    return "success"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
