from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection
from models import create_table
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title=os.getenv("APP_NAME", "FastReactApp"))

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to allowed domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create table if not exists
create_table()

@app.get("/api")
def root():
    return {"message": "Hello from FastAPI"}

@app.post("/api/items")
def create_item(name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (?)", (name,))
    conn.commit()
    conn.close()
    return {"message": f"Item '{name}' created."}

@app.get("/api/items")
def read_items():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    conn.close()
    return [dict(item) for item in items]

@app.put("/api/items/{item_id}")
def update_item(item_id: int, name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    if item is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")

    cursor.execute("UPDATE items SET name = ? WHERE id = ?", (name, item_id))
    conn.commit()
    conn.close()
    return {"message": f"Item with id {item_id} updated to '{name}'."}

@app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    if item is None:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")

    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()
    return {"message": f"Item with id {item_id} deleted."}
