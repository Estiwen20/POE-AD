import requests

class ComunicacionLibro():

    def __init__(self, ventanaPrincipal):
        self.url = 'http://localhost:8000/api/libros/'
        self.ventanaPrincipal = ventanaPrincipal
        pass

    def guardar(self, titulo, genero, paginas, año_publicacion):
        try:
            print(titulo, genero, paginas, año_publicacion)
            data = {
                'titulo': titulo,
                'genero': genero,
                'paginas': int(paginas),
                'año_publicacion': int(año_publicacion)
            }
            resultado = requests.post(self.url, json=data)
            print(resultado.json)
            return resultado        
        except:
            pass

    def actualizar(self, id, titulo, genero, paginas, año_publicacion):
        try:
            print(titulo, genero, paginas, año_publicacion)
            data = {
                'titulo': titulo,
                'genero': genero,
                'paginas': paginas,
                'año_publicacion': año_publicacion
            }
            resultado = requests.put(f"{self.url}{str(id)}/", json=data)
            print(resultado.json)
            return resultado
        except:
            pass
    
    def consultar(self, id):
        resultado = requests.get(f"{self.url}{str(id)}/")
        return resultado.json()
    
    def consultar_todo(self, titulo, genero, paginas, año_publicacion):
        url = self.url + "?"
        
        if titulo != '':
            url = url + 'titulo=' + str(titulo) + "&"
        if genero != '':
            url = url + 'genero=' + str(genero) + "&"
        if paginas != '':
            url = url + 'paginas=' + str(paginas) + "&"
        if año_publicacion != '':
            url = url + 'año_publicacion=' + str(año_publicacion) + "&"

        print(url)
        resultado = requests.get(url)
        return resultado.json()
    
    def eliminar(self, id):
        resultado = requests.delete(f"{self.url}{str(id)}/")
        return resultado.status_code