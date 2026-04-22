import sqlite3
from datetime import datetime
from pathlib import Path


DB_PATH = Path("orders.db")


def init_db() -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                username TEXT,
                category TEXT NOT NULL,
                item_name TEXT NOT NULL,
                created_at TEXT NOT NULL
            )
            """
        )
        conn.commit()


def save_order(user_id: int, username: str | None, category: str, item_name: str) -> None:
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute(
            """
            INSERT INTO orders (user_id, username, category, item_name, created_at)
            VALUES (?, ?, ?, ?, ?)
            """,
            (user_id, username, category, item_name, datetime.utcnow().isoformat()),
        )
        conn.commit()
