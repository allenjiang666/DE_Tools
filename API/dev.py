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
        payload['json_data'] = 'DATE,ID\n2022-10-21,0BF36018-6FBC-47DE-84DE-0924AF2343BB\n2022-10-11,2DE9EAA9-E413-438F-A6FA-87D85E8F2FA0\n2022-11-22,8A66DA69-E4C8-4683-90F4-533213C2704F\n2022-11-22,DB38D14D-5E61-4915-8CDF-DA2611ECCD49\n2022-11-22,992AC34C-D765-4230-BEF0-B44E752061C7\n2022-11-22,F3EB17D2-A921-40EE-9789-3194D5A5D75E\n2022-11-22,2D3E925C-7517-47AD-967E-383C900EB23B\n2022-11-22,D3225F3F-A7F9-4E20-B67C-B2ADC0D7FE57\n2022-11-22,1DBF3FA8-9DFB-4B37-BBDA-0E4A4B465F26\n2022-11-22,73F3DCBE-115C-492E-8BBC-88683156B462\n'
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