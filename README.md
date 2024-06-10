Esta aplicación permite gestionar contactos desde la línea de comandos.

Proyecto: "Aplicación de Gestión de Contactos"
Este proyecto consistirá en crear una aplicación de gestión de contactos desde la línea de comandos. Implementarás funcionalidades para agregar, eliminar, buscar y listar contactos. Además, utilizarás Git para controlar las versiones de tu proyecto y un entorno virtual para gestionar las dependencias.

Paso 1: Configuración Inicial
Crea un directorio para tu proyecto:

bash
Copiar código
mkdir gestion_contactos
cd gestion_contactos
Inicializa un repositorio Git:

bash
Copiar código
git init
Crea un archivo README.md para documentar tu proyecto:

markdown
Copiar código
# Aplicación de Gestión de Contactos

Esta aplicación permite gestionar contactos desde la línea de comandos.
Crea un archivo .gitignore para excluir archivos innecesarios:

bash
Copiar código
echo "venv/" > .gitignore
echo "__pycache__/" >> .gitignore
echo "*.pyc" >> .gitignore
Haz tu primer commit:

bash
Copiar código
git add README.md .gitignore
git commit -m "Initial commit: Add README and .gitignore"
Paso 2: Configuración del Entorno Virtual
Crea un entorno virtual:

bash
Copiar código
python -m venv venv
Activa el entorno virtual:

En Windows:
bash
Copiar código
.\venv\Scripts\activate
En macOS/Linux:
bash
Copiar código
source venv/bin/activate
Crea un archivo requirements.txt para las dependencias:

bash
Copiar código
touch requirements.txt
Instala cualquier dependencia que necesites (por ejemplo, tabulate para formatear tablas):

bash
Copiar código
pip install tabulate
pip freeze > requirements.txt
Haz un commit para el entorno virtual y las dependencias:

bash
Copiar código
git add requirements.txt
git commit -m "Setup virtual environment and add requirements.txt"
Paso 3: Estructura Básica del Proyecto
Crea un archivo principal para tu script en Python (gestion_contactos.py):

python
Copiar código
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
Haz un commit para la estructura básica del proyecto:

bash
Copiar código
git add gestion_contactos.py
git commit -m "Add basic structure for contact management application"
Paso 4: Implementar Funcionalidades Adicionales
Crear una rama para la nueva funcionalidad (por ejemplo, eliminar contacto):

bash
Copiar código
git checkout -b feature/eliminar_contacto
Agregar funcionalidad para eliminar contactos:

python
Copiar código
# gestion_contactos.py

def eliminar_contacto(nombre):
    global contactos
    contactos = [contacto for contacto in contactos if contacto["nombre"] != nombre]

def main():
    print("Aplicación de Gestión de Contactos")
    while True:
        comando = input("Comando (agregar/listar/eliminar/salir): ")
        if comando == "agregar":
            nombre = input("Nombre: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            agregar_contacto(nombre, telefono, email)
        elif comando == "listar":
            listar_contactos()
        elif comando == "eliminar":
            nombre = input("Nombre del contacto a eliminar: ")
            eliminar_contacto(nombre)
        elif comando == "salir":
            break

if __name__ == "__main__":
    main()
Haz un commit para esta nueva funcionalidad:

bash
Copiar código
git add gestion_contactos.py
git commit -m "Add feature to delete contacts"
Fusionar la rama de la nueva funcionalidad:

bash
Copiar código
git checkout main
git merge feature/eliminar_contacto
Paso 5: Continuar con Nuevas Funcionalidades
Repite el proceso de crear ramas, agregar nuevas funcionalidades y fusionarlas en la rama principal. Algunas funcionalidades adicionales pueden ser:

Buscar contactos por nombre:

Crea una rama feature/buscar_contacto.
Implementa la funcionalidad para buscar contactos por nombre.
Crea commits y fusiónalos a la rama principal.
Guardar y cargar contactos desde un archivo:

Crea una rama feature/persistencia.
Implementa la funcionalidad para guardar y cargar contactos desde un archivo.
Crea commits y fusiónalos a la rama principal.
Ejemplo de comandos para Git y el entorno virtual
Ver el historial de commits:

bash
Copiar código
git log
Ver el estado del repositorio:

bash
Copiar código
git status
Mostrar diferencias entre commits:

bash
Copiar código
git diff
Crear una nueva rama:

bash
Copiar código
git checkout -b nombre_de_la_rama
Fusionar una rama:

bash
Copiar código
git checkout main
git merge nombre_de_la_rama
Instalar dependencias desde requirements.txt:

bash
Copiar código
pip install -r requirements.txt
Guardar dependencias en requirements.txt:

bash
Copiar código
pip freeze > requirements.txt