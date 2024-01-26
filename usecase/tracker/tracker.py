from repository.models.tracker import Tracker
from repository.database.tracker.sqllite import TrackerSqllite
from typing import List
from repository.http.http import HttpRepository

class Response:
    code:int 
    message:str 
    data: List[Tracker]
    
class TrackerUsecase:
    repository = TrackerSqllite()
    usd_to_idr_currency =  15775.25
    def get_data(self):
        result = Response()
        result.data = []
        result.code = 200
        result.message = "success retrieve data"
        projects = self.repository.get_data()
        result.data = self.refactor_list(projects)
        return self.parse_to_dict(result)

    def add_data(self,data):
        result = Response()
        url = "https://api.coincap.io/v2/assets"
        coin_data = HttpRepository().add_url(url).get()
        if data['name'] != "":
            data['usd_price'] = self.parse_usd_to_idr(data['price'])
            self.repository.upsert_data(data)
        else:
            for i in coin_data['data']:
                data['name'] = i['name']
                data['price'] = self.parse_price(i['priceUsd'])
                data['usd_price'] = i['priceUsd']
                self.repository.upsert_data(data)
        result.code = 200
        result.message = "success insert data"
        return self.parse_to_dict(result)

    def delete_data(self,data):
        result = Response()
        self.repository.delete_data(data)
        result.code = 200
        result.message = "success delete data with id - {}".format(
            data)
        return self.parse_to_dict(result)

    def refactor_list(self,obj: List[Tracker]):
        res = []
        for x in obj:
            result = {}
            result['name'] = x.name
            result['price'] = x.price
            result['usd_price'] = x.usd_price
            res.append(result)
        return res

    def parse_price(self, data:str):
        return float(data) * self.usd_to_idr_currency

    def parse_usd_to_idr(self, data:str):
        return float(data) / self.usd_to_idr_currency
    
    def parse_to_dict(self, data:Response):
        return data.__dict__
