from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('form.html')
           
@app.route("/NumInputs", methods = ['GET', 'POST'])
def numInputs():
    if request.method == 'POST':
        inputs = int(request.form.get('txtInput'))
        
        return render_template('numero.html', inputs = inputs)


@app.route("/Calculo", methods = ['POST'])
def calculo():
  listaString = request.form.getlist('txtNumero')
  numeros = list(map(int, listaString))

  numMayor = max(numeros)
  numMenor = min(numeros)

  promedio = sum(numeros) / len(numeros)

  repeticiones = []
  for numero in numeros:
    apariciones = numeros.count(numero)
    repeticiones.append("{} aparece {} veces".format(numero, apariciones))

  return render_template('resultado.html', numMayor = numMayor, numMenor = numMenor, promedio = promedio, repeticiones = repeticiones)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)