from countries_crawler import getCountries
from numbers_crawler import get, getLastPage, fetchNumbers


countries = getCountries(refresh=False)
ct = countries[0]

pages = {"1":ct["link"]}

html = get(ct["name"], ct["link"], "1", refresh=False)
total_pages = getLastPage(html)
numbers = fetchNumbers(html)
print(numbers)