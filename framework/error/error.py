from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import IntegrityError
from fastapi.responses import JSONResponse
import json
from framework.logger import Logger


class Error:
    log = Logger()

    def error(self, e: Exception, id=""):
        response = {
            'code': 500,
            'message': str(e)
        }
        if isinstance(e, NoResultFound):
            response['code'] = 404
            response['message'] = f"No data found with id {id}"
        elif isinstance(e, IntegrityError):
            response['code'] = 400

        self.log.Error(response['message'])
        return JSONResponse(response, status_code=response['code'])
