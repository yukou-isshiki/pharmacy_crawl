from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_argument("")
options.add_argument("--headless")
driver = webdriver.Chrome(executable_path="", options=options)

file = "url_list.txt"

f = open(file, "w")

top_page_url = "https://www.himawari.metro.tokyo.jp/qq13/qqport/tomintop/"

driver.get(top_page_url)

WebDriverWait(driver, 600).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, "button-contents.button-contents-09.button")))

search_btn = driver.find_element_by_css_selector("#section-02 > div.section-main > div.home-contents > ul > li:nth-child(2) > span")

search_btn.click()

WebDriverWait(driver, 600).until(expected_conditions.element_to_be_clickable((By.ID, "ctl00_cphdrBody_uclButton_btnBack")))

next_btn = driver.find_element_by_css_selector("#ctl00_cphdrBody_uclButton_btnNext")

next_btn.click()

WebDriverWait(driver, 600).until(expected_conditions.element_to_be_clickable((By.ID, "ctl00_cphdrBody_uclButton_btnSearch")))

search_btn2 = driver.find_element_by_css_selector("#ctl00_cphdrBody_uclButton_btnSearch")

search_btn2.click()

WebDriverWait(driver, 600).until(expected_conditions.element_to_be_clickable((By.ID, "contents")))

pharmacy_conut = int(driver.find_element_by_css_selector("#ctl00_cphdrBody_lblCurrentPage").text.split("件")[0])

for i in range((pharmacy_conut // 20)):
    result_html = driver.page_source
    result_soup = BeautifulSoup(result_html, "html.parser")
    url_text_list = result_soup.select("#ctl00_cphdrBody_divSearchResult > div > table > thead > tr > th > h3 > a")
    for url_text_info in url_text_list:
        url_text = f"https://www.himawari.metro.tokyo.jp{url_text_info.get('href')}"
        f.write(url_text)
        f.write("\n")

    next_page_btn = driver.find_element_by_css_selector(f"#ctl00_cphdrBody_uclPageLink2_LinkNext{i+2}")
    next_page_btn.click()

driver.quit()