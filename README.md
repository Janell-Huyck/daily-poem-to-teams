# 🕊️ Daily Poem to Teams

This GitHub Action posts a reflective, uplifting poem to a Microsoft Teams channel once per day.  
The poems are generated using the OpenAI API and aim to offer moments of peace, connection, and encouragement — especially for people working in university environments.

---

## ✨ What It Does

- ⏱️ Runs automatically each morning (7–8 AM Eastern, depending on Daylight Saving Time)
- 🧠 Uses GPT-4 to generate a short, human-centered poem
- 📬 Posts the poem directly to a Teams channel via webhook
- 🛠️ Runs completely unattended, with no manual input needed

---

## 📜 Example Poem

> **"The Quiet Work"**  
>  
> The roots do not speak  
> of what they hold up.  
> They just hold.  
>  
> And when the storms come,  
> the tree does not shout its strength—  
> it simply stays.  
>  
> You do not need applause  
> to matter.  
> You only need  
> to keep  
> holding.  

---

## ⚙️ Setup Instructions

1. **Clone or fork this repo**
2. Add the following secrets to your GitHub repository:
   - `OPENAI_API_KEY` – [Create your key here](https://platform.openai.com/account/api-keys)
   - `TEAMS_WEBHOOK_URL` – Set up an [Incoming Webhook in Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

3. That’s it — the action will run daily and send your poem.

---

## 🧠 Tech Stack

- GitHub Actions (scheduled workflow)
- Python 3.10
- OpenAI GPT-4 API
- Microsoft Teams Incoming Webhook

---

## 💬 Want to Customize?

You can adjust the poem tone, format, or posting time by editing:
- `generate_and_post.py` → Controls poem prompt and formatting
- `.github/workflows/post-poem.yml` → Controls the schedule and environment

---

## 💛 Why This Exists

In a world that often feels heavy, uncertain, and divided —  
this project is one small way to offer stillness, warmth, and connection.  
A poem. A pause. A breath. Every day.

