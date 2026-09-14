from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
from database import save_data

#创建浏览器
def create_browser():
    options = Options()
    options.add_argument('--no-sandbox')
    options.add_experimental_option('detach',True)
    service = Service(ChromeDriverManager().install())
    a1 = webdriver.Chrome(service=service,options=options)
    a1.implicitly_wait(10)
    return a1


def open_browser(a1,url):
    a1.get(url)
    print("页面打开成功。")
    time.sleep(2)
    data_frame = a1.find_elements(By.XPATH,'//div[contains(@class,"video-card")]')
    print(f'找到{len(data_frame)}条数据。')
    if len(data_frame) > 0:
        find_element(a1)
    else:
        print("没有找到数据。")
        pass

def find_element(a1):
    video_list =[]
    title_elements = a1.find_elements(By.XPATH, '//p[contains(@class,"video-name")]')
    up_name_elements = a1.find_elements(By.XPATH,'//span[contains(@class,"up-name__text")]')
    v_count_elements = a1.find_elements(By.XPATH, '//span[contains(@class,"play-text")]')
    l_name_elements = a1.find_elements(By.XPATH, '//span[contains(@class,"like-text")]')
    for title,up,v_count,l_count in zip(title_elements,up_name_elements,v_count_elements,l_name_elements):
        item ={
            "标题":title.text,
            "up主":up.text,
            "播放量":v_count.text,
            "点赞数":l_count.text
        }
        video_list.append(item)
    print(f'采集了{len(video_list)}条数据。')
    save_data(video_list)



if __name__ == '__main__':
    url ='https://www.bilibili.com/v/popular/all?spm_id_from=333.1007.0.0'
    a1 = create_browser()
    open_browser(a1,url)
