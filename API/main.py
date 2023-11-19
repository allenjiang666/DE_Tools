from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI

app = FastAPI()


app.mount("/", StaticFiles(directory="static", html=True), name="static")


# @app.post("/convertsql" )
# async def create_item(data):
#     batch_test_json = get_json(data)
#     return batch_test_json
