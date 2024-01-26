from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from decouple import config 
from framework.delivery.http.http import HttpDelivery

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HttpDelivery(app).init_router()

if __name__ == "__main__":
    uvicorn.run("main:app", host=config('HOST'), port=int(config('PORT')))