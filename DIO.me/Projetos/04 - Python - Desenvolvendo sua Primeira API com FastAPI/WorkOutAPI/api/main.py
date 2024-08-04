from fastapi import FastAPI
from fastapi_pagination import add_pagination
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import RedirectResponse

from api.routers import api_router


# Middleware to /docs
class RedirectToDocsMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        if request.url.path == "/":
            return RedirectResponse(url="/docs")
        return await call_next(request)


class App(FastAPI):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(
            *args,
            **kwargs,
            version="0.0.1",
            title="WorkOutAPI",
        )

        self.add_middleware(RedirectToDocsMiddleware)
        self.include_router(api_router)


app = App()
add_pagination(app)
