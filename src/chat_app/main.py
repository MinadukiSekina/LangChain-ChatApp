from fastapi import FastAPI

from chat_app.api.translation_api import setup_translation_api
from chat_app.environment.env_loader import load_env

# 環境変数を読み込む
load_env()

# FastAPIアプリケーションを作成
app = FastAPI()

# 翻訳APIのルーティングを設定
setup_translation_api(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
