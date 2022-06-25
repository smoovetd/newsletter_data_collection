from cProfile import label
from http.client import HTTPException
from fastapi import FastAPI, HTTPException
import sys
sys.path.append('../')
from dto.news import News, WebNews
from backend.sqlite_db import DBConnection
from sqlite3 import OperationalError

db_con = DBConnection('test.db')

app = FastAPI()

@app.get("/item/")
async def get_all_items():
    res = list()
    for item in db_con.select_all_records():
        print(type(item))
        print(item)
        crnt_news = News(id=item[0], date=item[1], name=item[2], link=item[3], labels=item[4], content=item[5])
        res.append(crnt_news.get_news_dict())
    return res 

@app.get("/item/{item_id}")
async def get_item_by_id(item_id):
    try:
        item = db_con.select_record_by_id(item_id)
        #print(item)
        #print(type(item))
        crnt_news = News(id=item[0], date=item[1], name=item[2], link=item[3], labels=item[4], content=item[5])    
    except IndexError as ex:
        raise HTTPException(status_code=400, detail=f'Record with id {item_id} was not found!')
    except OperationalError as sql_ex:
        raise HTTPException(status_code=400, detail=str(sql_ex))

    return crnt_news.get_news_dict()

@app.delete("/item/{item_id}")
async def delete_item_by_id(item_id):
    try:
        res = db_con.delete_record_by_id(item_id)
    except IndexError as ex:
        raise HTTPException(status_code=400, detail=f'Record with id {item_id} was not found!')
    except OperationalError as sql_ex:
        raise HTTPException(status_code=400, detail=str(sql_ex))
    if res == True:
        return 'Record successfully removed!'
    else:
        return 'ERROR something went wrong!'

@app.post("/item/")
async def insert_item(crnt_web_news: WebNews):
    #print(crnt_web_news)
   # print(crnt_web_news.date)
    crnt_news = News(crnt_web_news.date, crnt_web_news.name, crnt_web_news.link, crnt_web_news.labels, crnt_web_news.content) 
    db_con.insert(crnt_news.get_news_dict())
    return crnt_news.get_news_dict()