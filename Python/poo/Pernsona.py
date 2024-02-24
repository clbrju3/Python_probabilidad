class persona:
    def __init__(self,nombre=" ",edad=""):
        self._nombre=nombre
        self._edad=edad
    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,nom):
        self._nombre=nom
    @nombre.deleter
    def nombre(self):
        del self._nombre
    @property
    def edad(self):
        return self._edad
    @edad.setter
    def edad(self,nom):
        self._edad=nom
    @edad.deleter
    def edad(self):
        del self._edad
    def comer(self,comida):
        print(f"{self.nombre} come {comida}")
    def __str__(self):
        return f"{self.nombre},{self.edad}"
