# gestion_contactos.py

contactos = []

def agregar_contacto(nombre, telefono, email):
    contactos.append({"nombre": nombre, "telefono": telefono, "email": email})

def listar_contactos():
    for contacto in contactos:
        print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

def main():
    print("Aplicación de Gestión de Contactos")
    while True:
        comando = input("Comando (agregar/listar/salir): ")
        if comando == "agregar":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agregar_contacto(nombre, telefono, email)
        elif comando == "listar":
            listar_contactos()
        elif comando == "salir":
            break

if __name__ == "__main__":
    main()
