from fastapi import FastAPI
from .controllers import set_parameters, to_speech
import uvicorn


class Application:
    def __init__(self) -> None:
        self.app = FastAPI()
        self.register_routers()

    def register_routers(self) -> None:
        self.app.include_router(set_parameters.router)
        self.app.include_router(to_speech.router)

    def run(self) -> None:
        uvicorn.run(self.app, host="127.0.0.1", port=5000)
