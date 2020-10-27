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

file1 = "url_list.txt"

f1 = open(file1, "r")

lines = f1.readlines()

file2 = "pharmacy_data.tsv"

f2 = open(file2, "w")

for url in lines:
    result_list = []
    print(url)
    driver.get(url)
    WebDriverWait(driver, 600).until(
        expected_conditions.element_to_be_clickable((By.ID, "ctl00_pnlContents")))
    result_btn = driver.find_element_by_css_selector("#ctl00_pnlContents > ul > li:nth-child(6) > a")
    result_btn.click()
    WebDriverWait(driver, 600).until(
        expected_conditions.element_to_be_clickable((By.ID, "ctl00_pnlContents")))
    result_html = driver.page_source
    result_soup = BeautifulSoup(result_html, "html.parser")
    pharmacy_name = result_soup.select("#ctl00_cphdrHeader_lblKikanRname")[0].text
    result_list.append(pharmacy_name)
    try:
        medicine_item_count = result_soup.select("#ctl00_cphdrBody_uclDetailIryoIyakuhin3_lblIryojissekiNaiyo0")[0].text[1:-2].replace(",","")
        result_list.append(medicine_item_count)
        result_data = "\t".join(result_list)
        print(result_data)
        f2.write(result_data)
        f2.write("\n")
    except IndexError:
        pass

driver.quit()