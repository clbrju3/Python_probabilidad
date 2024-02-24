from Pernsona import persona
class estudiante(persona):
    def __init__(self,nombre="",edad="",codes="",pro=""):
        super().__init__(nombre,edad)
        self._codes=codes
        self._pro=pro
    @property
    def codes(self):
        return self._codes
    @codes.setter
    def codes(self,cod):
        self._codes=cod
    @codes.deleter
    def codes(self):
        del self._codes
    @property
    def pro(self):
        return self._pro
    @pro.setter
    def pro(self,cod):
        self._pro=cod
    @pro.deleter
    def pro(self):
        del self._pro
    def comp(self,mat):
        print(f"Materia: {mat}")
    def __str__(self):
        return f"{super().__str__()} y {self.codes} o {self.pro}"