from langchain_core.prompts import ChatPromptTemplate


def create_translation_prompt() -> ChatPromptTemplate:
    """翻訳用のプロンプトテンプレートを作成"""
    system_template = "Translate the following from English into {language}"
    return ChatPromptTemplate.from_messages([("system", system_template), ("user", "{text}")])
