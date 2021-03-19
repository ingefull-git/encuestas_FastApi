import fastapi
import uvicorn
from fastapi.staticfiles import StaticFiles

from pathlib import Path
import views
import models
from db import engine
import os 

path = '/home/raul.sosa/Desktop/Dev/encuestas_fastApi_01/static/'
# parent_dir_path = os.path.dirname(os.path.realpath('static'))
# print("PARENT: ",parent_dir_path)
print("PARENT2: ",path)

app = fastapi.FastAPI()

app.mount("/static", StaticFiles(directory=path), name="static")

def configure():
    app.include_router(views.router)
    
models.Base.metadata.create_all(bind=engine)


configure()
if __name__ == '__main__':
    uvicorn.run("app:app", port=8000, reload=True)
