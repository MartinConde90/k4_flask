from myapp import app #del modulo app me importas la instancia

@app.route("/") #este app es la instancia del __init__
def index():
    return 'Aquí irá mi app'