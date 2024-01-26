from framework.infra import Infra
from .tracker.tracker import TrackerHttp
from .user.user import UserHttp
from fastapi import FastAPI

class HttpApplication:
    def __init__(self, infra:Infra):
        self.infra = infra
        
    def serve(self,app:FastAPI):
        TrackerHttp(self.infra).serve_router(app)
        UserHttp(self.infra).serve_router(app)
    
    