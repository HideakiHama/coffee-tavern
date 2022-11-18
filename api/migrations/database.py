import sqlalchemy as _sql
import sqlalchemy.ext.declarative as _declarative
import sqlalchemy.orm as _orm

SQLAlCHEMY_DATABASE_URL = "postgresql://coffee:tavern@db/coffee_tavern"
#sqlite:///./datebase.db

engine = _sql.create_engine(SQLAlCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
sessionLocal = _orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = _declarative.declarative_base()
