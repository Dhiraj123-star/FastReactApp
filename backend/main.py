from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection
from models import create_table, ItemCreate
from dotenv import load_dotenv
import os
import redis
import json
import logging

load_dotenv()

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Redis client
redis_client = redis.Redis(host='redis', port=6379, decode_responses=True)

app = FastAPI(title=os.getenv("APP_NAME", "FastReactApp"))

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create table on startup
create_table()

@app.get("/api")
def root():
    return {"message": "Hello from FastAPI"}

@app.post("/api/items")
def create_item(item: ItemCreate):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO items (name) VALUES (?)", (item.name,))
    conn.commit()
    conn.close()

    # Invalidate cache
    redis_client.delete("items_cache")
    logger.info("Cache invalidated after create")

    return {"message": f"Item '{item.name}' created."}

@app.get("/api/items")
def read_items():
    # Try cache
    cached_data = redis_client.get("items_cache")
    if cached_data:
        logger.info("Returning data from Redis cache")
        return json.loads(cached_data)

    # Fetch from DB
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items")
    items = [dict(row) for row in cursor.fetchall()]
    conn.close()

    # Cache result
    redis_client.set("items_cache", json.dumps(items))
    logger.info("Returning data from database and caching it")

    return items

@app.put("/api/items/{item_id}")
def update_item(item_id: int, name: str):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    if not item:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")

    cursor.execute("UPDATE items SET name = ? WHERE id = ?", (name, item_id))
    conn.commit()
    conn.close()

    # Invalidate cache
    redis_client.delete("items_cache")
    logger.info("Cache invalidated after update")

    return {"message": f"Item with id {item_id} updated to '{name}'."}

@app.delete("/api/items/{item_id}")
def delete_item(item_id: int):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM items WHERE id = ?", (item_id,))
    item = cursor.fetchone()
    if not item:
        conn.close()
        raise HTTPException(status_code=404, detail="Item not found")

    cursor.execute("DELETE FROM items WHERE id = ?", (item_id,))
    conn.commit()
    conn.close()

    # Invalidate cache
    redis_client.delete("items_cache")
    logger.info("Cache invalidated after delete")

    return {"message": f"Item with id {item_id} deleted."}
