class prenda:
    def __init__(self):
        self._tipo=""
        self._talla=""
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self,siu):
        self._tipo=siu
    @tipo.deleter
    def tipo(self):
        del self._tipo
    @property
    def talla(self):
        return self._talla
    @talla.setter
    def talla(self,siu):
        try:
         siu=int(siu)
        except ValueError:
            print("Su talla no es valida")
            siu=int(input("Digite su talla: "))
        self._talla=siu
    @talla.deleter
    def talla(self):
        del self._talla
