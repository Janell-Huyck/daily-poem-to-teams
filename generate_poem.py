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

# Load randomized content
opening_styles = load_lines('opening_styles.txt')
opening = random.choice(opening_styles)

prompt = (
    f"{opening} "
    "Write a short haiku (3 lines, following the 5-7-5 syllable pattern). "
    "The haiku should capture a fleeting moment of awareness — a glimpse that suggests something deeper without explaining it. "
    "Focus on a small, sensory detail: a sound, a breath, a shadow, a flicker of light. "
    "Avoid simply describing a scene. Instead, hint at a larger feeling or shift in perception. "
    "Leave room for the reader to wonder — do not conclude or explain. "
    "The tone should be still, subtle, and contemplative, like the pause at the end of a tai chi movement. "
    "Avoid beginning with common phrases like 'There is...' or 'I see...'. "
    "Use simple language grounded in physical senses. "
    "Let the haiku *be* the experience itself. "
    "Avoid unnecessary capitalization — begin with lowercase unless grammar requires otherwise. "
    "Avoid using the word 'haiku' in the poem. "
    "Write the poem in English only. "
    "Do not include any additional explanation or introductory text. "
    "The poem must be exactly 3 lines — no more, no less. "
    "Do not include extra line breaks, blank lines, or punctuation at the end of any line."
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
            temperature=0.7,
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
