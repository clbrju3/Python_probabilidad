class pi:
    def __init__(self,casa="siiuuu",jose=False):
        self.aja=casa
        self.yuhu=jose
    @property
    def aja(self):
        return self._aja
    @aja.setter
    def aja(self,casa):
        self._aja=casa
    @aja.deleter
    def aja(self):
        del self._aja
    @property
    def yuhu(self):
        return self._yuhu
    @yuhu.setter
    def yuhu(self,casa):
        self._yuhu=casa
    @yuhu.deleter
    def yuhu(self):
        del self._yuhu
    def __str__(self):
        return(f"Primero: {self.aja}\nSegundo: {self.yuhu}")
    
    