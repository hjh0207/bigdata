import requests	
from bs4 import BeautifulSoup	

#다음 영화 정보 가져오는 함수
def get_dmv():
    #리스트로 함수 밖으로 전달 시킬 변수
    m_list = list() #영화정보 리스트 변수 선언

    headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}	
    data = requests.get('https://movie.daum.net/ranking/reservation',headers=headers)	
        
    soup = BeautifulSoup(data.text, 'html.parser')	

    movielist = soup.select(".tit_item")
    rank = 0
    movie_list = soup.select(".thumb_cont")
    for tr in movie_list:
        rank = rank + 1	
        a_tag = tr.select_one("a")	
        txt_grade = tr.select_one("span.txt_grade")	
        txt_num = tr.select_one("span.txt_num")
        txt_date = tr.select_one(".txt_info > span.txt_num")
        m_list.append([rank, a_tag.text, txt_grade.text, txt_num.text, txt_date.text])
    
return m_list