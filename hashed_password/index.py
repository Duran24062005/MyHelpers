# Como hashear una contraseña
# Primero importamos bcrypt
import bcrypt

def encriptar_password():
    # creamos texto panoa a hashear
    my_string = "hola mundo"

    # Luego lo pasamos a byte ya que la función que vamos a utilizar necesita recibir así los datos (hashpwd)
    my_string_hashed_1 = b"hola mundo" # La b al inicio pasa el texto a byte
    my_string_hashed_2 = my_string.encode() # O de está manera tambien funciona.and

    # Para esto debempos tener en cuenta el SALT, este es un argumento que basicamente determina la fuerza del hasheado
    # mientras más alto es, más fuerte es el hasheado, pero eso tambien significa que tardará más en generarse y desencodificarse.

    # Pasamos a generar la salt, por defecto es 12, ya que no tarda nada.
    salt = bcrypt.gensalt(12)

    password_hasheado_1 = bcrypt.hashpw(my_string_hashed_1, salt)
    password_hasheado_2 = bcrypt.hashpw(my_string_hashed_2, salt)

    print(password_hasheado_1)
    print(password_hasheado_2)

def desencriptar_password(text_hashed):
    pass



def hash_pass1():
    my_string = "hola mundo"
    hash_value = hash(my_string)
    print(hash_value)