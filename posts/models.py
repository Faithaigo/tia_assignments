from sqlalchemy.orm import  Mapped, mapped_column
from extensions import db

class Posts(db.Model):
    id:Mapped[int] = mapped_column(primary_key=True)
    title:Mapped[str]
    content:Mapped[str]
    author:Mapped[str]