#pip install requests
#pip install bs4

import requests
from bs4 import BeautifulSoup

import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

classes = ["zCubwf","hgKElc","LTKOO sY7ric","Z0LcW","gsrt vk_bk FzvWSb YwPhnf",
            "pclqee","tw-data-text tw-text-small tw-ta","IZ6rdc",
            "O5uR6d LTKOO","vlzY6d","webanswers-webanswers_table__webanswers-table",
            "dDoNo ikb4Bb gsrt","sXLaOe","LWkfKe","VQF4g","qv3Wpe","kno-rdesc"]

useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

# Scrape data from Google search results
def online_data_scraper(query, print_source=False):  # Use snake_case for function name

    query = query.replace(" + ", " plus ")
    query = query.replace(" - ", " minus ")

    url = "https://www.google.co.in/search?q=" + query
    
    headers = {'User-Agent':useragent}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    for i in classes:
        try:
            result = soup.find(class_=i).get_text(strip=True)  # Strip extra whitespace
            if print_source:
                print(f"{Fore.GREEN}by class {i}")         
                return result
        except AttributeError:  # Handle specific exception
            pass
        except Exception:
            pass

    return None


#print(online_data_scraper("powershell", True))