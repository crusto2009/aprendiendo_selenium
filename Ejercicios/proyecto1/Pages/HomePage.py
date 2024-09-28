from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self,driver):
        self.driver = driver
        self.checbox_input = (By.XPATH,'//input[@id="aceptaOption:0"]')
        self.loader_div= (By.XPATH,'//div[@class="preloader"]')
        self.enviar_btn = (By.CSS_SELECTOR, "button[type='submit']")
        self.cedula_input = (By.XPATH,'//*[@id="cedulaTipo"]' )
        self.link_inicio = (By.XPATH,'//a[@href="http://www.policia.gov.co/"]')

    def click_tya_aceptar_home_page(self):
        wait = WebDriverWait(self.driver, timeout=102)
        element = self.driver.find_element(*self.loader_div)

        is_not_visible = wait.until(EC.invisibility_of_element_located(element))

        if is_not_visible:
            print("click")
            self.driver.find_element(*self.checbox_input).click()
            #self.driver.find_element(*self.link_inicio).click()


        self.driver.implicitly_wait(120)


    def click_enviar_home_page(self):
        # self.driver.switch_to.default_content()
        try:
            # Espera a que el botón de enviar esté visible y habilitado
            enviar_btn = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//*[@id='continuarBtn']"))
            )
            enviar_btn.click()

        except Exception as e:
            print(f"Error al hacer clic en el botón 'Enviar': {e}")


    def espera(self):
        self.driver.implicitly_wait(120)

