import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import argparse

def main():
    print("Hello from ai-agent!")

    # parse the input from the user
    parser = argparse.ArgumentParser(description = "Chatbot")
    parser.add_argument("user_prompt", type=str, help="User prompt for Chatbot")
    parser.add_argument("--verbose", action="store_true", help="Enable Verbose Output")
    args = parser.parse_args()

    # now we can access `args.user_prompt`
    user_prompt = args.user_prompt
    if user_prompt is None:
        raise RuntimeError("Failed to extract user input")

    verbose_mode = args.verbose
    messages = [types.Content(role="user", parts=[types.Part(text = user_prompt)])]

    # set up the environment to make the request 
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key is None:
        raise RuntimeError("No API key found!")
    
    client = genai.Client(api_key=api_key)

    if verbose_mode:
        print(f"User prompt: {user_prompt}")

    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages)
    
    if response.usage_metadata is None:
        raise RuntimeError("Failed to extract usage metadata")

    # only print the details if verbose was enabled
    if verbose_mode:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print("Response:")
    print(response.text)

if __name__ == "__main__":
    main()
