from pydantic import BaseModel, Field
from typing import List, Optional, Dict


class ImageItem(BaseModel):
	url: str
	alt: str


class SEOMeta(BaseModel):
	title: str
	description: str
	keywords: List[str] = Field(default_factory=list)
	og_title: Optional[str] = None
	og_description: Optional[str] = None
	og_image: Optional[str] = None


class BlogRequest(BaseModel):
	topic: str
	keywords: List[str] = Field(default_factory=list)
	target_language: str = "en"
	location: str = "US"
	tone: str = "informative"
	reading_level: str = "general"
	words: int = 900
	include_html: bool = True
	images_enabled: bool = True
	num_images: int = 2


class BlogResponse(BaseModel):
	title: str
	slug: str
	content_markdown: str
	content_html: str
	images: List[ImageItem]
	seo: SEOMeta
	jsonld: Dict[str, object]
	locale: str