from driver import get_driver

# features
import pipeline as pipeline
import storage as storage
import bundle as bundle

# bootstrap
import uvicorn


app = get_driver()


@app.get("/")
def root():
    return "Hello world from `Compound`!"


uvicorn.run(f"{__name__}:app")
