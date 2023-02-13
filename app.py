from multiprocessing.resource_tracker import ResourceTracker
from flask import Flask, flash, redirect, url_for, request, render_template
from settings.config import configuracion
from formulario import FormInicio

app= Flask(__name__)
app.config.from_object(configuracion)


@app.route('/')
def index():    
    return render_template('index.html', titulo='Inicio de la aplicación')

@app.route('/login/', methods=['GET','POST'])
def login():
    formulario= FormInicio()
    if (formulario.validate_on_submit()):
        flash(f'Inicio de sesión solicitado por el usuario {formulario.nombre.data} ')
        return redirect(url_for ('logueado'))
    return render_template('inicio.html',titulo='Iniciar sesion', formI=formulario)

@app.route('/logueado')
def logueado():
    return render_template('logueado.html')

app.run(host='localhost', port=5000, debug=True)
