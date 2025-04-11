import os
from openai import OpenAI

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_poem():
    prompt = (
        "Write a short, reflective free-verse poem (about 8–12 lines) for employees of a university. "
        "The tone should be steady, gentle, and human. Use timeless metaphors "
        "(nature, light, breath, etc.) to explore themes like connection, hope, or quiet strength. "
        "Avoid current events or modern imagery. The poem should feel like a pause — a moment to breathe."
    )

    response = client.chat.completions.create(
        model='gpt-4o',
        messages=[
            {'role': 'system', 'content': 'You are a thoughtful poet.'},
            {'role': 'user', 'content': prompt}
        ],
        temperature=0.8,
        max_tokens=200,
    )

    poem = response.choices[0].message.content.strip()
    print("\n=== Poem Generated ===\n")
    print(poem)
    print("\n======================\n")

    # Write poem to file
    with open('poem.txt', 'w') as f:
        f.write(poem)

if __name__ == '__main__':
    generate_poem()
