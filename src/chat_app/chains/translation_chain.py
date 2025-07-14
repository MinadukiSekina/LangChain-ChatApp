from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import Runnable

from chat_app.models.model_factory import create_model
from chat_app.prompts.translation_prompt import create_translation_prompt


def create_translation_chain() -> Runnable:
    """翻訳チェーンを作成"""
    model = create_model()
    prompt = create_translation_prompt()
    parser = StrOutputParser()

    return prompt | model | parser
