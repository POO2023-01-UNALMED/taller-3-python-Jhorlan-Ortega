class Marca:
    def __init__(self, nombre):
        self._nombre = nombre

    def setNombre(self, nombre):
        self._nombre = nombre

    def getNombre(self):
        return self._nombre


class TV:
    _numTV = 0

    def __init__(self, marca, estado):
        self._marca = marca
        self._estado = estado
        self._canal = 1
        self._volumen = 1
        self._precio = 500
        self._control = None
        TV._numTV += 1

    def getMarca(self):
        return self._marca

    def setMarca(self, marca):
        self._marca = marca

    def getControl(self):
        return self._control

    def setControl(self, control):
        self._control = control

    def getPrecio(self):
        return self._precio

    def setPrecio(self, precio):
        self._precio = precio


    def getVolumen(self):
        return self._volumen

    def getCanal(self):
        return self._canal

    def setCanal(self, canal):
        if self.estado:
            if (canal >= 1 and canal <= 120):
                self._canal = canal
        else:
            pass

    @classmethod
    def getNumTV(cls):
        return cls._numTV

    @classmethod
    def setNumTV(cls, numTV):
        cls._numTV = numTV

    def getEstado(self):
        return self._estado

    def turnOn(self):
        self._estado = True

    def turnOff(self):
        self._estado = False

    def canalUp(self):
        if self.estado == True:
            if (self._canal < 120):
                self._canal += 1

    def canalDown(self):
        if self.estado == True:
             if (self._canal > 1):
                 self._canal -= 1

    def volumenUp(self):
        if self.estado == True:
            if (self._estado == True and self._volumen < 7):
                self._volumen += 1

    def volumenDown(self):
        if self.estado == True
            if self._volumen > 1:
                self._volumen -= 1

    def setVolumen(self, nVolumen):
        if (nVolumen <= 7 and nVolumen >= 1):
            self._volumen = nVolumen
        else:
            pass


class Control:

    def __init__(self):
        self._tv = None

    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)

    def turnOn(self):
        self._tv.turnOn()

    def canalUp(self):
        self._tv.canalUp()

    def volumenUp(self):
        self._tv.volumenUp()

    def turnOff(self):
        self._tv.turnOff()

    def canalDown(self):
        self._tv.canalDown()

    def volumenDown(self):
        self._tv.volumenDown()

    def setCanal(self, canal):
        self._tv.setCanal(canal)

    def getTv(self):
        return self._tv

    def setTv(self, tv):
        self.tv = tv