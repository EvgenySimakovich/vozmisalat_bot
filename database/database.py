from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.tables import Base

DATABASE_NAME = 'vozmisalat_bot.db'

engine = create_engine(
    url=f'sqlite:///{DATABASE_NAME}',
    echo=True
)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


def create_db():
    Base.metadata.create_all(engine)


def get_session(query_func):
    def wrapper(*args, **kwargs):
        session = SessionLocal()
        query_result = query_func(session=session, *args, **kwargs)
        try:
            return query_result
        finally:
            session.close()

    return wrapper
