import undetected_chromedriver as uc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# import time to load up the linkedin login verification
import time
import pickle
if __name__ == '__main__':
    email = "princewill835@gmail.com"
    password = "Colla@200"

    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    # options.add_argument('proxy-server=106.122.8.54:3128')
    # options.add_argument(r'--user-data-dir=C:\Users\suppo\AppData\Local\Google\Chrome\User Data\Default')

    # using chrome because undetected_chromedriver closes immediately
    browser = webdriver.Chrome(
        options=options,
    )
    browser.get('https://secure.indeed.com/auth')
    #Cookies already saved to log into linkedin
    cookies = pickle.load(open("indeedcookies.pkl", "rb"))
    for cookie in cookies:
        try:
            browser.add_cookie(cookie)
        except Exception as e:
            print(e)
    browser.get('https://ng.indeed.com/')
    
    # browser.find_element(By.ID, "text_input_what").send_keys("Backend Engineer")
    # browser.find_element(By.ID, "text_input_where").send_keys("Backend Engineer")
    
    
        
    time.sleep(60)