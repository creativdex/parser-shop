from fastapi import FastAPI
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

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8070)
