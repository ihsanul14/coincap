from framework.database import Database
from sqlalchemy.orm import sessionmaker
from models import User

class Repository:
    db = Database().sql_lite()
    def get_data(self):
        Session = sessionmaker(bind=self.db)
        session = Session()
        result = {}
        result = session.query(User).all()
        session.close()
        return result


    def get_data_by_id(self,data):
        result = {}
        Session = sessionmaker(bind=self.db)
        session = Session()
        result = session.query(User).filter(Project.project_id == data).one()
        session.close()
        return result


    def add_data(self,data):
        Session = sessionmaker(bind=self.db)
        session = Session()
        query = User(project_id=data.project_id,
                        project_name=data.project_name)
        session.add(query)
        session.commit()
        session.close()
        return data


    def update_data(self,data):
        Session = sessionmaker(bind=self.db)
        session = Session()
        result = session.query(User).filter(
            User.project_id == data['project_id']).one()
        result.project_name = data['project_name']
        session.commit()
        session.close()
        return data


    def delete_data(self,data):
        Session = sessionmaker(bind=self.db)
        session = Session()
        query = session.query(User).filter(User.email == data).one()
        session.delete(query)
        session.commit()
        session.close()
        return data
        
