#!/usr/bin/env python3

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()
options.add_argument('--user-agent="Mozilla/5.0 (SMART-TV; Linux; Tizen 6.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/4.0 Chrome/76.0.3809.146 TV Safari/537.36"')
options.add_argument('--headless')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)
driver.get("https://youtube.com/tv")
wait = WebDriverWait(driver, 10)
try:
    time.sleep(2)
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/ytlr-app/zn-lazy-46/ytlr-guide-response/yt-focus-container/ytlr-guide-entry-renderer[10]/ytlr-button/ytlr-avatar-lockup/div[1]/ytlr-icon/div'))).click()
    wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]/ytlr-app/yt-route[1]/ytlr-surface-page/zylon-provider-1/ytlr-tv-browse-renderer/zn-lazy-33/ytlr-tv-secondary-nav-renderer/div/zylon-provider-1/yt-virtual-list/div/div[7]/ytlr-tab-renderer/ytlr-button/ytlr-avatar-lockup/div/yt-formatted-string'))).click()
    time.sleep(2)
    code = driver.find_element(By.CSS_SELECTOR, '.ytlr-link-phone-with-tv-code-renderer__pairing-code-text').get_attribute('innerHTML')
    print(f"The allmighty pairing code is: {code}")
    while True:
        pass
except TimeoutException:
    print("Timeout exceeded loading YT TV page. Exiting.")
    exit(1)

