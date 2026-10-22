import os
from google import genai

# 1. Initialize client using GEMINI_API_KEY from environment
client = genai.Client()

# 2. Flagged IP data from our log parsing script
flagged_ips = {
    "192.168.1.50": 3,
    "10.0.0.1": 3
}

# 3. Construct our AIOps SOC prompt
prompt = f"""
You are an automated SOC Incident Response assistant.
Analyze these high-frequency IP connections flagged by our firewall script:

Data: {flagged_ips}

Provide:
1. Classification (Internal vs. External ranges).
2. Risk assessment for each IP.
3. 2 immediate action steps for the network administrator.
Keep it concise and clear.
"""

print("--- CONNECTING TO GEMINI API FOR LIVE TRIAGE ---")

# 4. Call Gemini 3.8 Flash
response = client.models.generate_content(
    model="gemini-3.8-flash",
    contents=prompt
)

# 5. Output the live threat report
print("\n--- LIVE AI RESPONSE ---")
print(response.text)