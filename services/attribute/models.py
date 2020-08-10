from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Boolean, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates, backref
from sqlalchemy.sql.expression import func
# from sqlalchemy.sql.expression import text
import datetime
import uuid

Base = declarative_base()

class Attribute(Base):
    __tablename__ = 'attribute'
    # __table_args__ = (
    #     Index('ix_attribute_name', text('LOWER(name)')), 
    # )
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False, index=True, unique=True)
    description = Column(String)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(Integer, default=None)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    updated_by = Column(Integer, default=None)
    deleted_at = Column(DateTime, default=None)
    deleted_by = Column(Integer, default=None)
    is_deleted = Column(Boolean, default=False)
    options = relationship("AttributeOption", back_populates="attribute")

    @validates('name')
    def empty_name_to_null(self, key, value):
        if isinstance(value,str) and value == '':
            return None
        else:
            return value

                
Index('attribute_name_index', func.lower(Attribute.name), unique=True)

class AttributeOption(Base):
    __tablename__ = 'attribute_option'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False, index=True, unique=True)
    description = Column(String)
    attribute_id = Column(UUID(as_uuid=True), ForeignKey('attribute.id'), nullable=False)
    attribute = relationship("Attribute", back_populates="options")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(Integer, default=None)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    updated_by = Column(Integer, default=None)
    deleted_at = Column(DateTime, default=None)
    deleted_by = Column(Integer, default=None)
    is_deleted = Column(Boolean, default=False)
    
    def __repr__(self):
        return "<AttributeOption(id='{}', name='{}', description='{}', attribute_id='{}')>"\
                .format(self.id, self.name, self.description, self.attribute_id)

                
Index('attribute_option_name_index', func.lower(AttributeOption.name), unique=True)
