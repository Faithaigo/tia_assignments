from sqlalchemy.orm import  Mapped, mapped_column
from flask_login import UserMixin
from utils import db
    
class User(UserMixin,db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    full_name:Mapped[str]
    email:Mapped[str] = mapped_column(unique=True)
    password:Mapped[str]