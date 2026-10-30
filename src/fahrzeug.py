from abc import ABC, abstractmethod


class Fahrzeug(ABC):
    def __init__(self, kennzeichen: str, parkdauer: int):
        self.__kennzeichen = kennzeichen
        self.__parkdauer = parkdauer

    @property
    def kennzeichen(self):
        return self.__kennzeichen

    @property
    def parkdauer(self):
        return self.__parkdauer

    @abstractmethod
    def berechne_gebuehr(self) -> float:
        pass

    def __str__(self):
        return f"Fahrzeug [{self.__kennzeichen}]"