"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    with open('data.csv', 'r') as file:  
        lines=file.readlines()
    suma = sum([int(row[2]) for row in lines])

    return suma


def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        lines=file.readlines()
    letras = [row[0] for row in lines]
    
    salida = dict()
    for letra in letras:
        if letra in salida.keys():
            salida[letra] = salida[letra] + 1
        else:
            salida[letra] = 1
            
    tuplas = [(k, v) for k,v in salida.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)

    return tuplas


def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        lines=file.readlines()
    letras = [(row[0], row[2]) for row in lines]

    salida = dict()
    for letra, valornum in letras:
        if letra in salida.keys():
            salida[letra] = salida[letra] + int(valornum)
        else:
            salida[letra] = int(valornum)
            
    tuplas = [(k, v) for k,v in salida.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)

    return tuplas


def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    from datetime import datetime
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    log_month = [row[2] for row in data]
    count_per_month = dict()
    for ddate in log_month:
        yyear, mmonth, dday = int(ddate[:4]), int(ddate[5:7]), int(ddate[8:10])
        if mmonth == 2 and dday == 29:
            dday = 28
        month =  datetime.strptime(f'{yyear}-{mmonth}-{dday}', '%Y-%m-%d').strftime('%m')
        if month in count_per_month.keys():
            count_per_month[month] = count_per_month[month] + 1
        else:
            count_per_month[month] = 1
            
    tuplas = [(k, v) for k,v in count_per_month.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)

    return tuplas


def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_letters = [[row[0], row[1]] for row in data]
    letter_values = dict()
    for dl in data_letters:
        letter = dl[0]
        if letter not in letter_values.keys():        
            letter_values[letter] = (
                max([
                    int(row[1]) 
                    for row in data_letters 
                    if row[0] == letter
                ]),
                min([
                    int(row[1]) 
                    for row in data_letters 
                    if row[0] == letter
                ])
            )
        
    tuplas = [(k, v[0], v[1]) for k,v in letter_values.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    
    return tuplas


def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_dict = [row[4].split(',') for row in data]
    data_dict = [row_kv for row in data_dict for row_kv in row]
    data_dict = [row.split(":") for row in data_dict]

    letter_values = dict()
    for kvpair in data_dict:
        kkey = kvpair[0]
        if kkey not in letter_values.keys():        
            letter_values[kkey] = (
                min([
                    int(row[1]) 
                    for row in data_dict 
                    if row[0] == kkey
                ]),
                max([
                    int(row[1]) 
                    for row in data_dict
                    if row[0] == kkey
                ])
            )
            
    tuplas = [(k, v[0], v[1]) for k,v in letter_values.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    
    return tuplas


def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_letters = [[row[0], row[1]] for row in data]

    letter_values = dict()
    for kvpair in data_letters:
        kkey = int(kvpair[1])
        if kkey not in letter_values.keys():        
            letter_values[kkey] = (
                [row[0] for row in data_letters if int(row[1]) == kkey]
            )
            
    tuplas = [(k, v) for k,v in letter_values.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    
    return tuplas


def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_letters = [[row[0], row[1]] for row in data]

    letter_values = dict()
    for kvpair in data_letters:
        kkey = int(kvpair[1])
        if kkey not in letter_values.keys():        
            letter_values[kkey] = (
                [row[0] for row in data_letters if int(row[1]) == kkey]
            )
            
    letter_values = {key:list(dict.fromkeys(value)) for (key, value) in letter_values.items()}
    tuplas = [(k, sorted(v, key=operator.itemgetter(0), reverse=False)) for k,v in letter_values.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    
    return tuplas


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_dict = [row[4].split(',') for row in data]
    data_dict = [row_kv for row in data_dict for row_kv in row]
    data_dict = [row.split(":") for row in data_dict]

    letter_values = dict()
    for kvpair in data_dict:
        kkey = kvpair[0]
        if kkey in letter_values.keys():        
            letter_values[kkey] = letter_values[kkey] + 1
        else:
            letter_values[kkey] = 1 

    tuplas = [(k, v) for k,v in letter_values.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    dict_tuplas = dict(tuplas)
    
    return dict_tuplas


def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_letters = [(row[0], len(row[3].split(',')), len(row[4].split(','))) for row in data]
    
    return data_letters


def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_letters = [[row[1], row[3].split(',')] for row in data]
    data_letters = [
        [lt, row[0]]
        for row in data_letters
        for lt in row[1]
    ]

    data_sum_letters = dict()
    for letra, valornum in data_letters:
        if letra in data_sum_letters.keys():
            data_sum_letters[letra] = data_sum_letters[letra] + int(valornum)
        else:
            data_sum_letters[letra] = int(valornum)
            
    tuplas = [(k, v) for k,v in data_sum_letters.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    dict_tuplas = dict(tuplas)
    
    return dict_tuplas


def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    import operator

    with open('data.csv', 'r') as file:  
        data=file.readlines()
    data = [row.replace('\n', '') for row in data]
    data = [row.split("\t") for row in data]

    data_values = [[row[0], row[4].split(",")] for row in data]
    data_values = [
        [   
            row[0],
            dl.split(":")[1]
        ]
        for row in data_values
        for dl in row[1]
    ]

    data_sum_letters = dict()
    for letra, valornum in data_values:
        if letra in data_sum_letters.keys():
            data_sum_letters[letra] = data_sum_letters[letra] + int(valornum)
        else:
            data_sum_letters[letra] = int(valornum)
            
    tuplas = [(k, v) for k,v in data_sum_letters.items()]
    tuplas = sorted(tuplas, key=operator.itemgetter(0), reverse=False)
    dict_tuplas = dict(tuplas)
    
    return dict_tuplas
