from bs4 import BeautifulSoup
import requests
import re


# # Standard headers to fetch a website
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36"
}


def fetch_website_contents(url: str, timeout: int = 20) -> str:
    try:
        resp = requests.get(url, headers=headers, timeout=timeout)
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "html.parser")
        title = soup.title.string if soup.title else "No title found"

        for tag in soup(["script", "style", "noscript", "svg"]):
            tag.decompose()

        text = soup.get_text(separator="\n")
        lines = [re.sub(r"\s+", " ", line).strip() for line in text.splitlines()]
        lines = [line for line in lines if line]
        content = "\n".join(lines)
        
        # Include title at the beginning
        return f"{title}\n\n{content}"
    
    except requests.exceptions.HTTPError as e:
        return f"Error: Could not fetch content from {url} - HTTP {e.response.status_code} ({e.response.reason})"
    except requests.exceptions.RequestException as e:
        return f"Error: Could not fetch content from {url} - {str(e)}"
    except Exception as e:
        return f"Error: Unexpected error fetching {url} - {str(e)}"



def fetch_website_links(url):
    """
    Return the links on the webiste at the given url
    I realize this is inefficient as we're parsing twice! This is to keep the code in the lab simple.
    Feel free to use a class and optimize it!
    """
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    links = [link.get("href") for link in soup.find_all("a")]
    return [link for link in links if link]


