import re
from typing import List, Dict
from app.schemas.blog import SEOMeta


def slugify(value: str) -> str:
	value = value.lower().strip()
	value = re.sub(r"[^a-z0-9\s-]", "", value)
	value = re.sub(r"[\s_-]+", "-", value)
	value = re.sub(r"^-+|-+$", "", value)
	return value or "post"


def make_title(topic: str, location: str, language: str) -> str:
	loc = location.upper() if location else ""
	return f"{topic} — A Practical Guide ({loc})"


def make_description(topic: str, keywords: List[str], locale: str) -> str:
	kws = ", ".join(keywords[:5]) if keywords else topic
	return f"SEO-optimized guide to {topic} for {locale}. Covers {kws}."


def make_keywords(topic: str, keywords: List[str]) -> List[str]:
	base = [topic]
	return list(dict.fromkeys(base + keywords))


def build_jsonld(
	title: str,
	description: str,
	slug: str,
	images: List[str],
	locale: str,
) -> Dict[str, object]:
	url = f"https://example.com/blog/{slug}"
	return {
		"@context": "https://schema.org",
		"@type": "BlogPosting",
		"headline": title,
		"description": description,
		"image": images,
		"inLanguage": locale,
		"mainEntityOfPage": {
			"@type": "WebPage",
			"@id": url,
		},
		"author": {"@type": "Organization", "name": "BlogGen"},
		"publisher": {
			"@type": "Organization",
			"name": "BlogGen",
			"logo": {"@type": "ImageObject", "url": "https://example.com/logo.png"},
		},
	}


def build_seo_meta(
	title: str, description: str, keywords: List[str], og_image: str | None
) -> SEOMeta:
	return SEOMeta(
		title=title,
		description=description,
		keywords=keywords,
		og_title=title,
		og_description=description,
		og_image=og_image,
	)