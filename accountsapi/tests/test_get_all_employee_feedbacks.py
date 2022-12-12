from fastapi.testclient import TestClient
from main import app
from queries.EmployeeFeedback_queries import EmployeeFeedbackFormOut2
from routers.EmployeeFeedback import EmployeeFeedbackRepository
from fastapi import status

client = TestClient(app)


feedback_out = EmployeeFeedbackFormOut2(
    id=2,
    employer_name="Aki",
    date="2021-03-05",
    description="Hello",
    account_id=1,
)


class fakeFeedbackRepository:
    def get_all_feedbacks(self):
        return feedback_out


def test_read_feedback():
    app.dependency_overrides[EmployeeFeedbackRepository] = fakeFeedbackRepository
    response = client.get("/get_all_employeeFeedbacks")
    assert response.status_code == status.HTTP_200_OK
    assert response.json() == feedback_out.dict()
