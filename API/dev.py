from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sql_to_json import get_json
from pin_match import run_metaflow
import time 

class ConvertSqlInput(BaseModel):
    # Define your data structure here
    query: str
    email: str
    bucket: str
    file_path: str
    download: bool


class PinMatchInput(BaseModel):

    year: int
    month: int
    db: str
    schm: str
    s3: str
    prefix: str

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.post("/convertsql")
async def convertsql(user_input: ConvertSqlInput):
    time.sleep(3)
    user_input = user_input.dict()
    payload = {}
    if user_input['download']:
        payload['json_data'] = user_input
    payload['message'] = "Job is successful!"
    
    return payload

@app.post("/pinmatch")
async def pinmatch(cliArgs:PinMatchInput):
    cliArgs = cliArgs.dict()
    command = [
        "python3", "pin_match/pl_pin_match.py",
        "--environment=pypi",
        "run",
        f"--year={cliArgs['year']}",
        f"--month={cliArgs['month']}",
        f"--db={cliArgs['db']}",
        f"--schema={cliArgs['schm']}",
        f"--s3={cliArgs['s3']}",
        f"--prefix={cliArgs['prefix']}"
    ]
    output = run_metaflow(command )
    payload = {}
    payload['flow_status_link'] = f"https://metaflow.ml.bestegg.com/PLPinMatch/{output['run_id']}"
    payload['message'] = output['message']
    return payload

app.mount("/", StaticFiles(directory="dist", html=True), name="static")