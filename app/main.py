from fastapi import FastAPI
from . import models
from .database import engine
from fastapi.middleware.cors import CORSMiddleware
from .routers import post, user, auth, vote
from .config import setting

# models.Base.metadata.create_all(bind = engine)

app = FastAPI()

origins = ["https://www.google.com"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


print(setting.database_username)
app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Hello World"}






