#importamos las librerias necesarias de selenium
"""importamos el modulo webdriver"""
from selenium import webdriver
"""importamos el modulo "By" para poder utilizar los localizadores"""
from selenium.webdriver.common.by import By

#creamos una varible donde guardamos la instancia de webdriver de selenium.
#le decimos que el driver del navegador que vamos a usar es el de "Chrome".
driver=webdriver.Chrome()

#Creamos un metodo para abrir una url, pasamos la direccion por parametro(url).
#Practica con esta pagina web https://www.globalsqa.com/angularJs-protractor/Multiform/#/form/profile
def openBrower(url):
    driver.get(url)
    # Podemos obtener informacion del navegador con los siguiente metodos:
    # driver.title: optenemos el titulo de la pagina actual
    title= driver.title
    # driver.current_url: capturar la url actual del navegador.
    url = driver.current_url
    # driver.back(): presionar el boton atras del navegador.
    driver.back()
    # driver.back(): presionar el boton adelante del navegador.
    driver.forward()
    #driver.refresh(): refrescar el navegador
    driver.refresh()

#llamamos al mentodoy le enviamos la url.
openBrower("https://www.globalsqa.com/angularJs-protractor/Multiform/#/form/profile")



