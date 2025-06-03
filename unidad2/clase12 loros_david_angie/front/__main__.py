import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from front.vistas.interfaz import Interfaz

def main():
    Interfaz()  # Inicia la interfaz gráfica

if __name__ == "__main__":
    main()

