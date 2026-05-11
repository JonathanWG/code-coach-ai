import pytest
from src.infrastructure.ai.gemini_adapter import GeminiAdapter
import os

def test_gemini_adapter_generate_challenge():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        pytest.skip("GOOGLE_API_KEY not set in environment variables")
    
    adapter = GeminiAdapter(api_key=api_key)

    result = adapter.generate_challenge(theme="string manipulation", difficulty="Easy")

    assert "title" in result
    assert "description" in result
    assert isinstance(result["tags"], list)

    print("Generated Challenge:", result)

