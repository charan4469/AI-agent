import openai

# Set your OpenAI API key
openai.api_key = "YOUR_API_KEY"

def chat(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        temperature=0.7
    )
    return response.choices[0].text.strip()

print("Welcome to AI Chat Assistant! Type 'exit' to quit.")
while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        break
    reply = chat(user_input)
    print(f"Assistant: {reply}")