# from fastapi.testclient import TestClient
# from main import app
# from authenticator import MyAuthenticator
# from queries.EmployeeInfo_queries import EmployeeInfoOut, EmployeeInfoRepo


# client = TestClient(app)


# def test_get_employee_info_by_id():
#     # Arrange
#     def fake_get_current_user():
#         return {}
    
#     class fakeInfoRepository:
#         def get_one(self, account_id: 1):
#             return info_out
    
#     app.dependency_overrides[EmployeeInfoRepo] = fakeInfoRepository
#     app.dependency_overrides[MyAuthenticator] = fake_get_current_user
    
#     json = {
#         "full_name": "Lexey",
#         "career_title": "Test Career",
#         "location": "Test Locatiom",
#         "education": "Test Education",
#         "about": "Test About",
#         "pic_url": "TestURL",
#         "account_id": 1,
#     }

#     info_out = {
#         "full_name": "Lexey",
#         "career_title": "Test Career",
#         "location": "Test Locatiom",
#         "education": "Test Education",
#         "about": "Test About",
#         "pic_url": "TestURL",
#         "account_id": 1,
#     }
    
#     headers = {"Authorization": "Bearer z1232131"}
    
#     # Act
#     response = client.post("/users/{account_id}/create_employee_info", json=json, headers=headers)

#     # Assert
#     # assert response.status_code == 200
#     assert response.json() == info_out
    
#     # CLean up
#     app.dependency_overrides = {}