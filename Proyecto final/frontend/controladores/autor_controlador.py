import requests

class ComunicacionAutor():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/api/autores/'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, nombre, edad, nacionalidad):
        try:
            print(nombre, edad, nacionalidad)
            data = {
                'nombre': nombre,
                'edad': edad,
                'nacionalidad': nacionalidad
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado
        except:
            pass

    def actualizar(self, id, nombre, edad, nacionalidad):
        try:
            print(nombre, edad, nacionalidad)
            data = {
                'nombre': nombre,
                'edad': edad,
                'nacionalidad': nacionalidad
            }
            resultado = requests.put(f"{self.url}{str(id)}/", json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        resultado = requests.get(f"{self.url}{str(id)}/")
        return resultado.json()
    
    def consultar_todo(self, nombre, edad, nacionalidad):
        url = self.url + "?"
        
        if nombre != '':
            url = url + 'nombre=' + str(nombre) + "&"
        if edad != '':
            url = url + 'edad=' + str(edad) + "&"
        if nacionalidad != '':
            url = url + 'nacionalidad=' + str(nacionalidad) + "&"

        print(url)
        resultado = requests.get(url)
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(f"{self.url}{str(id)}/")
        return resultado.status_code