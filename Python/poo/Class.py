class figura:
    def __init__(self,lados="3"):
        self._lados=lados
    @property
    def lados(self):
        return self._lados
    @lados.setter
    def lados(self,valor):
        if valor<3:
            print("No hay figura con menos de 3 lados")
        else:
            self._lados=valor
    @lados.deleter
    def lados(self):
        del self._lados
    def __str__(self):
        return f"{self.lados}"