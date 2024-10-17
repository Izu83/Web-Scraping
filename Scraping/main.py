from fastapi import FastAPI, HTTPException, Query
import requests
from bs4 import BeautifulSoup

app = FastAPI()

@app.get("/scrape")
async def scrape(url: str = Query(..., description="The URL to scrape")):
    try:
        response = requests.get(url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title.string if soup.title else "No title found"
        
        paragraphs = [p.get_text() for p in soup.find_all("p", limit=3)]

        return {
            "url": url,
            "title": title,
            "paragraphs": paragraphs
        }
    except requests.RequestException as e:
        raise HTTPException(status_code=400, detail=f"Failed to fetch the URL: {e}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occured: {e}")