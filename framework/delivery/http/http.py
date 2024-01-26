from usecase import Usecase
from framework.error import Error
from fastapi import FastAPI
from .user import UserRouter
from .tracker import TrackerRouter

class HttpDelivery:
    usecase = Usecase()
    error = Error()
    def __init__(self, app:FastAPI):
        self.app = app
        
    def init_router(self):
        UserRouter(self.app, self.error, self.usecase).init_router()
        TrackerRouter(self.app, self.error, self.usecase).init_router()