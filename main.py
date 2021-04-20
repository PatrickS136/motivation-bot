from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import requests

# CHROME DRIVER & Account credentials
CHROME_DRIVER="D:/chromedriver_win32/chromedriver.exe"

EMAIL="YOUR EMAIL"
PASSWORD="YOUR PASSWORD"

driver=webdriver.Chrome(executable_path=CHROME_DRIVER)

driver.get("https://twitter.com/")

# Go to login page
time.sleep(2)
loginButton=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span')
loginButton.click()

# Enter account credentials
time.sleep(2)
emailInput=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input')
passwordInput=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input')

emailInput.send_keys(EMAIL)
passwordInput.send_keys(PASSWORD)

# Click on login button
login=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span')
login.click()

# Get a random quote using ZenQuotes
response=requests.get("https://zenquotes.io/api/random")
response.raise_for_status()
data=response.json()
quote=f'"{data[0]["q"]}"'
author=f'-{data[0]["a"]}'
print(quote)
print(author)

# Send the tweet
time.sleep(5)
tweetArea=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div')
tweetArea.send_keys(f"{quote}\n\n{author}")
time.sleep(3)
tweetButton=driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div/div/span/span')
tweetButton.click()

time.sleep(3)

# Close browser
# driver.quit()