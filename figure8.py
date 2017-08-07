
from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, VARCHAR, DATE, TEXT, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref, sessionmaker, joinedload
from sqlalchemy import create_engine
import uuid
engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()


class Patent(Base):
    __tablename__ = 'patent'
    id = Column(VARCHAR(20), primary_key=True)
    type = Column(VARCHAR(20))
    number = Column(VARCHAR(64))
    country = Column(VARCHAR(20))
    date = Column(DATE)
    abstract =Column(TEXT)
    title = Column(TEXT)
    kind = Column(VARCHAR(10))
    num_claims =Column(Integer())
    def __init__(self, id, type, number, country, date, abstract,title, kind, num_claims):
        self.id = id
        self.type = type
        self.number=number
        self.country = country
        self.date = date
        self.abstract = abstract
        self.title = title
        self.kind = kind
        self.num_claims = num_claims
    def __repr__(self):
        return "<Patent('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')>" % (self.id, self.type, self.number,self.date,  self.country,self.abstract, self.kind,self.title ,self.num_claims)

#lawyer
class Lawyer(Base):
    __tablename__ = 'lawyer'
    id = Column(VARCHAR(36), primary_key=True)
    country = Column(VARCHAR(10))
    name_first = Column(VARCHAR(64))
    name_last = Column(VARCHAR(64))
    organization = Column(VARCHAR(64))
    def __init__(self, id, type, country, data, abstract, kind):
        self.id = id
        self.country = country
        self.name_first = name_first
        self.name_last = name_last
        self.organization = organization
    def __repr__(self):
        return "<Lawyer('%s', '%s', '%s', '%s', '%s')>" % (self.id, self.country, self.name_first, self.name_last, self.organization)



#rawlawyer
class RawLawyer(Base):
    __tablename__ = 'rawlawyer'
    uuid = Column(VARCHAR(36), primary_key=True)
    patent_id  = Column(VARCHAR(20), ForeignKey('patent.id'))
    lawyer_id = Column(VARCHAR(20), ForeignKey('lawyer.id'))
    name_first = Column(VARCHAR(64))
    name_last = Column(VARCHAR(64))
    organization = Column(VARCHAR(64))
    country =Column(VARCHAR(10))
    sequence = Column(Integer())

    def __init__(self, patent_id, lawyer_id):
        self.uuid = uuid
        self.patent_id = patent_id
        self.lawyer_id = lawyer_id
        self.country = country
        self.name_first = name_first
        self.name_last = name_last
        self.organization = organization
        self.sequence = sequence

    def __repr__(self):
        return "<RawLawyer('%s', '%s','%s', '%s','%s', '%s','%s', '%s')>" % (self.uuid, self.sequence, self.country, self.name_first, self.name_last, self.organization, self.patent_id, self.lawyer_id)


#patent_lawyer
class Patent_Lawyer(Base):
    __tablename__ = 'patent_lawyer'
    no_mean = Column(VARCHAR(2), primary_key=True)
    patent_id = Column(VARCHAR(20), ForeignKey('patent.id'))
    lawyer_id = Column(VARCHAR(36), ForeignKey('inventor.id'))
    user_patent = relationship("Patent", backref= backref('patent_lawyer'))
    user_inventor = relationship("Inventor", backref= backref('patent_lawyer'))

    def __init__(self, patent_id, lawyer_id):
        self.patent_id = patent_id
        self.lawyer_id = lawyer_id
    def __repr__(self):
        return "<Patent_Lawyer('%s', '%s')>" % (self.patent_id, self.lawyer_id)
