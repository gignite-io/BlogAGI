# BlogGen

BlogGen is a FastAPI + React application that provides SEO + GEO optimized blog generation. It is designed to integrate with AgnoOS (via the `agno-main/cookbook`) and remains modular for future features (social posts, newsletters).

## Quickstart

### API
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r api/requirements.txt
uvicorn app.main:app --reload --port 8000 --app-dir api
```

Optional: integrate Agno cookbook
```bash
export BLOGGEN_AGNO_COOKBOOK_PATH=/absolute/path/to/agno-main/cookbook
```

### Client
```bash
cd client
npm i
npm run dev
```

Open http://localhost:5173

## API

POST `/api/v1/blog/generate`
- Request: topic, keywords[], target_language, location, tone, reading_level, words, include_html, images_enabled, num_images
- Response: title, slug, content_markdown, content_html, images[], seo, jsonld, locale

## Architecture

- Modular FastAPI with versioned routing (`/api/v1`)
- Middleware: logging + global exception handler
- SEO: JSON-LD `BlogPosting`, OpenGraph, slugging, localized notes
- AgnoOS integration: `app/services/adapter_agno.py` (stubbed; wire to your agents/teams/tools)
- Client: minimal React UI for generation, preview, copy, download

## Tests
```bash
pytest -q
```