import re

# Definición de patrones para cada tipo de token
patrones = [
    (r'\{', 'L_LLAVE'),
    (r'\}', 'R_LLAVE'),
    (r'\[', 'L_CORCHETE'),
    (r'\]', 'R_CORCHETE'),
    (r'\,', 'COMA'),
    (r'\:', 'DOS_PUNTOS'),
    (r'\"(\\.|[^\\"])*\"', 'STRING'),
    (r'true|false', 'PR_BOOLEAN'),
    (r'null', 'PR_NULL'),
    (r'-?(0|[1-9]\d*)(\.\d+)?([eE][+-]?\d+)?', 'NUMBER'),
]

# Función que implementa el analizador léxico
def analizador_lexico(linea):
    tokens = []
    while linea:
        # Ignorar espacios en blanco
        if linea[0] == ' ':
            linea = linea[1:]
            continue

        # Encontrar el primer patrón que coincida con la línea
        encontrado = False
        for patron in patrones:
            resultado = re.match(patron[0], linea)
            if resultado:
                tokens.append((resultado.group(0), patron[1]))
                linea = linea[len(resultado.group(0)):]
                encontrado = True
                break

        # Si no se encontró ningún patrón, hay un carácter no válido
        if not encontrado:
            # Imprimir mensaje de error y continuar con la siguiente línea
            print("Error léxico: carácter no válido en la línea", linea)
            return []

    return tokens

# Leer el JSON de entrada línea por línea
with open("input.json") as archivo:
    for linea in archivo:
        # Eliminar saltos de línea y espacios en blanco al inicio y fin de la línea
        linea = linea.strip()

        # Ignorar líneas en blanco
        if not linea:
            continue

        # Analizar léxicamente la línea y obtener los tokens
        try:
            tokens = analizador_lexico(linea)
        except Exception as e:
            # Imprimir mensaje de error y continuar con la siguiente línea
            print("Error léxico:", e)
            continue

        # Imprimir los tokens de la línea
        for token in tokens:
            print(token[1], end=" ")
        print()
