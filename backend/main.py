from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import get_db_connection
from models import create_table

app = FastAPI()

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # For production, specify allowed domains
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
