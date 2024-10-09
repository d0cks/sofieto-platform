from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from modelo import Base, engine

class Aula(Base):
    __tablename__='aula'
    id = Column(Integer, primary_key=True)
    data = Column(DateTime, nullable=False)
    desc = Column(String(60))
    
    cliente_id = Column(ForeignKey('cliente.id'), nullable=False)
    cliente = relationship('Cliente', back_populates='aula')

Base.metadata.create_all(engine)
