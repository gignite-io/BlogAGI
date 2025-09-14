import { useState } from "react";
import { generateBlog, type BlogRequest } from "./api";

type BlogResponse = {
	title: string;
	slug: string;
	content_markdown: string;
	content_html: string;
	images: { url: string; alt: string }[];
	seo: { title: string; description: string; keywords: string[]; og_image?: string };
	jsonld: object;
	locale: string;
};

export default function App() {
	const [topic, setTopic] = useState("Sustainable Tourism");
	const [keywords, setKeywords] = useState("eco travel, local culture, carbon footprint");
	const [language, setLanguage] = useState("en");
	const [location, setLocation] = useState("US");
	const [tone, setTone] = useState("informative");
	const [readingLevel, setReadingLevel] = useState("general");
	const [words, setWords] = useState(800);
	const [imagesEnabled, setImagesEnabled] = useState(true);
	const [numImages, setNumImages] = useState(2);
	const [loading, setLoading] = useState(false);
	const [result, setResult] = useState<BlogResponse | null>(null);
	const [error, setError] = useState<string | null>(null);
	const [tab, setTab] = useState<"preview" | "markdown">("preview");

	async function onSubmit(e: React.FormEvent) {
		e.preventDefault();
		setLoading(true);
		setError(null);
		setResult(null);
		try {
			const req: BlogRequest = {
				topic,
				keywords: keywords.split(",").map(k => k.trim()).filter(Boolean),
				target_language: language,
				location,
				tone,
				reading_level: readingLevel,
				words,
				include_html: true,
				images_enabled: imagesEnabled,
				num_images: numImages,
			};
			const data = await generateBlog(req);
			setResult(data);
		} catch (err: any) {
			setError(err?.message || "Unknown error");
		} finally {
			setLoading(false);
		}
	}

	function copyMarkdown() {
		if (!result) return;
		navigator.clipboard.writeText(result.content_markdown);
	}

	function downloadMarkdown() {
		if (!result) return;
		const blob = new Blob([result.content_markdown], { type: "text/markdown" });
		const link = document.createElement("a");
		link.href = URL.createObjectURL(blob);
		link.download = `${result.slug || "post"}.md`;
		link.click();
	}

	return (
		<div style={{ maxWidth: 1000, margin: "24px auto", padding: 16, fontFamily: "system-ui, sans-serif" }}>
			<h1>BlogGen</h1>
			<form onSubmit={onSubmit} style={{ display: "grid", gap: 12, gridTemplateColumns: "1fr 1fr" }}>
				<label style={{ gridColumn: "1 / -1" }}>
					Topic
					<input value={topic} onChange={e => setTopic(e.target.value)} required style={{ width: "100%" }} />
				</label>
				<label style={{ gridColumn: "1 / -1" }}>
					Keywords (comma-separated)
					<input value={keywords} onChange={e => setKeywords(e.target.value)} style={{ width: "100%" }} />
				</label>
				<label>
					Language
					<input value={language} onChange={e => setLanguage(e.target.value)} />
				</label>
				<label>
					Location
					<input value={location} onChange={e => setLocation(e.target.value)} />
				</label>
				<label>
					Tone
					<input value={tone} onChange={e => setTone(e.target.value)} />
				</label>
				<label>
					Reading level
					<input value={readingLevel} onChange={e => setReadingLevel(e.target.value)} />
				</label>
				<label>
					Words
					<input type="number" value={words} onChange={e => setWords(parseInt(e.target.value || "0", 10))} />
				</label>
				<label>
					Images
					<input type="checkbox" checked={imagesEnabled} onChange={e => setImagesEnabled(e.target.checked)} />
				</label>
				<label>
					Num images
					<input type="number" value={numImages} onChange={e => setNumImages(parseInt(e.target.value || "0", 10))} />
				</label>
				<div style={{ gridColumn: "1 / -1" }}>
					<button type="submit" disabled={loading}>{loading ? "Generating..." : "Generate"}</button>
				</div>
			</form>

			{error && <p style={{ color: "crimson" }}>{error}</p>}

			{result && (
				<div style={{ marginTop: 24 }}>
					<div style={{ display: "flex", gap: 8 }}>
						<button onClick={() => setTab("preview")} disabled={tab === "preview"}>Preview</button>
						<button onClick={() => setTab("markdown")} disabled={tab === "markdown"}>Markdown</button>
						<div style={{ flex: 1 }} />
						<button onClick={copyMarkdown}>Copy</button>
						<button onClick={downloadMarkdown}>Download</button>
					</div>
					<h2>{result.seo.title}</h2>
					<p>{result.seo.description}</p>
					{tab === "preview" ? (
						<div dangerouslySetInnerHTML={{ __html: result.content_html }} />
					) : (
						<pre style={{ whiteSpace: "pre-wrap" }}>{result.content_markdown}</pre>
					)}
				</div>
			)}
		</div>
	);
}