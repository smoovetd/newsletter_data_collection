from cProfile import label
from fastapi import FastAPI
import sys
sys.path.append('../')
from dto.news import News, WebNews

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
async def insert_item(crnt_web_news: WebNews):
    print(crnt_web_news)
    print(crnt_web_news.date)
    crnt_news = News(crnt_web_news.date, crnt_web_news.name, crnt_web_news.link, crnt_web_news.labels, crnt_web_news.content) 
    return crnt_news.get_news_dict()