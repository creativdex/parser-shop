from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import logging

import uvicorn
from router import router


logging.basicConfig(
    filename="result.log",
    encoding="utf-8",
    level=logging.INFO,
)
logging.getLogger("uvicron").setLevel(logging.WARNING)

app = FastAPI()
app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8070)
