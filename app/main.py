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

@app.get("")

def read_root():
    return {"Hello": "World"}


"""
Definition of the User endpoint with possibilities to: 
    • see the number of time user x listenned to artist
    • update the number of time user x listenned to artist y
"""
class User(BaseModel):
    user_id: int


@app.get("/user/{user_id}")
def read_user_listens(user_id: int, query_artist: Union[str, None] = None):
    df_lastfm = pd.read_csv('lastfm-matrix-germany.csv', sep=',', index_col = 'user')
    
    #Initializing variables
    column_artist=None
    times_listenned = "0"
    user_exist=False

    for column in df_lastfm.columns: #selecting column corresponding to the artist
        if column == query_artist:
            column_artist = column
    for index in df_lastfm.index: #verifying user existence
        if index==user_id:
            user_exist=True
    if column_artist == None:
        query_artist="artist not found in database"
    if user_exist == False:
        user_id = "user doesn't exist"
    if column_artist != None and user_exist:
        times_listenned =  str(df_lastfm.at[int(user_id),column_artist])
        return {
            "User": user_id,
            "Artist":query_artist,
            "Times listenned": times_listenned 
        }
    return {
            "User": user_id,
            "Artist":query_artist,
            "Times listenned": times_listenned 
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
            "User": user_id,
            "Artist":artist_listenned,
            "Times listenned": times_listenned 
        }
    return {
            "User": user_id,
            "Artist":artist_listenned,
            "Times listenned": times_listenned 
    }

"""
Definition of the Recommandations endpoint with possibilities to get recommandations such as: 
    • Random artists
    • Still unknown artists
    • Artists that are similar to the ones already listenned
"""

@app.get("/recommandations/{user_id}")
def read_user_recommandations(user_id: int, query_artist: Union[str, None] = None):
    
    df_lastfm = pd.read_csv('lastfm-matrix-germany.csv', sep=',', index_col = 'user')
    
    # Initializing variables
    user_exist=False

    random_artists = ['user']
    still_unknown_artists = ['user']
    similar_artists = []

    for index in df_lastfm.index: #verifying user existence
        if index==user_id:
            user_exist=True
    if user_exist:
        # Selecting 5 random columns in the dataframe excepting 'user'
        while random_artists.__contains__('user'):
            random_artists = df_lastfm.sample(n=5,axis='columns').columns.to_list()
        while still_unknown_artists.__contains__('user'):
            df_user = df_lastfm.loc[[int(user_id)]] #selecting user's row
            still_unknown_artists = df_user[df_user == 0][:].dropna(axis=1).sample(n=5,axis='columns').columns.to_list() #5 artists never listenned by the user
        return {
            "User": user_id,
            "Artist":query_artist,
            "Random artists suggested": random_artists,
            "Still unknown artists": still_unknown_artists
        }
    else:
        user_id = "user doesn't exist"

    return {
            "user": user_id
    }