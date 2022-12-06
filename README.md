### Coffee Tavern

> This application is a linkedin but for the people in the service industry.

## Team:
>Person 1 - Hideaki Hama

>Person 2 - Curtis Cheung

>Person 3 - Lexey Olsen

>Person 4 - Christopher Shih

### Stack:

# Front-End
    - React
    - Javascript

# Back-End
    - Fast API
    - PostgreSQL
    - Python

# Platform
    - Docker



Run these commands in terminal to set up the application

```shell
#This will create the database in your docker 
$ docker volume create coffee_tavern-data
$ docker volume create tagsapi-data    
```
```shell
#This will build and compose up the images and containers for your docker at the same time 

$ docker compose up --build 
```                

```shell
# ***(Mac User Only)*** 
# Will do everything Thanos the project***(Mac User Only)***
$ bash thanos.sh 
```


