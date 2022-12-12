# Coffee Tavern

> This application is a linkedin but for the people in the service industry.

## Team:
>Person 1 - Hideaki Hama
>Person 2 - Curtis Cheung
>Person 3 - Lexey Olsen
>Person 4 - Christopher Shih

## Stack:

#### Front-End
    - React
    - Javascript

#### Back-End
    - Fast API
    - PostgreSQL
    - Python

#### Platform
    - Docker

## Unit-Test
> test_get_all_accounts.py -> Curtis Cheung
> test_get_account_by_id.py -> Lexey Olsen
> test_get_all_employee_feedbacks.py -> Christopher Shih
> test_get_all_employer_feedbacks.py -> Hideaki Hama

## Database Urls

**tags api db:**
 postgres://csbbehie:dmMYbL26VrUlKm6nT8E-qTo0XfR0qkWR@stampy.db.elephantsql.com/csbbehie

**accounts api db:**
postgres://qqurjzyt:4J9_f7CSKfSxuYsiCRmJTzXZkrpxsQo3@stampy.db.elephantsql.com/qqurjzyt

_**Run these commands in terminal to set up the application**_

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

## Application Design
<details><summary>Api Endpoints</summary>

<details><summary>Job Form</summary>

| Method | URL |
| ------ | ------ |
| POST | /create_form/ |
| GET | /get_all_form |
| GET | /get_all_form/{form_id} |
| PUT | /update_job_form/{id} |
| DELETE | /delete_job_form/{id} |

<details><summary>POST in/out</summary>

input:
```shell
{
  "employer": "string",
  "position": "string",
  "location": "string",
  "from_date": "2022-12-12",
  "to_date": "2022-12-12",
  "tag": "string",
  "description": "string"
}
```

output:
```shell
{
  "employer": "string",
  "position": "string",
  "location": "string",
  "from_date": "2022-12-12",
  "to_date": "2022-12-12",
  "tag": "string",
  "description": "string"
}
```
</details>
<details><summary>GET ALL out</summary>

output:
```shell
[
  {
    "id": 0,
    "employer": "string",
    "position": "string",
    "location": "string",
    "tag": "string",
    "description": "string",
    "account_id": 0
  }
]
```
</details>
<details><summary>GET BY ID in/out</summary>

inuput:
```shell
The id of the form you want to get
```

output:
```shell
{
  "id": 0,
  "employer": "string",
  "position": "string",
  "location": "string",
  "from_date": "2022-12-12",
  "to_date": "2022-12-12",
  "tag": "string",
  "description": "string",
  "account_id": 0
}
```
</details>
<details><summary>PUT in/out</summary>

inuput:
```shell
The id of the form you want to edit
&
{
  "employer": "string",
  "position": "string",
  "location": "string",
  "from_date": "2022-12-12",
  "to_date": "2022-12-12",
  "tag": "string",
  "description": "string"
}
```

output:
```shell
{
  "employer": "string",
  "position": "string",
  "location": "string",
  "from_date": "2022-12-12",
  "to_date": "2022-12-12",
  "tag": "string",
  "description": "string"
}
```
</details>
<details><summary>DELETE in/out</summary>

input:
```shell
The id of the form you want to delete
```

output:
```shell
true or false
```
</details>
</details>

<details><summary>Apply</summary>

| Method | URL |
| ------ | ------ |
| POST | /apply/{employer_id} |
| GET | /get_applicants |
| DELETE | /delete_application/{id} |

<details><summary>POST in/out</summary>

input:
```shell
The id of the employer you want to send your application to
```

output:
```shell
{
  "id": 0,
  "full_name": "string",
  "education": "string",
  "employer_id": 0,
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```

</details>
<details><summary>GET out</summary>

output:
```shell
[
  {
    "id": 0,
    "full_name": "string",
    "education": "string",
    "employer_id": 0,
    "account_id": {
      "id": 0,
      "user_name": "string",
      "email": "string",
      "hashed_password": "string",
      "role": "string"
    }
  }
]
```

