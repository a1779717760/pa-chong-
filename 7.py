from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC

browser = webdriver.Chrome()
wait = WebDriverWait(browser,10)
def search():
    browser.get('https://www.taobao.com')
    input = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR , "#q"))
    )
    submit = WebDriverWait(browser,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'body > div.screen-outer.clearfix > div.main > div.main-inner.clearfix > div.tbh-service.J_Module > div > ul > li:nth-child(1) > a:nth-child(1)')))

    submit.click()

def main():
    search()

if __name__ == '__main__':
    main()