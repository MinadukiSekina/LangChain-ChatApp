from langchain.chat_models import init_chat_model
from langchain.chat_models.base import BaseChatModel


def create_model(
    model_name: str = "gemini-2.0-flash", model_provider: str = "google_genai"
) -> BaseChatModel:
    """モデルインスタンスを作成するファクトリ関数"""
    return init_chat_model(model_name, model_provider=model_provider)
