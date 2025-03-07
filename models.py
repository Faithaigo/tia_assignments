from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin


class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

class Posts(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str]
    content:Mapped[str]
    author:Mapped[str]
    
class User(UserMixin,db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    full_name:Mapped[str]
    email:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str]