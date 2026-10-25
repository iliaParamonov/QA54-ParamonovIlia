#open browser
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
try:
    driver.get("https://telranedu.web.app/login")
    #by TAG_NAME
    div = driver.find_elements(By.TAG_NAME,"div")
    print(len(div))
    div2 = driver.find_element(By.CSS_SELECTOR,"div")
    #div3 = driver.find_element(By.XPATH,"div")
    h1 = driver.find_element(By.TAG_NAME,"h1")
    h1_2 = driver.find_element(By.CSS_SELECTOR,"h1")

    input = driver.find_element(By.TAG_NAME,"input")
    input1 = driver.find_element(By.CSS_SELECTOR,"input")

    a_list = driver.find_elements(By.TAG_NAME,"a")
    a_list_1 = driver.find_elements(By.CSS_SELECTOR,"a")
    print(len(a_list))
    # by class
    container = driver.find_element(By.CLASS_NAME, "container")  # runing by pairs class = container
    container_1 = driver.find_element(By.CSS_SELECTOR, ".container")  # searching only "container"
    nav_bar = driver.find_elements(By.CLASS_NAME, "active")
    nav_bar_1 = driver.find_elements(By.CSS_SELECTOR, ".active")
    print(len(nav_bar))
    print(len(nav_bar_1))


finally:
    driver.quit()