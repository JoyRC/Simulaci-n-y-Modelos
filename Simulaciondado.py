
import random

def lanzar_dado():
    return random.randint(1, 6)

def main():
    
    while True:
        input ("Presiona 'Enter' para lanzar el dado o escribe 'salir' para terminar: ")
        
        if input.lower() == 'salir':
                break
    
        resultado = lanzar_dado()
        print(f"Has lanzado un {resultado}!")
    
    print("Gracias por jugar. ¡Hasta la próxima!")

if __name__ == "__main__":
    main()    