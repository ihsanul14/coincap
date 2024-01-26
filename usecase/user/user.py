from repository.models.user import User
from repository.database.user.sqllite import UserSqllite 
from typing import List

class ResponseData:
    token:str 
    data: User
    
class Response:
    code:int 
    message:str 
    data:ResponseData

    
class UserUsecase:
    repository = UserSqllite()

    def sign_up(self,data):
        result = Response()
        result.data = self.repository.add_data(data)
        result.code = 200
        result.message = "success signup"
        result.data = {
            'email' : data['email']
        } 
        return self.parse_to_dict(result)

    def sign_in(self,data):
        result = Response()
        user_data = self.repository.get_data_by_id(data)
        result.code = 200
        result.message = "success signin" 
        result.data = self.repository.sign_in(user_data)
        return self.parse_to_dict(result)

    def delete_data(self,data):
        result = {}
        self.repository.delete_data(data)
        result['code'] = 200
        result['message'] = "success delete data with id - {}".format(
            data['email'])
        return result
    
    def logout(self):
        res = {
            'code': 200,
            'message': 'success logout'
        }
        return res
    
    def parse_to_dict(self, data:Response):
            return data.__dict__
