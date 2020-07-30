from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Category
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

# configure Session class with desired options
Session = sessionmaker()

# later, we create the engine

engine = create_engine(DATABASE_URI)

# associate it with our custom Session class
Session.configure(bind=engine)


@contextmanager
def session_scope():
    """Provide a transactional scope around a series of operations."""
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()


def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


# def load_yaml():
#     with session_scope() as s:
#         for data in yaml.load_all(open('categories.yaml')):
#             category = Category(**data)
#             s.add(category)


if __name__ == '__main__':
    # recreate_database()
    # add_data()
    category = Category(
            name='Test Category',
            description='Testing database',
            parent_id=None
    )
    # try:
    #     s = Session()
    #     s.add(category)
    #     s.commit()
    #     print(s.query(Category).first())
    # except Exception as e:
    #     print(e)
    
    with session_scope() as session:
        parent = session.query(Category).first()
        category.parent_id = parent.id
        session.add(category)
        session.commit()