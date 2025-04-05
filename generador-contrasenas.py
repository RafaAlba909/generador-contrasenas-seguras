import random
import string
import secrets
import re

def generar_contraseña(longitud=12, incluir_caracteres_especiales=True):
    """
    Genera una contraseña segura con las especificaciones proporcionadas.

    Args:
    longitud (int): Longitud de la contraseña a generar (por defecto 12).
    incluir_caracteres_especiales (bool): Si se deben incluir caracteres especiales (por defecto True).

    Returns:
    str: Contraseña generada
    """

    caracteres = string.ascii_letters + string.digits 
    if incluir_caracteres_especiales:
        caracteres += string.punctuation  

    contraseña = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    
    return contraseña

def validar_contraseña(contraseña):
    """
    Valida si una contraseña es suficientemente segura según ciertos criterios.

    Args:
    contraseña (str): Contraseña a validar.

    Returns:
    bool: True si la contraseña es segura, False en caso contrario.
    """
    if len(contraseña) < 8:
        return False
    if not re.search(r'[A-Za-z]', contraseña):  
        return False
    if not re.search(r'[0-9]', contraseña):  
        return False
    if not re.search(r'[\W_]', contraseña):  
        return False
    return True

def generar_y_validar_contraseñas(cantidad=5, longitud=12, incluir_caracteres_especiales=True):
    """
    Genera y valida varias contraseñas, y muestra si son seguras.

    Args:
    cantidad (int): Cantidad de contraseñas a generar (por defecto 5).
    longitud (int): Longitud de las contraseñas (por defecto 12).
    incluir_caracteres_especiales (bool): Si se deben incluir caracteres especiales (por defecto True).
    """
    contraseñas_generadas = []
    for _ in range(cantidad):
        contraseña = generar_contraseña(longitud, incluir_caracteres_especiales)
        es_segura = validar_contraseña(contraseña)
        contraseñas_generadas.append((contraseña, es_segura))

    for index, (contraseña, es_segura) in enumerate(contraseñas_generadas):
        print(f"Contraseña {index + 1}: {contraseña} - {'Segura' if es_segura else 'Insegura'}")

if __name__ == "__main__":
    cantidad = int(input("¿Cuántas contraseñas deseas generar? "))
    longitud = int(input("¿Qué longitud deseas para las contraseñas? "))
    incluir_caracteres_especiales = input("¿Incluir caracteres especiales? (s/n): ").strip().lower() == 's'
    
    generar_y_validar_contraseñas(cantidad, longitud, incluir_caracteres_especiales)
