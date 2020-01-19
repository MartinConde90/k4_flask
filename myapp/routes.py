from myapp import app #del modulo app me importas la instancia
from flask import render_template #render_template es una funcion

@app.route("/") #este app es la instancia del __init__
def index():
    return render_template('index.html')

@app.route("/detail")
def detail():
    return render_template('detail.html')