from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import student

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(student.router, prefix="/students", tags=["Students"])
