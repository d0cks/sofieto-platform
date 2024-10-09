from sqlalchemy import Column, Integer, String, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from modelo import Base, engine

class Contato(Base):
    __tablename__='contato'
    id = Column(Integer, primary_key=True)
    celular = Column(Integer)
    email = Column(String(30))
    
    cliente_id = Column(ForeignKey('cliente.id'), nullable=False)
    cliente = relationship('Cliente', back_populates='contato')

Base.metadata.create_all(engine)