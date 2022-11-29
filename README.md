<h1 align=center>KptnCook data challenge</h1>

<h3>Objectives</h3>

1. Create an endpoint to <b>get</b> the number of times user x listenned to artist y: 
    - <b>user_id</b>
    - <b>Number of listens</b>

2. Create an endpoint to **update** the listens for artists y by user x:
    - <b>user_id</b>
    - Update of <b>Number of listens</b>
    - Save dataset to csv tu use it back later

3. Create an endpoint for each user to **get** recommandations such as:
    - Random artists: taking a sample of 5 artists
    - Still unknown artists: taking a sample of 5 never listenned artists  
    - Artists that are similar to the ones already listenned


<h3>Environment configuration</h3>

To build the docker image:
```
docker build -t kptncook-data-challenge .
```
To check vulnerabilities from docker image:
```
docker scan kptncook-data-challenge
```
To run the docker image:
```
docker run -d --name kptncook-data-challenge_container -p 80:80 kptncook-data-challenge
out: 176b0cb9897582f3c923fd3c179cb700415762ddc96e081176adb726a3a681e5
```

Commands to run after a code update
```
docker stop kptncook-data-challenge_container
docker rm kptncook-data-challenge_container
docker build -t kptncook-data-challenge .  
docker run -d --name kptncook-data-challenge_container -p 80:80 kptncook-data-challenge
```
or simply execute <b>run_docker.bat</b>

To access api :
    http://localhost
    
To see the doc:
    http://127.0.0.1/docs

<h3>Recommendations based on similar artists</h3>

To recommend similar artists to the ones already listenned, here are the steps:
1. 5 already listenned artist are selected
2. <b>corrwith()</b> Pandas' function is used to find each 5 previous selected most similar artist, based on a correlation rank.

corrwith() allows us to choose among 3 different correlation ranks : <b>pearson, kendall, spearman</b>.


<h3>Acknowledgments</h3>

* [Python FastAPI vs Flask](https://www.turing.com/kb/fastapi-vs-flask-a-detailed-comparison)
* [Introduction to FastApi](https://www.datacamp.com/tutorial/introduction-fastapi-tutorial)
* [FastAPI in Containers - Docker](https://fastapi.tiangolo.com/deployment/docker/)
* [Recommendation engine using pandas](https://www.geeksforgeeks.org/building-recommendation-engines-using-pandas/)