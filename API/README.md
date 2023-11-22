## Fix fasapi not serving other routes after mount:

In FastAPI, the order in which routes are declared can affect their accessibility. Ensure that your other routes are declared before mounting the static files. This is because the app.mount call for static files might be catching all requests and trying to serve them as static files, leading to a 404 error for your API routes.

## 422 Unprocessable Entity

A 422 Unprocessable Entity error in FastAPI usually indicates that the input data sent to the endpoint does not match the expected schema. Since your create_item function in the /convertsql route is expecting data, you need to define the expected data structure using Pydantic models. This error is often related to how the data is being sent from the client or how it's being received in FastAPI.

```python
from pydantic import BaseModel
class userInput(BaseModel):
    # Define your data structure here
    query: str
    email: str
    bucket: str
    file_path: str
    download: bool

@app.post("/convertsql")
async def create_item(user_input: userInput):
  return user_input
```

## OPTIONS 405 Method Not Allowed

The error INFO: 127.0.0.1:63183 - "OPTIONS /convertsql HTTP/1.1" 405 Method Not Allowed indicates a CORS (Cross-Origin Resource Sharing) issue. When a browser makes a request to a server in a different origin (domain, scheme, or port), it first sends an HTTP OPTIONS request to check if the CORS policy of the server allows the actual request. In your case, the FastAPI server is not handling this preflight OPTIONS request correctly, leading to the 405 Method Not Allowed error.

To resolve this, you need to set up CORS in your FastAPI application. FastAPI provides a way to do this easily using the CORSMiddleware

```python
from fastapi.middleware.cors import CORSMiddleware

# Set up CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
```

## Subprocess

`subprocess.run`:

Synchronous Operation: The `run` function is blocking, meaning it waits for the subprocess to complete, which simplifies its use in many scenarios.

`subprocess.Popen`:

Asynchronous Operation: Allows for asynchronous operation, meaning your Python script can continue running while the subprocess is executing.
However, if the main python is terminated or exit, the subprocess will also be termainated unless `start_new_session=True`.
