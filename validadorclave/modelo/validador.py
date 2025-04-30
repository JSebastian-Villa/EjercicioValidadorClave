from abc import ABC, abstractmethod


class ReglaValidacion(ABC):
    def __init__(self, _longitud_esperada: int):
        self._longitud_esperada = _longitud_esperada

    def _validar_longitud(self, clave: str) -> bool:
        pass
    def _contiene_mayuscula(self, clave: str) -> bool:
        pass

    def _contiene_minuscula(self, clave: str) -> bool:
        pass

    def _contiene_numero(self, clave: str) -> bool:
        pass

    @abstractmethod
    def es_valida(self, clave: str) -> bool:
        pass

    class ReglaValidacionGanimedes(ReglaValidacion):
        def _init_(self):
            pass

        def contiene_caracter_especial(self, clave: str) -> bool:
            pass

        def es_valida(self, clave: str) -> bool:
            pass









