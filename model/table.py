from sqlalchemy import Column, String, Integer, VARCHAR
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Indian_colleges_table(Base):
    __tablename__ = "indian_colleges_data"

    id = Column("id", Integer, primary_key=True)
    name = Column("name", String(50))
    city = Column("city", String(100))
    state = Column("state", String(100))
    rank = Column("rank", Integer)
    fees = Column("fees", Integer)
    courses = Column("courses", String(100))
