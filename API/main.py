from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
# from fastapi.middleware.cors import CORSMiddleware

class Item(BaseModel):
    # Define your data structure here
    query: str
    email: str
    bucket: str
    file_path: str
    download: bool


app = FastAPI()

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allows all origins
#     allow_credentials=True,
#     allow_methods=["*"],  # Allows all methods
#     allow_headers=["*"],  # Allows all headers
# )

@app.post("/convertsql")
async def create_item(item: Item):
    print(item.dict())
    return item.dict()

@app.get("/hello")
def read_root():
    return {"Hello": "World"}

app.mount("/", StaticFiles(directory="dist", html=True), name="static")