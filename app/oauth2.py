from jose import JWTError, jwt
from datetime import datetime, timedelta
from . import schemas, database, models
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from .config import settings

oauth2_schema = OAuth2PasswordBearer(tokenUrl='login')

# Secret key
# Algorithm
# Expiration time

# secret key we only know
SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm  # algorithm used for hash the password
# time until the token is useless
ACCESS_TOKEN_EXPIRE_MINUTES = settings.access_token_expire_minutes


def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})

    # encode a token with the data pass by the user (data contains user_id)
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt


def verify_access_token(token: str, credentials_exception):
    try:
        # decode of the data contained in the token
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])

        # extract the user_id of the data decoded before
        id: str = payload.get("user_id")

        if id is None:
            raise credentials_exception  # if there is no id, it throws an error

        # validate the token schema, in this case is just an id
        # create the schema with the id we got from the token
        token_data = schemas.TokenData(id=id)
    except JWTError:
        raise credentials_exception

    return token_data


def get_current_user(token: str = Depends(oauth2_schema), db: Session = Depends(database.get_db)):
    # create the exception
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                          detail=f"Could not validate credentials", headers={"WWW-Authenticate": "Bearer"})

    token = verify_access_token(token, credentials_exception)
    user = db.query(models.User).filter(models.User.id == token.id).first()

    return user
