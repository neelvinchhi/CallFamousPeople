import openai
from credentials import OPENAI_KEY

def generate_text(prompt):
    openai.api_key = OPENAI_KEY
    model = 'gpt-3.5-turbo'
    max_tokens = 100

    response = openai.Completion.create(
        engine=model,
        prompt=prompt,
        max_tokens=max_tokens,
        n=1,
        stop=None,
    )

    generated_text = response.choices[0].text.strip()
    return generated_text

