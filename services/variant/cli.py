from crud import Session
from models import Variant, Base
from config import DATABASE_URI
from sqlalchemy import create_engine

engine = create_engine(DATABASE_URI)

# session = Session()

# categories = session.query(Attribute).all()

# for category in categories:
#     description = input(f"Description for '{category.name}': $")
#     category.description = description
#     session.add(category)

# session.commit()
# session.close()

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

recreate_database()