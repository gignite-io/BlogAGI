from fastapi import APIRouter
from app.schemas.blog import BlogRequest, BlogResponse
from app.services.pipeline import generate_blog_post


router = APIRouter()


@router.post("/generate", response_model=BlogResponse)
async def generate_blog(request: BlogRequest) -> BlogResponse:
	return await generate_blog_post(request)