
#creamos una varible donde guardamos la instancia de webdriver de selenium.
#le decimos que el driver del navegador que vamos a usar es el de "Chrome".

# Inicializar el WebDriver con las opciones
#driver=webdriver.Chrome()

#Maximizar el nevegador
#driver.maximize_window()


# Podemos obtener informacion del navegador con los siguiente metodos:
# driver.title: optenemos el titulo de la pagina actual
title = driver.title
# driver.current_url: capturar la url actual del navegador.
url = driver.current_url
# driver.back(): presionar el boton atras del navegador.
# driver.back()
# driver.back(): presionar el boton adelante del navegador.
# driver.forward()
# driver.refresh(): refrescar el navegador
# driver.refresh()