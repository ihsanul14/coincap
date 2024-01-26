from jose import JWTError, jwt
from decouple import config
from fastapi import HTTPException,status, Depends
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timezone,timedelta
from repository.models import User
from fastapi.responses import JSONResponse
    
class JwtMiddleware:
    secret_key = config('SECRET_AUTH')
    algorithm = "HS256"
    token_expiration = 30
    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
    
    def unauthorized(self, e=None):
        message = e if e is not None else 'unauthorized'
        return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail={
            'code': 401,
            'message': message
        },
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    def generate_token(self, data:dict):
        expire = datetime.now(timezone.utc) + timedelta(minutes=self.token_expiration)
        data['exp'] = expire
        encoded_jwt = jwt.encode(data, self.secret_key, self.algorithm)
        return encoded_jwt

    def validate_token(self, token: str = Depends(oauth2_scheme)):
        try:
            payload = jwt.decode(token, self.secret_key, self.algorithm)
            email: str = payload.get("email")
            if email is None:
                raise self.unauthorized('payload is not valid')
        except JWTError as e:
            raise self.unauthorized(str(e.args))
        