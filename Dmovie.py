import requests	
from bs4 import BeautifulSoup	
	
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}	
data = requests.get('https://movie.daum.net/ranking/boxoffice/weekly',headers=headers)	
	
soup = BeautifulSoup(data.text, 'html.parser')	

movielist = soup.select(".tit_item")
for tr in movielist:
    a_tag = tr.select_one("a")
    print(a_tag.text)