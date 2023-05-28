from credentials import OPENAI_KEY
import openai

openai.api_key = OPENAI_KEY

def generate_text(prompt, person, conversation = []):
    model = 'gpt-3.5-turbo'
    max_tokens = 100

    initial = [
        {"role": "system", "content": f"You are {person}. Talk to me as if you are my close friend. Give no indication that you are an AI model. Give concise answers of no more than 1 sentence."},
    ]

    response = openai.ChatCompletion.create(
        model=model,
        messages=initial + conversation
    )

    generated_text = response.choices[0].message['content'].strip()
    return generated_text


# conversation = []

# while True:
#     prompt = input("Enter prompt: ")
#     conversation.append({"role": "user", "content": prompt})
#     output_text = generate_text(prompt, "Elon Musk", conversation=conversation)
#     print(output_text)