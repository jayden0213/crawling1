import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

baseUrl = 'https://search.naver.com/search.naver?sm=tab_dts&where=article&query='
plusUrl1 = input('검색어를 입력하세요: ')
plusUrl2 = input('상세 검색어를 입력하세요: ')
url = baseUrl + urllib.parse.quote_plus(plusUrl1) + urllib.parse.quote_plus('&#34;' + plusUrl2 + '&#34;')

html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_cafe_title')

for i in title:
    print(i.text.strip())
    print(i.attrs['href'])
    print()
