from abc import ABC, abstractmethod


class AIProviderPort(ABC):
    @abstractmethod
    def generate_challenge(self,theme: str, difficulty: str) -> str:
        """
        Generates a coding challenge based on the provided theme and difficulty.
        """
        pass