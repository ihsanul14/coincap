from usecase import Usecase
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends, Body
from framework.error import Error
from framework.validator.validator import Validate
from models import UpdateUserRequest, User,CreateUserRequest

router_group = "/api/user"

class UserRouter:
    def __init__(self, app:FastAPI, error: Error, usecase: Usecase):
        self.app = app
        self.error = error
        self.usecase = usecase
        
        
    def init_router(self):
        @self.app.get(router_group)
        def get_user():
            try:
                response = self.usecase.get_data()
                return JSONResponse(response, status_code=response['code'])
            except Exception as e:
                return self.error.error(e)
            
        # @self.app.get(router_group_with_id)
        # def list_project_by_id(id):
        #     try:
        #         response = self.usecase.get_data_by_id(id)
        #         return JSONResponse(response, status_code=response['code'])
        #     except Exception as e:
        #         return self.error.error(e)

        # @self.app.post(router_group)
        # def create_project(request: CreateProjectRequest):
        #     try:
        #         response = self.usecase.add_data(request)
        #         return JSONResponse(response, status_code=response['code'])
        #     except Exception as e:
        #         return self.error.error(e)

        # @self.app.put(router_group_with_id)
        # def update_project(request: UpdateProjectRequest,id):
        #     try:
        #         request.json['project_id'] = id
        #         validation_error = Validate(request, UpdateProjectRequest)
        #         if validation_error:
        #             return JSONResponse({'code': '400', 'message' : validation_error}, status_code=400)
        #         response = self.usecase.update_data(
        #             request.json)
        #         return JSONResponse(response, status_code=response['code'])
        #     except Exception as e:
        #         return self.error.error(e)

        # @self.app.delete(router_group_with_id)
        # def delete_project(id):
        #     try:
        #         response = self.usecase.delete_data(id)
        #         return JSONResponse(response, status_code=response['code'])
        #     except Exception as e:
        #         return self.error.error(e)
