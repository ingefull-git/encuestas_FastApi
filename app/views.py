import fastapi
from fastapi import BackgroundTasks, Depends, FastAPI, Request
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from db import SessionLocal
from models import Pregunta
from schemas import EncuestaRequest

templates = Jinja2Templates(directory="../templates")

router = fastapi.APIRouter()

def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@router.get('/')
async def dashboard(request: Request, db: Session = Depends(get_db)):
    """
    list all the encuestas from the database
    """
    encuestas = db.query(Pregunta)
    encuestas_list = encuestas.all()
    return templates.TemplateResponse("dashboard.html", {'title': 'Dashboard Page',
                                                         'request': request,
                                                         'encuestas_list': encuestas_list})


@router.post("/encuesta")
async def encuesta_create(encuesta_request: EncuestaRequest, 
                          background_tasks: BackgroundTasks, 
                          db: Session = Depends(get_db)):
    """
    add one or more encuestas to the database
    """
    encuesta = Pregunta()
    encuesta.nombre = encuesta_request.nombre
    encuesta.creada = encuesta_request.creada
    encuesta.vence = encuesta_request.vence
    db.add(encuesta)
    db.commit()
    return {
        "code": "success",
        "message": "encuesta was added to the database"
    }
    
   
