from .fahrzeug import Fahrzeug
from .exceptions import (
    ParkhausVollError,
    FahrzeugNichtGefundenError
)


class Parkhaus:
    def __init__(self, kapazitaet: int):
        self.kapazitaet = kapazitaet
        self.__fahrzeuge = {}

    def einfahrt(self, fahrzeug):
        if not isinstance(fahrzeug, Fahrzeug):
            raise TypeError(
                "Nur Objekte vom Typ Fahrzeug dürfen einfahren."
            )

        if len(self.__fahrzeuge) >= self.kapazitaet:
            raise ParkhausVollError(
                "Parkhaus ist voll."
            )

        self.__fahrzeuge[fahrzeug.kennzeichen] = fahrzeug

    def ausfahrt(self, kennzeichen):
        if kennzeichen not in self.__fahrzeuge:
            raise FahrzeugNichtGefundenError(
                f"Fahrzeug '{kennzeichen}' nicht gefunden."
            )

        fahrzeug = self.__fahrzeuge.pop(kennzeichen)
        return fahrzeug.berechne_gebuehr()

    def bericht(self):
        for kennzeichen, fahrzeug in self.__fahrzeuge.items():
            yield (
                kennzeichen,
                fahrzeug.berechne_gebuehr()
            )

    def __len__(self):
        return len(self.__fahrzeuge)

    def __contains__(self, kennzeichen):
        return kennzeichen in self.__fahrzeuge