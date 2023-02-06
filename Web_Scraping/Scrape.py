# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in a dictionary
    data = {
        "news_title": news_title,
        "news_paragraph": news_paragraph,
        "featured_image": featured_image(browser),
        "facts": mars_facts(),
        "last_modified": dt.datetime.now(),
        "hemi_images": mars_hemisphers(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data


def mars_news(browser):

   # Visit the mars nasa news site
    url = 'https://redplanetscience.com/'
    browser.visit(url)

   # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

   # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    try:
       slide_elem = news_soup.select_one('div.list_text')
       slide_elem.find('div', class_='content_title')

       # Use the parent element to find the first <a> tag and save it as  `news_title`
       news_title = slide_elem.find('div', class_='content_title').get_text()

       # Use the parent element to find the paragraph text
       news_p = slide_elem.find('div', class_='article_teaser_body').get_text()

    except AttributeError:
        return None, None
    return news_title, news_p

def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    # Add try/except for error handling
    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base url to create an absolute url
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes='table table-dark')

def mars_hemisphers(browser):
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    html = browser.html
    initial_soup = soup(html, 'html.parser')
    hemi_soup = initial_soup.find_all('div', attrs={'class': 'item'})
    hemi_links = []
    [hemi_links.append(i.a['href']) for i in hemi_soup]
    pic_links = []
    for i in hemi_links:
        pic_url = f'https://astrogeology.usgs.gov{i}'
        browser.visit(pic_url)
        html1 = browser.html
        img_soup = soup(html1, 'html.parser')
        img_src = img_soup.find('div', attrs={'class': 'downloads'})
        img_name = img_soup.find('h2', attrs={'class': 'title'}).text
        pic_links.append({"Image_name": img_name, "Image_URL": img_src.ul.li.a["href"]})

    return pic_links


