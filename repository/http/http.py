import requests

class HttpRepository:
    url:str
    header:dict 
    body:dict 
    
    def add_url(self, url):
        self.url = url
        return self
    
    def add_header(self, header):
        self.header = header
        return self
    
    def add_body(self, body):
        self.body = body
        return self
    
    def get(self):
        res = requests.get(self.url,timeout=30)
        data = res.json()
        return data
        