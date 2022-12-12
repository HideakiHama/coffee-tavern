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

# Stack

- HTML/CSS
- Python
- FastAPI
- JavaScript
- React
- PostgreSQL
- Bootstrap ---
- RESTful APIs
- Docker
- Microservices

# Design

## Employer/Employee Feedback
On top of the nav bar there are two section for feedback 'Create Feedback' and 'Past Feedback'
  ### 'Create Feedback'
- Let's talk about Create Feedback first. Assuming you already have created account for employer or employee go ahead and click on 'Create Feedback' at the top.
- Like what the name said this page are for user to create a feedback to employee or employer.
- There are three input field that user have to enter.  The employer or employee's name, date of the feedback, and the feedback that user is trying giving the feedback to.

### 'Past Feedback'
- Next after successful creation of feedback the website will redirect you to the homepage.
- Go ahead and click on 'Past Feedback'
- This is where you see the list of feedback that you sent to employer or employee in the past. It shows the employee or employers name (Depend on what role you signed up as, if your role are employer then you will see feedback to your past employee). A date of sending the feedback and the feedback description.
- There are also two buttons 'Edit feedback button' which will send you do edit page. 'Other Feedback" which will send you to page with all the feedback by others for the specific employee or employer.
- Lets take a look page for editing the feedback. Go ahead and press the 'Edit Feedback'
### 'Edit Feedback'
- This is the page where you can edit feedback for employer or employee.  You can edit section for name, date, and feedback description.
- There is delete button if you decided you wanted to delete the feedback.
- This page and the page to check 'Other feedback' has a back button that conveniently take you back to 'Past Feedback' Page.

## Employer/Employee Profiles
- This section are for user to check the profiles of other user who made an account on our website.
- Click on the 'Check Profile' To reroute to their profile.





# Port Information

  Account API: Port:8000
- URL -> http://localhost:8000/docs#/

  Tags API: Port:8100
- URL -> http://localhost:8100/docs#/

  React: Port 3000  (For checking the FrontEnd)
- URL -> http://localhost:3000/

        RESTful Employer Feedback
1. create_employer_feedback_form are function for:
- POST - Creating new employer feedback form
http://localhost:8000/employer-feedback-form/<account_id>
2. get_one_employer_feedback_form are function for:
- GET - Getting detail feedback from employer
http://localhost:8000/employer-feedback-form/<EmployerFeedback_id>
3. get_all_with_id are function for:
- GET - getting list of feedback from specific employers
http://localhost:8000/employer-feedbacks/<account_id>
4. get_all_employer_feedbacks are function for:
- GET - getting all the Employer Feedback regardless of who wrote it
http://localhost:8000/get_all_employerFeedbacks
5. Edit_Employer_Feedback are function for:
- PUT - Editing feedback
http://localhost:8000/employer-feedback-form/<EmployerFeedback_id>
6. Delete_Employer_Feedback are function for:
- DELETE - Deleting feedback
http://localhost:8000/employer-feedback-form/<EmployerFeedback_id>

        RESTful Employee Feedback
1. create_employee_feedback_form are function for:
- POST - Creating new employee feedback form
http://localhost:8000/employee-feedback-form/<account_id>
2. get_one_employee_feedback_form are function for:
- GET - Getting detail feedback from employee
http://localhost:8000/employee-feedback-form/<EmployeeFeedback_id>
3. get_all_with_id are function for:
- GET - getting list of feedback from specific employees
http://localhost:8000/employee-feedbacks/<account_id>
4. get_all_employee_feedbacks are function for:
- GET - getting all the Employee Feedback regardless of who wrote it
http://localhost:8000/get_all_employeeFeedbacks
5. Edit_Employee_Feedback are function for:
- PUT - Editing feedback
http://localhost:8000/employee-feedback-form/<EmployeeFeedback_id>
6. Delete_Employee_Feedback are function for:
- DELETE - Deleting feedback
http://localhost:8000/employee-feedback-form/<EmployeeFeedback_id>


## Accounts microservices

- Model 1 - Employer Form - Employer form has 5 properties
    1) id - SERIAL - PRIMARY KEY - NOT NULL
    2) account_id - INT - REFERENCE - accounts(id)
    3) employee_name - VARCHAR(max length of 255)
    4) date - VARCHAR(max length of 10)- NOT NULL,
    5) description - TEXT

- Model 2 - Employee Form - Employee form has 5 properties
    1) id - SERIAL - PRIMARY KEY - NOT NULL
    2) account_id - INT - REFERENCE - accounts(id)
    3) employee_name - VARCHAR(max length of 255)
    4) date - VARCHAR(max lenght of 10) - NOT NULL,
    5) description - TEXT