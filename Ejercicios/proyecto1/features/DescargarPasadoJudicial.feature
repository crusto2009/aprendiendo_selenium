# Created by CristianH at 27/07/2024
Feature: Obtener información personal del pasado judicial
  # Enter feature description here

  Scenario: Descargar pasado judicial
    # Enter steps here
    Given ingresa a la pagina de la policia
                    When acepte terminos y condiciones
    And  ingrese mis datos personales y de clic en enviar
    Then visualizo mi nombre y mi cedula en la pagina