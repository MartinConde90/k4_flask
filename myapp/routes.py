from myapp import app 
from flask import render_template, request #render_template es una funcion
import csv

@app.route("/") #este app es la instancia del __init__
def index(): #esa funcion va asociada al recurso entre parentesis de arriba, los paremetros que metamos arriba tras /, irán aquí
    '''
    leer el fichero sales.csv y transformarlo en un diccionario
    '''
    fSales = open('./data/sales.csv','r') #los puntos hacen salir de myapp, y luego que entre en data y sales, 'r' es solo lectura

    csvreader = csv.reader(fSales, delimiter=',') #es un manejador de csv
    registros = []
    for linea in csvreader:
        registros.append(linea)
    
    cabecera = registros[0] # aqui tenemos la primera linea de sales.cvs, con pais, producto etc etc

    ventas = []
    for datos in registros[1:]:
        d = {} #lo ponemos dentro para que se ponga a cero cada vez que pasemos por ahi
        for ix, nombre_campo in enumerate(cabecera): # enumerate devuelve una tupla con la posicion y el dato
            d[nombre_campo] = datos[ix]
        ventas.append(d)

        '''
        i = 0
        for nombre_campo in cabecera: # delego el control del nombre y yo llevo el indice
            d[nombre_campo] = datos[i]
            i += 1
        
        for ix in range(len(cabecera)): # delego el control del indice y yo llevo el nombre
            nombre_campo = cabecera[ix]
            d[nombre_campo] = datos[ix]
        '''
        

    '''
    procesarlo para obtener los totales
    '''
    datos = {}
    for linea in ventas:
        if linea['region'] in datos:
            regAct = datos[linea['region']]
            regAct['ingresos_totales'] += float(linea['ingresos_totales'])
            regAct['beneficios_totales'] += float(linea['beneficio'])
        else:
            datos[linea['region']] = {'ingresos_totales': float(linea['ingresos_totales']), 'beneficios_totales': float(linea['beneficio'])}
    '''
    Finalmente devolvemos una lista de tuplas con la estructura
    [('Region', {'ingresos_totales': valor, 'beneficios_totales': valor}),...]
    '''
    resultado = []
    for clave in datos:
        resultado.append((clave, datos[clave]))


    '''
    enviarlo a index.html
    '''
    return render_template('index.html', registros=resultado)


@app.route("/detail")
def detail():

    datos = {}
    region_name = request.values['region'] #values es un diccionario con los datos
    for linea in ventas:
        print(linea['region'])
        if linea['region'] == region_name:
            if linea['pais'] in datos:
                regAct = datos[linea['pais']]
                regAct['ingresos_totales'] += float(linea['ingresos_totales'])
                regAct['beneficios_totales'] += float(linea['beneficio'])
            else:
                datos[linea['pais']] = {'ingresos_totales': float(linea['ingresos_totales']), 'beneficios_totales': float(linea['beneficio'])}

    print(datos)
    return render_template('detail.html', region=region_name, registros=datos)
