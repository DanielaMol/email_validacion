# importar la función que devolverá una instancia de una conexión
from distutils.log import error
from email_app.config.mysqlconnection import connectToMySQL
from flask import flash
from email_app import app
from flask_bcrypt import Bcrypt
import re #*!el módulo regex
#*crea un objeto de expresión regular que usaremos más adelante
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

bcrypt = Bcrypt(app)
#?estamos creando un objeto llamado bcrypt
#?# que se realiza invocando la función Bcrypt con nuestra aplicación como argumento       


class Email:
    db_name="esquema_email"

    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.creador_en = data['created_at']
        self.actualizado_en = data['updated_at']
# ahora usamos métodos de clase para consultar nuestra base de datos
    @classmethod
    def get_all(cls): #*!obtener toda la informacion de la base de datos
        query = "SELECT * FROM email;"
        # asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL(cls.db_name).query_db(query)
        # crear una lista vacía
        emails = []
        print(emails)
        # Iterar sobre los resultados de la base de datos
        for x in results:
            emails.append(cls(x))
        #retornamos una lista de objetos
        return emails
    
    #*METODOS DE CREACION (CREATE)
    @classmethod
    def save(cls, data): #*!guardar informacion en la base de datos
        query = "INSERT INTO email ( email) VALUES ( %(email)s );"
        #*!data es un diccionario que se pasará al método de guardar desde server.py
        return connectToMySQL(cls.db_name).query_db( query, data )

    #*METODOS ESTATICOS - VALIDACION
        #? los métodos estáticos no tienen self o cls pasados a los parámetros
        #*!necesitamos tomar un parámetro para representar
    

    @staticmethod
    def validate_email(input): #*!validaciones
        is_valid = True # asumimos que esto es true
        #*!prueba si un campo coincide con el patrón
        if not EMAIL_REGEX.match(input['email']): 
            flash("Dirección de correo electrónico no válida!")
            is_valid = False
        return is_valid