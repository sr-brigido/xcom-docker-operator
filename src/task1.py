from datetime import datetime
import pickle

dataHoje = datetime.today().strftime('%d/%m/%Y')

saida = {
    'data': dataHoje
}

with open('/tmp/script.out', 'wb+') as output:
    pickle.dump(saida,output)