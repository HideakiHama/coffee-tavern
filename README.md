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

# Unit-Test
> test_get_all_accounts.py -> Curtis Cheung
> test_get_account_by_id.py -> Lexey Olsen
> test_get_all_employee_feedbacks.py -> Christopher Shih
> test_get_all_employer_feedbacks.py -> Hideaki Hama

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
tags api db = postgres://mjlcehbq:68CQlz4J0QGLvquHOSHqQjs97X_vpuyS@arjuna.db.elephantsql.com/mjlcehbq
accounts api db = postgres://uuafgwdr:WDx2393zSgqxcFkuOJct-_98SI0zi5pF@arjuna.db.elephantsql.com/uuafgwdr

