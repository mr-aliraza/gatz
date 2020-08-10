from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime, ForeignKey, Boolean, Index
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship, validates, backref
from sqlalchemy.sql.expression import func
# from sqlalchemy.sql.expression import text
import datetime
import uuid

Base = declarative_base()

class Variant(Base):
    __tablename__ = 'variant'
    # __table_args__ = (
    #     Index('ix_variant_name', text('LOWER(name)')), 
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
    options = relationship("VariantOption", back_populates="variant")

    @validates('name')
    def empty_name_to_null(self, key, value):
        if isinstance(value,str) and value == '':
            return None
        else:
            return value

                
Index('variant_name_index', func.lower(Variant.name), unique=True)

class VariantOption(Base):
    __tablename__ = 'variant_option'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    name = Column(String, nullable=False, index=True, unique=True)
    description = Column(String)
    variant_id = Column(UUID(as_uuid=True), ForeignKey('variant.id'), nullable=False)
    variant = relationship("Variant", back_populates="options")
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    created_by = Column(Integer, default=None)
    updated_at = Column(DateTime, onupdate=datetime.datetime.utcnow)
    updated_by = Column(Integer, default=None)
    deleted_at = Column(DateTime, default=None)
    deleted_by = Column(Integer, default=None)
    is_deleted = Column(Boolean, default=False)
    
    def __repr__(self):
        return "<VariantOption(id='{}', name='{}', description='{}', variant_id='{}')>"\
                .format(self.id, self.name, self.description, self.variant_id)

                
Index('variant_option_name_index', func.lower(VariantOption.name), unique=True)
