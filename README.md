# wechat-chatgpt-bot

这是一个用于部署微信公众号接入 ChatGPT 机器人的 Flask 项目。

## 文件列表

- `app.py`: Flask 应用主脚本，从环境变量读取微信和 OpenAI 凭证。
- `requirements.txt`: Python 依赖列表。
- `Procfile`: Render.com/Heroku 部署启动命令。
- `README.md`: 项目说明。

## 部署到 Render.com

1. 在 GitHub 新建仓库并上传以上四个文件。
2. 登录 Render.com → New → Web Service → 选择该仓库。
3. 填写 Build Command: `pip install -r requirements.txt`。
4. 填写 Start Command: `gunicorn app:app --bind 0.0.0.0:$PORT`。
5. 添加环境变量并 Deploy。
6. 在微信公众号后台服务器配置填写:
   ```
   URL: https://<your-render-app>.onrender.com/wechat
   Token: myChatGPTtoken123
   EncodingAESKey: sQXh2a1Cit4lX1hNVzcwSANh761aZxMD0cQX6zb3ISA
   ```
