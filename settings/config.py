import os

class configuracion (object):
    SECRET_KEY= os.environ.get('SECRET_KEY') or 'contraseña'

# la variable SECRET_KEYes parte importante de las aplicaciones flask ya que se puede utilizar como llave criptografica
# en la generacion de firmas digitales y tokens

# para este ejemplo la extension flask-wtf la usa para proteger los formualrios de ataques del tipo 
# CSRF (croos-site Request Forgery / falsificacion de solicitudes entre sitios)