from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sql_to_json import get_json
import time 

class userInput(BaseModel):
    # Define your data structure here
    query: str
    email: str
    bucket: str
    file_path: str
    download: bool


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/convertsql")
async def create_item(user_input: userInput):
    time.sleep(3)
    user_input = user_input.dict()
    payload = {}
    if user_input['download']:
        payload['json_data'] = user_input
    payload['message'] = "Job is successful!"
    
    return payload

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

app.mount("/", StaticFiles(directory="dist", html=True), name="static")