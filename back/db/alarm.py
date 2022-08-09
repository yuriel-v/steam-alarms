from sqlalchemy import Column, Float, Integer, String
from db import Base


class Alarm(Base):
    __tablename__ = "alarms"

    appid = Column(Integer, primary_key=True)
    item_name = Column(String, primary_key=True)
    price = Column(Float)
    amount_ref = Column(Integer)
    difference = Column(Float)

    def fire_alarm(self, amount):
        if amount > self.amount_ref:
            self.amount_ref = amount

        elif self.amount_ref - amount >= self.difference:
            self.amount_ref = amount
            return True

        return False
