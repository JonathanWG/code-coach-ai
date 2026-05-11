import pytest
from src.domain.entities import Challenge

def test_challenge_creation_valid_data():
    """
    Testa se o objeto Challenge é criado corretamente com dados válidos.
    """
    data = {
        "title": "Reverse a String",
        "description": "Write a function that reverses a string without using built-in reverse methods.",
        "difficulty": "Easy",
        "tags": ["logic", "python"]
    }
    challenge = Challenge(**data)
    
    assert challenge.title == data["title"]
    assert challenge.difficulty == "Easy"
    assert "logic" in challenge.tags

def test_challenge_invalid_difficulty():
    """
    Testa se o Pydantic bloqueia uma dificuldade que não seja Easy, Medium ou Hard.
    """
    with pytest.raises(ValueError):
        Challenge(
            title="Invalid",
            description="Testing error",
            difficulty="Extreme",  # Isso deve causar erro
            tags=[]
        )

def test_challenge_should_raise_error_on_empty_description():
    """
    Garante que a descrição não seja uma string vazia ou apenas espaços.
    """
    with pytest.raises(ValueError):
        Challenge(
            title="Valid Title",
            description="",  # Descrição vazia
            difficulty="Easy",
            tags=[]
        )