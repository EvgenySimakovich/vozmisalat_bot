from database.database import get_session
from database.tables import User


@get_session
async def get_user(telegram_id: int, session):
    user = session.query(User).filter_by(telegram_id=telegram_id).one_or_none()
    return user


@get_session
async def get_users(session):
    users = session.query(User).all()
    return users


@get_session
async def add_user(telegram_id: int, username: str, session) -> None:
    user_data = {
        'telegram_id': telegram_id,
        'username': username,
    }
    new_user = User(**user_data)
    session.add(new_user)
    session.commit()


def generate_promo():
    pass


async def add_promo():
    pass


async def get_promo():
    pass
