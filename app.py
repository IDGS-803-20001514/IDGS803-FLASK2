from flask import Flask, render_template, request
import forms

app = Flask(__name__)

# @app.route('/')
# def formulario():
#     return render_template('formulario.html')

@app.route('/Alumnos', methods = ['GET', 'POST'])
def alumnos():
    alumnos = forms.UseForm(request.form)

    if request.method == 'POST':
        
        print(alumnos.matricula.data)
        print(alumnos.nombre.data)

    return render_template('alumnos.html', form = alumnos)       

@app.route('/')
def formulario():
    return render_template('cajasDinamicas.html')
           
@app.route("/generarCajas", methods = ['GET', 'POST'])
def generarCajas():

    if request.method == 'POST':

        fields = int(request.form.get('numero'))

        return render_template('cajasDinamcasResult.html', fields = fields)
        
    return render_template('cajas-dinamicas.html')

@app.route('/resultado', methods = ['GET', 'POST'])
def resultado():

    if request.method == 'POST':

        fields = int(request.form.get('numeroRegistro'))

        valores = []

        for i in range(fields):

            valores[i] = int(request.form.get('txtNum' + str(i)))

        return render_template('resultado.html', valores = valores)


if __name__ == "__main__":
    app.run(debug = True)