docker compose down
docker volume rm coffee_tavern-data
# docker volume rm tags-data
# docker image prune --all
docker volume create coffee_tavern-data
# docker volume create tags-data 
docker compose up --build