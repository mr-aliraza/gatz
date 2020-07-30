from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
import datetime
import uuid

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    parent_id = Column(UUID(as_uuid=True))
    attributes = relationship("CategoryAttribute")
    variants = relationship("CategoryVariant")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, default=None)
    is_deleted = Column(Boolean, default=False)
    
    def __repr__(self):
        return "<Category(name='{}', description='{}', parent_id={})>"\
                .format(self.name, self.description, self.parent_id)

class CategoryAttribute(Base):
    __tablename__ = 'category_attributes'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=False)
    attribute_id = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, default=None)
    is_deleted = Column(Boolean, default=False)
    
    def __repr__(self):
        return "<CategoryAttribute(category_id='{}', attribute_id='{}')>"\
                .format(self.category_id, self.attribute_id)


class CategoryVariant(Base):
    __tablename__ = 'category_variants'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    category_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=False)
    variant_id = Column(UUID(as_uuid=True), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    deleted_at = Column(DateTime, default=None)
    is_deleted = Column(Boolean, default=False)
    
    def __repr__(self):
        return "<CategoryVariant(category_id='{}', variant_id='{}')>"\
                .format(self.category_id, self.variant_id)

# class Attributes(Base):
#     __tablename__ = 'articles'
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     options = relationship("Option")
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
#     updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
#     deleted_at = Column(DateTime, default=datetime.datetime.utcnow)
#     is_deleted = Column(bool, default=False)


# class Option(Base):
#     __tablename__ = 'comments'
#     id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
#     article_id = Column(Integer, ForeignKey('articles.id'))
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)
#     updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
#     deleted_at = Column(DateTime, default=datetime.datetime.utcnow)
#     is_deleted = Column(bool, default=False)