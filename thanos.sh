docker compose down
docker volume rm coffee_tavern-data
docker volume create coffee_tavern-data 
docker compose up --build