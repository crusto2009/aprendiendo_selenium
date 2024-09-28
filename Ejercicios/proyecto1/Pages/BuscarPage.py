from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BuscarPage:

    def __init__(self,driver):
        self.driver = driver
        self.cedula_input = (By.XPATH,'//*[@id="cedulaTipo"]' )

    def enter_cedula_buscar_page(self):
        self.driver.find_element(*self.cedula_input).send_keys("Hola mundo")