from typing import Any, Optional, Dict

from fastapi import FastAPI, HTTPException


class SomeFastAPIError(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None
        ) -> None:
        super().__init__(
            status_code=status_code, detail=detail, headers=headers
        )


app = FastAPI()


@app.get("/error")
async def get_error():
    raise SomeFastAPIError(503, "Hello")

