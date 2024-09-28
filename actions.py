"""
| **Acción**          | **Descripción**                                      | **Ejemplo**                                                                                      |
|---------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------|
| **Abrir URL**       | Navega a una URL específica.                         | `driver.get("https://www.ejemplo.com")`                                                       |
| **Buscar elemento**  | Localiza un elemento en la página.                  | `element = driver.find_element(By.ID, "miElemento")`                                          |
| **Hacer clic**      | Simula un clic en un elemento.                       | `element.click()`                                                                                |
| **Enviar texto**    | Ingresa texto en un campo de entrada.               | `element.send_keys("Texto a enviar")`                                                          |
| **Limpiar campo**   | Limpia el texto de un campo de entrada.             | `element.clear()`                                                                                |
| **Obtener texto**    | Extrae el texto de un elemento.                     | `texto = element.text`                                                                           |
| **Seleccionar opción**| Selecciona una opción en un menú desplegable.      | `from selenium.webdriver.support.ui import Select`<br>`select = Select(driver.find_element(By.ID, "miSelect"))`<br>`select.select_by_visible_text("Opción")` |
| **Esperar**         | Espera a que un elemento esté presente.             | `from selenium.webdriver.common.by import By`<br>`from selenium.webdriver.support.ui import WebDriverWait`<br>`from selenium.webdriver.support import expected_conditions as EC`<br>`WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "miElemento")))` |
| **Mover el mouse**  | Mueve el cursor sobre un elemento.                  | `from selenium.webdriver.common.action_chains import ActionChains`<br>`actions = ActionChains(driver)`<br>`actions.move_to_element(element).perform()` |
| **Tomar captura de pantalla** | Captura una imagen de la página actual. | `driver.save_screenshot("captura.png")`                                                      |
"""