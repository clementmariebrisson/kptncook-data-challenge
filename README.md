<h1 align=center>KptnCook data challenge</h1>


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
To access api :
    http://localhost
    
To see the doc:
    http://127.0.0.1/docs


Commands to run after a code update
```
docker stop kptncook-data-challenge_container
docker rm kptncook-data-challenge_container
docker build -t kptncook-data-challenge .  
docker run -d --name kptncook-data-challenge_container -p 80:80 kptncook-data-challenge
```
or simply execute <b>run_docker.bat</b>

<h3>Objectives:</h3>

1. Create an endpoint to <b>get</b> the list of artists which user x listenned returning: 
    - <b>user_id</b>
    - <b>list_artists_listenned</b>

2. Create an endpoint to **update** the list of artists which user x listenned returning:
    - <b>user_id</b>
    - Update of <b>list_artists_listenned</b>
3. Create an endpoint for each user to **get** recommandations such as:
    - Random artists 
    - Still unknown artists
    - Artists that are similar to the ones already listened
