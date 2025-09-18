# gork-discord

A _very_ simple Discord bot written in discord.py that simply replies to '@gork is this real'

Inspired by [espeon/gork](https://github.com/espeon/gork), which does a simillar thing on [Bluesky](https://bsky.app/profile/gork.bluesky.bot).

A publically accessible version of this bot is available here: https://discord.com/oauth2/authorize?client_id=1399927550322675873

## Self Hosting

1. Ensure that you have [Docker](https://docs.docker.com/get-started/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/) installed with the following commands: `docker version`, `docker compose version`
2. Fill `.env.example` with the token of your Discord bot and rename it to `.env`.
3. Run `docker compose up`.
