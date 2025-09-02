from fastapi import FastAPI, Request, HTTPException, status
from fastapi.responses import HTMLResponse, PlainTextResponse, JSONResponse
from starlette.responses import Response
from pydantic import BaseModel
from datetime import datetime
from typing import List
import json



app = FastAPI()

# Route GET/ping pour assurer que ça marche
@app.get("/ping")
def get_ping():
    return PlainTextResponse(content="pong", status_code=200)