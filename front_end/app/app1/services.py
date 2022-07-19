from typing import Type
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
    '''
    for persona in response["results"]:
        print(persona["estudiante"]["nombre"])
        print(persona["nombre_carrera"])
    '''
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

 #--------------------------------------------------------------------   
def api_create(name,apellido_p,apellido_m,edad,email,telefono):
    
    url="http://127.0.0.1:8000/persona/api_create/"
    _json={
    "nombre": name,
    "apellido_paterno": apellido_p,
    "apellido_materno": apellido_m,
    "edad": edad,
    "email": email,
    "telefono": telefono
}
    
    print(json.dumps(_json))
    encabezado={"Content-Type":"application/json"}
    response=requests.post(url,data=json.dumps(_json),headers=encabezado)
    print(response.content)
    return response
