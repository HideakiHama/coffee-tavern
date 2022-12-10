# test_feedback.py
from fastapi.testclient import TestClient
from main import app
from authenticator import MyAuthenticator
from queries.EmployerFeedback_queries import EmployerFeedbackFormOut2
from routers.EmployerFeedback import EmployerFeedbackRepository


client = TestClient(app)


def fake_get_current_user():
    return {}


feedback_out = EmployerFeedbackFormOut2(
    id=0,
    employee_name="Curtis",
    date="2022-12-09T21:58:51.572Z",
    description="Great Worker, never stops. Inspirational",
    account_id=1,
)


class fakeFeedbackRepository:
    def get_all_feedbacks(self):
        return feedback_out


def test_read_feedback():
    app.dependency_overrides[MyAuthenticator] = fake_get_current_user
    app.dependency_overrides[EmployerFeedbackRepository] = fakeFeedbackRepository
    response = client.get("/get_all_employerFeedbacks")
    assert response.status_code == 200
    assert response.json() == feedback_out.dict()
