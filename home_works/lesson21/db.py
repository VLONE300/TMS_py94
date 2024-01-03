from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.schema import Column
from sqlalchemy import types

engine = create_engine(
    "postgresql+psycopg2://vlone:qwerty1234@localhost/hw_lesson17"
)


class Base(DeclarativeBase):
    ...


class Product(Base):
    __tablename__ = "product"
    id = Column("id", types.Integer(), primary_key=True)
    name = Column("name", types.String(), nullable=False)
    protein = Column("protein", types.Float(), nullable=True)
    fats = Column("fats", types.Float(), nullable=True)
    carbs = Column("carbs", types.Float(), nullable=True)
    gramms = Column("gramms", types.Float(), nullable=False)


Base.metadata.create_all(engine)
