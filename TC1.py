import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v148.fed_cm import click_dialog_button
from selenium.webdriver.edge.service import Service

srv = Service(r"C:\Drivers\msedgedriver.exe")

driver = webdriver.Edge(service=srv)
driver.get("https://www.amazon.in")
driver.maximize_window()

driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input").send_keys("Tshirt")

driver.find_element(By.XPATH, "//*[@id='nav-search-submit-button']").click()

time.sleep(180)
driver.quit()