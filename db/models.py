from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class LastAction(Base):
    __tablename__ = "lastactions"

    id = Column(Integer, primary_key=True, nullable=False, unique=True)
    actionName = Column(String, nullable=False)
    userId = Column(Integer, nullable=False)
    date = Column(String, nullable=False)
