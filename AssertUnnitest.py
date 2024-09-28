"""
| **Método de Aserción**                  | **Descripción**                                                                                     |
|-----------------------------------------|-----------------------------------------------------------------------------------------------------|
| `assertEqual(a, b)`                     | Verifica que `a` y `b` sean iguales.                                                               |
| `assertNotEqual(a, b)`                  | Verifica que `a` y `b` no sean iguales.                                                            |
| `assertTrue(x)`                         | Verifica que `x` sea verdadero.                                                                    |
| `assertFalse(x)`                        | Verifica que `x` sea falso.                                                                        |
| `assertIsNone(x)`                       | Verifica que `x` sea `None`.                                                                       |
| `assertIsNotNone(x)`                    | Verifica que `x` no sea `None`.                                                                    |
| `assertIn(a, b)`                        | Verifica que `a` esté en `b`.                                                                      |
| `assertNotIn(a, b)`                     | Verifica que `a` no esté en `b`.                                                                   |
| `assertGreater(a, b)`                   | Verifica que `a` sea mayor que `b`.                                                                |
| `assertLess(a, b)`                      | Verifica que `a` sea menor que `b`.                                                                |
| `assertGreaterEqual(a, b)`              | Verifica que `a` sea mayor o igual que `b`.                                                        |
| `assertLessEqual(a, b)`                 | Verifica que `a` sea menor o igual que `b`.                                                        |
| `assertAlmostEqual(a, b, places)`       | Verifica que `a` y `b` sean casi iguales, con una precisión dada en `places`.                      |
| `assertNotAlmostEqual(a, b, places)`    | Verifica que `a` y `b` no sean casi iguales, con una precisión dada en `places`.                   |
| `assertIsInstance(obj, cls)`            | Verifica que `obj` sea una instancia de `cls`.                                                     |
| `assertNotIsInstance(obj, cls)`         | Verifica que `obj` no sea una instancia de `cls`.                                                  |
| `assertRaises(exc, func, *args, **kwargs)` | Verifica que la llamada a `func` con los argumentos dados lance la excepción `exc`.             |
| `assertLogs(logger, level)`             | Verifica que se generen logs con el nivel especificado en `logger`.                                |

"""

""" Configuración y Limpieza """
#setUp(self):
# Método que se ejecuta antes de cada prueba. Se utiliza para preparar el entorno necesario para los tests,
# como inicializar objetos, abrir conexiones, etc.

#tearDown(self):
# Método que se ejecuta después de cada prueba. Se utiliza para limpiar el entorno después de la ejecución del test,
# como cerrar conexiones o eliminar datos.
