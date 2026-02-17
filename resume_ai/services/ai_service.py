import requests

def analyze_resume_with_ollama(text):
    prompt = f"""
You are an experienced HR professional.

Analyze this resume and provide:

1. Skills detected
2. Strengths
3. Weaknesses
4. Suggestions for improvement

Resume:
{text}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )
    print(response.status_code)
    print(response.text)

    return response.json()["response"]



