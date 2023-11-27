from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from pydantic import BaseModel
from sql_to_json import get_data
from pin_match import run_metaflow


app = FastAPI()

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
    data_str ,file_type = get_data(user_input)
    payload = {}
    if user_input['download']:
        payload['json_data'] = data_str
    payload["file_type"] = file_type
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

    if cliArgs["flowSwitch"]:
        payload,current_process = run_metaflow(command )
        print("process start")
    
    else: 
        if current_process is not None:
            current_process.terminate()
            current_process= None
            print('process ternimated')
            payload = {
                "run_id":0,
                "message": "current flow has been terminated"
            }
        else: 
            payload = {
                "run_id":0,
                "message": "There is no flow runing"
            }
    return payload

# ------------------------ Serve Vue app static files ------------------------ #
app.mount("/", StaticFiles(directory="dist", html=True), name="static")