</details>
<details><summary>DELETE in/out</summary>

input:
```shell
The id of the application you want to delete
```

output:
```shell
true or false
```
</details>
</details>

<details><summary>Employer Feedback Form</summary>

| Method | URL |
| ------ | ------ |
| POST | /employer-feedback-form/{account_id} |
| GET | /employer-feedback-form/{EmployerFeedback_id} |
| PUT | /employer-feedback-form/{EmployerFeedback_id} |
| DELETE | /employer-feedback-form/{EmployerFeedback_id} |
| GET | /employer-feedbacks/{account_id} |
| GET | /get_all_employerFeedbacks |

<details><summary>POST in/out</summary>

input:
```shell
{
  "employee_name": "string",
  "date": "2022-12-12",
  "description": "string"
}
```

output:
```shell
{
  "id": 0,
  "employee_name": "string",
  "date": "2022-12-12",
  "description": "string",
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```
</details>
<details><summary>GET one employer feedback form in/out</summary>

input:
```shell
The id of the form you want to get
```

output:
```shell
{
  "id": 0,
  "employee_name": "string",
  "date": "2022-12-12",
  "description": "string",
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```
</details>
<details><summary>PUT in/out</summary>

input:
```shell
The id of the feedback you want to edit
&
{
  "employee_name": "string",
  "date": "2022-12-12",
  "description": "string"
}
```

output:
```shell
{
  "id": 0,
  "employee_name": "string",
  "date": "2022-12-12",
  "description": "string",
  "account_id": 0
}
```
</details>
<details><summary>DELETE in/out</summary>

input:
```shell
The id of the feeback you want to delete
```

output:
```shell
true or false
```
</details>
<details><summary>GET all feebacks for employee by id in/out</summary>

input:
```shell
The id of the employee you want to get all the feebacks for
```

output:
```shell
[
  {
    "id": 0,
    "employee_name": "string",
    "date": "2022-12-12",
    "description": "string",
    "account_id": 0
  }
]
```
</details>
<details><summary>GET all out</summary>

output:
```shell
[
  {
    "id": 0,
    "employee_name": "string",
    "date": "2022-12-12",
    "description": "string",
    "account_id": 0
  }
]
```
</details>
</details>


<details><summary>Employee Feedback Form</summary>

| Method | URL |
| ------ | ------ |
| POST | /employee-feedback-form/{account_id} |
| GET | /employee-feedback-form/{EmployeeFeedback_id} |
| PUT | /employee-feedback-form/{EmployeeFeedback_id} |
| DELETE | /employee-feedback-form/{EmployeeFeedback_id} |
| GET | /employee-feedbacks/{account_id} |
| GET | /get_all_employeeFeedbacks |

<details><summary>POST in/out</summary>

input:
```shell
{
  "employer_name": "string",
  "date": "2022-12-12",
  "description": "string"
}
```

output:
```shell
{
  "id": 0,
  "employer_name": "string",
  "date": "2022-12-12",
  "description": "string",
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```
</details>
<details><summary>GET one employee feedback form in/out</summary>

input:
```shell
The id of the form you want to get
```

output:
```shell
{
  "id": 0,
  "employer_name": "string",
  "date": "2022-12-12",
  "description": "string",
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```
</details>
<details><summary>PUT in/out</summary>

input:
```shell
The id of the feedback you want to edit
&
{
  "employer_name": "string",
  "date": "2022-12-12",
  "description": "string"
}
```

output:
```shell
[
  {
    "id": 0,
    "employee_name": "string",
    "date": "2022-12-12",
    "description": "string",
    "account_id": 0
  }
]
```
</details>
<details><summary>DELETE in/out</summary>

input:
```shell
The id of the feeback you want to delete
```

output:
```shell
true or false
```
</details>
<details><summary>GET all feebacks for employer by id in/out</summary>

input:
```shell
The id of the employer you want to get all the feebacks for
```

