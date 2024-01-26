from .response import resp
from repository import Repository
from .response import list_project,refactored_project_by_id

class Usecase:
    repository = Repository()
    def get_data(self):
        result = {}
        result['data'] = []
        result['code'] = 200
        result['message'] = "success retrieve data"
        projects = self.repository.get_data()
        result = list_project(result,projects)
        return result


    def get_data_by_id(self,data):
        result = {}
        result['code'] = 200
        result['message'] = "success retrieve projects data with id = {}".format(
            data)
        result['data'] = refactored_project_by_id(self.repository.get_data_by_id(data))
        return result


    def add_data(self,data):
        result = {}
        result['data'] = self.repository.add_data(data)
        result['code'] = 200
        result['message'] = "success insert data"
        result = resp(result)
        return result


    def update_data(self,data):
        result = {}
        result['data'] = self.repository.update_data(data)
        result['code'] = 200
        result['message'] = "success update data with id = {}".format(
            data['project_id'])
        result = resp(result)
        return result


    def delete_data(self,data):
        result = {}
        result['data'] = self.repository.delete_data(data)
        result['code'] = 200
        result['message'] = "success delete data with id = {}".format(
            data['id'])
        result = resp(result)
        return result
