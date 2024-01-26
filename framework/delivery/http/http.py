from fastapi import FastAPI
from application.http.http import HttpApplication
from framework.infra import Infra

class HttpDelivery:
    infra = Infra()
    def __init__(self, app:FastAPI):
        self.app = app
        
    def init_router(self):
        HttpApplication(self.infra).serve(self.app)