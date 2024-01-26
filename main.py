from fastapi import FastAPI
import uvicorn
from decouple import config 
from framework import HttpDelivery

app = FastAPI()
HttpDelivery(app).init_router()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(config('PORT')))