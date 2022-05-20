#!/usr/bin/env python3

import logging
import uvicorn
from fastapi import FastAPI, Request
from typing import List

app = FastAPI()

log = logging.getLogger("uvicorn.default")



@app.get("/home")
def home() -> str:
    return "hello world"


if __name__ == "__main__":
    """
    Main entrypoint, start ASGI server.
    """
    uvicorn.run(app, host="0.0.0.0", port=8080)
