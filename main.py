from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(
    title = 'Secrets'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://176.215.237.117:810"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Text(BaseModel):
    text: str

@app.post('/check')
async def check(text: Text):
    if text.text == 'Hello':
        return {'ok': True}
    else:
        return {'ok': False}