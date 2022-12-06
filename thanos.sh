docker compose down
docker volume rm coffee_tavern-data
docker volume rm tagsapi-data
docker image prune --all
docker volume create coffee_tavern-data
docker volume create tagsapi-data  
docker compose up --build