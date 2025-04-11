import os
from openai import OpenAI
import requests

client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))

def generate_poem():
    prompt = (
        "Write a short, reflective free-verse poem for employees of a university. "
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

    print("\n=== Poem Generated ===\n")
    print(response.choices[0].message.content.strip())
    print("\n======================\n")

    return response.choices[0].message.content.strip()

def post_to_all_teams_channels(poem_text):
    payload = {
        '@type': 'MessageCard',
        '@context': 'https://schema.org/extensions',
        'summary': 'Daily Poem',
        'themeColor': '0078D7',
        'title': '📜 Daily Poem',
        'text': poem_text
    }

    webhook_keys = [k for k in os.environ if k.startswith('TEAMS_WEBHOOK_')]
    print(f"🔗 Found {len(webhook_keys)} Teams webhooks in environment variables.")
    print(f"These are the keys: {webhook_keys}")

    for key in webhook_keys:
        value = os.environ.get(key)
        if value and value.startswith('https://'):
            print(f"🔗 Attempting to post to {key}...")
            response = requests.post(value, json=payload)
            print(f"📬 Status: {response.status_code}")
            print(f"📨 Response: {response.text}")
            if response.status_code not in (200, 202):
                print(f"❌ Failed to post to {key}")
            else:
                print(f"✅ Successfully posted to {key}")


if __name__ == '__main__':
    poem = generate_poem()
    post_to_all_teams_channels(poem)
