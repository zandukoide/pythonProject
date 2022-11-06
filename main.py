
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge('C:/Users/rober/OneDrive/Escritorio/Mantenimiento/edgedriver_win64/msedgedriver.exe')
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.com/")
