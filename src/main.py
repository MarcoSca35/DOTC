"""Application main module."""

from fastapi import FastAPI


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],)


@app.get("/")
def read_root():
    return {"status": "ok", "message": "API funcionando correctamente 🚀"}


