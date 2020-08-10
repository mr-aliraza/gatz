from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Attribute, AttributeOption
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import json
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm.exc import NoResultFound
import status
from sqlalchemy.sql.expression import func

import sys

sys.path.append("/home/ali/gatz")


from services.protos.attribute import attribute_pb2, attribute_pb2_grpc

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
#         for data in yaml.load_all(open('attributes.yaml')):
#             attribute = Attribute(**data)
#             s.add(attribute)


def get_attribute(id):
    response = attribute_pb2.Attribute(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute not found!")
    try:
        with session_scope() as session:
            try:
                attribute = session.query(Attribute).filter(Attribute.id==id, Attribute.is_deleted==False).first()
            except DataError:
                response = attribute_pb2.Attribute(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute not found!")
                session.commit
                return response
            if attribute:
                response = attribute_pb2.Attribute(id=str(attribute.id), name=attribute.name, description=attribute.description)
            session.commit()
    except Exception as e:
        print(e)
        pass
    return response


def update_attribute(id, name, description, user_id):
    name = name.title()
    response = attribute_pb2.Attribute(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute not found!")
    try:
        with session_scope() as session:
            try:
                attribute = session.query(Attribute).filter(Attribute.id == id, Attribute.is_deleted==False).first()
            except DataError:
                response = attribute_pb2.Attribute(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute not found!")
                session.commit
                return response
            if attribute:
                attribute.name = name
                attribute.description = description
                attribute.updated_at = datetime.now()
                attribute.updated_by = user_id
                response = attribute_pb2.Attribute(result="success", status=status.STATUS_200_OK, message="Attribute updated successfully!")
            session.commit()
    except IntegrityError:
        response.message = "Attribute already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def delete_attribute(id, user_id):
    response = attribute_pb2.Attribute(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute not found!")
    try:
        with session_scope() as session:
            try:
                attribute = session.query(Attribute).filter(Attribute.id == id, Attribute.is_deleted==False).first()
            except DataError:
                response = attribute_pb2.Attribute(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute not found!")
                session.commit
                return response
            if attribute:
                options = session.query(AttributeOption).filter(AttributeOption.attribute_id == id, AttributeOption.is_deleted==False).first()
                if options:
                    response.message = "Attribute have options cannot be deleted!"
                    response.status = status.STATUS_403_FORBIDDEN
                else:
                    attribute.deleted_at = datetime.now()
                    attribute.deleted_by = user_id
                    attribute.is_deleted = True
                    response.message = "Attribute deleted successfully!"
                    response.result = "success"
                    response.status = status.STATUS_204_NO_CONTENT
            session.commit()
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def create_attribute(name, description, user_id):
    name = name.title()
    attribute = Attribute(
        name=name,
        description=description,
        created_by=user_id
    )
    response = attribute_pb2.Attribute(result="failed")
    try:
        with session_scope() as session:
            session.add(attribute)
            response = attribute_pb2.Attribute(result="success", status=status.STATUS_201_CREATED, message="Attribute created successfully!")
            session.commit()
    except IntegrityError as e:
        with session_scope() as session:
            try:
                attribute = session.query(Attribute).filter(Attribute.is_deleted==True, Attribute.name.ilike(name)).first()
            except DataError:
                attribute = None
            if attribute:
                attribute.name = name
                attribute.description = description
                attribute.created_at = datetime.now()
                attribute.created_by = user_id
                attribute.updated_at = None
                attribute.updated_by = None
                attribute.is_deleted = False
                attribute.deleted_at = None
                attribute.deleted_by = None
                session.commit()
                response = attribute_pb2.Attribute(result="success", status=status.STATUS_201_CREATED, message="Attribute created successfully!")
                return response
            else:
                session.commit()
        response.message = "Attribute already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def read_attribute_database():
    attributes_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        attributes = session.query(Attribute).filter(Attribute.is_deleted==False).all()
        for item in attributes:
            attribute = attribute_pb2.Attribute(id=str(item.id), name=item.name, description=item.description)
            attributes_list.append(attribute)
    return attributes_list


def get_option(id):
    response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute Option not found!")
    try:
        with session_scope() as session:
            try:
                option = session.query(AttributeOption).filter(AttributeOption.id==id, AttributeOption.is_deleted==False).first()
            except DataError:
                response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute Option not found!")
                session.commit
                return response
            if option:
                response = attribute_pb2.AttributeOption(id=str(option.id), name=option.name, description=option.description,
                                                   attribute_id=str(option.attribute_id), attribute_name=option.attribute.name)
            session.commit()
    except Exception as e:
        print(e)
        pass
    return response


def update_option(id, name, description, attribute_id, user_id):
    name = name.title()
    response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute Option not found!")
    try:
        with session_scope() as session:
            try:
                option = session.query(AttributeOption).filter(AttributeOption.id == id, AttributeOption.is_deleted==False).first()
            except DataError:
                response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute Option not found!")
                session.commit
                return response
            if option:
                if attribute_id:
                    try:
                        attribute = session.query(Attribute).filter(Attribute.id == attribute_id, Attribute.is_deleted==False).first()
                    except DataError:
                        response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute not found!")
                        session.commit
                        return response
                    if attribute:
                        option.attribute_id = attribute.id
                    else:
                       response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute not found!")
                       session.commit
                       return response
                option.name = name
                option.description = description
                option.updated_at = datetime.now()
                option.updated_by = user_id
                response = attribute_pb2.AttributeOption(result="success", status=status.STATUS_200_OK, message="Attribute Option updated successfully!")
            session.commit()
    except IntegrityError:
        response.message = "Attribute Option already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def delete_option(id, user_id):
    response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute Option not found!")
    try:
        with session_scope() as session:
            try:
                option = session.query(AttributeOption).filter(AttributeOption.id == id, AttributeOption.is_deleted==False).first()
            except DataError:
                response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute not found!")
                session.commit
                return response
            if option:
                option.deleted_at = datetime.now()
                option.deleted_by = user_id
                option.is_deleted = True
                response.message = "Attribute Option deleted successfully!"
                response.result = "success"
                response.status = status.STATUS_204_NO_CONTENT
            session.commit()
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def create_option(name, description, attribute_id, user_id):
    name = name.title()
    option = AttributeOption(
        name=name,
        description=description,
        created_by=user_id
    )
    response = attribute_pb2.Attribute(result="failed")
    try:
        with session_scope() as session:
            if attribute_id:
                try:
                    attribute = session.query(Attribute).filter(Attribute.id == attribute_id, Attribute.is_deleted==False).first()
                    if attribute:
                        option.attribute_id = attribute.id
                    else:
                        response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute not found!")
                        session.commit
                        return response
                except DataError:
                    response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute not found!")
                    session.commit
                    return response
                session.add(option)
                response = attribute_pb2.AttributeOption(result="success", status=status.STATUS_201_CREATED, message="Attribute Option created successfully!")
            else:
                response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute is required!")
            session.commit()
    except IntegrityError as e:
        with session_scope() as session:
            try:
                option = session.query(AttributeOption).filter(AttributeOption.is_deleted==True, AttributeOption.name.ilike(name)).first()
            except DataError:
                option = None
            if option:
                if attribute_id:
                    attribute = session.query(Attribute).filter(Attribute.id == attribute_id, Attribute.is_deleted==False).first()
                    if attribute:
                        option.attribute_id = attribute.id
                    else:
                        response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Attribute not found!")
                        session.commit
                        return response
                else:
                    response = attribute_pb2.AttributeOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Attribute is required!")
                option.name = name
                option.description = description
                option.created_at = datetime.now()
                option.created_by = user_id
                option.updated_at = None
                option.updated_by = None
                option.is_deleted = False
                option.deleted_at = None
                option.deleted_by = None
                session.commit()
                response = attribute_pb2.Attribute(result="success", status=status.STATUS_201_CREATED, message="Attribute Option created successfully!")
                return response
            else:
                session.commit()
        response.message = "Attribute Option already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def read_options_database():
    options_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        options = session.query(AttributeOption).filter(AttributeOption.is_deleted==False).all()
        for item in options:
            option = attribute_pb2.AttributeOption(id=str(item.id), name=item.name, description=item.description,
                                                      attribute_id=str(item.attribute_id), attribute_name=item.attribute.name)
            options_list.append(option)
    return options_list


def read_attribute_options_database(id):
    options_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        try:
            options = session.query(AttributeOption).filter(AttributeOption.attribute_id==id, AttributeOption.is_deleted==False).all()
        except DataError:
            options = []
        for item in options:
            option = attribute_pb2.AttributeOption(id=str(item.id), name=item.name, description=item.description,
                                                      attribute_id=str(item.attribute_id), attribute_name=item.attribute.name)
            options_list.append(option)
    return options_list