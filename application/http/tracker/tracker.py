from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr, confloat,Field
from fastapi import FastAPI, Depends,Request
from usecase.tracker.tracker import TrackerUsecase
from framework.infra import Infra
from ...middleware import JwtMiddleware
from typing import List

router_group = "/api/tracker"
router_group_with_id = "/api/tracker/{id}"

class CreateTrackerRequest(BaseModel):
    name: constr(strict=True)
    price: confloat(ge=0)
    
class DeleteTrackerRequest(BaseModel):
    name: constr(strict=True, min_length=1)

class Tracker(BaseModel):
    name:str
    price:float
    usd_price:str
class Response(BaseModel):
    code:int = Field(200)
    message:str 
    data: List[Tracker]

class GeneralResponse(BaseModel):
    code:int = Field(200)
    message:str 
    
class BadRequestResponse(BaseModel): 
    code:int = Field(400)
    message:str
class ErrorResponse(BaseModel): 
    code:int = Field(500)
    message:str    
    
class TrackerHttp:
    usecase = TrackerUsecase()
    def __init__(self, infra:Infra):
        self.error = infra.error
        self.validator = infra.validator
    
    def success(self, response):
        return JSONResponse(response, status_code=200)
    
    def bad_request(self, message:str):
        return JSONResponse({'code': 400, 'message' : message},status_code=400)
    
    def general_error(self, error):  
        return JSONResponse(error,status_code=error['code'])
        
    def serve_router(self, app:FastAPI):
        @app.get(router_group,response_model=Response,responses={500:{'model':ErrorResponse}})
        async def get_tracker(middleware = Depends(JwtMiddleware().validate_token)):
            try:     
                response = self.usecase.get_data()
                return self.success(response)
            except Exception as e:
                return self.general_error(self.error.error(e))
            
        @app.post(router_group,response_model=GeneralResponse,responses={400:{'model':BadRequestResponse},500:{'model':ErrorResponse}})
        async def create_tracker(data: Request,request:CreateTrackerRequest,middleware = Depends(JwtMiddleware().validate_token)):
            try:
                request_json = await data.json()
                validation_error = self.validator.Validate(request_json, CreateTrackerRequest)
                if validation_error:
                    return self.bad_request(validation_error)
                response = self.usecase.add_data(request_json)
                return self.success(response)
            except Exception as e:
                return self.general_error(self.error.error(e))

        @app.delete(router_group_with_id,response_model=GeneralResponse,responses={400:{'model':BadRequestResponse},500:{'model':ErrorResponse}})
        async def delete_tracker(id:str,middleware = Depends(JwtMiddleware().validate_token)):
            try:
                request = {'name': id}
                validation_error = self.validator.Validate(request, DeleteTrackerRequest)
                if validation_error:
                    return self.bad_request(validation_error)
                response = self.usecase.delete_data(id)
                return self.success(response)
            except Exception as e:
                return self.general_error(self.error.error(e,id))
