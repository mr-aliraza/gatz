from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Boolean, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates, backref
from sqlalchemy.sql.expression import func
# from sqlalchemy.sql.expression import text
import datetime
import uuid

Base = declarative_base()

class Category(Base):
    __tablename__ = 'categories'
    # __table_args__ = (
    #     Index('ix_category_name', text('LOWER(name)')), 
    # )
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False, index=True, unique=True)
    description = Column(String)
    parent_id = Column(UUID(as_uuid=True), ForeignKey('categories.id'), nullable=True)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(Integer, default=None)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    updated_by = Column(Integer, default=None)
    deleted_at = Column(DateTime, default=None)
    deleted_by = Column(Integer, default=None)
    is_deleted = Column(Boolean, default=False)
    children = relationship("Category", backref=backref('parent', remote_side=[id]))
    attributes = relationship("CategoryAttribute")
    variants = relationship("CategoryVariant")

    @validates('name')
    def empty_name_to_null(self, key, value):
        if isinstance(value,str) and value == '':
            return None
        else:
            return value

    @validates('parent_id')
    def empty_parent_to_null(self, key, value):
        if isinstance(value,str) and value == '':
            return None
        else:
            return value
    
    # def __repr__(self):
    #     return "<Category(name='{}', description='{}', parent_id={})>"\
    #             .format(self.name, self.description, self.parent_id)

                
Index('category_name_index', func.lower(Category.name), unique=True)

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