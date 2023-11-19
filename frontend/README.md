# Set up vue and fastapi to host on sagemaker instance

There are a few key point for this set up

## vite.config.js

Make sure to set up base in the config

```javascript
base: process.env.NODE_ENV === "production" ? "/proxy/8000/" : "/
```

## Vue router

1. create a const

```javascript
const base = process.env.NODE_ENV === "production" ? "/proxy/
8000/" : "/";
```

2. add this variable to reateWebHistory() function as input:

```javascript
import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";

const base = process.env.NODE_ENV === "production" ? "/proxy/8000/" : "/";

const router = createRouter({
  history: createWebHistory(base),
  routes: [
    {
      path: "/",
      name: "home",
      component: HomeView,
    },
    {
      path: "/sqlToJson",
      name: "sqlToJson",
      component: () => import("../views/SqlJsonView.vue"),
    },
});

export default router;
```

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
