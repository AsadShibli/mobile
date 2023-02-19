from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

s= Service("msedgedriver.exe") # connecting to web driver
options = webdriver.EdgeOptions()
options.add_experimental_option("detach",True)

driver = webdriver.Edge(service=s,options=options)



#get all codes for only first page right now
driver.get("https://www.gsmarena.com.bd/smartphones")


div_items = driver.find_elements(by=By.XPATH, value="//div[@class='product-thumb']")
total_count = len(div_items)

all_data = []



for i in range(1, total_count + 1, 1):
    product_link = driver.find_element(by=By.XPATH,
                                       value='//*[@id="all"]/div[1]/div/div/div[2]/div/div[1]/div[' + str(
                                           i) + ']/div/a[1]')
    product_link.click()

    # get the data for the page
    page_data = driver.page_source

    # append the data to the list
    all_data.append(page_data)

    driver.back()



# scroll to the bottom of the page
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# get the last page link
last_link = driver.find_element(by=By.XPATH, value='//*[@id="all"]/div[1]/div/div/div[2]/div/div[2]/nav/ul/li[last()]/a')

# click on the last page link
last_link.click()

# get the current page URL
last_page_url = driver.current_url



j = 2
while True:

    driver.get("https://www.gsmarena.com.bd/smartphones/{}".format(j))



    for i in range(1, total_count + 1, 1):
        product_link = driver.find_element(by=By.XPATH,
                                           value='//*[@id="all"]/div[1]/div/div/div[2]/div/div[1]/div[' + str(
                                               i) + ']/div/a[1]')
        product_link.click()

        # get the data for the page
        page_data = driver.page_source

        # append the data to the list
        all_data.append(page_data)

        driver.back()

    all_data_Str = ' '.join(all_data)

    current_url = driver.current_url
    if current_url == last_page_url:
        break
    j = j + 1



with open('mobie10.html','w',encoding='utf-8') as f:
    f.write(all_data_Str)





#now single page e iterate all item , then multipage e iterate , 