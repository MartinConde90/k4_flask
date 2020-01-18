from flask import Flask

app = Flask(__name__) #instancia de flask, esto contiene toda nuestra app 

@app.route('/') #nos crea una ruta(punto de entrada) en nuestro servidor detras de '/' es lo que va despues del .es/, app se refiere a la instancia de arriba
def hello_world():
    return 'Hola, mundo'
# set FLASK_APP=hello.py en el terminal, crea una ventana a nivel del terminal, mete el programa en la variable
# flask run ---> levanta un servidor flask de pruebas

@app.route('/otrorecurso')
def otro():
    return  '''
    <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Mi pagina</title>
        </head>
        <body>
            <h1>Mi saludo</h1>
            <p>Hola, mundo</p>
        </body>
    </html>
    '''