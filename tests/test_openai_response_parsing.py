import pytest

from langchain_openai.chat_models.base import BaseChatOpenAI


def _make_model() -> BaseChatOpenAI:
    # Provide dummy values to avoid relying on environment configuration.
    return BaseChatOpenAI(model="gpt-3.5-turbo", api_key="test")


def test_create_chat_result_with_valid_choices():
    model = _make_model()
    response = {
        "choices": [
            {
                "message": {
                    "role": "assistant",
                    "content": "Hello!",
                }
            }
        ]
    }

    result = model._create_chat_result(response)

    assert len(result.generations) == 1
    assert result.generations[0].message.content == "Hello!"


def test_create_chat_result_with_empty_choices():
    model = _make_model()
    response = {"choices": []}

    result = model._create_chat_result(response)

    assert result.generations == []


def test_create_chat_result_with_null_choices_raises_value_error():
    model = _make_model()
    response = {"choices": None}

    with pytest.raises(ValueError) as excinfo:
        model._create_chat_result(response)

    assert "choices" in str(excinfo.value)
    assert "null value" in str(excinfo.value)


