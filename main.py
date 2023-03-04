from collections import Counter
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def formulario():
    return render_template('indexCajasDinamicas.html')
           
@app.route("/numInputs", methods = ['GET', 'POST'])
def numInputs():
    if request.method == 'POST':
        numeroInputs = int(request.form.get('txtNumeroInputs'))
        
        return render_template('cajasDinamicasInputs.html', numeroInputs = numeroInputs)


@app.route("/cajasDinamicasInputs", methods = ['POST'])
def cajasDinamicasInputs():
  numeroCaja = request.form.getlist('txtNumeroR')
  lstNumero = list(map(int, numeroCaja))

  mayor = max(lstNumero)
  menor = min(lstNumero)

  promedio = sum(lstNumero) / len(lstNumero)

  contador = Counter(numeroCaja)
  resultados = contador.most_common()
  resultado = []
  for i in resultados:
        if i[1] > 1:
            resultado.append('El numero {0} se repite: {1}'.format(i[0], i[1]))

  return render_template('cajasDinamicasResultado.html', numMayor = mayor, numMenor = menor, promedio = promedio, resultadoFinal = resultado)

if __name__ == "__main__":
    app.run(debug = True, port = 8080)