import pytest
from src.domain.entities import Challenge
from uuid import UUID

def test_challenge_creation_valid_data():
    """
Tests whether the Challenge object is created correctly with valid data.    
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
    Tests whether Pydantic blocks a difficulty that is not Easy, Medium or Hard.
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
    Tests whether the Challenge object raises an error when the description is empty.
    """
    with pytest.raises(ValueError):
        Challenge(
            title="Valid Title",
            description="",  # Descrição vazia
            difficulty="Easy",
            tags=[]
        )

def test_challenge_should_have_auto_generated_id():
    """Garante que cada desafio receba um UUID único por padrão"""
    challenge1 = Challenge(title="Test 1", description="Description 10 chars", difficulty="Easy")
    challenge2 = Challenge(title="Test 2", description="Description 10 chars", difficulty="Easy")
    
    assert challenge1.id != challenge2.id
    assert isinstance(challenge1.id, UUID)