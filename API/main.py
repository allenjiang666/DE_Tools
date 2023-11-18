from fastapi import FastAPI, HTTPException, Query
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
import sqlite3
import json

# Create a FastAPI instance
app = FastAPI()

# Allow requests from http://localhost:5173
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

# Mount the 'static' directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Define a Pydantic model for the data
class Item(BaseModel):
    id: str
    data: str

# SQLite database connection and cursor
conn = sqlite3.connect("metadata.db")
cursor = conn.cursor()

# Create the table if it doesn't exist
cursor.execute("""
    CREATE TABLE IF NOT EXISTS meta_table (
        id TEXT PRIMARY KEY,
        data TEXT
    )
""")
conn.commit()

@app.get("/", response_class=HTMLResponse)
async def read_index():
    # Serve your HTML file as a response
    with open("static/index.html", "r") as file:
        html_content = file.read()
    return HTMLResponse(content=html_content)

# CRUD Operations


@app.post("/items/", )
async def create_item(item: Item):
    try:
        cursor.execute("INSERT INTO meta_table (id, data) VALUES (?, ?)", (item.id, item.data))
        conn.commit()
        return item
    except sqlite3.IntegrityError:
        raise HTTPException(status_code=400, detail="Item with this id already exists")

@app.get("/items/{id}")
async def read_item(id: str):
    cursor.execute("SELECT id, data FROM meta_table WHERE id=?", (id,))
    row = cursor.fetchone()
    if row is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"id": row[0], "data":json.loads(row[1])}

@app.put("/items/{id}", )
async def update_item(id: str, item: Item):
    cursor.execute("UPDATE meta_table SET data=? WHERE id=?", (item.data, id))
    conn.commit()
    return {"id": id, "data": item.data}

@app.delete("/items/{id}", )
async def delete_item(id: str):
    cursor.execute("DELETE FROM meta_table WHERE id=?", (id,))
    conn.commit()
    return {"id": id, "data": None}

@app.get("/items/")
async def read_items(
        type: str = Query(None),
        user: str = Query(None),
    ):
        
    query = "SELECT id, JSON_EXTRACT(data, '$.user') as user ,JSON_EXTRACT(data, '$.type') as type FROM meta_table WHERE"
    conditions = []
    params = []

    if type:
        conditions.append("JSON_EXTRACT(data, '$.type')= ?")
        params.append(type)
    if user:
        conditions.append("JSON_EXTRACT(data, '$.user')= ?")
        params.append(user)

    if conditions:
        query += " " + "AND".join(conditions)

    if type is None and user is None:
        query = "SELECT id, JSON_EXTRACT(data, '$.user') as user ,JSON_EXTRACT(data, '$.type') as type FROM meta_table"
        params = []

    cursor.execute(query,params)
    results = cursor.fetchall()
    return results

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
