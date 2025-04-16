# eSigma

![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?style=for-the-badge&logo=discord&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

A feature-rich Discord bot designed for voice channel interactions, playing random audio clips, and providing customized responses when users join voice channels.

## Features

- **Automatic Voice Greetings**: Plays specific audio when users join voice channels
- **Random Audio Playback**: Plays random audio clips from a predefined directory
- **User-Specific Responses**: Different responses for different users
- **Permission Management**: Restricts certain commands to authorized users
- **Robust Error Handling**: Comprehensive logging and error recovery
- **Cross-Platform Support**: Works on Windows, Linux, and macOS

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/discord-voice-bot.git
   cd discord-voice-bot
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up configuration**:
   - Create a `bottoken.py` file with your Discord bot token:
     ```python
     bot_token = "YOUR_DISCORD_BOT_TOKEN"
     ```
   - Configure user IDs and other settings in `content.py`

4. **Prepare audio files**:
   - Place MP3 files in:
     - `data/randomvc/` for random audio clips
     - `data/inoutvc/user_id/` for user-specific join sounds

## Usage

### Commands

- `/play`: Start playing random audio in your voice channel
- `/stop`: Stop the audio playback

### Automatic Features

- Plays specific audio when users join voice channels
- Sends welcome messages to the bot owner when starting up

## Configuration

Edit `content.py` to customize:

- User IDs and permissions
- Response messages
- Audio file paths
- Channel settings

## File Structure

```
discord-voice-bot/
├── bot.py                # Main bot application
├── content.py            # Configuration and messages
├── bottoken.py           # Bot token (gitignored)
├── data/
│   ├── dependencies/     # FFmpeg and other dependencies
│   ├── inoutvc/         # User join/leave sounds
│   └── randomvc/        # Random audio clips
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.8+
- discord.py
- FFmpeg (system-wide or in dependencies folder)

## Contributing

Contributions are welcome! Please open an issue or pull request for any improvements.

## License

[MIT](https://choosealicense.com/licenses/mit/)