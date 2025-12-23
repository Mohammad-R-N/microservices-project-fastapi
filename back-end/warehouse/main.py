from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import products

app = FastAPI()


app.include_router(products.router)


origins = [
    "http://localhost",
    "http://localhost:7000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
