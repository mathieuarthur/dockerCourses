from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.router import routing

app = FastAPI()

app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

routing(app)