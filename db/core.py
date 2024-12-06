from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base
from .dbconfig import DATABASE_URI

engine = create_engine(DATABASE_URI, echo=True)
Session = sessionmaker(bind=engine)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
