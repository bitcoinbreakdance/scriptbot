import openai

# Replace YOUR_API_KEY with your actual API key
openai.api_key = "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"

# Initialize conversation
conversation = True

# Start a conversation loop
while conversation:
    # Ask the user for input
    prompt = input("You: ")
    if prompt.strip().lower() == "exit":
        conversation = False
        print("Goodbye!")
        break
    # Use the OpenAI API to generate text
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024
    )
    # Print the generated text
    print("ChatGPT: ",response["choices"][0]["text"])
