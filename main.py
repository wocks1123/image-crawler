from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import time
import uuid
import requests
import os

from utils.config import config


def download_image(image_url, dest_path):
    img_data = requests.get(image_url).content

    file_ext = image_url.split(".")[-1]
    if file_ext[-1] != "jpg" or file_ext[-1] != "png":
        file_ext = "jpg"

    file_name = str(uuid.uuid1()) + "." + file_ext

    with open(os.path.join(dest_path, file_name), 'wb') as fp:
        fp.write(img_data)


WAIT_TIME = 0.8 # sec
def to_next(driver, image_area_selector, next_btn_selector):
    driver.implicitly_wait(1)
    time.sleep(WAIT_TIME)
    # 사진
    img_link = driver.find_element_by_css_selector(image_area_selector).get_attribute("src")

    # 이미지 오른쪽화살표 클릭해서 이동
    driver.find_element_by_css_selector(next_btn_selector).click()
    driver.implicitly_wait(1)

    return img_link


def crawling_img_from_google(driver, keyword, count):
    driver.implicitly_wait(0.5)
    driver.get('https://www.google.co.kr/')

    selector = '#tsf > div:nth-child(2) > div.A8SBwf > div.RNNXgb > div > div.a4bIc > input'
    driver.find_element_by_css_selector(selector).send_keys(keyword)
    driver.find_element_by_css_selector(selector).send_keys(Keys.ENTER)
    driver.implicitly_wait(1)
    # 이미지탭 선택
    selector = "#hdtb-msb-vis > div:nth-child(2) > a"
    driver.find_element_by_css_selector(selector).click()

    # 첫 이미지 클릭
    selector = "#islrg > div.islrc > div:nth-child(1) > a.wXeWr.islib.nfEiy.mM5pbd > div.bRMDJf.islir > img"
    driver.find_element_by_css_selector(selector).click()
    time.sleep(2)

    dest_path = os.path.join(config["dest-path"], keyword)
    if os.path.exists(dest_path) is False:
        os.mkdir(dest_path)

    image_area_selector = "#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div.OUZ5W > div.zjoqD > div > div.v4dQwb > a > img"
    next_btn_selector = "#Sva75c > div > div > div.pxAole > div.tvh9oe.BIB1wf > c-wiz > div.OUZ5W > div.zjoqD > div > div.ZGGHx > a.gvi3cf > div"

    for i in range(count):
        print("{:04d} ".format(i), end="")
        try:
            img_link = to_next(driver, image_area_selector, next_btn_selector)
            download_image(img_link, dest_path)
            print("img_link :", img_link)
        except Exception as e:
            print("Error...", e)



def crawling_img_from_naver(driver, keyword, count):
    driver.implicitly_wait(0.5)
    driver.get('https://www.naver.com/')

    # 검색어 입력창
    selector = "#query"
    driver.find_element_by_css_selector(selector).send_keys(keyword)
    driver.find_element_by_css_selector(selector).send_keys(Keys.ENTER)
    driver.implicitly_wait(1)
    # 이미지탭 선택
    selector = "#lnb > div > div.lnb_menu > ul > li.lnb2 > a > span"
    driver.find_element_by_css_selector(selector).click()

    # 첫 이미지 클릭
    selector = "#_sau_imageTab > div.photowall._photoGridWrapper > div.photo_grid._box > div:nth-child(1) > a.thumb._thumb > span.img_border"
    driver.find_element_by_css_selector(selector).click()
    time.sleep(2)

    dest_path = os.path.join(config["dest-path"], keyword + "_naver")
    if os.path.exists(dest_path) is False:
        os.mkdir(dest_path)

    # iamge selector
    image_area_selector = "body > div.image_viewer_wrap._sauImageViewer > div.image_viewer > div.viewer_content._content_wrapper > div > a > img"
    # next btn
    next_btn_selector = "body > div.image_viewer_wrap._sauImageViewer > div.image_viewer > div.viewer_content._content_wrapper > a.btn_next._next"

    for i in range(count):
        print("{:04d} ".format(i), end="")
        try:
            img_link = to_next(driver, image_area_selector, next_btn_selector)
            download_image(img_link, dest_path)
            print("img_link :", img_link)
        except Exception as e:
            print("Error...", e)


if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(config["driver-path"], options=options)
    driver.implicitly_wait(0.5)

    if config["site"] == "google":
        crawling_img_from_google(driver, config["keyword"], config["count"])
    else:
        crawling_img_from_naver(driver, config["keyword"], config["count"])