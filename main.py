from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge(executable_path='C:/Users/rober/OneDrive/Escritorio/Mantenimiento/edgedriver_win64/msedgedriver.exe')

driver.get("https://www.amazon.com/")

selec = driver.find_element(By.ID, 'twotabsearchtextbox')
selec.send_keys("HP Pavilion azul" + Keys.ENTER)

primero = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div[1]/div/span[1]/div[1]/div[3]/div/div/div/div/div/div/div/div[2]/div/div/div[1]/h2/a/span')
primero.click()

agregar = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[9]/div[6]/div[1]/div[4]/div/div/div/div/div/form/div/div/div/div/div[3]/div/div[9]/div/div/span/div/div/span/span/span/span')
agregar.click()

agregar2 = driver.find_element(By.XPATH, '/html/body/div[4]/div/div/ul/li[2]/a')
agregar2.click()

carrito = driver.find_element(By.ID, 'add-to-cart-button')
carrito.click()

mirar_carro = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[1]/div[2]/div/div[1]/span/span/a')
mirar_carro.click()
time.sleep(7)