output:
```shell
[
  {
    "id": 0,
    "employer_name": "string",
    "date": "2022-12-12",
    "description": "string",
    "account_id": 0
  }
]
```
</details>
<details><summary>GET all out</summary>

output:
```shell
[
  {
    "id": 0,
    "employer_name": "string",
    "date": "2022-12-12",
    "description": "string",
    "account_id": 0
  }
]
```
</details>
</details>

<details><summary>User Info</summary>

| Method | URL |
| ------ | ------ |
| POST | /users/{account_id}/create_employee_info |
| GET | /users/{account_id}/get_employee_info |
| PUT | /users/{account_id}/update_employee_info |
| GET | /get_all_employee_profile |
| POST | /users/{account_id}/create_employer_info |
| GET | /users/{account_id}/get_employer_info |
| PUT | /users/{account_id}/update_employer_info |
| GET | /get_all_employer_profile |

<details><summary>POST in/out</summary>

input:
```shell
{
  "full_name": "string",
  "career_title": "string",
  "location": "string",
  "education": "string",
  "about": "string",
  "pic_url": "string"
}
```

output:
```shell
{
  "full_name": "string",
  "career_title": "string",
  "location": "string",
  "education": "string",
  "about": "string",
  "pic_url": "string",
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```

</details>
<details><summary>GET employee info by id in/out</summary>

input:
```shell
The id for the account you want to get info for
```

output:
```shell
{
  "full_name": "string",
  "career_title": "string",
  "location": "string",
  "education": "string",
  "about": "string",
  "pic_url": "string",
  "account_id": 0
}
```
</details>
<details><summary>PUT employee in/out</summary>

input:
```shell
{
  "full_name": "string",
  "career_title": "string",
  "location": "string",
  "education": "string",
  "about": "string",
  "pic_url": "string"
}
```

output:
```shell
{
  "full_name": "string",
  "career_title": "string",
  "location": "string",
  "education": "string",
  "about": "string",
  "pic_url": "string",
  "account_id": 0
}
```
</details>
<details><summary>GET all employee infos out</summary>

output:
```shell
[
  {
    "full_name": "string",
    "career_title": "string",
    "location": "string",
    "education": "string",
    "about": "string",
    "pic_url": "string",
    "account_id": 0
  }
]
```

</details>
<details><summary>POST in/out</summary>

input:
```shell
{
  "company_name": "string",
  "job_type": "string",
  "location": "string",
  "about": "string",
  "pic_url": "string"
}
```

output:
```shell
{
  "company_name": "string",
  "job_type": "string",
  "location": "string",
  "about": "string",
  "pic_url": "string",
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```

</details>
<details><summary>GET employee info by id in/out</summary>

input:
```shell
The id for the account you want to get info for
```

output:
```shell
{
  "company_name": "string",
  "job_type": "string",
  "location": "string",
  "about": "string",
  "pic_url": "string",
  "account_id": {
    "id": 0,
    "user_name": "string",
    "email": "string",
    "hashed_password": "string",
    "role": "string"
  }
}
```
</details>
<details><summary>PUT employer in/out</summary>

input:
```shell
{
  "company_name": "string",
  "job_type": "string",
  "location": "string",
  "about": "string",
  "pic_url": "string"
}
```

output:
```shell
{
  "company_name": "string",
  "job_type": "string",
  "location": "string",
  "about": "string",
  "pic_url": "string",
  "account_id": 0
}
```
</details>
<details><summary>GET all employer infos out</summary>

output:
```shell
[
  {
    "company_name": "string",
    "job_type": "string",
    "location": "string",
    "about": "string",
    "pic_url": "string",
    "account_id": 0
  }
]
```

</details>
</details>



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

</details>

- Model 2 - Employee Form - Employee form has 5 properties
    1) id - SERIAL - PRIMARY KEY - NOT NULL
    2) account_id - INT - REFERENCE - accounts(id)
    3) employee_name - VARCHAR(max length of 255)
    4) date - VARCHAR(max lenght of 10) - NOT NULL,
    5) description - TEXT