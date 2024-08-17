#Parámetros Comunes en Chrome (usando ChromeOptions)
"""
# Crear una instancia de ChromeOptions
options = webdriver.ChromeOptions()

# Configurar el navegador para que inicie maximizado
options.add_argument("--start-maximized")
#Oculta la barra de información que aparece en Chrome
options.add_argument("--disable-infobars")
options.add_argument("--headless")


#creamos una varible donde guardamos la instancia de webdriver de selenium.
#le decimos que el driver del navegador que vamos a usar es el de "Chrome".

# Inicializar el WebDriver con las opciones
driver=webdriver.Chrome(options=options)

"""


#--headless:
"""
Inicia el navegador en modo sin cabeza (headless), es decir, sin interfaz gráfica.
Es útil para ejecutar pruebas en entornos donde no se requiere una interfaz visual
(como servidores CI/CD).
#Ejemplo:
options.add_argument("--headless")
"""

#--disable-gpu:
"""
Deshabilita el uso de la GPU. Generalmente se usa junto con el modo headless 
en sistemas Windows para evitar problemas gráficos.
#Ejemplo:
options.add_argument("--disable-gpu")
"""

#--incognito:
"""
Inicia el navegador en modo incógnito (sin guardar historial, cookies, etc.).
#Ejemplo:
options.add_argument("--incognito")
"""

#--disable-extensions:
""" 
Deshabilita todas las extensiones del navegador.
#Ejemplo:
options.add_argument("--disable-extensions")
"""

#--window-size=width,height:
""" 
Inicia el navegador con un tamaño de ventana específico. 
Útil si necesitas una resolución particular.
#Ejemplo:
options.add_argument("--window-size=1920,1080")
"""

#--disable-notifications:
""" 
Desactiva las notificaciones automáticas que algunas páginas web intentan mostrar.
#Ejemplo:
options.add_argument("--disable-notifications")
"""


#--no-sandbox:
""" Desactiva el modo sandboxing del navegador. 
Esto es a veces necesario en entornos de contenedores, pero puede disminuir la seguridad. 
#Ejemplo:
options.add_argument("--no-sandbox")
"""


# --disable-infobars:
""" 
Oculta la barra de información que aparece en Chrome que dice "Chrome 
is being controlled by automated test software".
#Ejemplo:
options.add_argument("--disable-infobars")
"""

#--remote-debugging-port=9222:
""" 
Habilita el depurador remoto en el puerto especificado.
Es útil para depuración avanzada.
#Ejemplo:
options.add_argument("--remote-debugging-port=9222")
"""

#--user-agent="custom_user_agent":
""" 
Establece un User-Agent personalizado para todas las solicitudes del navegador.
#Ejemplo:
options.add_argument("--user-agent=CustomUserAgentString")
"""

#--lang=es:
""" 
Configura el idioma del navegador. En este ejemplo, 
se establece el idioma en español.
#Ejemplo:
options.add_argument("--lang=es")
"""

#--ignore-certificate-errors:
""" Ignora los errores de certificado SSL, útil para pruebas en entornos de desarrollo
donde los certificados pueden no ser válidos.
#Ejemplo:
options.add_argument("--ignore-certificate-errors")
"""

#--disable-popup-blocking:
"""
Desactiva el bloqueador de pop-ups del navegador.
#Ejemplo:
options.add_argument("--disable-popup-blocking")
"""