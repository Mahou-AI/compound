from driver import get_driver
from pathlib import Path

app = get_driver()


_bundle = Path(__file__).parent.joinpath("bundle")


@app.get("/bundle/config")
def config():
    return
