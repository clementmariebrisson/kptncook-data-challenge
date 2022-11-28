
from typing import Union

#from fastapi import FastAPI, File, UploadFile


"""
@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.post("/files/")
async def create_file(file: Union[bytes, None] = File(default=None)):
    if not file:
        return {"message": "No file sent"}
    else:
        return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: Union[UploadFile, None] = None):
    if not file:
        return {"message": "No upload file sent"}
    else:
        return {"filename": file.filename}
"""

from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import os


app = FastAPI(
    title = "KptnCook challenge api",
    description = "api made to update what a user had listenned and recommand him artists",
    version = "0.1"
)


class Item(BaseModel):

    name: str
    price: float
    is_offer: Union[bool, None] = None

class User(BaseModel):
    user_id: int

@app.get("/user/{user_id}")
def read_user_listens(user_id: int, query_artist: Union[str, None] = None):
    
    df_lastfm = pd.read_csv('lastfm-matrix-germany.csv', sep=',', index_col = 'user')

    column_artist=None
    times_listenned = "0"
    user_exist=False

    for column in df_lastfm.columns:
        if column == query_artist:
            column_artist = column
    for index in df_lastfm.index:
        if index==user_id:
            user_exist=True
    if column_artist == None:
        query_artist="artist not found in database"
    if user_exist == False:
        user_id = "user doesn't exist"
    if column_artist != None and user_exist:
        times_listenned = df_lastfm[[column_artist]].iloc[[user_id]].to_csv()
    print("value: ", df_lastfm[[column_artist]].iloc[[user_id]])
    return {
        "user": user_id,
        "artist":query_artist,
        "times listenned": times_listenned 
    }

@app.put("/user/{user_id}")
def put_user_listen(user_id: int, artist_listenned: Union[str, None] = None):
    
    df_lastfm = pd.read_csv('lastfm-matrix-germany.csv', sep=',', index_col = 'user')

    column_artist=None
    times_listenned = "0"
    user_exist=False

    for column in df_lastfm.columns:
        if column == artist_listenned:
            column_artist = column
    for index in df_lastfm.index:
        if index==user_id:
            user_exist=True
    if column_artist == None:
        artist_listenned="artist not found in database"
    if user_exist == False:
        user_id = "user doesn't exist"
    if column_artist != None and user_exist:
        df_lastfm[[column_artist]].iloc[[user_id]] = df_lastfm[[column_artist]].iloc[[user_id]] + 1
        times_listenned = df_lastfm[[column_artist]].iloc[[user_id]].to_csv()
    print("value: ", df_lastfm[[column_artist]].iloc[[user_id]])
    return {
        "user": user_id,
        "artist":artist_listenned,
        "times listenned": times_listenned 
    }


@app.get("")

def read_root():
    return {"Hello": "World"}
"""
def read_root():
    df_lastfm = pd.read_csv('lastfm-matrix-germany.csv')
    return df_lastfm.to_json()
"""

@app.get("/items/{item_id}")

def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")

def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}
