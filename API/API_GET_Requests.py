from base64 import encode
import requests as r

a = r.get("https://servicodados.ibge.gov.br/api/v1/localidades/estados/35/municipios")
a.encoding="UTF-8"
with open("API/json_response.txt",'w') as f:
    for i in a.text:
        f.write(i)