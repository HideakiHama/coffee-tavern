import fastapi as _fastapi
import services as _services, schemas as _schemas
import sqlalchemy.orm as _orm

app = _fastapi.FastAPI()
_services.create_database()

@app.post("/users/",response_models=_schemas.User)
def create_user(user:_schemas.UserCreate, db: _orm.Session=_fastapi.Depends(_services.get_db)):
