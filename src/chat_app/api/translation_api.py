from fastapi import FastAPI
from langserve import add_routes

from chat_app.chains.translation_chain import create_translation_chain


def setup_translation_api(app: FastAPI) -> None:
    """翻訳APIのルートを設定"""
    translation_chain = create_translation_chain()

    add_routes(
        app,
        translation_chain,
        path="/translate",
    )
