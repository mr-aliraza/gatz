from datetime import datetime

from sqlalchemy import create_engine
from config import DATABASE_URI
from models import Base, Variant, VariantOption
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
import json
from sqlalchemy.exc import IntegrityError, DataError
from sqlalchemy.orm.exc import NoResultFound
import status
from sqlalchemy.sql.expression import func

import sys

sys.path.append("/home/ali/gatz")


from services.protos.variant import variant_pb2, variant_pb2_grpc

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
#         for data in yaml.load_all(open('variants.yaml')):
#             variant = Variant(**data)
#             s.add(variant)


def get_variant(id):
    response = variant_pb2.Variant(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant not found!")
    try:
        with session_scope() as session:
            try:
                variant = session.query(Variant).filter(Variant.id==id, Variant.is_deleted==False).first()
            except DataError:
                response = variant_pb2.Variant(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant not found!")
                session.commit
                return response
            if variant:
                response = variant_pb2.Variant(id=str(variant.id), name=variant.name, description=variant.description)
            session.commit()
    except Exception as e:
        print(e)
        pass
    return response


def update_variant(id, name, description, user_id):
    name = name.title()
    response = variant_pb2.Variant(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant not found!")
    try:
        with session_scope() as session:
            try:
                variant = session.query(Variant).filter(Variant.id == id, Variant.is_deleted==False).first()
            except DataError:
                response = variant_pb2.Variant(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant not found!")
                session.commit
                return response
            if variant:
                variant.name = name
                variant.description = description
                variant.updated_at = datetime.now()
                variant.updated_by = user_id
                response = variant_pb2.Variant(result="success", status=status.STATUS_200_OK, message="Variant updated successfully!")
            session.commit()
    except IntegrityError:
        response.message = "Variant already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def delete_variant(id, user_id):
    response = variant_pb2.Variant(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant not found!")
    try:
        with session_scope() as session:
            try:
                variant = session.query(Variant).filter(Variant.id == id, Variant.is_deleted==False).first()
            except DataError:
                response = variant_pb2.Variant(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant not found!")
                session.commit
                return response
            if variant:
                options = session.query(VariantOption).filter(VariantOption.variant_id == id, VariantOption.is_deleted==False).first()
                if options:
                    response.message = "Variant have options cannot be deleted!"
                    response.status = status.STATUS_403_FORBIDDEN
                else:
                    variant.deleted_at = datetime.now()
                    variant.deleted_by = user_id
                    variant.is_deleted = True
                    response.message = "Variant deleted successfully!"
                    response.result = "success"
                    response.status = status.STATUS_204_NO_CONTENT
            session.commit()
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def create_variant(name, description, user_id):
    name = name.title()
    variant = Variant(
        name=name,
        description=description,
        created_by=user_id
    )
    response = variant_pb2.Variant(result="failed")
    try:
        with session_scope() as session:
            session.add(variant)
            response = variant_pb2.Variant(result="success", status=status.STATUS_201_CREATED, message="Variant created successfully!")
            session.commit()
    except IntegrityError as e:
        with session_scope() as session:
            try:
                variant = session.query(Variant).filter(Variant.is_deleted==True, Variant.name.ilike(name)).first()
            except DataError:
                variant = None
            if variant:
                variant.name = name
                variant.description = description
                variant.created_at = datetime.now()
                variant.created_by = user_id
                variant.updated_at = None
                variant.updated_by = None
                variant.is_deleted = False
                variant.deleted_at = None
                variant.deleted_by = None
                session.commit()
                response = variant_pb2.Variant(result="success", status=status.STATUS_201_CREATED, message="Variant created successfully!")
                return response
            else:
                session.commit()
        response.message = "Variant already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def read_variant_database():
    variants_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        variants = session.query(Variant).filter(Variant.is_deleted==False).all()
        for item in variants:
            variant = variant_pb2.Variant(id=str(item.id), name=item.name, description=item.description)
            variants_list.append(variant)
    return variants_list


def get_option(id):
    response = variant_pb2.VariantOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant Option not found!")
    try:
        with session_scope() as session:
            try:
                option = session.query(VariantOption).filter(VariantOption.id==id, VariantOption.is_deleted==False).first()
            except DataError:
                response = variant_pb2.VariantOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant Option not found!")
                session.commit
                return response
            if option:
                response = variant_pb2.VariantOption(id=str(option.id), name=option.name, description=option.description,
                                                   variant_id=str(option.variant_id), variant_name=option.variant.name)
            session.commit()
    except Exception as e:
        print(e)
        pass
    return response


def update_option(id, name, description, variant_id, user_id):
    name = name.title()
    response = variant_pb2.VariantOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant Option not found!")
    try:
        with session_scope() as session:
            try:
                option = session.query(VariantOption).filter(VariantOption.id == id, VariantOption.is_deleted==False).first()
            except DataError:
                response = variant_pb2.VariantOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant Option not found!")
                session.commit
                return response
            if option:
                if variant_id:
                    try:
                        variant = session.query(Variant).filter(Variant.id == variant_id, Variant.is_deleted==False).first()
                    except DataError:
                        response = variant_pb2.VariantOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant not found!")
                        session.commit
                        return response
                    if variant:
                        option.variant_id = variant.id
                    else:
                       response = variant_pb2.VariantOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant not found!")
                       session.commit
                       return response
                option.name = name
                option.description = description
                option.updated_at = datetime.now()
                option.updated_by = user_id
                response = variant_pb2.VariantOption(result="success", status=status.STATUS_200_OK, message="Variant Option updated successfully!")
            session.commit()
    except IntegrityError:
        response.message = "Variant Option already exists with same name!"
        response.status = status.STATUS_403_FORBIDDEN
        return response
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def delete_option(id, user_id):
    response = variant_pb2.VariantOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant Option not found!")
    try:
        with session_scope() as session:
            try:
                option = session.query(VariantOption).filter(VariantOption.id == id, VariantOption.is_deleted==False).first()
            except DataError:
                response = variant_pb2.VariantOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant not found!")
                session.commit
                return response
            if option:
                option.deleted_at = datetime.now()
                option.deleted_by = user_id
                option.is_deleted = True
                response.message = "Variant Option deleted successfully!"
                response.result = "success"
                response.status = status.STATUS_204_NO_CONTENT
            session.commit()
    except Exception as e:
        print(e)
        response.message = "Unexpected error occurred!"
        response.status = status.STATUS_500_INTERNAL_SERVER_ERROR
        pass
    return response


def create_option(name, description, variant_id, user_id):
    name = name.title()
    option = VariantOption(
        name=name,
        description=description,
        created_by=user_id
    )
    response = variant_pb2.Variant(result="failed")
    try:
        with session_scope() as session:
            if variant_id:
                try:
                    variant = session.query(Variant).filter(Variant.id == variant_id, Variant.is_deleted==False).first()
                    if variant:
                        option.variant_id = variant.id
                    else:
                        response = variant_pb2.VariantOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant not found!")
                        session.commit
                        return response
                except DataError:
                    response = variant_pb2.VariantOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant not found!")
                    session.commit
                    return response
                session.add(option)
                response = variant_pb2.VariantOption(result="success", status=status.STATUS_201_CREATED, message="Variant Option created successfully!")
            else:
                response = variant_pb2.VariantOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant is required!")
            session.commit()
    except IntegrityError as e:
        with session_scope() as session:
            try:
                option = session.query(VariantOption).filter(VariantOption.is_deleted==True, VariantOption.name.ilike(name)).first()
            except DataError:
                option = None
            if option:
                if variant_id:
                    variant = session.query(Variant).filter(Variant.id == variant_id, Variant.is_deleted==False).first()
                    if variant:
                        option.variant_id = variant.id
                    else:
                        response = variant_pb2.VariantOption(result="failed", status=status.STATUS_404_NOT_FOUND, message="Variant not found!")
                        session.commit
                        return response
                else:
                    response = variant_pb2.VariantOption(result="failed", status=status.STATUS_400_BAD_REQUEST, message="Variant is required!")
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
                response = variant_pb2.Variant(result="success", status=status.STATUS_201_CREATED, message="Variant Option created successfully!")
                return response
            else:
                session.commit()
        response.message = "Variant Option already exists with same name!"
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
        options = session.query(VariantOption).filter(VariantOption.is_deleted==False).all()
        for item in options:
            option = variant_pb2.VariantOption(id=str(item.id), name=item.name, description=item.description,
                                                      variant_id=str(item.variant_id), variant_name=item.variant.name)
            options_list.append(option)
    return options_list


def read_variant_options_database(id):
    options_list = []
    """Reads the route guide database.
        Returns:
        The full contents of the route guide database as a sequence of
        route_guide_pb2.Features.
    """
    with session_scope() as session:
        try:
            options = session.query(VariantOption).filter(VariantOption.variant_id==id, VariantOption.is_deleted==False).all()
        except DataError:
            options = []
        for item in options:
            option = variant_pb2.VariantOption(id=str(item.id), name=item.name, description=item.description,
                                                      variant_id=str(item.variant_id), variant_name=item.variant.name)
            options_list.append(option)
    return options_list