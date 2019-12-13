import json
import os
import requests

base_url = 'http://wichi.siu.edu.ar/pentaho/plugin/cda/api/doQuery?'
USERNAME = 'usuario_transparencia'
PASSWORD = 'clave_transparencia'
# headers={'Content-type':'application/json', 'Accept':'application/json'}


def get_api_data(name, params):
    resp = requests.post(base_url, auth=(USERNAME, PASSWORD), data=params)  #, headers=headers)
    data = resp.json()
    return data

data_folder = 'data'
query_folder = 'queries'
directory = os.fsencode(query_folder)

for filen in os.listdir(directory):
     filename = os.fsdecode(filen)
     if filename.endswith(".json"):
        path = os.path.join(query_folder, filename)
        f = open(path, 'r')
        query = json.load(f)
        f.close()
        name = query['name']
        data = get_api_data(name=name, params=query['params'])
        print('##############')
        print(name)
        print('##############')
        print(data)
        # save
        data_str = json.dumps(data, indent=4)
        save_to = os.path.join(data_folder, filename)
        f = open(save_to, 'w')
        f.write(data_str)
        f.close()
