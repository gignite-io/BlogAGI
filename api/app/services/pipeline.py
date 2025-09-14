from typing import List
from markdown import markdown as md_to_html

from app.schemas.blog import BlogRequest, BlogResponse, ImageItem
from app.services.seo import (
	slugify, make_title, make_description, make_keywords,
	build_jsonld, build_seo_meta,
)
from app.services.localization import resolve_locale, localized_note
from app.services.adapter_agno import adapter


def _build_images(slug: str, topic: str, locale: str, num: int) -> List[ImageItem]:
	num = max(0, min(6, num))
	images: List[ImageItem] = []
	for i in range(num):
		url = f"https://picsum.photos/seed/{slug}-{i}/1200/630"
		alt = f"{topic} illustration ({locale}) #{i+1}"
		images.append(ImageItem(url=url, alt=alt))
	return images


def _compose_markdown(
	title: str,
	topic: str,
	keywords: List[str],
	tone: str,
	reading_level: str,
	locale: str,
	images: List[ImageItem],
	words: int,
) -> str:
	approx_sections = max(3, min(8, (words // 250)))
	sections = keywords[:approx_sections] if keywords else [topic]
	lines: List[str] = []
	lines.append(f"# {title}")
	lines.append("")
	lines.append(f"_Tone: {tone.capitalize()}, Reading level: {reading_level}_")
	lines.append("")
	lines.append(f"> {localized_note(locale)}")
	lines.append("")
	lines.append(f"## Introduction")
	lines.append(f"This article explores {topic} in the context of {locale}.")
	lines.append("")
	for sec in sections:
		lines.append(f"## {sec.capitalize()}")
		lines.append(f"- Key insights about {sec} for {locale}")
		lines.append(f"- Practical tips tailored to local norms")
		lines.append("")
	if images:
		lines.append("## Visuals")
		for img in images:
			lines.append(f"![{img.alt}]({img.url})")
			lines.append("")
	lines.append("## Conclusion")
	lines.append(f"In summary, {topic} requires localized strategy in {locale}.")
	return "\n".join(lines)


async def generate_blog_post(request: BlogRequest) -> BlogResponse:
	# Try Agno adapter first
	adapter_result = adapter.generate_blog(request.model_dump())
	if adapter_result:
		# Adapt fields from adapter_result to BlogResponse if available
		pass

	locale = resolve_locale(request.target_language, request.location)
	title = make_title(request.topic, request.location, request.target_language)
	slug = slugify(title)
	images = _build_images(slug, request.topic, locale, request.num_images if request.images_enabled else 0)
	description = make_description(request.topic, request.keywords, locale)
	keywords = make_keywords(request.topic, request.keywords)
	og_image = images[0].url if images else None
	seo = build_seo_meta(title, description, keywords, og_image)

	content_markdown = _compose_markdown(
		title=title,
		topic=request.topic,
		keywords=request.keywords,
		tone=request.tone,
		reading_level=request.reading_level,
		locale=locale,
		images=images,
		words=request.words,
	)
	content_html = md_to_html(content_markdown) if request.include_html else ""

	jsonld = build_jsonld(
		title=title,
		description=description,
		slug=slug,
		images=[img.url for img in images],
		locale=locale,
	)

	return BlogResponse(
		title=title,
		slug=slug,
		content_markdown=content_markdown,
		content_html=content_html,
		images=images,
		seo=seo,
		jsonld=jsonld,
		locale=locale,
	)