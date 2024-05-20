import os, ast

try:
    xcom = ast.literal_eval(os.getenv('X_COM'))
    print(f'XCom Recebida! A data de hoje é: {xcom['data']}')

except ValueError:
    print('Opa, não chegou nada aqui man')
