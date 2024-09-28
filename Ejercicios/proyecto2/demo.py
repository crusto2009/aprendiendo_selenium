from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

options = webdriver.ChromeOptions()

options.add_argument("--start-maximized")

# Configura el controlador (driver) para tu navegador. Ejemplo con Chrome:
driver = webdriver.Chrome(options=options)

# Abre la página web deseada
driver.get("https://antecedentes.policia.gov.co:7005/WebJudicial/")


try:

    wait = WebDriverWait(driver, timeout=102)
    element = driver.find_element(By.XPATH,'//div[@class="preloader"]')

    is_not_visible = wait.until(EC.invisibility_of_element_located(element))

    if is_not_visible:
        # Espera a que el checkbox esté visible y selecciona la opción "Acepto"
        acepta_option = WebDriverWait(driver, 160).until(
            EC.element_to_be_clickable((By.ID, "aceptaOption:0"))
        )

        if acepta_option:
            print("click")
            acepta_option.click()

        # Espera a que el botón de enviar esté habilitado
        continuar_btn = WebDriverWait(driver, 160).until(
            EC.element_to_be_clickable((By.ID, "continuarBtn"))
        )

        if continuar_btn:
            print("click")
            continuar_btn.click()

    driver.implicitly_wait(12000)


    #assert  driver.title == "Policía Nacional de Colombia"
    #assert  driver.current_url == "https://antecedentes.policia.gov.co:7005/WebJudicial/antecedentes.xhtml"

    wait = WebDriverWait(driver, timeout=1102)

    element = driver.find_element(By.XPATH, '//div[@class="preloader"]')

    is_not_visible = WebDriverWait(driver,2000).until(
        EC.invisibility_of_element_located(element)
    )
    time.sleep(9)

    driver.switch_to.default_content()

    visible_input = WebDriverWait(driver, 2200).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="cedulaInput"]'))
    )
    if visible_input:
        visible_input.send_keys("Hola mundo")

        # No olvides cerrar el navegador después de terminar
        driver.quit()




except Exception as e:
    print(f"Error al enviar el formulario: {e}")
finally:
    # No olvides cerrar el navegador después de terminar
    driver.quit()

