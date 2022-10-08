#importing necessary frameworks and libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time

service = Service('.\drivers\chromedriver.exe') #reading the chrome driver file for accessing the browser

#chrome driver settings
def create_chrome_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=AutomationControlled")
  
  driver = webdriver.Chrome(service=service,options=options)
  #google sign in page URL
  driver.get("https://accounts.google.com/v3/signin/identifier?dsh=S-670663931%3A1665236501230352&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F1%2F&emr=1&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F1%2F&osid=1&passive=1209600&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&ifkv=AQDHYWo2ZT7pc7CYGgKbSnPCMOwA0IhAPSYd56XXPxfTXLwte-3ms4_oYYhLtzZPlH8ue09QQjRb#inbox")
  return driver


#main function
def main():
  #getting chrome driver info
  chrome_driver = create_chrome_driver()
  time.sleep(2)
  #entering email id
  chrome_driver.find_element(by="xpath",value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input").send_keys("youremailid@gmail.com",Keys.RETURN)
  time.sleep(2)
  #entering password
  chrome_driver.find_element(by="xpath",value="/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/input").send_keys("password",Keys.RETURN)
  time.sleep(2)


if __name__ == "__main__":
  main()