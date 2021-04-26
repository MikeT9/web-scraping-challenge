from selenium import webdriver
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape():
    # Set up Splinter
    driver = webdriver.Chrome(ChromeDriverManager().install())

    # Visit url
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    driver.get(url)

    html= driver.page_source
    soup = bs(html)

    news_title_div = soup.find('div', id="content_title")
    
    news_p_div = soup.find('div', id="article_teaser_body")

    # import ipdb; ipdb.set_trace()
    news_title = news_title_div.find_all('strong')[0].text

    news_p = news_p_div.find_all('strong')[0].text

    driver.close()

     # Visit url
    url = "https://data-class-jpl-space.s3.amazonaws.com/JPL_Space/index.html"
    driver.get(url)

    html= driver.page_source
    soup = bs(html)

    news_title_div = soup.find('div', id="content_title")
    
    news_p_div = soup.find('div', id="article_teaser_body")

    # import ipdb; ipdb.set_trace()
    news_title = news_title_div.find_all('strong')[0].text

    news_p = news_p_div.find_all('strong')[0].text

    driver.close()
    

if __name__ == "__main__":
    print(scrape_info() )