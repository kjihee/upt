
# coding: utf-8





from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, VARCHAR, DATE, TEXT, Integer, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy import create_engine
import uuid



engine = create_engine('sqlite:///:memory:', echo=True)




Base = declarative_base()




#patent
class Patent(Base):
    __tablename__ = 'patent'
    id = Column(VARCHAR(20), primary_key=True)
    type = Column(VARCHAR(20))
    number = Column(VARCHAR(64))
    country= Column(VARCHAR(20))
    date = Column(TEXT)
    abstract = Column(TEXT)
    title = Column(TEXT)
    kind = Column(VARCHAR(20))
    num_claims =Column(Integer())

    def __init__(self, id, type, country, date,number, abstract, kind, title, num_claims):
        self.id = id
        self.type = type
        self.country = country
        self.number = number
        self.date =date
        self.abstract = abstract
        self.title = title
        self.kind = kind
        self.num_claims = num_claims
    def __repr__(self):
        return "<Patent('%s', '%s', '%s', '%s', '%s', '%s',  '%s', '%s', '%s')>" % (self.id, self.type, self.country, self.date, self.number, self.abstract,self.title,  self.kind, self.num_claims)




#Inventor
class Inventor(Base):
    __tablename__ = 'inventor'
    id = Column(VARCHAR(36), primary_key=True)
    name_first = Column(VARCHAR(64))
    name_last = Column(VARCHAR(64))
    nationality = Column(VARCHAR(10))
    def __init__(self, id, name_first, name_last, nationality):
        self.id = id
        self.name_first = name_first
        self.name_last = name_last
        self.nationality = nationality
    def __repr__(self):
        return "<Inventor('%s', '%s', '%s', '%s')>" % (self.id, self.name_first, self.name_last, self.nationality)




#location
class Location(Base):
    __tablename__ = 'location'
    id = Column(VARCHAR(36), primary_key=True)
    city = Column(VARCHAR(128))
    state = Column(VARCHAR(10))
    country = Column(VARCHAR(10))
    latitude = Column(Float)
    longitude = Column(Float)

    def __init__(self, id, city, state, country, latitude, longitude):
        self.id = id
        self.city = city
        self.state = state
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
    def __repr__(self):
        return "<Location('%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.city, self.state, self.country, self.latitude, self.longitude)


#rawlocation
class RawLocation(Base):
    __tablename__ = 'rawlocation'
    id = Column(VARCHAR(256), primary_key=True)
    location_id = Column(VARCHAR(256), ForeignKey('location_id'))
    city = Column(VARCHAR(128))
    state = Column(VARCHAR(10))
    country = Column(VARCHAR(10))

    def __init__(self, id, location_id, city, state, country):
        self.id = id
        self.country = country
        self.state = state
        self.city = city
        self.location_id = location_id
    def __repr__(self):
        return "<RawLoaction('%s', '%s', '%s', '%s', '%s')>" % (self.id, self.location_id, self.city, self.country, self.state)



#rawinventor
class RawInventor(Base):
    __tablename__ = 'rawinventor'
    uuid = Column(VARCHAR(36), primary_key=True)
    patent_id  = Column(VARCHAR(20), ForeignKey('patent.id'))
    inventor_id = Column(VARCHAR(20), ForeignKey('inventor.id'))
    rawlocation_id = Column(VARCHAR(256), ForeignKey('rawlocation.id'))
    name_first = Column(VARCHAR(64))
    name_last = Column(VARCHAR(64))
    nationality = Column(VARCHAR(10))
    sequence = Column(Integer())


    def __init__(self, uuid, patent_id, inventor_id, rawlocation_id, nationality, name_first, name_last, sequence):
        self.uuid = uuid
        self.patent_id = patent_id
        self.inventor_id = inventor_id
        self.rawlocation_id = rawlocation_id
        self.nationality = nationality
        self.name_first = name_first
        self.name_last = name_last
        self.sequence = sequence

    def __repr__(self):
        return "<RawInventor('%s', '%s','%s', '%s','%s', '%s','%s', '%s')>" % (self.uuid, self.patent_id, self.rawlocation_id, self.inventor_id, self.name_first, self.name_last, self.nationality, self.sequence)



#patent_inventor
class Patent_Inventor(Base):
    __tablename__ = 'patent_inventor'
    #의미없는 키 넣어버림
    no_mean = Column(VARCHAR(2), primary_key=True)
    patent_id = Column(VARCHAR(20), ForeignKey('patent.id'))
    inventor_id= Column(VARCHAR(36), ForeignKey('inventor.id'))
    user_patent = relationship("Patent", backref= backref('patent_inventor'))
    user_inventor = relationship("Inventor", backref= backref('patent_inventor'))


    def __init__(self, patent_id, inventor_id):
        self.patent_id = patent_id
        self.inventor_id = inventor_id
    def __repr__(self):
        return "<Patent_Inventor('%s', '%s')>" % (self.patent_id, self.inventor_id)

#location_inventor
class LocationInventor(Base):
    __tablename__ = 'location_inventor'
    no_mean = Column(VARCHAR(2), primary_key=True)
    location_id = Column(VARCHAR(20), ForeignKey('location.id'))
    inventor_id = Column(VARCHAR(36), ForeignKey('inventor.id'))
    user_location = relationship("Patent", backref= backref('location_inventor'))
    user_inventor = relationship("Inventor", backref= backref('location_inventor'))

    def __init__(self, location_id, inventor_id):
        self.location_id = location_id
        self.inventor_id = inventor_id
    def __repr__(self):
        return "<LocationInventor('%s', '%s')>" % (self.location_id, self.inventor_id)
