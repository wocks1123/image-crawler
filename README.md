# image-crawler
- selenium기반 이미지 크롤러

- 입력 키워드를 검색하여 해당하는 이미지를 google이나 naver 이미지에서 다운로드한다.

## env

- `Windows10`
- `python3.6`

- 필요 모듈은 `requirements.txt`에 포함



## 사용법

### command line

- `main.py` 실행

- driver-path : chrome web driver가 설치된 경로
- keyword : 검색어
- dest-path : 이미지를 저장할 경로. dest_path + keyword의 경로에 이미지를 저장한다.
- count : 검색해서 저장할 이미지 수
- site : google, naver 중 하나 선택(default=google)

ex

```bash
python main.py --driver-path="D:/etc/chromedriver" --keyword="자동차" --dest-path="D:/DB/data" --count=5 --site="google"
```



### Driver 설치

selenium을 사용하기 위해서는 브라우저의 webdriver가 필요하다. 크롬 브라우저를 사용할 것이기 때문에 chrome web driver를 설치해준다. 설치는 [링크](https://sites.google.com/a/chromium.org/chromedriver/downloads)에서 할 수 있다.

![0000](https://i.imgur.com/0yG730c.png)

컴퓨터에 설치된 크롬 브라우저 버전에 해당하는 것을 선택한다. 크롬의 버전 확인은 `설정`에서 볼 수 있다. 크롬 버전을 선택하고, 자신의 OS에 맞는 버전을 설치하면 된다.





### selenuim 기본 코드(참고)

```
from selenium import webdriver

driver = webdriver.Chrome('C:/etc/Downloads/chromedriver')
driver.implicitly_wait(3)
driver.get('https://nid.naver.com/nidlogin.login')
# 아이디/비밀번호를 입력해준다.
driver.find_element_by_name('id').send_keys('naver_id')
driver.find_element_by_name('pw').send_keys('mypassword1234')
driver.find_element_by_name('id').click()
```
