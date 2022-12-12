from fastapi.testclient import TestClient
from main import app
from authenticator import MyAuthenticator
from queries.JobForm_queries import JobFormRepository, JobPostFormOut2, JobPostForm

client = TestClient(app)

test_get_all_form = JobPostForm(
    id: 1,
    employer: "Netflix",
    position: "L4",
    location: "Seattle",
    tag: "3",
    description: "fun place",
    account_id: 1
)

test_job_formOut = {
    "id": 1,
    "employer": "Apple",
    "position": "iphone team",
    "location": "Texas",
    "from_date": "2022-12-11",
    "to_date": "2022-12-11",
    "tag": "Full-Time",
    "description": "Only geniuses work here",
    "account_id": {
        "id": 1,
        "user_name": "bob",
        "email": "bob@gmail.com",
        "hashed_password": "$2b$12$HZZybt0TssMum31f2S3TdOAkfTY/0BvtCHMTj7zRFmNv3Y8O4rMti",
        "role": "Employer"
        }
    }


test_job_formIn = {
    "employer": "Apple",
    "position": "iphone team",
    "location": "Texas",
    "from_date": "2022-12-11",
    "to_date": "2022-12-11",
    "tag": "Full-Time",
    "description": "Only geniuses work here"
}

def get_fake_current_user():
    return {}



class JobFormRepo:
    def get_all(self):
        return [test_get_all_form]


def test_create_job_form():
    app.dependency_overrides[JobFormRepository] = JobFormRepo
    app.dependency_overrides[MyAuthenticator] = fake_get_current_user

    response = client.post("get_all_form")
    assert response.status_code == 200
    assert response.json() == [test_get_all_form.dict()]
