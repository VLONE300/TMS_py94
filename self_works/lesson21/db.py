from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.sql.schema import Column
from sqlalchemy import types

engine = create_engine(
    "postgresql+psycopg2://vlone300:pass@localhost/user_from_another_site"
)


class Base(DeclarativeBase):
    ...


class NewUser(Base):
    __tablename__ = "NewUser"
    id = Column("id", types.Integer(), primary_key=True)
    name = Column("name", types.String(), nullable=False)
    email = Column("email", types.String(), nullable=False)
    age = Column("age", types.Integer(), nullable=False)


Base.metadata.create_all(engine)
