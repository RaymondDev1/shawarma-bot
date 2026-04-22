import os
from dataclasses import dataclass


@dataclass
class Config:
    bot_token: str


def load_config() -> Config:
    token = os.getenv("BOT_TOKEN")
    if not token:
        raise RuntimeError(
            "BOT_TOKEN environment variable is not set. "
            "Set it before running the bot."
        )
    return Config(bot_token=token)
