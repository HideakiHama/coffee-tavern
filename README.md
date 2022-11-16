Run these commands to set up docker
 docker volume create coffee_tavern-data
 docker compose up --build
 uvicorn main:app --reload
