import crawler
from bs4 import BeautifulSoup

def getCountries(refresh=False):
    urls = [
        "https://temporary-phone-number.com/countrys/",
        "https://temporary-phone-number.com/countrys/page2"
        ]

    if(refresh):
        html1 = crawler.get(urls[0])
        html2 = crawler.get(urls[1])
        crawler.write("cpage1", html1)
        crawler.write("cpage2", html2)
    else:
        html1 = crawler.load("cpage1")
        html2 = crawler.load("cpage2")

    countries_p1 = fetch_countries(html1)
    countries_p2 = fetch_countries(html2)
    
    return countries_p1 + countries_p2

def fetch_countries(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div","col-sm-6 col-md-4 col-lg-3 col-xs-12")
    countries = []
    for item in items:
        link = item.a.attrs["href"]
        name = item.find('span','info-box-number').text
        countries.append({
            "name":name,
            "link":link
        })
    
    return countries