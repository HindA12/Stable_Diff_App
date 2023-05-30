#importing the libraries
import os
import selenium
from selenium import webdriver
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

#URLs from which we will scrape the images
url_1 = 'https://www.decoist.com/2014-07-07/moroccan-living-rooms/?chrome=1'
url_2 = 'https://www.thespruce.com/moroccan-living-rooms-4777186'
url_3 = 'https://homedesignlover.com/living-room-designs/moroccan-living-rooms/'
url_4 = 'https://www.houszed.com/moroccan-living-room-ideas/'
url_5 = 'https://fr.freepik.com/search?format=search&people=exclude&query=salon+marocain+traditionnel&selection=1&type=photo'
url_6 = 'https://fr.freepik.com/search?format=search&page=2&people=exclude&query=salon+marocain+traditionnel&selection=1&type=photo'

links = [] #List in which we will store images links

driver = webdriver.Chrome(ChromeDriverManager().install()) #initializing the driver

#Scraping from website 1
driver.get(url_1)
xpath1 = '//*[@id="page"]/div[2]/div/div/div[3]/div/article/div[4]/p['
xpath2 = ']/a/span/img'
for i in range(2, 66):
    try :
        xpath = xpath1 + str(i) + xpath2
        link = driver.find_element(By.XPATH, xpath).get_attribute('src')
        links.append(link)
    except : 
        pass

#Scraping from website 2
driver.get(url_2)
images = driver.find_elements(By.XPATH, '//img[contains(@class, " universal-image__image")]')
for i in range(len(images)):
    try :
        links.append(images[i].get_attribute('src'))
    except :
        pass

#Scraping from website 3
driver.get(url_3)
xpath1 = '/html/body/div[1]/div[1]/div[2]/div[3]/p['
xpath2 = ']/div/img'
links = []
for i in range(3, 46):
    xpath = xpath1 + str(i) + xpath2
    try :
        link = driver.find_element(By.XPATH, xpath).get_attribute('src')
        links.append(link)
    except :
        pass

#Scraping from website 4
driver.get(url_4)
xpath1 = '//*[@id="post-5631"]/div[2]/div[2]/div/figure['
xpath2 = ']/figure/img'
links = []
for i in range(3, 17):
    xpath = xpath1 + str(i) + xpath2
    try :
        link = driver.find_element(By.XPATH, xpath).get_attribute('src')
        links.append(link)
    except :
        pass

#Scraping from website 5
driver.get(url_5)
images = driver.find_elements(By.XPATH, '//img[contains(@class, "portrait loaded")]')
links = []
for i in range(len(images)):
    links.append(images[i].get_attribute('src'))

#Scraping from website 6
driver.get(url_6)
images = driver.find_elements(By.XPATH, '//img[contains(@class, "portrait loaded")]')
for i in range(len(images)):
    links.append(images[i].get_attribute('src'))


#Downloading the images
path1 = 'D:\myconcept_images\image'
path2 = '.jpg'
for i in range(len(links)):
    try :
        response = requests.get(links[i]) #On envoie une demande à l'URL de l'image
        if response.status_code == 200: #Si notre demande est acceptée, on télécharge notre image
            url = path1+str(i+102)+path2
            with open(url, "wb") as f:
                f.write(response.content)
    except : 
        pass