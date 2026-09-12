# Telegram Bot Prototype

A small Python prototype for integrating a Telegram bot with an external application/API workflow.

## Purpose

The repository was created as an experiment in message-driven automation and bot integration. `app.py` contains the main application logic and `requirements.txt` records the Python dependencies.

## Configuration

The current prototype imports its bot token from `token.py`; it does not yet read the value from an environment variable. Before running or extending the project, revoke the committed token, replace the hard-coded configuration with environment-based loading, and exclude local secret files from Git.

## Security

The repository currently contains a token-shaped value in tracked history. Rotation is required even if the current file is later changed, because the old value remains accessible from earlier commits.


## Goal

The prototype connects Telegram messages to a small Python service and an external text-generation workflow. Its value is as an early integration experiment, not as a production bot framework.

## Installation and Use

After revoking the exposed token and changing `token.py` to load a replacement from a local secret source, create an environment and install the recorded dependencies:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```

On Windows PowerShell, activate the environment with `.venv\Scripts\Activate.ps1`. The Flask health service uses the `PORT` environment variable and defaults to port 5001. Review `app.py` before use because the bot and Flask server run concurrently.
