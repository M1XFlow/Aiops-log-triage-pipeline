from google import genai

# Initialize client using your GEMINI_API_KEY environment variable
client = genai.Client()

print("--- SUPPORTED MODELS FOR YOUR API KEY ---")
# List all models available to your account
for model in client.models.list():
    print(model.name)