#Selenium proporciona soporte para estas 8 estrategias de ubicación de elementos tradicionales en WebDriver:

"""
| Método                   | Descripción                                                                                                          |
|--------------------------|----------------------------------------------------------------------------------------------------------------------|
| nombre de la clase       | Localiza elementos cuyo nombre de clase contiene el valor de búsqueda                                                |
| selector de css          | Localiza elementos que coinciden con un selector CSS                                                                 |
| identificación           | Localiza elementos cuyo atributo ID coincide con el valor de búsqueda                                                |
| nombre                   | Localiza elementos cuyo atributo NAME coincide con el valor de búsqueda                                              |
| Texto del enlace         | Localiza elementos de anclaje cuyo texto visible coincide con el valor de búsqueda                                   |
| texto de enlace parcial  | Localiza los elementos de anclaje cuyo texto visible contiene el valor de búsqueda. Si hay varios elementos coincidentes, solo se seleccionará el primero. |
| nombre de etiqueta       | Localiza elementos cuyo nombre de etiqueta coincide con el valor de búsqueda                                         |
| xpath                    | Localiza elementos que coinciden con una expresión XPath                                                             |


"""
#Inicialmente creamos la instancia del driver navegador.
"""driver = webdriver.Chrome() el nevegador a utilizar es Chrome"""

"""Nombre de la clase -> driver.find_element(By.CLASS_NAME, "information")"""
#Buscamos un elementos que contenga la clase "information"""
#Resultado:
"""selecciona los elementos:
#<input class="information" type="text" id="fname" name="fname" value="Jane"><br><br>
#<input class="information" type="text" id="lname" name="lname" value="Doe"><br><br>"""
"""Ver html al final del documento"""

"""///////////////////////////////////////////////////////////////////////////// """


"""selector de css -> driver.find_element(By.CSS_SELECTOR, "#fname")"""
#CSS es el lenguaje que se utiliza para diseñar páginas HTML.
# Podemos utilizar la estrategia de localizador del selector CSS para identificar el elemento en la página.
#Resultado:
# si es id:
"""selecciona el elemento id(#):
<input class="information" type="text" id="fname" name="fname" value="Jane"><br><br>"""
"""Ver html al final del documento"""


"""///////////////////////////////////////////////////////////////////////////// """

"""Identificación (id unico) -> driver.find_element(By.ID, "lname")"""
#Podemos utilizar el atributo ID de un elemento de una página web para localizarlo.
#Resultado:
# si es id:
"""selecciona el elemento id(#) 'lname':
<input class="information" type="text" id="lname" name="lname" value="Doe"><br><br>
"""
"""Ver html al final del documento"""

"""///////////////////////////////////////////////////////////////////////////// """

"""nombre -> driver.find_element(By.NAME, "newsletter")"""
#Podemos utilizar el atributo NAME de un elemento de una página web para localizarlo.
#Resultado:
"""selecciona el checkbox 'newsletter
<input type="checkbox" name="newsletter" value="1" /><br><br>
"""
"""Ver html al final del documento"""

"""///////////////////////////////////////////////////////////////////////////// """

"""
Texto del enlace -> driver.find_element(By.LINK_TEXT, "Selenium Official Page")"""
#Si el elemento que queremos localizar es un enlace, podemos utilizar el localizador de texto de enlace para identificarlo en la página web.
#Resultado:
"""selecciona el link 'Selenium Official Page'
<a href ="www.selenium.dev">Selenium Official Page</a>
"""
"""Ver html al final del documento"""

"""///////////////////////////////////////////////////////////////////////////// """

"""
Texto de enlace parcial -> driver.find_element(By.PARTIAL_LINK_TEXT, "Official Page")"""
#Si el elemento que queremos localizar es un enlace, podemos utilizar el localizador de texto parcial del enlace para identificarlo en la página web.
#Resultado
"""
Selecciona el link  que contenga parcialmente 'Official Page'
<a href ="www.selenium.dev">Selenium Official Page</a> 
"""
"""Ver html al final del documento"""

"""///////////////////////////////////////////////////////////////////////////// """

""" nombre de etiqueta -> driver.find_element(By.TAG_NAME, "a")"""
#Podemos utilizar la etiqueta HTML como localizador para identificar el elemento web en la página.
#Resultado
"""
Selecciona el elemento 'a' en la pagina:
<a href ="www.selenium.dev">Selenium Official Page</a> 
"""
"""Ver html al final del documento"""

"""///////////////////////////////////////////////////////////////////////////// """

""" xpath  -> driver.find_element(By.XPATH, "//input[@value='f']")"""
#Un documento HTML puede considerarse como un documento XML y, a continuación, podemos utilizar xpath,
# que será la ruta recorrida para llegar al elemento de interés para localizar el elemento
#Resultado:
"""seleccionamos el input con la propiedad value = 'f'
 <input type="radio" name="gender" value="f" />Female <br>
"""
"""Ver html al final del documento"""

"""///////////////////////////////////////////////////////////////////////////// """


"""
<html>
<body>
<style>
.information {
  background-color: white;
  color: black;
  padding: 10px;
}
</style>
<h2>Contact Selenium</h2>

<form action="/action_page.php">
  <input type="radio" name="gender" value="m" />Male &nbsp;
  <input type="radio" name="gender" value="f" />Female <br>
  <br>
  <label for="fname">First name:</label><br>
  <input class="information" type="text" id="fname" name="fname" value="Jane"><br><br>
  <label for="lname">Last name:</label><br>
  <input class="information" type="text" id="lname" name="lname" value="Doe"><br><br>
  <label for="newsletter">Newsletter:</label>
  <input type="checkbox" name="newsletter" value="1" /><br><br>
  <input type="submit" value="Submit">
</form> 

<p>To know more about Selenium, visit the official page 
<a href ="www.selenium.dev">Selenium Official Page</a> 
</p>

</body>
</html>
"""