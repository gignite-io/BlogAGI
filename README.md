# BlogGen

A FastAPI + React application for SEO + GEO optimized blog generation, designed to integrate with AgnoOS via the `agno-main/cookbook`.

## Structure
- `api/` — FastAPI service (with SEO, JSON-LD, localization)
- `client/` — React UI (Vite + TypeScript)
- `tests/` — API tests (pytest)
- `docs/` — Additional docs
- `cookbook/` — Placeholder docs for AgnoOS integration (external repo recommended)

## Run the API
```bash
# From repo root
python3 -m venv .venv && source .venv/bin/activate || true
python -m pip install -r api/requirements.txt
uvicorn app.main:app --reload --port 8000 --app-dir api
```

If `venv` is unavailable on your system, install requirements to user site packages:
```bash
python3 -m pip install --user -r api/requirements.txt
python3 -m uvicorn app.main:app --reload --port 8000 --app-dir api
```

## Run the Client
```bash
cd client
npm i
npm run dev
```
Open http://localhost:5173

## AgnoOS Integration
Optionally set the path to your Agno cookbook before starting the API:
```bash
export BLOGGEN_AGNO_COOKBOOK_PATH=/absolute/path/to/agno-main/cookbook
```
The adapter is in `api/app/services/adapter_agno.py`. Wire your agents/teams as needed.

## Tests
```bash
pytest -q
```

## API Reference
POST `/api/v1/blog/generate` — generate an SEO + GEO optimized blog post.
- Request: `topic`, `keywords[]`, `target_language`, `location`, `tone`, `reading_level`, `words`, `include_html`, `images_enabled`, `num_images`
- Response: `title`, `slug`, `content_markdown`, `content_html`, `images[]`, `seo`, `jsonld`, `locale`