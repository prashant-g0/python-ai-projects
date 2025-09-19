from openai import OpenAI

# set-up client and api_key
# client = OpenAI(api_key="your api key here")
client = OpenAI()

# github : github.com/prashant-g0
# ai response generation function
def rewrite_msg(msg, role):
    prompt = f'You are an assistant that rewrites WhatsApp messages (avoid email formats). Rewrite the following message so it is clear, polite, and suitable for the role: "{role}". Original message: "{msg}"'

    response = client.responses.create(model="gpt-4o-mini", input=prompt)
    return response.output_text.strip()

# insta: @prash.coder
# Bot and user interaction function 
def main():
    print("=== AI WhatsApp Message Rewriter ===")

    while True:
        print("\nPrashBOT: Enter your raw message (or 'exit' to quit) ")
        raw_msg = input("\nUser: ")
        
        if raw_msg.lower() == "exit":
            print("PrashBot: GoodBye!")
            break
        print("\nPrashBOT: Enter the role of receiver (Professor/Boss/Friend/Teammate) ")
        role = input("\nUser: ").strip()

        print("\nPrashBOT: Rewritten Message")
        try:
            result = rewrite_msg(raw_msg, role)
            print(result + "\n")
        except Exception as e:
            print("PrashBOT: Error! ", str(e))

# Code runner - main block
if __name__ == "__main__":
    main()