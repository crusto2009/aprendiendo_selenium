import unittest

#importamos las librerias necesarias de selenium
"""importamos el modulo webdriver"""
from selenium import webdriver
"""importamos el modulo "By" para poder utilizar los localizadores"""
from selenium.webdriver.common.by import By

# Crear una instancia de ChromeOptions
options = webdriver.ChromeOptions()

# Configurar el navegador para que inicie maximizado
options.add_argument("--start-maximized")
#Oculta la barra de información que aparece en Chrome
options.add_argument("--disable-infobars")
#options.add_argument("--headless")
#options.add_argument("--window-size=800,600")
options.add_argument("--lang=es")


#creamos una varible donde guardamos la instancia de webdriver de selenium.
#le decimos que el driver del navegador que vamos a usar es el de "Chrome".

# Inicializar el WebDriver con las opciones
driver=webdriver.Chrome(options=options)

class InitDemo(unittest.TestCase):


    def __init__(self,url):
        self.url=url
    #Creamos un metodo para abrir una url, pasamos la direccion por parametro(url).
    #Practica con esta pagina web https://www.globalsqa.com/angularJs-protractor/Multiform/#/form/profile
    def openBrower(self):
        driver.get(self.url)

        print(driver.title)
        # Validar que la página ha cambiado y contiene resultados
        self.assertIn("", driver.title)

        driver.implicitly_wait(13)

        try:
            #Buscamos el elemento por el atributo name y el nombre name
            Inputname = driver.find_element(By.XPATH, "//input[@name='name']")
            Inputname.send_keys("Hola mundo")
        except Exception as error:
            print(error)

        driver.quit()

#llamamos al mentodoy le enviamos la url.
demo = InitDemo("https://www.globalsqa.com/angularJs-protractor/Multiform/#/form/profile")
demo.openBrower()



