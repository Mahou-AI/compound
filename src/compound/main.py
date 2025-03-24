from fastapi import FastAPI
import transformers as transformers
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return "Hello world from `Compound`!"


uvicorn.run(f"{__name__}:app")
