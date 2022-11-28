cd "C:\Users\cmbri\Documents\4.Perso\projet\kptncook-data-challenge"
docker stop kptncook-data-challenge_container
docker rm kptncook-data-challenge_container
docker build -t kptncook-data-challenge .  
docker run -d --name kptncook-data-challenge_container -p 80:80 kptncook-data-challenge