import os
import sys
from fastapi.testclient import TestClient

sys.path.append(os.path.abspath("api"))
from app.main import app  # noqa: E402

client = TestClient(app)


def test_generate_blog_minimal():
	payload = {
		"topic": "Sustainable Tourism",
		"keywords": ["eco travel", "local culture", "carbon footprint"],
		"target_language": "en",
		"location": "US",
		"tone": "informative",
		"reading_level": "general",
		"words": 600,
		"include_html": True,
		"images_enabled": True,
		"num_images": 2,
	}
	resp = client.post("/api/v1/blog/generate", json=payload)
	assert resp.status_code == 200, resp.text
	data = resp.json()
	assert "content_markdown" in data
	assert "content_html" in data
	assert data["seo"]["title"]
	assert data["jsonld"]["@type"] == "BlogPosting"
	assert data["images"] == [] or isinstance(data["images"][0]["alt"], str)


def test_generate_blog_locale():
	payload = {
		"topic": "Festival Foods",
		"keywords": [],
		"target_language": "es",
		"location": "MX",
		"tone": "friendly",
		"reading_level": "general",
		"words": 400,
		"include_html": False,
		"images_enabled": False,
		"num_images": 0,
	}
	resp = client.post("/api/v1/blog/generate", json=payload)
	assert resp.status_code == 200
	data = resp.json()
	assert data["locale"] == "es-MX"
	assert data["content_html"] == ""