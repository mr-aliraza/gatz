from crud import Session
from models import Category

session = Session()

categories = session.query(Category).all()

for category in categories:
    description = input(f"Description for '{category.name}': $")
    category.description = description
    session.add(category)

session.commit()
session.close()