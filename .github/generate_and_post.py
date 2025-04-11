import os
import openai
import requests

openai.api_key = os.getenv('OPENAI_API_KEY')

def generate_poem():
    prompt = (
        "Write a short, reflective free-verse poem for employees of a university. "
        "The tone should be steady, gentle, and human. Use timeless metaphors "
        "(nature, light, breath, etc.) to explore themes like connection, hope, or quiet strength. "
        "Avoid current events or modern imagery. The poem should feel like a pause — a moment to breathe."
    )
    response = openai.ChatCompletion.create(
        model='gpt-4',
        messages=[
            {'role': 'system', 'content': 'You are a thoughtful poet.'},
            {'role': 'user', 'content': prompt}
        ],
        max_tokens=200,
        temperature=0.8
    )
    return response.choices[0].message.content.strip()

def post_to_all_teams_channels(poem_text):
    payload = {
        'text': f"📜 *Daily Poem*\n\n{poem_text}"
    }

    for key, value in os.environ.items():
        if key.startswith('TEAMS_WEBHOOK_') and value.startswith('https://'):
            print(f"Posting to {key}...")
            response = requests.post(value, json=payload)
            if response.status_code != 200:
                print(f"❌ Failed to post to {key}: {response.text}")
            else:
                print(f"✅ Successfully posted to {key}")

if __name__ == '__main__':
    poem = generate_poem()
    post_to_all_teams_channels(poem)
