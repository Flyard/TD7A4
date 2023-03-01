# Part 1: no compose

### Flask app:

**Building the flask app**
```zsh
cd no-docker-compose
docker build -t <appName>:<tag> .
```

Code example:
```zsh
cd no-docker-compose
docker build -t flask-app:v0 .
```

**Running the app**
```zsh
docker run -v /Users/florian.ranaivoson/Documents/ESILV/S8/cloud/td6/no-docker-compose:/app -p 9000:9000 flask-app:v0
```

---
**Mongo**

Creation of the volume to make the mongo database persistent
```zsh
docker volume create mongoApp
```

**Run the container**
```zsh
docker run -d --name mongodbPersistant -p 27017:27017 -v mongoApp:/data/db mongo \

docker exec -it mongoApp bash
```

Now you should be in the mongo container. 
If you want to enter in a database, use `mongosh <database>`

# Part 2: compose

```zsh
docker-compose up -d
```

**Run the container**
```zsh
docker compose exec flask bash
```
