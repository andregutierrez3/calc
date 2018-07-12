
from start import app
from calc import Calc
from flask import request, jsonify

@app.route('/')
@app.route("/calculadora/<m>")
def operacao(m=0):



    if request.method == 'POST':

        x = Calc(request.form.get['X'], request.form.get['Y'])

        if m == 'divisao':

            r = {'resultado': x.divisao()}

            return jsonify(r)

        elif m == "multiplicacao":

            r = {'resultado': x.multiplicacao()}

            return jsonify(r)

        elif m == 'soma':

            r = {'resultado': x.soma()}

            return jsonify(r)

        elif m == 'sub':

            r = {'resultado': x.sub()}

            return jsonify(r)

    elif request.method == 'GET':
        return "FACA UM POST PARA USAR A CALCULADORA"

    else:
        return "Defina uma operacao basica"


app.run(debug=True)
