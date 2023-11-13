import time
from selenium.webdriver.common.by import By
from selenium import webdriver
from fake_useragent import UserAgent
from concurrent.futures import ThreadPoolExecutor
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


ua = UserAgent()
user_agent = ua.random
url = 'https://twitter.com/i/flow/login'
options = webdriver.ChromeOptions()


options.add_argument(f'user-agent={user_agent}')
# options.add_argument('--headless')
options.add_argument("--disable-gpu")
options.add_argument("--incognito")
options.add_experimental_option('excludeSwitches', ['enable-logging'])

def twitter(login, password, post):
    try:
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(url)

        username_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input')))
        username_input.send_keys(login)

        username_submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div')))
        username_submit.click()
        password_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input')))
        password_input.send_keys(password)

        password_submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div')))
        password_submit.click()

        twit_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div')))
        twit_button.click()
        twit_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[1]/div[2]/div/div/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div')))
        twit_input.send_keys(post)

        twit_submit = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div[2]/div[2]/div/div/div/div[4]/div/span/span')))
        twit_submit.click()

        driver.quit()
        time.sleep(2)
    except Exception as e:
        print('Oops.., try again')


def process_account(account, post):
    login, password = account.split(':')
    twitter(login, password, post)

with open('accounts.txt', 'r', encoding='utf-8') as f:
    accounts = f.read().split('\n')
    accounts = [account for account in accounts if account]


with open('post.txt', 'r', encoding='utf-8') as f:
    posts = f.read().split('\n')
    posts = [post for post in posts if post]


with ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(process_account, accounts, posts)
