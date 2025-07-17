from flask import Flask, render_template, request, redirect
import csv
import os

app = Flask(__name__)

FACTURAS_FILE = 'facturas.csv'

@app.route('/extra', methods=['GET', 'POST'])
def formulario():
    if request.method == 'POST':
        datos = [
            request.form['nombre'],
            request.form['rfc'],
            request.form['regimen'],
            request.form['cfdi']
        ]

        archivo_existe = os.path.isfile(FACTURAS_FILE)
        with open(FACTURAS_FILE, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            if not archivo_existe:
                writer.writerow(['Nombre', 'RFC', 'Régimen Fiscal', 'Uso del CFDI'])
            writer.writerow(datos)

        return redirect('/extra')

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)