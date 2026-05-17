from flask import Flask, request, jsonify
import os
from src.application.use_cases.generate_challenge import GenerateChallengeUseCase
from src.infrastructure.ai.gemini_adapter import GeminiAdapter

app = Flask(__name__)

def bootstrap_challenge_use_case() -> GenerateChallengeUseCase:
    api_key = os.getenv("GOOGLE_API_KEY")
    gemini_adapter = GeminiAdapter(api_key=api_key)
    return GenerateChallengeUseCase(ai_provider=gemini_adapter)


@app.post("/generate_challenge/")
def generate_challenge():

    data = request.get_json()
    theme = data.get("theme")
    difficulty = data.get("difficulty")

    if not theme or not difficulty:
        return jsonify({"status": "error", "message": "Both 'theme' and 'difficulty' are required."}), 400

    try:
        use_case = bootstrap_challenge_use_case()
        challenge = use_case.execute(theme=theme, difficulty=difficulty)
        return jsonify({"status": "success", "challenge": challenge})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
