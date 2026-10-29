from openai import OpenAI
from dotenv import load_dotenv
import sys
from sample_message import SAMPLE_MESSAGE

load_dotenv()
try:
    client = OpenAI()
except Exception as e:
    print("Error loading environment variables or initializing OpenAI client:", e)
    sys.exit(1)


def main():
    messages = [{"role": "system", "content": SAMPLE_MESSAGE}]

    print("-" * 50)
    print("Welcome to TaskBuddy! Type 'exit' to quit.")
    print(
        "         - Dump your tasks and to-dos here, and I'll help you organize them."
    )
    print("-" * 50)

    while True:
        try:
            user_input = input("\nYou : ")
            if user_input.lower().strip() in ["exit", "quit"]:
                print("Exiting TaskBuddy. Goodbye!")
                break

            if not user_input.strip():
                print("Please enter a valid task or command.")
                continue

            messages.append({"role": "user", "content": user_input})

            response = client.chat.completions.create(
                model="gpt-4o-mini", messages=messages
            )

            reply = response.choices[0].message.content
            print(f"\nTaskBuddy : {reply}")
            messages.append({"role": "assistant", "content": reply})

        except KeyboardInterrupt:
            print("\nExiting TaskBuddy. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            continue

if __name__ == "__main__":
    main()