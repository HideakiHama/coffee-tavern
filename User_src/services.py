import database as _database

def create_database():
    return _database.Base.metadata.create_all(bind=_database.engine) # this creates our database

def get_db():
    db = _database.SessionLocal()
    try:
        yield db
    finally:
        db.close()
