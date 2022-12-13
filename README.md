# Coffee Tavern

> This application is a linkedin but for the people in the service industry. 
> Linkedin is a site primarily for people in the tech industry. But where is Linkedin for service employees and employers? 
> Our application's name is Coffee-Tavern, we are the answer to helping that barista or bartender find a quick job when the hours have been cut due to seasonal changes.
> Or for that store manager at a flower shop who is in need of a sales clerk, because its Valentine's day and will have no time training a new clerk.
> The communication is made via a employer making an account and creating a job post form. The employee will be able to look at that post through a board of jobs and send their information to the employer for an offer.

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

<!-- **tags api db:**
 postgres://csbbehie:dmMYbL26VrUlKm6nT8E-qTo0XfR0qkWR@stampy.db.elephantsql.com/csbbehie

**accounts api db:**
postgres://qqurjzyt:4J9_f7CSKfSxuYsiCRmJTzXZkrpxsQo3@stampy.db.elephantsql.com/qqurjzyt -->

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

<details><summary> GUI Map</summary>

![Alt text](Images/CT-home-page.png)
![Alt text](Images/CT-signup.png)
![Alt text](Images/CT-login.png)

**Employee Map**

![Alt text](Images/CT-employee-createinfo.png)
![Alt text](Images/CT-employee-profilepage.png)
![Alt text](Images/CT-employee-editinfo.png)
![Alt text](Images/CT-Board-of-jobs.png)
![Alt text](Images/CT-send-feedback-to-employee.png)
![Alt text](Images/CT-list-of-employees-feedbacks-to-employers.png)
![Alt text](Images/CT-list-of-employers.png)

**Employer Map**

![Alt text](Images/CT-employer-create-info.png)
![Alt text](Images/CT-employer-profile.png)
![Alt text](Images/CT-employer-edit-info.png)
![Alt text](Images/CT-employer-create-job-post.png)
![Alt text](Images/CT-employee-feedbacks-from-employer.png)
![Alt text](Images/CT-employer-send-feedback-to-employee.png)
![Alt text](Images/CT-list-of-employees.png)
![Alt text](Images/CT-employer-applicants.png)
![Alt text](Images/CT-tag-form.png)

</details>

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

input:
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

