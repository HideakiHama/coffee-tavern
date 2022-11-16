### Log in

* Endpoint path: /token
* Endpoint method: POST

* Request shape (form):
  * username: string
  * password: string

* Response: Account information and a token
* Response shape (JSON):
    ```json
    {
      "account": {
        user_name: "user_name"
      },
      "token": string
    }
    ```
### Log out

* Endpoint path: /token
* Endpoint method: DELETE

* Headers:
  * Authorization: Bearer token

* Response: Always true
* Response shape (JSON):
    ```json
    true
    ```

### SignUp

* Endpoint path: /singup
* Endpoint method: POST

* Request shape(form):
    * first_name: string
    * last_name: string
    * user_name: string
    * password: string
    * email: string
    * status: string

* Response: Account information
* Response shape (JSON):
    ```json
    {
      "account": {
        first_name: "first_name",
        last_name: "last_name",
        user_name: "user_name",
        password: "password",
        email: "email",
        status: "status"
      }
    }
    ```

### List of Job Posting

* Endpoint path: /joblistview
* Endpoint method: GET

* Response: List of Job Posting
* Response shape (JSON):
    ```json
    {
      "Jobs": {
        id: "id",
        job_name: "job_name",
        employer: "employer",
        location: "location",
        tags: "tags"
      }
    }
    ```
### Job Description

* Endpoint path: /jobdescription/{id}
* Endpoint method: GET

* Response: Job Description
* Response shape (JSON):
    ```json
    {
      "Jobs": {
        id: "id",
        job_name: "job_name",
        employer: "employer",
        location: "location",
        tags: "tags",
        description: "description"
      }
    }
    ```
### Create Job Posting

* Endpoint path: /jobpost
* Endpoint method: POST

* Request shape (form):
  * position: string
  * location: string
  * from_date: date
  * to_date: date
  * tags: string
  * description: string

* Response: Job Description
* Response shape (JSON):
    ```json
    {
      "Jobs": {
        id: "id",
        name: "name",
        employer: "employer", <- this is not in the signup form since we can pull the employer name from who is posting
        location: "location",
        tags: "tags",
        description: "description"
      }
    }
    ```

### Employer Feedback Form

* Endpoint path: /employerfeedbackform/
* Endpoint method: POST

* Response: Employer Feedback of Employee
* Response shape (JSON):
    ```json
    {
      "FeedBack of Employee": {
        employee_name: "employee_name",
        description: "description"
      }
    }
    ```

### Employee Feedback Form

* Endpoint path: /employeefeedbackform/
* Endpoint method: POST

* Response: Employee Feedback of Employer
* Response shape (JSON):
    ```json
    {
      "FeedBack of Employee": {
        employer_name: "employer_name",
        description: "description"
      }
    }
    ```
### Delete Job Posting

* Endpoint path: /jobdescription/{id}
* Endpoint method:  

* Headers:
  * Authorization: Bearer token

    (Specific Employer who made the job post)

* Response: Delete specific job post
* Response shape (JSON):
    ```json
    true
    ```
  (Return True if delete was successful)


 ### Update/Edit Job Posting

* Endpoint path: /jobdescription/{id}
* Endpoint method: PUT

* Headers:
  * Authorization: Bearer token

    (Specific Employer who made the job post)

* Response: Update or Edit Job Description
* Response shape (JSON):
    ```json
    {
      "Jobs": {
        id: "id",
        job_name: "job_name",
        employer: "employer",
        location: "location",
        tags: "tags",
        description: "description"
      }
    }
