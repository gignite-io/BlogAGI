import json
import time
from typing import Callable
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse


def add_middlewares(app: FastAPI) -> None:
	@app.middleware("http")
	async def log_requests(request: Request, call_next: Callable):
		start_time = time.time()
		response = await call_next(request)
		duration_ms = int((time.time() - start_time) * 1000)
		try:
			app.logger.info(json.dumps({
				"path": request.url.path,
				"method": request.method,
				"status_code": response.status_code,
				"duration_ms": duration_ms,
			}))
		except Exception:
			pass
		return response

	@app.exception_handler(Exception)
	async def unhandled_exception_handler(_: Request, exc: Exception):
		return JSONResponse(status_code=500, content={"detail": "Internal server error", "error": str(exc)})