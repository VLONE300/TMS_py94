from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.schema import Column
from sqlalchemy import types


engine = create_engine(
    "postgresql+psycopg2://tms21:pass@localhost/lsn21"
)


class Base(DeclarativeBase):
    ...


class User(Base):
    __tablename__ = "new_user"
    id = Column("id", types.Integer(), primary_key=True)
    name = Column("name", types.String(), nullable=False)
    email = Column("email", types.String(), nullable=False)
    age = Column("age", types.Integer(), nullable=False)


Base.metadata.create_all(engine)