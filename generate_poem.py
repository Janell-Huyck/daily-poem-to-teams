import os
import sys
from openai import OpenAI

api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("❌ OPENAI_API_KEY not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

def generate_poem():
    prompt = (
        "Write a short, reflective free-verse poem (about 8–12 lines) for employees of a university. "
        "Use line breaks and stanza spacing (blank lines) where appropriate. "
        "The tone should be steady, gentle, and human. Use timeless metaphors "
        "(nature, light, breath, etc.) to explore themes like connection, hope, or quiet strength. "
        "Avoid current events or modern imagery. The poem should feel like a pause — a moment to breathe."
    )

    try:
        response = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {'role': 'system', 'content': 'You are a thoughtful poet.'},
                {'role': 'user', 'content': prompt}
            ],
            temperature=0.8,
            max_tokens=200,
        )
    except Exception as e:
        print(f"❌ Error while generating poem: {e}")
        return None

    poem = response.choices[0].message.content.strip()
    return poem if poem else None

if __name__ == '__main__':
    poem = generate_poem()
    if poem:
        print("\n=== Poem Generated ===\n")
        print(poem)
        print("\n======================\n")
        with open('poem.txt', 'w') as f:
            f.write(poem)
    else:
        print("❌ No poem generated. Exiting with error.")
        sys.exit(1)
