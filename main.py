from typing import Dict, List, Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# 1. Pydantic Model for Data Validation and Serialization
class Item(BaseModel):
    """Defines the structure of an item."""
    name: str
    description: Optional[str] = None
    price: float
    
# In-memory "database" (a dictionary where keys are item names)
items_db: Dict[str, Item] = {}

# FastAPI application instance
app = FastAPI(title="Simple CRUD API")

# -----------------
# 2. CRUD Operations
# -----------------

# 🟢 CREATE (POST)
@app.post("/items/", response_model=Item, status_code=201)
async def create_item(item: Item):
    """Creates a new item."""
    if item.name in items_db:
        raise HTTPException(status_code=400, detail="Item already exists")
    items_db[item.name] = item
    return item

# 🔵 READ All (GET)
@app.get("/items/", response_model=List[Item])
async def read_items():
    """Returns a list of all items."""
    return list(items_db.values())

# 🔵 READ One (GET)
@app.get("/items/{item_name}", response_model=Item)
async def read_item(item_name: str):
    """Returns a specific item by name."""
    if item_name not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    return items_db[item_name]

# 🟡 UPDATE (PUT)
@app.put("/items/{item_name}", response_model=Item)
async def update_item(item_name: str, item: Item):
    """Updates an existing item or creates it if it doesn't exist."""
    if item_name not in items_db:
        # Optionally, create the item if it doesn't exist (PUT standard)
        # or raise an error (more common in strict APIs)
        raise HTTPException(status_code=404, detail="Item not found to update")
        
    items_db[item_name] = item  # Replaces the existing item data
    return item

# 🔴 DELETE (DELETE)
@app.delete("/items/{item_name}", status_code=204)
async def delete_item(item_name: str):
    """Deletes an item by name."""
    if item_name not in items_db:
        raise HTTPException(status_code=404, detail="Item not found")
    del items_db[item_name]
    return {"message": "Item deleted successfully"}

# -----------------
# 3. Running the App
# -----------------

# Run this from your terminal: uvicorn main:app --reload