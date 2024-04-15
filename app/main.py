from fastapi import FastAPI
from . import exams, blocks

app = FastAPI()

app.include_router(exams.router, prefix='/exams', tags=['Exames'])
app.include_router(blocks.router, prefix='/blocks', tags=['Blockchain'])
