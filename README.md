# 🕊️ Daily Haiku to Teams and SMS

This GitHub Action posts a short, reflective haiku to a Microsoft Teams channel once per day — and optionally sends the same haiku as an SMS message to one or more phones.  
The haiku are generated using the OpenAI API and aim to offer moments of peace, connection, and encouragement — especially for people working in university environments.

---

## ✨ What It Does

- ⏱️ Runs automatically each morning (7–8 AM Eastern, depending on Daylight Saving Time)
- 🧠 Uses GPT-4 to generate a short, nature-inspired haiku
- 📬 Posts the haiku directly to a Teams channel via webhook
- 📱 Optionally sends the haiku by SMS to one or more phones
- 🛠️ Runs completely unattended, with no manual input needed

---

## 📜 Example Haiku

> **[Daily Haiku]**  
>  
> soft light on the path  
>  
> the river hums below frost  
>  
> breath curling upward  

---

## ⚙️ Setup Instructions

### 1. Clone or fork this repository

### 2. Add GitHub **Secrets**:
- `OPENAI_API_KEY` – [Create your key here](https://platform.openai.com/account/api-keys)
- `OUTLOOK_USERNAME` – Your Outlook.com sender email address (e.g., `haikubot@outlook.com`)
- `OUTLOOK_APP_PASSWORD` – Your Outlook app password for secure SMTP sending
- `TEAMS_WEBHOOK_RANDOM` – Set up an [Incoming Webhook in Teams](https://learn.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook)

### 3. Add GitHub **Variables**:
- `SMS_RECIPIENTS` – Comma-separated list of SMS gateway addresses (see below for examples)

---

## 📱 How to Add SMS Recipients

The `SMS_RECIPIENTS` GitHub **Variable** holds all the phone numbers you want to receive the daily haiku by text.  
You can update it at any time in GitHub Settings → Secrets and Variables → Actions → Variables (no code changes needed).

✅ Format: comma-separated list, **no spaces**

Example:

`5551234567@vtext.com,5559876543@txt.att.net`


| Carrier | SMS Gateway Address Format |
|:--------|:----------------------------|
| Verizon | `{number}@vtext.com` |
| Spectrum | `{number}@vtext.com` |
| AT&T | `{number}@txt.att.net` |
| T-Mobile | `{number}@tmomail.net` |
| Sprint | `{number}@messaging.sprintpcs.com` |
| Boost Mobile | `{number}@myboostmobile.com` |
| US Cellular | `{number}@email.uscc.net` |
| Cricket Wireless | `{number}@sms.cricketwireless.net` |

✅ Example: For a Verizon number `555-123-4567`, you would enter `5551234567@vtext.com`.

✅ You can add or remove numbers any time by editing the GitHub Variable — no need to touch the code or YAML.

---

## 🧠 Tech Stack

- GitHub Actions (scheduled workflow)
- Python 3.10
- OpenAI GPT-4 API
- Microsoft Teams Incoming Webhook
- Outlook.com SMTP (for sending SMS via email gateways)

---

## 💬 Want to Customize?

You can adjust the haiku tone, structure, or posting time by editing:
- `generate_poem.py` → Controls haiku generation prompt and formatting
- `.github/workflows/post-poem.yml` → Controls the schedule, Teams posting, and SMS notification

---

## 💛 Why This Exists

In a world that often feels heavy, uncertain, and divided —  
this project is one small way to offer stillness, warmth, and connection.  
A haiku. A breath. A pause. Every day.
