from function.autoplius_scraper import autoplius_scraper
from bs4 import BeautifulSoup
import requests
import pytest
import pandas as pd

url = "https://en.autoplius.lt/ads/used-cars?page_nr=1"

def test_getPageNo():
    scraper = autoplius_scraper()
    assert scraper.getPageNo(100) == 5

def test_scrape_page():
    scraper = autoplius_scraper()
    scraped_webpage = scraper.scrape_page(url)
    assert isinstance(scraped_webpage, BeautifulSoup)

def test_into_pandas():
    scraper = autoplius_scraper()
    pandas_dataframe = scraper.into_pandas()
    isinstance(pandas_dataframe, pd.DataFrame)

def test_into_csv():
    scraper = autoplius_scraper()
    # scraper.scrape_page(url)
    # scraper.find_announcements()
    # scraper.scrape_details()
    scraper.into_pandas()
    assert scraper.into_csv() == "Pandas dataframe has been successfully exported to the directory as autoplius.csv"

