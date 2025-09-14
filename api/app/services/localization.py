from typing import Tuple

def resolve_locale(language: str, location: str) -> str:
	lang = (language or "en").split("-")[0].lower()
	loc = (location or "US").upper()
	return f"{lang}-{loc}"


def localized_note(locale: str) -> str:
	primary = locale.split("-")[0]
	examples = {
		"en": "All prices and references use local conventions.",
		"es": "Precios y referencias según convenciones locales.",
		"fr": "Prix et références selon les conventions locales.",
		"de": "Preise und Referenzen nach lokalen Gepflogenheiten.",
	}
	return examples.get(primary, "Localized for regional context and culture.")