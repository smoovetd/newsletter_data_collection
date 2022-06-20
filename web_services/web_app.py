from fastapi import FastAPI

app = FastAPI()

@app.get("/item/")
async def get_all_items():
    return "get_all_items is not implemented yet"

@app.get("/item/{item_id}")
async def get_item_by_id(item_id):
    return f"get_item_by_id {item_id} is not implemented yet"

@app.delete("/item/{item_id}")
async def delete_item_by_id(item_id):
    return f"delete_item_by_id {item_id} is not implemented yet"

@app.post("/item/")
async def insert_item():
    return f"insert_item is not implemented yet"