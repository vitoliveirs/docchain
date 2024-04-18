import json
import ipfshttpclient
import os
from datetime import datetime

class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return json.JSONEncoder.default(self, obj)

def addData(Data: dict, Hash: str):
    try:
        # Conecta ao daemon do IPFS
        client = ipfshttpclient.connect('/ip4/62.169.20.134/tcp/5001')

        # Converte o dicionário em uma string JSON
        jsonData = json.dumps(Data, cls=MyEncoder)

        # Adiciona a string ao IPFS
        ipfsAdd = client.add_str(jsonData)

        document = Data['document']

        # Converte a string JSON em bytes
        jsonData_bytes = jsonData.encode('utf-8')

        # Define o caminho completo para o arquivo JSON
        file_path = os.path.join('app', 'ipfsExams', f'{Hash}-exam.json')
        # Cria um novo arquivo JSON localmente
        with open(file_path, 'wb') as json_file:
            json_file.write(jsonData_bytes)

    except Exception as e:
        raise ValueError(f"Falha ao adicionar arquivo ao IPFS. Detalhes: {str(e)}")

    return 1