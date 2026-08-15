import os
from google import genai

# Gemini API key environment variable se li jayegi
API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    print("❌ GEMINI_API_KEY set nahi hai.")
    exit()

client = genai.Client(api_key=API_KEY)

SYSTEM_PROMPT = """
Tum Zoro AI ho — Somesh ka personal AI assistant.
Tum Hindi, Hinglish aur English mein naturally baat kar sakte ho.
Friendly, helpful aur clear answers do.
"""

print("⚔️ Zoro AI started!")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() in ["exit", "quit"]:
        print("Zoro: Bye buddy! 👋")
        break

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                SYSTEM_PROMPT,
                user_input
            ]
        )

        print("Zoro:", response.text)

    except Exception as e:
        print("❌ Error:", e)
