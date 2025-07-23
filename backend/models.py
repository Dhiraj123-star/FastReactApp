import sqlite3
import os
from pydantic import BaseModel, StringConstraints
from typing import Annotated
from dotenv import load_dotenv

load_dotenv()
# Validation: non-empty name
class ItemCreate(BaseModel):
    name: Annotated[str, StringConstraints(min_length=1, strip_whitespace=True)]


def create_table():
    db_url = os.getenv("DATABASE_URL", "test.db")
    conn = sqlite3.connect(db_url)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()
