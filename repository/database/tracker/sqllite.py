from framework.database.database import Database
from sqlalchemy.orm import sessionmaker
from ...models import Tracker
from sqlalchemy.exc import IntegrityError

class TrackerSqllite:
    db = Database().sql_lite()
    def get_data(self):
        Session = sessionmaker(bind=self.db)
        session = Session()
        result = {}
        result = session.query(Tracker).all()
        session.close()
        return result


    def upsert_data(self,data:Tracker):
        try:
            return self.add_data(data)
        except IntegrityError:
            return self.update_data(data)
    
    def add_data(self,data:Tracker):
        Session = sessionmaker(bind=self.db)
        session = Session()
        query = Tracker(name=data['name'],price=data['price'], usd_price=data['usd_price'])
        session.add(query)
        session.commit()
        session.close()
        return data

    def update_data(self,data:Tracker):
        Session = sessionmaker(bind=self.db)
        session = Session()
        result:Tracker = session.query(Tracker).filter(Tracker.name == data['name']).one()
        result.price = data['price']
        result.usd_price = data['usd_price']
        session.commit()
        session.close()
        return data


    def delete_data(self,data):
        Session = sessionmaker(bind=self.db)
        session = Session()
        query = session.query(Tracker).filter(Tracker.name == data).one()
        session.delete(query)
        session.commit()
        session.close()
        return data
        
