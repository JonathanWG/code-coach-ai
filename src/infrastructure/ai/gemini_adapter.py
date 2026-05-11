from src.application.ports.ai_provider import AIProviderPort
from src.domain.entities import Challenge
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from typing import Dict, Any



class GeminiAdapter(AIProviderPort):
    def __init__(self, api_key: str, model: str = "gemini-2.5-flash"):
        self.api_key = api_key
        self.llm = ChatGoogleGenerativeAI(model=model, google_api_key=api_key, temperature=0.7)
        self.parser = JsonOutputParser()

    def generate_challenge(self, theme, difficulty) -> Dict[str,Any]:
        prompt = ChatPromptTemplate.from_messages([
            ("system",(
                "You are a coding challenge generator. "
                "Output ONLY a JSON object. "
                "Format: {format_instructions}"
            )),
            ("human",(
                "Generate a coding challenge with the following theme: {theme} and difficulty: {difficulty}. "
                "Include a title, description, difficulty level (Easy, Medium, Hard) and relevant tags."
            ))
            
        ]).partial(format_instructions= self.parser.get_format_instructions())

        chain = prompt | self.llm | self.parser
        return chain.invoke({"theme": theme, "difficulty": difficulty})
        
        