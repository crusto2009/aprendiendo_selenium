"""

Page Object Model (POM)
Descripción:
El Page Object Model (POM) es uno de los patrones más populares para organizar el código de pruebas
en Selenium.

En este patrón, cada página web se representa como una clase, y cada elemento de la página se
define como un atributo de esa clase. Las interacciones con la página
(como hacer clic, enviar texto, etc.) se encapsulan en métodos dentro de la clase.

Ventajas:

- Facilita el mantenimiento del código, ya que cualquier cambio en la UI de la página se
refleja solo en la clase correspondiente.

- Reutilización de código.

- Separación clara entre la lógica de la página y los casos de prueba.

#Ejemplo:

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = driver.find_element(By.ID, "username")
        self.password_field = driver.find_element(By.ID, "password")
        self.login_button = driver.find_element(By.ID, "loginButton")

    def login(self, username, password):
        self.username_field.send_keys(username)
        self.password_field.send_keys(password)
        self.login_button.click()

#test:
def test_login_valid_user():
    login_page = LoginPage(driver)
    login_page.login("user", "pass")
    assert "Dashboard" in driver.title


"""