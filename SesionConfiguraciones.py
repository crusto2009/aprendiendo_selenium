from selenium import webdriver

#configuracion de tipos de carga.

"""¿Cuándo elegir cada estrategia?
normal: Cuando necesitas asegurarte de que todo esté listo antes de proceder.
eager: Para optimizar tiempos cuando los recursos externos no son esenciales para la prueba.
none: Para interacciones rápidas en páginas dinámicas o progresivas"""

#Optenemos el metodo de configuracion:
options = webdriver.ChromeOptions()

#options.page_load_strategy = "normal"
"""	Se utiliza de forma predeterminada, espera a que se descarguen todos los recursos.
Descripción: Esta es la estrategia por defecto. El script de Selenium espera hasta que toda la página esté completamente cargada,
incluyendo los recursos externos como imágenes, CSS, y scripts.
Uso recomendado: Útil cuando necesitas asegurarte de que todos los elementos de la página estén disponibles 
antes de interactuar con ellos.
"""

#options.page_load_strategy = "eager"
"""	El acceso al DOM está listo, pero otros recursos como imágenes aún pueden estar cargándose
Descripción: Con esta estrategia, Selenium considera que la página ha terminado de cargarse una vez que el documento DOM (Document Object Model)
está completamente construido, pero antes de que se hayan cargado todos los recursos externos (como imágenes).
Uso recomendado: Puede ser útil cuando los recursos externos no son 
necesarios para las acciones que se desean realizar, y se busca reducir el tiempo de espera.

"""

#options.page_load_strategy = "none"
"""	No bloquea el navegador 
Descripción: Con esta estrategia, Selenium no espera a que la página se cargue por completo. 
Inicia las acciones tan pronto como el navegador recibe la primera respuesta del servidor.
Uso recomendado: Útil para situaciones en las que la carga de la página es asíncrona o si necesitas 
realizar acciones en una página que se carga progresivamente.

"""
driver = webdriver.Chrome(options=options)
driver.get("http://www.google.com.co")
driver.quit()