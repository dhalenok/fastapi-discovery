from sqlalchemy import Column, Integer, String

from fastapi_discovery.database import Base


class Expense(Base):
    __tablename__ = "expenses"
    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Integer)
    category = Column(String)
