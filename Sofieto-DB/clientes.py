from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from modelo import Base, engine

class Cliente(Base):
    __tablename__ ='cliente'
    id = Column(Integer, primary_key=True)
    nome = Column(String(30))
   
    contato = relationship('Contato', back_populates='cliente', uselist=False)
    aula = relationship('Aula', back_populates='cliente')

Base.metadata.create_all(engine)