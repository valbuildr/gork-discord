# gork-discord

A _very_ simple Discord bot written in discord.py that simply replies to '@gork is this real'

Inspired by [espeon/gork](https://github.com/espeon/gork), which does a simillar thing on [Bluesky](https://bsky.app/profile/gork.bluesky.bot).

A publically accessible version of this bot is available here: https://discord.com/oauth2/authorize?client_id=1399927550322675873

## Self Hosting

1. Ensure you have [Python 3.11](https://www.python.org/downloads/release/python-31113/) (or later) installed. This probably works on later Python versions but I'm unsure.
2. Download this repositories code: https://github.com/valbuildr/gork-discord/archive/refs/heads/main.zip
3. (Optional) Create and begin using a virtual environment: `python3 -m venv .venv` then being using it. Here's a list of commands for various shell types: https://docs.python.org/3/library/venv.html#how-venvs-work
4. Install discord.py: `python3 -m pip install discord.py`
5. Fill out `config.ex.py` and rename it to `config.py`.
6. Run `main.py`: `python3 main.py`
