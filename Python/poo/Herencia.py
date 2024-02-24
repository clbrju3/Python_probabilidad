from Class import figura
class derivada (figura):
    def __init__(self,lados=3,angulos=""):
        super().__init__(lados)
        self._angulos="90"
    @property
    def angulos(self):
        return self._angulos
    @angulos.setter
    def angulos(self,angulo):
        self._angulos=angulo
    @angulos.deleter
    def angulos(self):
        del self._angulos
    def __str__(self):
        return f"{super().__str__()} y {self.angulos}"
