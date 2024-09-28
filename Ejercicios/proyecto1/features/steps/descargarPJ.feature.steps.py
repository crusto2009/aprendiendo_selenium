from selenium import webdriver
from SeleniumLearnig.Ejercicios.proyecto1.Pages.HomePage import HomePage
from SeleniumLearnig.Ejercicios.proyecto1.Pages.BuscarPage import BuscarPage

@given(u'ingresa a la pagina de la policia')
def step_impl(context):
    # Crear una instancia de ChromeOptions
    options = webdriver.ChromeOptions()

    # Configurar el navegador para que inicie maximizado
    options.add_argument("--start-maximized")

    options.page_load_strategy = "eager"

    context.driver = webdriver.Chrome(options=options)
    context.driver.get("https://antecedentes.policia.gov.co:7005/WebJudicial/")
    context.home_page = HomePage(context.driver)
    context.buscar_page = BuscarPage(context.driver)

@when(u'acepte terminos y condiciones')
def step_impl(context):
    context.home_page.click_tya_aceptar_home_page()
    #context.home_page.click_enviar_home_page()


@when(u'ingrese mis datos personales y de clic en enviar')
def step_impl(context):
    context.buscar_page.enter_cedula_buscar_page()


@then(u'visualizo mi nombre y mi cedula en la pagina')
def step_impl(context):
    pass

