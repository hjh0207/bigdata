import requests	
from bs4 import BeautifulSoup	
	
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}	
data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)	
	
soup = BeautifulSoup(data.text, 'html.parser')	

movielist = soup.select(".tit_item")
rank = 0
for tr in movielist:
    a_tag = tr.select_one("a")	
    rank = rank + 1	
    print(f'{rank}위 {a_tag.text}')	