import crawler
from bs4 import BeautifulSoup


def get(name, link, page, refresh=False):  
    if(refresh):
        html = crawler.get(link)
        crawler.write(name+"_"+page, html)
    else:
        html = crawler.load(name+"_"+page)
    
    return html
        
def getLastPage(html):
    no = crawler.getLastPageNo(html)
    return int(no)

def fetchNumbers(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all("div","col-sm-6 col-md-4 col-lg-3 col-xs-12")
    numbers = []
    for item in items:
        try:
            num = {}
            link = item.find("a").attrs["href"]
            num["link"] = link
            num["country"] = item.find("span", "info-box-text").text
            num["number"] = item.find("span", "info-box-number").text
            numbers.append(num)
        except Exception as e:
            print(e)
    return numbers
    
    