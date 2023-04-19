from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from time import sleep
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.db import IntegrityError
from selenium.webdriver.common.action_chains import ActionChains
import re 

s = Service(r"D:\Kinjal\chromedriver_win32\chromedriver.exe")
options = webdriver.ChromeOptions()
options.add_argument('--disable-blink-features=AutomationControlled')
# driver = webdriver.Chrome(service=s, options=options)

class awsIOTblog:
    def __init__(self):
        self.driver = webdriver.Chrome(service=s, options=options)
        sleep(5)
        # self.driver = webdriver.Chrome(chrome_driver_path)

    def blogdata(self):
        data={}
        try:
            self.driver.maximize_window()
            self.driver.get("https://aws.amazon.com/blogs/iot/")
            sleep(10)
            
            # Find the HTML element with the attribute
            elements = self.driver.find_elements(By.XPATH,'//article[@typeof="TechArticle"]')
            # print(elements)
            totalblogonpage = len(elements)
            print("totalblogonpage: ",totalblogonpage)
            
            # for element in elements:
            #     print(element.text.encode('utf8'))
                
            for i in range(totalblogonpage):
                blogs = self.driver.find_elements(By.XPATH,'//article[@typeof="TechArticle"]')
                blog = blogs[i]
                # print(blog)
                print(blog.text.encode('utf8'))
                
                # # Scroll the link into view
                # self.driver.execute_script("arguments[0].scrollIntoView();", blog)
                
               # Find the img tag
                # img_tag = blog.find_element(By.XPATH,'//div[@class="lb-col lb-mid-6 lb-tiny-24"]/a/img')
                img_tag = blog.find_element(By.CLASS_NAME,'wp-post-image')

                # Get the src attribute
                img_src = img_tag.get_attribute("src")

                print("Blog Image: ",img_src)
                
                title_tag = blog.find_element(By.CLASS_NAME,'blog-post-title')
                title = title_tag.text
                print("Blog Title: ", title)
                
                author_element = blog.find_element(By.XPATH,'//span[@property="name"]')
                author_name = author_element.text.encode('utf8')

                # find the element containing the published date
                date_element = blog.find_element(By.XPATH,'//time[@property="datePublished"]')
                published_date = date_element.get_attribute("datetime")
                
                # print the extracted data
                print(f"Blog Author: {author_name}")
                print(f"Blog Published date: {published_date}")    
                
                # extract the href link
                element = blog.find_element(By.CSS_SELECTOR,'h2.lb-bold.blog-post-title > a')
                # title = element.get_attribute('textContent')
                href = element.get_attribute('href')
                print("Blog Link: ", href)
                
                link = blog.find_element(By.XPATH,"/html/body/div[3]/div/main/article[1]/div/div[2]/h2/a").click()
                sleep(10)
                
                # Go back to the previous page
                self.driver.back()
                
                # Wait for the previous page to load
                WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((By.XPATH,'//article[@typeof="TechArticle"]')))
                
                 # Increment the index and repeat for the next blog article
                i += 1
                
                # description_data = blog.find_element(By.CLASS_NAME,"blog-post-excerpt")
                # description = description_data.text.encode('utf8')
                # print("Blog Description:",description)
                
                print("\n")
            
        except Exception as e:
            print(e)
            sleep(10)

awsIOTblogs = awsIOTblog()
awsIOTblogs.blogdata()
