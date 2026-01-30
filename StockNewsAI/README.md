# Company Stock News Summarizer

An intelligent tool that automatically scrapes financial websites, filters relevant news links, and generates comprehensive stock news summaries for companies using OpenAI's GPT models.

## Overview

This project uses AI to analyze financial websites (like Yahoo Finance) and create detailed summaries of company stock news. It intelligently:
- Filters relevant links from finance websites
- Extracts content from multiple news sources
- Generates comprehensive, well-structured summaries

## Features

- **Intelligent Link Filtering**: Uses GPT-5-nano to identify and prioritize the most relevant financial news links (up to 10 links)
- **Content Extraction**: Automatically fetches and processes content from multiple news sources
- **Comprehensive Summaries**: Generates detailed markdown-formatted summaries using GPT-4.1-mini
- **Error Handling**: Gracefully handles failed link fetches and provides status updates
- **Smart Filtering**: Excludes irrelevant content like ads, terms of service, and promotional pages

## Requirements

### Python Packages

- `openai` - OpenAI API client
- `beautifulsoup4` - HTML parsing
- `requests` - HTTP requests
- `python-dotenv` - Environment variable management
- `IPython` - Jupyter notebook display utilities

### API Key

You need an OpenAI API key to use this tool. The API key should:
- Start with `sk-proj-`
- Be stored in a `.env` file as `OPENAI_API_KEY`

## Installation

1. Clone or navigate to this directory:
```bash
cd StockNewsAI
```

2. Install required packages:
```bash
pip install openai beautifulsoup4 requests python-dotenv ipython
```

3. Create a `.env` file in the project directory:
```bash
echo "OPENAI_API_KEY=your_api_key_here" > .env
```

Replace `your_api_key_here` with your actual OpenAI API key.

## Usage

### Basic Usage

Open the Jupyter notebook `cOMPANY_STOCK_SUMMARIZER.ipynb` and run the cells:

```python
# Example: Generate a summary for Apple
create_news_summary("Apple", "https://finance.yahoo.com/")
```

### Function Reference

#### `select_relevant_links(company_name, url)`
Filters and selects up to 10 relevant financial news links from a given website.

**Parameters:**
- `company_name` (str): Name of the company to analyze
- `url` (str): Base URL of the finance website (e.g., Yahoo Finance stock page)

**Returns:**
- Dictionary with filtered links and their types

#### `fetch_content_from_all_relevant_links(company_name, url)`
Fetches content from all relevant links identified for a company.

**Parameters:**
- `company_name` (str): Name of the company
- `url` (str): Base URL of the finance website

**Returns:**
- Markdown-formatted string containing all fetched content

#### `create_news_summary(company_name, url)`
Main function that generates a comprehensive stock news summary.

**Parameters:**
- `company_name` (str): Name of the company to summarize
- `url` (str): Base URL of the finance website

**Returns:**
- Displays a formatted markdown summary in the notebook

### Example

```python
# Generate summary for Microsoft
create_news_summary("Microsoft", "https://finance.yahoo.com/quote/MSFT")

# Generate summary for Apple
create_news_summary("Apple", "https://finance.yahoo.com/")
```

## How It Works

1. **Link Discovery**: The tool first extracts all links from the provided finance website URL
2. **AI-Powered Filtering**: GPT-5-nano analyzes the links and selects up to 10 most relevant ones, prioritizing:
   - Company stock news and price movements
   - Financial reports and earnings
   - Company announcements
   - Competitor analysis
   - Industry trends
   - Market analysis
3. **Content Extraction**: The scraper module fetches content from each selected link
4. **Summary Generation**: GPT-4.1-mini analyzes all collected content and generates a comprehensive, well-structured summary

## Project Structure

```
StockNewsAI/
├── cOMPANY_STOCK_SUMMARIZER.ipynb  # Main notebook
├── scraper.py                            # Web scraping utilities
├── README.md                             # This file
└── .env                                  # API key configuration (create this)
```

## Dependencies

### scraper.py Functions

- `fetch_website_links(url)`: Extracts all links from a webpage
- `fetch_website_contents(url)`: Fetches and cleans content from a webpage

## Models Used

- **GPT-5-nano**: Used for intelligent link filtering and selection
- **GPT-4.1-mini**: Used for generating comprehensive news summaries

## Notes

- The tool truncates content to 5,000 characters before summarization to manage token limits
- Failed link fetches are reported but don't stop the summarization process
- The scraper uses standard browser headers to avoid blocking
- Content is cleaned to remove scripts, styles, and other non-text elements

## Troubleshooting

### API Key Issues

If you see "There might be a problem with your API key":
1. Check that your `.env` file exists and contains `OPENAI_API_KEY=your_key`
2. Verify your API key starts with `sk-proj-` and is valid
3. Ensure you're running from an activated environment

### Import Errors

If imports fail:
- Make sure you're running from an activated environment (should show `(llms)` in prompt)
- Verify all required packages are installed: `pip install -r requirements.txt` (if available)



