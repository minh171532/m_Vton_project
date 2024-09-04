import time
import jwt
from typing import Dict
from config import CONFIG 

JWT_SECRET = CONFIG.SECRET
JWT_ALGORITHM = CONFIG.ALGORITHM 

# function used for signing the JWT string
def signJWT(username: str) -> Dict[str, str]:
    payload = {
        "username": username,
        "expires": time.time() + 60 * 60 * 24
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token


def decodeJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
    
def refreshJWT(token: str) -> dict:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        username = decoded_token['username']
        return signJWT(username)
    except:
        return {}