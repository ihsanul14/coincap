from fastapi.responses import JSONResponse
from pydantic import BaseModel, constr,Field
from fastapi import FastAPI, Request,Depends
from framework.infra import Infra
from usecase.user.user import UserUsecase
from application.middleware import JwtMiddleware

class SignUpRequest(BaseModel):
    email: constr(strict=True, min_length=1)
    password: constr(strict=True, min_length=1)
    password_confirmation: constr(strict=True, min_length=1)
    
class SignInRequest(BaseModel):
    email: constr(strict=True, min_length=1)
    password: constr(strict=True, min_length=1)

class DeleteUserRequest(BaseModel):
    email: constr(strict=True, min_length=1)

class Token(BaseModel):
    token:str
    
class SignInResponse(BaseModel):
    code:int = Field(200)
    message:str 
    data: Token
    
class Response(BaseModel):
    code:int = Field(200)
    message:str 
    
class BadRequestResponse(BaseModel): 
    code:int = Field(400)
    message:str
class ErrorResponse(BaseModel): 
    code:int = Field(500)
    message:str

class UserHttp:
    usecase = UserUsecase()
    def __init__(self, infra:Infra):
        self.error = infra.error
        self.validator = infra.validator
    
    def success(self, response):
        return JSONResponse(response, status_code=200)
    
    def bad_request(self, message:str):
        return JSONResponse({'code': '400', 'message' : message},status_code=400)
    
    def general_error(self, error):  
        return JSONResponse(error,status_code=error['code'])
        
    def serve_router(self, app:FastAPI):
        @app.post('/api/signup',response_model=Response,responses={400:{'model':BadRequestResponse},500:{'model':ErrorResponse}})
        async def sign_up(data: Request, request:SignUpRequest):
            request_json = await data.json()
            try:
                validation_error = self.validator.Validate(request_json, DeleteUserRequest)
                if validation_error:
                    return self.bad_request(validation_error)
                
                if request_json['password'] != request_json['password_confirmation']:
                    return self.bad_request("password missmatch")   
                response = self.usecase.sign_up(request_json)
                return self.success(response)
            except Exception as e:
                return self.general_error(self.error.error(e))
        
        @app.post('/api/signin',response_model=SignInResponse,responses={400:{'model':BadRequestResponse},500:{'model':ErrorResponse}})    
        async def sign_in(data: Request,request:SignInRequest):
            request_json = await data.json()
            try:
                response = self.usecase.sign_in(request_json)
                return self.success(response)
            except Exception as e:
                return self.general_error(self.error.error(e))
            
        @app.delete('/api/user',response_model=Response,responses={400:{'model':BadRequestResponse},500:{'model':ErrorResponse}})
        async def delete_user(data: Request,request:DeleteUserRequest):
            request_json = await data.json()
            try:
                validation_error = self.validator.Validate(request_json, DeleteUserRequest)
                if validation_error:
                    return self.bad_request(validation_error)
                response = self.usecase.delete_data(request_json)
                return self.success(response)
            except Exception as e:
                return self.general_error(self.error.error(e,request_json['email']))

        @app.post('/api/logout',response_model=Response,responses={500:{'model':ErrorResponse}})
        async def logout(middleware = Depends(JwtMiddleware().validate_token)):
            response = self.usecase.logout()
            return self.success(response)
            
