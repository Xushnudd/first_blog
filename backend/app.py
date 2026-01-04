from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

engine = create_engine('sqlite:///maktab.db', echo=True)

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str]
    email:Mapped[str]
    
Base.metadata.create_all(engine)

with Session(engine) as session:
    new_user = User(name="Ali", email="ali@example.com")
    session.add(new_user)
    session.commit()
    
with Session(engine) as session:
    statement = select(User).where(User.name == "Ali")
    user = session.execute(statement).scalars().all()
    for i in user:
        print(f"ID: {i.id}, Ismi: {i.name}")