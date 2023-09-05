import os

def clear_terminal():
    # Comando para borrar la terminal 
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    number = 0

    while number <= 50:
        clear_terminal()
        print(f"Número actual: {number}")
        
        key = input("Presiona 'n' para incrementar el número o Enter para salir: ")
        
        if key.lower() == 'n':
            number += 1
        else:
            break

if __name__ == "__main__":
    main()