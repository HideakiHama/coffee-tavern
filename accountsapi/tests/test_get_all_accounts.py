from fastapi.testclient import TestClient
from main import app
from queries.accounts import Account, AccountRepo

client = TestClient(app)

test_account = Account (
    id=1,
    user_name="lexey",
    email="lexey@email.com",
    hashed_password="123abc",
    role="Employee",
)

class TestAccountQueries:
    def getId(self, user_name="lexey"):
        return [test_account]


def test_get_all_accounts():
    app.dependency_overrides[AccountRepo] = TestAccountQueries
    response = client.get("/api/get_account/1")
    assert response.status_code == 200
    assert response.json() == [test_account.dict()]
