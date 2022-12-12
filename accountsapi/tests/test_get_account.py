from fastapi.testclient import TestClient
from main import app
from queries.accounts import AccountOut, AccountRepo

client = TestClient(app)

test_account_out = AccountOut(
    id=1,
    user_name="curtis",
    email="curtis@email.com",
    role="Employer"
)


class TestAccountQueries:
    def get_all(self):
        return [test_account_out]


def test_get_all_accounts():
    app.dependency_overrides[AccountRepo] = TestAccountQueries
    response = client.get("/api/get_all_account")
    assert response.status_code == 200
    assert response.json() == [test_account_out.dict()]
