from typing import Text
from sqlalchemy.sql.expression import column
from database import Base
from sqlalchemy import String,Boolean,Integer,Column


class Item(Base):
    __tablename__='items'
    id = Column(Integer,primary_key= True)
    name = Column(String(200),nullable=False,unique=True)
    description =Column(String)
    price =Column(Integer,nullable=False)
    on_offer =Column(Boolean,default=False)


    def __repr__(self):

        return f"<Item name = {self.name} price = {self.price}>"