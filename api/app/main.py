from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import get_settings
from app.core.middleware import add_middlewares

# Routers
from app.routers.v1.blog import router as blog_router


def create_app() -> FastAPI:
	settings = get_settings()
	app = FastAPI(title="BlogGen API", version="1.0.0")

	app.add_middleware(
		CORSMiddleware,
		allow_origins=settings.cors_allow_origins,
		allow_credentials=True,
		allow_methods=["*"],
		allow_headers=["*"],
	)

	add_middlewares(app)
	app.include_router(blog_router, prefix="/api/v1/blog", tags=["blog"])
	return app


app = create_app()