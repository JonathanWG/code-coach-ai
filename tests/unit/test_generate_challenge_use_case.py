import pytest
from src.application.ports.ai_provider import AIProviderPort
from src.application.use_cases.generate_challenge import GenerateChallengeUseCase
from unittest.mock import MagicMock
from src.domain.entities import Challenge

def test_generate_challenge_use_case():
    mock_ai_provider = MagicMock(spec=AIProviderPort)

    mock_ai_provider.generate_challenge.return_value = {
        "title": "Reverse a String",
        "description": "Write a function that reverses a string without using built-in reverse methods.",
        "difficulty": "Easy",
        "tags": ["logic", "python"]
    }

    use_case = GenerateChallengeUseCase(ai_provider=mock_ai_provider)
    result = use_case.execute(theme="string manipulation", difficulty="Easy")

    assert isinstance(result, Challenge)
    assert result.title == "Reverse a String"
    assert result.difficulty == "Easy"
    assert "logic" in result.tags

    mock_ai_provider.generate_challenge.assert_called_once_with(theme="string manipulation", difficulty="Easy") 