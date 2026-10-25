from selenium import webdriver
from selenium.common import ElementClickInterceptedException, NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service(executable_path="C:/Development/chromedriver.exe")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)
driver.get("https://tinder.com/")
sleep(10)

login_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/div[2]/div[2]")
login_button.click()

sleep(5)
facebook_login = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div")
facebook_login.click()

sleep(5)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

input("Complete the Facebook sign-in in the browser, then press Enter here to continue...")

driver.switch_to.window(base_window)
print(driver.title)
sleep(10)

allow_location_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div/div/div/div[3]/button[1]/div[2]/div[2]")
allow_location_button.click()
sleep(10)

notifications_button = driver.find_element(By.XPATH, "/html/body/div[2]/main/div[1]/div/div/div[3]/button[1]/div[2]/div[2]")
notifications_button.click()
sleep(10)

cookies = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]")
cookies.click()
sleep(15)

for n in range(5):

    # Add a 1-second delay between likes.
    sleep(30)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div/div/main/div/div/div[1]/div/div[3]/div/div[4]/button/span/span/svg/path")
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(10)

driver.quit()

