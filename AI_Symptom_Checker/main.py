"""
Symptom Checker Bot (with OpenAI)
- Uses OpenAI to process symptom descriptions
- Gives probable common condition, doctor type, and mild OTC suggestions
- Always includes medical disclaimer
"""

from openai import OpenAI

# set-up client 
client = OpenAI(api_key="YOUR_API_KEY_HERE")

# disclaimer
DISCLAIMER = (
    "\n*** Disclaimer ***\n"
    "This tool is for informational purposes only.\n"
    "It does NOT provide medical diagnosis or treatment.\n"
    "Consult a healthcare professional for accurate advice.\n"
    "For emergencies, call local emergency services.\n"
)

# github: github.com/prashant-g0
# response generation
def ask_bot(symptom_text):
    prompt = f"""
    You are a cautious health assistant.
    User describes symptoms: "{symptom_text}".

    Your task:
    1. Suggest the most probable common minor condition(s).
    2. Recommend what type of doctor (e.g., General Physician, Orthopedist, Psychiatrist).
    3. Optionally suggest mild over-the-counter remedies (like rest, fluids, paracetamol).
    4. If symptoms are severe (red flags: chest pain, difficulty breathing, loss of consciousness, high fever > 40C), say: "⚠️ Emergency, seek immediate medical care".
    5. If the input is NOT health-related, politely refuse and say you only provide health-related guidance.
    6. Always end with the disclaimer: {DISCLAIMER}.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt
    )

    return response.output_text

#insta: @prash.coder
# user-bot intraction
def main():
    print(DISCLAIMER)
    while True:
        user = input("\nDescribe your symptoms (or type 'exit'): ").strip()
        if user.lower() == "exit":
            print("Goodbye — take care!")
            break
        reply = ask_bot(user)
        print("\n" + reply)

# main file
if __name__ == "__main__":
    main()
