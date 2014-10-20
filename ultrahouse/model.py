# -*- coding: utf-8 -*-
# Copyright 2014, wywy GmbH

from sqlalchemy import Column, Unicode, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Device(Base):
    __tablename__ = 'department'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode, unique=True)
    mac = Column(Unicode, unique=True)

    def __repr__(self):
        return "<Device(name={}, mac={})>".format(self.name, self.mac)


from sqlalchemy import create_engine
engine = create_engine('sqlite:///ultrahouse.db')


from sqlalchemy.orm import sessionmaker
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)
