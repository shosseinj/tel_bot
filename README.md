# Telegram Bot Prototype

A small Python prototype for integrating a Telegram bot with an external application/API workflow.

## Purpose

The repository was created as an experiment in message-driven automation and bot integration. `app.py` contains the main application logic and `requirements.txt` records the Python dependencies.

## Configuration

The current prototype imports its bot token from `token.py`; it does not yet read the value from an environment variable. Before running or extending the project, revoke the committed token, replace the hard-coded configuration with environment-based loading, and exclude local secret files from Git.

## Security

The repository currently contains a token-shaped value in tracked history. Rotation is required even if the current file is later changed, because the old value remains accessible from earlier commits.
