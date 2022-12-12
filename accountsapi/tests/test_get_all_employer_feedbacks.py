from fastapi.testclient import TestClient
from main import app
from queries.EmployerFeedback_queries import EmployerFeedbackFormOut2, EmployerFeedbackRepository

client = TestClient(app)

test_employer_feedback = EmployerFeedbackFormOut2(
    id=1,
    employee_name="Viego",
    date="2013-11-12",
    description="He was great",
    account_id=2,
)


class TestEmployerFeedbackRepo:
    def get_all_feedbacks(self):
        return [test_employer_feedback]


def test_get_all_employer_feedbacks():
    app.dependency_overrides[EmployerFeedbackRepository] = TestEmployerFeedbackRepo
    response = client.get('/get_all_employerFeedbacks')
    assert response.status_code == 200
    assert response.json() == [test_employer_feedback]
