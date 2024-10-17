# FastAPI Web Scraping API

This project is a **Web Scraping API** built using **FastAPI**. The main purpose of this API is to scrape a given URL, extract relevant information, and make this data easily accessible for other applications or services. In the future, the project aims to integrate with a **Large Language Model (LLM)** like ChatGPT to enable intelligent querying of the scraped data.

## Project Overview

- **API Framework:** FastAPI
- **Web Scraping Tools:** Requests and BeautifulSoup
- **Future Integration:** LLM (like ChatGPT)

The idea is to create an API that can take a URL from the user, scrape the webpage for useful information (like titles, paragraphs, and other content), and return that information in a structured format. Eventually, we aim to use a language model that can understand and answer questions based on the scraped data.

## Features

- **Scrape a Given URL:** Users can provide a URL, and the API will fetch and extract the page's content.
- **Clean and Structured Data:** The API returns the page's title and key paragraphs in JSON format.
- **Easy Integration:** Designed to be easily integrated with other applications, like chatbots or AI services.

## How It Works

1. **User provides a URL** through the API endpoint.
2. The API **scrapes the web page** using tools like `requests` and `BeautifulSoup`.
3. It extracts the **title and key paragraphs** from the webpage.
4. The data is returned in **JSON format** for easy processing.
5. **Future Integration:** The scraped data can be fed into an LLM like ChatGPT to allow for more intelligent querying of the information.

## Future Plans

- **LLM Integration:** Integrate with a large language model to allow users to ask questions like "What's the main idea of this page?" or "Summarize this content for me."
- **Enhanced Scraping Capabilities:** Improve the scraping logic to handle more complex page structures and extract richer content.
- **Authentication:** Add authentication and rate limiting to secure the API.

## Getting Started

### Prerequisites

Make sure you have the following installed:
- **Python 3.8+**
- **FastAPI**: `pip install fastapi`
- **Uvicorn** (for running the server): `pip install uvicorn`
- **BeautifulSoup and Requests**: `pip install beautifulsoup4 requests`

### Running the Project

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fastapi-web-scraper.git
   cd fastapi-web-scraper

2. Start the fastapi server
   ```bash
   uvicorn main:app --reload

3. Acces the API documentation at:
    ```arudinio
    http://127.0.0.1:8000/docs

