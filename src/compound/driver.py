from fastapi import FastAPI


_shared_driver = FastAPI()


def get_driver() -> FastAPI:
    return _shared_driver
