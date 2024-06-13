import os
import aiohttp

from bs4 import BeautifulSoup
from typing import Dict


async def fetch_content(article_url: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(article_url) as response:
            if response.status == 200:
                content = await response.read()
                return content
            else:
                print(f"Error fetching content: {url}")
                return None


async def parse_times_of_india(article_url: str) -> Dict[str, str]:
    response = dict()
    content = await fetch_content(article_url)
    soup = BeautifulSoup(content, "html.parser")
    content = soup.find(attrs={"class": "_s30J clearfix"})
    if content is not None:
        response["title"] = soup.find('h1').get_text()
        response["content"] = soup.find(attrs={'class': '_s30J clearfix'}).get_text()
        return response
    else:
        return None
