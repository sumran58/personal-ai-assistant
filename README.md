# 🤝 Personal Assistant (n8n + Streamlit)

A personal AI assistant with a chat-based web UI, powered by an [n8n](https://n8n.io/) automation workflow. The Streamlit frontend sends user messages to an n8n webhook, where an LLM agent decides which tool to use and returns a response.

## Features

The assistant agent (defined in [`sysprompt.md`](sysprompt.md)) can:

1. Answer general knowledge questions (with web search when needed).
2. Manage **Google Calendar** — create events, fetch single or multiple events.
3. Manage **Gmail** — read, summarize, and reply to emails.
4. Manage **Google Tasks** — create, fetch, and delete to-dos.
5. Manage **notes** via **Google Docs** — create, append, and read.
6. Track **expenses** via **Google Sheets** — add entries, fetch history, and calculate totals.

## Architecture

```
Streamlit UI (app.py)  --HTTP POST-->  n8n Webhook  -->  AI Agent  -->  Google Workspace tools
```

- **`app.py`** — Streamlit chat interface. Collects user input and posts it as JSON to the n8n webhook, then renders the returned response.
- **n8n workflow** (not included in this repo) — receives the webhook call, runs an AI agent configured with the system prompt in `sysprompt.md`, and calls out to Google Calendar, Gmail, Google Tasks, Google Docs, and Google Sheets tools as needed.
- **`sysprompt.md`** — the system prompt that defines the agent's role, available tools, and decision-making rules.
- **`test_webhook.py`** — a small script for sanity-testing the n8n webhook directly (without the UI).

## Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) for dependency management
- A running [n8n](https://n8n.io/) instance with the corresponding workflow imported and activated, exposing a webhook (see the URL used in `app.py` / `test_webhook.py`)
- Google account access configured in n8n (Calendar, Gmail, Tasks, Docs, Sheets credentials)

## Setup

1. Clone the repo and install dependencies:

   ```bash
   uv sync
   ```

2. Start your n8n instance and make sure the assistant workflow is active, exposing a webhook at:

   ```
   http://localhost:5678/webhook/<your-webhook-id>
   ```

3. Update the webhook URL in `app.py` if it differs from your n8n instance.

## Running the app

Start the Streamlit UI:

```bash
uv run streamlit run app.py
```

Then open the app in your browser (Streamlit will print the local URL, typically `http://localhost:8501`) and start chatting.

## Testing the webhook directly

You can bypass the UI and test the n8n webhook with:

```bash
uv run python test_webhook.py
```

This sends a sample message and prints the raw response from the workflow.

## Project structure

```
.
├── app.py                # Streamlit chat UI
├── main.py                # Placeholder entry point
├── sysprompt.md            # System prompt for the n8n AI agent
├── test_webhook.py         # Script to test the n8n webhook directly
├── pyproject.toml          # Project dependencies (managed with uv)
└── uv.lock                # Locked dependency versions
```

## Notes

- The n8n workflow itself is not stored in this repository; you'll need to build or import it separately in your n8n instance, using `sysprompt.md` as the agent's system prompt.
- Google Workspace credentials (Calendar, Gmail, Tasks, Docs, Sheets) must be configured as credentials/connections inside n8n, not in this codebase.
