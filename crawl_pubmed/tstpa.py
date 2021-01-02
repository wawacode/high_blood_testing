from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from lxml import html
from mypage.settings import BASE_DIR
from translate import Translator
import os
driver=webdriver.Firefox()
driver.get("https://pubmed.ncbi.nlm.nih.gov/?term=hyptertension")
#下面这句话就是让浏览器等待5秒
wait=WebDriverWait(driver,5)
#自动化测试
#让页面等到什么时间的方法until
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".ds1>ul>li:nth-child(1)"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".dropdown-block>button"))).click()
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,".per-page-container>select>option:nth-child(5)"))).click()
etree=html.etree
#page_source会把当前浏览器的源码收集起来
html=driver.page_source
docs=etree.HTML(html)
articles=docs.xpath("//article//a[@class='labs-docsum-title']/@href")
base_url="https://pubmed.ncbi.nlm.nih.gov"
for arts in articles:
    driver.get(base_url+arts)
    htmls=driver.page_source
    docss=etree.HTML(htmls)
    title=docss.xpath("//h1[@class='heading-title']/text()")[0]
    title=title.strip()
    abstract=""
    if docss.xpath("//div[@class='abstract']/div/p"):
        abstract=docss.xpath("//div[@class='abstract']/div/p/text()")[0]
        abstract=abstract.strip()
        sub_abstract=abstract.split(",")
        trans=Translator(to_lang="chinese")
        content=""
        for item in sub_abstract:
            content+=trans.translate(item)+","
    with open(os.path.join(BASE_DIR,"files/"+title+".txt"),'w',encoding="utf8") as f:
        f.write(content)