from datetime import date, datetime, timedelta

from pydantic import BaseModel



class EncuestaRequest(BaseModel):
    nombre: str
    creada: date = date.today()
    vence: date = date.today() + timedelta(days=6)
    
    
