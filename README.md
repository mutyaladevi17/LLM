### Website Summarizer (Notebook)

This project is a small **website-to-summary** tool built in a Jupyter notebook. The code:
- Fetches a webpage’s text (strips scripts/styles/noise)
- Sends the cleaned text to a **local Ollama model** via the OpenAI Python SDK
- Displays a short, humorous **markdown summary** (prompt is currently finance-focused)

---

### What’s in this folder

- **`Website_summarizer.ipynb`**: Main notebook (scrape → summarize → render markdown)
- **`scraper.py`**: Fetches a URL and extracts readable text using BeautifulSoup

---

### Requirements

- Python 3.9+
- A running **Ollama** server (the notebook uses `base_url="http://localhost:11434/v1"`)

Python packages used:
- `openai`
- `requests`
- `beautifulsoup4`
- `lxml`
- `python-dotenv`
- `ipython` (for markdown display in notebooks)

Example install:

```
pip install openai requests beautifulsoup4 lxml python-dotenv ipython
```
or
```
sudo apt openai requests beautifulsoup4 lxml python-dotenv ipython
```
---
### Setup (Ollama)

1. Install Ollama and start it.
2. Pull a model (the notebook example uses `phi3:latest`).

Example:

```
ollama pull phi3:latest
```
---
### How to use

1. Open **`Website_summarizer.ipynb`**.
2. Run the cells to define:
   - The Ollama OpenAI-compatible client (`base_url="http://localhost:11434/v1"`)
   - The summarization prompt
   - `display_summary(url, model)`
3. Call:
```
display_summary(
    url="https://example.com/some-article",
    model="phi3:latest")
```
The summary is returned as **markdown** and rendered directly in the notebook.

---

### Recommendation: use a bigger model for better summaries

Smaller models (like `phi3`) can be fast, but they may miss nuance, context, or key details—especially on long or complex pages.

For **more accurate summaries**, try a **larger model** in Ollama (examples: `llama3.1:8b`, `qwen2.5:7b`, or larger variants if your machine can handle them).  
Just swap the `model="..."` argument in `display_summary(...)`.

---

### Notes / limitations

- Pages that rely heavily on client-side JavaScript, require logins, or are paywalled may not scrape cleanly.
- The prompt is currently written as a “financial market analysis assistant”; edit `system_prompt` in the notebook to match your topic and tone.
- Be mindful of site terms/robots policies when scraping.