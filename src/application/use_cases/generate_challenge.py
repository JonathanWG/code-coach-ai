from src.application.ports.ai_provider import AIProviderPort
from src.domain.entities import Challenge

class GenerateChallengeUseCase:
    def __init__(self, ai_provider : AIProviderPort):
        self.ai_provider = ai_provider

    def execute(self, theme: str, difficulty: str) -> Challenge:
        """
        Executes the use case to generate a coding challenge based on the provided theme and difficulty.
        """
        challenge_data = self.ai_provider.generate_challenge(theme=theme, difficulty=difficulty)
        return Challenge(**challenge_data)