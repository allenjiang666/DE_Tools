from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from sql_to_json import get_data
from pin_match import run_metaflow
import time 


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# --------------------------- create CAS test file --------------------------- #
class userInput(BaseModel):
    # Define your data structure here
    query: str
    email: str
    bucket: str
    file_path: str
    download: bool

@app.post("/convertsql")
async def create_item(user_input: userInput):
    user_input = user_input.dict()
    # data_str ,file_type = get_data(user_input)
    payload = {}
    if user_input['download']:
        payload['json_data'] = "This is test"
    payload["file_type"] = "csv"
    payload['message'] = "Job is successful!"

    
    return payload

# ------------------------------- PL Pin Match ------------------------------- #
class PinMatchInput(BaseModel):
    year: int
    month: int
    db: str
    schm: str
    s3: str
    prefix: str
    flowSwitch:bool

current_process = None

@app.post("/pinmatch")
async def pinmatch(cliArgs:PinMatchInput):
    global current_process
    
    cliArgs = cliArgs.dict()

    print(cliArgs["flowSwitch"],current_process )
    date = str(cliArgs['year'])+str(cliArgs['month'])
    command = [
        "python3", "pin_match/pl_pin_match.py",
        "--environment=pypi",
        "run",
        f"--date={date}",
        f"--db={cliArgs['db']}",
        f"--schema={cliArgs['schm']}",
        f"--s3={cliArgs['s3']}",
        f"--prefix={cliArgs['prefix']}"
    ]

    if cliArgs["flowSwitch"] and current_process is None:
        payload,current_process = run_metaflow(command )
        print("process start")
    
    if not cliArgs["flowSwitch"] and current_process is not None:
        current_process.terminate()
        current_process= None
        print('process ternimated')
        payload = {
            "run_id":0,
            "message": "current flow has been terminated"
        }

    return payload

app.mount("/", StaticFiles(directory="dist", html=True), name="static")