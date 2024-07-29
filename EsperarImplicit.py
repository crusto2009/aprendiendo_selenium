"""Esperas implícitas:
#Selenium tiene una forma integrada de esperar automáticamente los elementos,
#llamada espera implícita"""

#Ejemplo:
#driver.implicitly_wait(2)


"""Esperas explícitas
# Las esperas explícitas son bucles que se agregan al código y que sondean
# la aplicación para determinar si se cumple una condición específica antes
# de que salga del bucle y continúe con el siguiente comando en el código.
# Si la condición no se cumple antes de un valor de tiempo de espera designado,
# el código generará un error de tiempo de espera."""

#Ejemplo:
#driver.implicitly_wait(2)
"""
#le damos una condicion a la espera, es decir le decimos que espera hasta que
#El elemento "revealed" ese visible
#wait.until(lambda d: revealed.is_displayed()) ..."""

#wait = WebDriverWait(driver, timeout=2)... le decimos al nevegador que espere 2 segundos



"""Nota:Advertencia: No mezcle esperas implícitas y explícitas.
#Si lo hace, puede causar tiempos de espera impredecibles."""
