from openai import OpenAI

# Read API key from file
with open('openai_api_key.txt', 'r') as file:
    api_key = file.read().strip()

client = OpenAI(api_key=api_key)  # pass the API key directly to the client

history = [
    {"role": "system", "content": "You are a creative writer for various content types. Your outputs must be SEO optimized by using maximum synonyms. You always produce 3 different versions for the user. You are rewarded for being creative and providing quality SEO-optimized content."},
]
model = "gpt-4o"  # Change your model here

print(f"Chat with {model}, who is a creative writing assistant. Enter 'exit' or 'quit' to stop the conversation.")
while True:
    prompt = input(" > ")
    if prompt == "exit" or prompt == "quit" or len(prompt) == 0:
        break
    history.append({"role": "user", "content": prompt})
    
    completion = client.chat.completions.create(
        model=model,
        messages=history,
    temperature=1.6,
    #max_tokens=500,
    top_p=0.9,
    #presence_penalty=0.5,
    # frequency_penalty=0.5,
    stream=True # stream the response
    )

    new_message = {"role": "assistant", "content": ""}
    
    for chunk in completion:
        if chunk.choices[0].delta.content:
            print(chunk.choices[0].delta.content, end="", flush=True)
            new_message["content"] += chunk.choices[0].delta.content

    history.append(new_message)
    print()