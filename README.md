# Discord Bot

A simple Discord bot with meme API integration and message handling capabilities.

## Features

- Responds to `!hello` and `!ping` commands
- Responds to messages starting with `$hello`
- Meme API integration for fetching random memes
- Modern Discord.py implementation using commands framework

## Setup

1. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your Discord bot token:
   - Option A: Set environment variable
     ```bash
     export DISCORD_TOKEN='your_bot_token_here'
     ```
   - Option B: Replace `'YOUR_BOT_TOKEN_HERE'` in the code with your actual token

3. Run the bot:
   ```bash
   python3 discord_bot.py
   ```

## Commands

- `!hello` - Bot responds with "Hello!"
- `!ping` - Bot responds with "Pong!"
- `!meme` - Bot sends a random meme from the meme API
- `$hello` - Bot responds with "Hello World!" (works in any message)

## Requirements

- Python 3.7+
- discord.py
- requests

## Security Note

Never share your Discord bot token publicly. Use environment variables or secure configuration files to store sensitive information.
