import os
import sys
import random
from openai import OpenAI

# --- Helpers ---
def load_lines(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        print(f"❌ File not found: {filename}")
        sys.exit(1)

# --- Setup ---
api_key = os.environ.get('OPENAI_API_KEY')
if not api_key:
    print("❌ OPENAI_API_KEY not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)

# --- Load randomized content ---
opening_styles = load_lines('opening_styles.txt')
themes = load_lines('poem_themes.txt')

opening = random.choice(opening_styles)
theme = random.choice(themes)

prompt = (
    f"Write a short, reflective free-verse poem (8–12 lines) for employees of a university. "
    f"{opening} The poem should explore the theme of {theme}. "
    "Use stanza spacing (blank lines) where appropriate. "
    "Avoid beginning with common phrases like 'In the...' or 'There is...'. "
    "The tone should be steady, gentle, and human. Use timeless metaphors "
    "(nature, breath, light, etc.). Avoid current events or modern imagery. "
    "The poem should feel like a pause — a moment to breathe."
)

# --- Generate poem ---
def generate_poem():
    print("\n--- Prompt Sent to OpenAI ---\n")
    print(prompt)
    print("\n-----------------------------\n")

    try:
        response = client.chat.completions.create(
            model='gpt-4o',
            messages=[
                {'role': 'system', 'content': 'You are a thoughtful poet.'},
                {'role': 'user', 'content': prompt}
            ],
            temperature=0.85,
            max_tokens=200,
        )
    except Exception as e:
        print(f"❌ Error while generating poem: {e}")
        return None

    poem = response.choices[0].message.content.strip()
    return poem if poem else None

# --- Save poem or fail ---
if __name__ == '__main__':
    poem = generate_poem()
    if poem:
        print("\n=== Poem Generated ===\n")
        print(poem)
        print("\n======================\n")
        with open('poem.txt', 'w', encoding='utf-8') as f:
            f.write(poem)
    else:
        print("❌ No poem generated. Exiting with error.")
        sys.exit(1)
