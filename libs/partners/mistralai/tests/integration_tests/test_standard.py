"""Standard LangChain interface tests."""

from langchain_core.language_models import BaseChatModel
from langchain_tests.integration_tests import (  # type: ignore[import-not-found]
    ChatModelIntegrationTests,  # type: ignore[import-not-found]
)

from langchain_mistralai import ChatMistralAI


class TestMistralStandard(ChatModelIntegrationTests):
    @property
    def chat_model_class(self) -> type[BaseChatModel]:
        return ChatMistralAI

    @property
    def chat_model_params(self) -> dict:
        return {"model": "mistral-large-latest", "temperature": 0}

    @property
    def supports_json_mode(self) -> bool:
        return True
