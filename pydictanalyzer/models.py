from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Object(Base):
    __tablename__ = "objects"

    id = Column(Integer, primary_key=True, autoincrement=True)
    path = Column(String, unique=True)
    type = Column(String(1))
    size = Column(Integer)

    def __repr__(self):
        return "Object. Id: {}, path: {}, type: {}, size: {}".format(self.id, self.path, self.type, self.size)


class Cardinality(Base):
    __tablename__ = "cardinality"

    id = Column(Integer, ForeignKey('objects.id'), primary_key=True)
    nbr_of_elements = Column(Integer)

    def __repr__(self):
        return "Cardinality object. Object id: {}, number of elements: {}".format(self.id, self.nbr_of_elements)


class Checksum(Base):
    __tablename__ = "checksums"

    id = Column(Integer, ForeignKey('objects.id'), primary_key=True)
    checksum = Column(String)
