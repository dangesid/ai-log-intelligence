import requests 

class OllamaClient:
    def __init__(self, model="mistral"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    def generate(self, prompt):
        payload = {
            "model": self.model,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.4,
                "top_p": 0.9    
        }
    }

        response = requests.post(self.url, json=payload)
        response.raise_for_status()

        return response.json()["response"]
    