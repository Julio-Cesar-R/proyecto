import requests,json, jsonify

def apilist(url):
   
    response=requests.get(url)
    print(f"El codigo de espuesta de la api es {response.status_code}")
    response=json.loads(response.text)
    print("++++++++++++++++++++++")
    print(response)
    print("********************")
    print(response["results"])
    print("===========================")
    for persona in response["results"]:
        print(persona["estudiante"]["nombre"])
        print(persona["nombre_carrera"])
    return response

def api_detail(pk):

    url=f"http://127.0.0.1:8000/persona/api_buscar_pk/{str(pk)}/"
    response=requests.get(url)
    print(f"El codigo de espuesta de la api es {response.status_code}")
    response=json.loads(response.text)
    print("============================")
    print(response)
    if response:
        return response
    else:
        return jsonify({"respuesta":"El registro no existe"})
    
