# generate_poem.py

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

def clean_poem(poem):
    """Remove unwanted trailing dashes, ellipses, and extra whitespace from each line."""
    lines = [line.rstrip('—. ').rstrip() for line in poem.splitlines()]
    return '\n'.join(lines)

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
    f"Write a haiku poem (5 syllables / 7 syllables / 5 syllables) for employees of a university. "
    f"{opening} The haiku should explore the theme of {theme}. "
    "Use timeless imagery (nature, light, breath, seasons). "
    "The tone should be gentle, human, and reflective. "
    "Avoid clichés, common sayings, and modern references. "
    "Do not use dashes, ellipses, or ending punctuation at the end of lines unless absolutely necessary. "
    "Let line breaks create the natural pauses. "
    "Do not capitalize the beginning of each line unless grammatically necessary (e.g., proper nouns). "
    "The haiku should feel like a moment of quiet recognition."
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
            temperature=0.9,
            max_tokens=100,
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
        poem = clean_poem(poem)  # Apply the cleanup here
        print("\n=== Cleaned Poem Generated ===\n")
        print(poem)
        print("\n===============================\n")
        with open('poem.txt', 'w', encoding='utf-8') as f:
            f.write(poem)
    else:
        print("❌ No poem generated. Exiting with error.")
        sys.exit(1)
