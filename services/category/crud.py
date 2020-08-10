from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Category
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import json
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm.exc import NoResultFound
import status
from sqlalchemy.sql.expression import func

import sys

sys.path.append("/home/ali/gatz")


from services.protos.category import category_pb2, category_pb2_grpc

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


def get_category(id):
    response = category_pb2.Category(result="failed", status=status.STATUS_404_NOT_FOUND, message="Category not found!")
    try:
        with session_scope() as session:
            try:
                category = session.query(Category).filter(Category.id==id, Category.is_deleted==False).first()
            except DataError:
                session.commit()
                response.message = "Category does not exist!"
                response.status = status.STATUS_404_NOT_FOUND
                return response
            if category:
                response = category_pb2.Category(id=str(category.id), name=category.name, description=category.description, parent_id=str(category.parent_id))
                if category.parent:
                    response.parent_name = category.parent.name
                else:
                    response.parent_name = "None"
            session.commit()
    except Exception as e:
        print(e)
        pass
    return response


def get_category_parents():
    categories_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        categories = session.query(Category).filter(Category.parent_id==None, Category.is_deleted==False).all()
        for item in categories:
            category = category_pb2.Category(id=str(item.id), name=item.name, description=item.description, parent_id=str(item.parent_id))
            if item.parent:
                category.parent_name = item.parent.name
            else:
                category.parent_name = "None"
            categories_list.append(category)
    return categories_list


def get_category_childs(id):
    categories_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        try:
            categories = session.query(Category).filter(Category.parent_id==id, Category.is_deleted==False).all()
        except DataError:
            categories = []
        for item in categories:
            category = category_pb2.Category(id=str(item.id), name=item.name, description=item.description, parent_id=str(item.parent_id))
            if item.parent:
                category.parent_name = item.parent.name
            else:
                category.parent_name = "None"
            categories_list.append(category)
    return categories_list


def update_category(id, name, description, parent_id, user_id):
    name = name.title()
    response = category_pb2.Category(result="failed", status=status.STATUS_404_NOT_FOUND, message="Category not found!")
    try:
        with session_scope() as session:
            try:
                category = session.query(Category).filter(Category.id == id, Category.is_deleted==False).first()
            except DataError:
                session.commit()
                response.message = "Category does not exist!"
                response.status = status.STATUS_404_NOT_FOUND
                return response
            if not category:
                return response
            elif parent_id:
                try:
                    parent = session.query(Category).filter(Category.is_deleted==False, Category.id==parent_id).first()
                except DataError:
                    session.commit()
                    response.message = "Category parent does not exist!"
                    response.status = status.STATUS_404_NOT_FOUND
                    return response
                if parent:
                    if parent.id == category.id:
                        response.message = "Category cannot be sub category of itself!"
                        response.status = status.STATUS_403_FORBIDDEN
                        return response
                    result = session.query(Category).filter(Category.id == id, Category.is_deleted==False) \
                        .update({"name": name, "description": description, "parent_id": parent.id, "updated_at": datetime.now(), "updated_by": user_id})
                    if result:
                        response = category_pb2.Category(result="success", status=status.STATUS_200_OK, message="Category updated successfully!")
                else:
                    session.commit()
                    response.message = "Category parent does not exist!"
                    return response
            else:
                result = session.query(Category).filter(Category.id == id, Category.is_deleted==False) \
                    .update({"name": name, "description": description, "updated_at": datetime.now(), "updated_by": user_id})
                if result:
                    response = category_pb2.Category(result="success", status=status.STATUS_200_OK, message="Category updated successfully!")
            session.commit()
    except IntegrityError:
        response.message = "Category already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def delete_category(id, user_id):
    response = category_pb2.Category(result="failed")
    try:
        with session_scope() as session:
            try:
                child = session.query(Category).filter(Category.parent_id == id, Category.is_deleted==False).first()
            except DataError:
                session.commit()
                response.message = "Category does not exist!"
                response.status = status.STATUS_404_NOT_FOUND
                return response
            if child:
                response.message = "Category have sub categories cannot be deleted!"
                response.status = status.STATUS_400_BAD_REQUEST
            else:
                try:
                    category = session.query(Category).filter(Category.id == id, Category.is_deleted==False).first()
                except DataError:
                    session.commit()
                    response.message = "Category does not exist!"
                    response.status = status.STATUS_404_NOT_FOUND
                    return response
                if category:
                    category.updated_at = None
                    category.deleted_at = datetime.now()
                    category.is_deleted = True
                    category.deleted_by = user_id
                    response.message = "Category deleted successfully!"
                    response.result = "success"
                    response.status = status.STATUS_204_NO_CONTENT
            session.commit()
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def create_category(parent_id, name, description, user_id):
    name = name.title()
    category = Category(
        name=name,
        description=description,
        created_by=user_id
    )
    response = category_pb2.Category(result="failed")
    try:
        with session_scope() as session:
            if parent_id:
                try:
                    parent = session.query(Category).filter(Category.is_deleted==False, Category.id==parent_id).first()
                    if parent:
                        category.parent_id = parent.id
                    else:
                        session.commit()
                        response.message = "Category parent does not exist!"
                        response.status = status.STATUS_404_NOT_FOUND
                        return response
                except DataError:
                    session.commit()
                    response.message = "Category parent does not exist!"
                    response.status = status.STATUS_404_NOT_FOUND
                    return response
            session.add(category)
            response = category_pb2.Category(result="success", status=status.STATUS_201_CREATED, message="Category created successfully!")
            session.commit()
    except IntegrityError as e:
        with session_scope() as session:
            try:
                category = session.query(Category).filter(Category.is_deleted==True, Category.name.ilike(name)).first()
            except DataError:
                category = None
            if category:
                category.name = name
                category.description = description
                category.created_at = datetime.now()
                category.created_by = user_id
                category.updated_at = None
                category.updated_by = None
                category.is_deleted = False
                category.deleted_at = None
                category.deleted_by = None
                if parent_id:
                    category.parent_id = parent_id
                else:
                    category.parent_id = None
                    # result = session.query(Category).filter(Category.is_deleted==True, Category.name.ilike(name)) \
                    #     .update({"name": name, "description": description, "created_at": datetime.now(), "created_by": user_id,
                    #             "updated_at": None, "updated_by": None, "parent_id": None,
                    #             "is_deleted": False, "deleted_at": None, "deleted_by": None})
                # if result:
                session.commit()
                response = category_pb2.Category(result="success", status=status.STATUS_201_CREATED, message="Category created successfully!")
                return response
                # else:
                #     session.commit()
                #     response.message = "Unable to create category!"
                #     response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
                #     return response
            else:
                session.commit()
        response.message = "Category already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def read_category_database():
    categories_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        categories = session.query(Category).filter(Category.is_deleted==False).all()
        for item in categories:
            category = category_pb2.Category(id=str(item.id), name=item.name, description=item.description, parent_id=str(item.parent_id))
            if item.parent:
                category.parent_name = item.parent.name
            else:
                category.parent_name = "None"
            categories_list.append(category)
    return categories_list