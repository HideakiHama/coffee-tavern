from main import app
from fastapi.testclient import TestClient
from token_auth import get_current_user
from queries.TagQueries import TagOut, TagRepository, TagIn, Tags
import pdb



client = TestClient(app)

def fake_get_current_user():
    return {}

# tag_in = TagIn(tag="barista") 
tag_out = TagOut(id=1, tag="bartender")

# class FakeTagCreateRepo:
#     def create(self):
#         pdb.set_trace()
#         return tag_in

class FakeTagRepository:
    def get_all(self):
        return tag_out
    

def test_read_main():
    app.dependency_overrides[get_current_user] = fake_get_current_user
    app.dependency_overrides[TagRepository] = FakeTagRepository
    response = client.get("/get_all_tags")
    assert response.status_code == 200
    assert response.json() == tag_out.dict()


# def test_create_tag():
#     app.dependency_overrides[get_current_user] = fake_get_current_user
#     app.dependency_overrides[TagRepository] = FakeTagCreateRepo
#     # pdb.set_trace()
#     response = client.post("/create_tag_form")
#     print(dir(response))
#     print(response)
#     assert response.status_code == 200
#     assert response.json() == tag_in.dict()

