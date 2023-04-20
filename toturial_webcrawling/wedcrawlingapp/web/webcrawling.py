from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class WebCrawling :
    # 멤버 변수 정의하기 : 클래스 내의 영역에서 사용 가능 
    driver = "" # 문자열은 아니나 그냥 넣음 
    # 생성자 
    def __init__(self,url) :
        self.url = url 
    # 웹크롤링 데이터 조회하기 
    def getData(self) :
        file_path = "c:/ChromeDriver_exe/chrome_109_driver.exe"
        #url = "http://www.melon.com/chart/index.htm"
        driver = webdriver.Chrome(file_path)
        driver.get(self.url)

        titles = driver.find_elements(By.CSS_SELECTOR,"tr div.ellipsis.rank01 > span > a")[0:10]
        singers = driver.find_elements(By.CSS_SELECTOR,"tr div.ellipsis.rank02 > a")[0:10]
        
        melon_list = []
        for i in range (0, len(titles), 1 ) :
            melon_list.append(dict(zip(['no','title','singer'],[i+1,titles[i].text,singers[i].text])))
        
        self.driver = driver 
        
        return melon_list
    
    # 웹드라이버 종료하기  
    def webdriver_quit(self) :
        time.sleep(3)
        self.driver.quit()