from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title = 'Secrets'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], #http://176.215.237.117:810
    # allow_credentials=True,
    allow_methods=["POST"],
    allow_headers=["*"],
)

class Secret(BaseModel):
    text: str

@app.post('/check')
async def check(secret: Secret):
    if secret.text == 'Hello':
        return {'ok': True, 'message': 'Congratulations! You found the secret code!'}
    else:
        return {'ok': False, 'message': 'Poop! Wrong secret code!'}