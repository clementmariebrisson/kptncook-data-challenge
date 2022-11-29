from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import numpy as np
import os

app = FastAPI(
    title = "KptnCook Challenge API",
    description = "API made to update user listens and recommand him artists",
    version = "0.1"
)

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
        times_listenned =  str(df_lastfm.at[int(user_id),column_artist])
        return {
            "user": user_id,
            "artist":query_artist,
            "times listenned": times_listenned 
        }
    return {
            "user": user_id,
            "artist":query_artist,
            "times listenned": times_listenned 
    }

@app.put("/user/{user_id}")
def put_user_listen(user_id: int, artist_listenned: Union[str, None] = None):
    
    df_lastfm = pd.read_csv('lastfm-matrix-germany.csv', sep=',', index_col = 'user')

    #Initializing variables
    column_artist=None
    times_listenned = "0"
    user_exist=False

    for column in df_lastfm.columns: #selecting column corresponding to the artist
        if column == artist_listenned:
            column_artist = column
    for index in df_lastfm.index: #verifying user existence
        if index==user_id:
            user_exist=True
    if column_artist == None:
        artist_listenned="artist not found in database"
    if user_exist == False:
        user_id = "user doesn't exist"
    if column_artist != None and user_exist:
        df_lastfm.at[int(user_id),column_artist] += 1 #adding one listen to the artist the user listenned
        times_listenned =  str(df_lastfm.at[int(user_id),column_artist]) #to string for the output
        df_lastfm.to_csv('lastfm-matrix-germany.csv') #saving the new dataframe   
        return {
            "user": user_id,
            "artist":artist_listenned,
            "times listenned": times_listenned 
        }
    return {
            "user": user_id,
            "artist":artist_listenned,
            "times listenned": times_listenned 
    }

@app.get("")

def read_root():
    return {"Hello": "World"}