import os
from typing import Optional, Any, Dict
from app.core.config import get_settings


class AgnoAdapter:
	def __init__(self):
		self._available = False
		self._cookbook_path: Optional[str] = None
		self._init_from_env()

	def _init_from_env(self):
		settings = get_settings()
		path = settings.agno_cookbook_path or os.getenv("BLOGGEN_AGNO_COOKBOOK_PATH")
		if path and os.path.isdir(path):
			self._cookbook_path = path
			self._available = True
		else:
			self._available = False

	def is_available(self) -> bool:
		return self._available

	def generate_blog(self, request: Dict[str, Any]) -> Optional[Dict[str, Any]]:
		if not self._available:
			return None
		# TODO: Import and invoke agno cookbook pipelines here.
		return None


adapter = AgnoAdapter()