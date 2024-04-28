from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext
import secrets

# Generate a random secret key of 32 bytes
# secret_key = secrets.token_hex(32)

# print(secret_key)

# to run the server: uvicorn main:app --reload
# open the link, add /docs at the end

SECRET_KEY ="some-secret-key-001"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30



db = {
    "dimitrii":{
        "username": "dimitrii",
        "full_name": "Dimitrii U",
        "email": "01@gmail.com",
        "hashed_password": "$2b$12$/FadsrJ71ROZ2zMkm1.THOW/vzPwBgo8yKuvbUS.CqtEK7MPH/HNG", #generated for try out
        "disabled": False
    }
}

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str or None = None

class User(BaseModel):
    username: str
    email: str or None = None
    full_name : str or None= None
    disabled:bool or None = None

class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl = "token")


app = FastAPI()

#Hashing password
def verify_password(plain_password, hashed_password):
    """Verifies whether a plain password matches its hashed counterpart.
Parameters:
plain_password: The user-provided plain text password.
hashed_password: The stored hashed password from the database.
Returns:
True if the passwords match, otherwise False."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    """Generates a hash for a given plain password.
Parameters:
password: The plain text password to hash.
Returns:
The hashed password."""
    return pwd_context.hash(password)

def get_user(db, username: str):
    """Retrieves user data from the database based on the provided username.
Parameters:
db: The database (in-memory dictionary in this case).
username: The username of the user to retrieve.
Returns:
A UserInDB object containing user details (if found), or None."""
    if username in db:
        user_data = db[username]
        return UserInDB(**user_data) #** -pass dictionary parameters from db
    

def authenticate_user(db, username: str, password: str):
    """authenticate_user(db, username: str, password: str):
Authenticates a user during login.
Parameters:
db: The database (in-memory dictionary in this case).
username: The username provided during login.
password: The password provided during login.
Returns:
The authenticated user (if valid), or False."""
    user = get_user(db, username)
    if not user:
        return False
    if not verify_password(password, user.hashed_password):
        return False
    
    return user


def create_access_token(data:dict, expires_delta: timedelta or None = None): # type: ignore
    """Creates an access token (JWT) for the user.
Parameters:
data: A dictionary containing data to encode into the token (e.g., "sub": user.username).
expires_delta: Optional expiration time for the token (default is 15 minutes).
Returns:
The encoded JWT access token."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now() + expires_delta

    else:
        expire = datetime.now() + timedelta(minutes = 15)


    to_encode.update({"exp": expire})   
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

async def get_current_user(token: str = Depends(oauth2_scheme)):
    """Retrieves the current user based on the provided access token.
Parameters:
token: The access token passed in the request header.
Returns:
The user associated with the token (if valid), or raises an exception."""
    credential_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                         detail = "Could not validate credentials", headers = {"WWW-Authenticate": "Bearer"})
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credential_exception
        
        token_data = TokenData(username=username)
    except JWTError:
        raise credential_exception
    
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credential_exception
    
    return user

async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    """Ensures that the current user is active (not disabled).
Parameters:
current_user: The user obtained from the access token.
Returns:
The active user (if not disabled), or raises an exception."""
    if current_user.disabled:
        raise HTTPException(status_code=400, detail = "Inactive user")
    
    return current_user


@app.post("/token", response_model=Token)
async def login_for_access_token(form_data:OAuth2PasswordRequestForm = Depends()):
    """Endpoint for user login.
Validates credentials, generates an access token, and returns it.
Uses the OAuth2PasswordRequestForm model for form data."""
    user = authenticate_user(db, form_data.username,form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail = "Incorrect username or password", headers={"WWW-Authenticate": "Bearer"})
    access_token_expires = timedelta(minutes =ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub":user.username}, expires_delta=access_token_expires)
    
    return {"access_token": access_token, "token_type":"bearer"}

@app.get("/users/me/", response_model=User)
async def read_user_me(current_user: User = Depends(get_current_user)):
    """Endpoint to get the current user’s details.
Depends on the get_current_user function."""
    return current_user

@app.get("/users/me/items")
async def read_own_items(current_user: User = Depends(get_current_user)):
    """Endpoint to get items owned by the current user.
Depends on the get_current_user function."""
    return [{"item_id": 1, "owner": current_user}]

#Get a password for try-out

#pwd = get_password_hash("qwerty123")
#print(pwd)


# class Data(BaseModel):
#     name:str



# #accept API requests
# @app.post("/create/")
# async def create(data: Data):
#     return {"data": data}

# #Create endpoints
# @app.get("/test/{item_id}") #path parameter item_id
# async def test(item_id:str, query: int): #query parameter
#     return {"hello": item_id}
