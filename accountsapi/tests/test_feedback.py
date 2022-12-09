# test_feedback.py
from fastapi.testclient import TestClient
from main import app
from authenticator import MyAuthenticator
from queries.EmployeeFeedback_queries import EmployeeFeedbackFormOut2
from routers.EmployeeFeedback import EmployeeFeedbackRepository
from datetime import date

client = TestClient(app)


def fake_get_current_user():
    return {}


feedback_out = EmployeeFeedbackFormOut2(
    id=0,
    employer_name="Aki",
    date="2022-12-12",
    description="Hello",
    account_id=1,
)


class fakeFeedbackRepository:
    def get_all_feedbacks(self):
        return feedback_out  # Change it


def test_read_feedback():
    app.dependency_overrides[MyAuthenticator] = fake_get_current_user
    app.dependency_overrides[EmployeeFeedbackRepository] = fakeFeedbackRepository
    response = client.get("/get_all_employeeFeedbacks")
    assert response.status_code == 200
    assert response.json() == feedback_out.dict()
