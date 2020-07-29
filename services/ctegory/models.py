from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.dialects.postgresql import UUID
import datetime
import uuid

Base = declarative_base()

class Category(Base):
    __tablename__ = 'category'
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, nullable=False)
    title = Column(String)
    author = Column(String)
    pages = Column(Integer)
    published = Column(Date)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return "<Category(title='{}', author='{}', pages={}, published={})>"\
                .format(self.title, self.author, self.pages, self.published)