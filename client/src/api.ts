export type BlogRequest = {
	topic: string;
	keywords: string[];
	target_language: string;
	location: string;
	tone: string;
	reading_level: string;
	words: number;
	include_html: boolean;
	images_enabled: boolean;
	num_images: number;
};

const API_BASE = (import.meta as any).env.VITE_API_BASE || "http://localhost:8000";

export async function generateBlog(req: BlogRequest) {
	const res = await fetch(`${API_BASE}/api/v1/blog/generate`, {
		method: "POST",
		headers: { "Content-Type": "application/json" },
		body: JSON.stringify(req),
	});
	if (!res.ok) {
		throw new Error(`API error: ${res.status}`);
	}
	return res.json();
}