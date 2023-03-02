"""
Este módulo contiene el script principal del proyecto.
"""

import os
import subprocess


def main():
    """Este es el docstring de mi_paquete"""
    # Crear directorio 'build' si no existe
    os.makedirs('build', exist_ok=True)

    # Compilar archivo index.html
    subprocess.run(['touch', 'build/index.html'], check=False)


if __name__ == '__main__':
    main()

