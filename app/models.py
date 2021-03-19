from datetime import datetime
from sqlalchemy import (Boolean, Column, Date, DateTime, ForeignKey, Integer,
                        Numeric, String)
from sqlalchemy.orm import relationship

from db import Base


class Pregunta(Base):
    __tablename__ = "preguntas"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    nombre = Column(String, unique=True, index=True, nullable=False)
    creada = Column(Date, nullable=False)
    vence = Column(Date, nullable=False)
    # usuario = Column(User, blank=True, null=True, on_delete=models.CASCADE)
    # tag = Column(Tag, blank=True, null=True, on_delete=models.SET_NULL)
    
    def __str__(self):
        return self.nombre
    
    def vencida(self):
        if self.vence < datetime.today():
            return True
        return False
    

