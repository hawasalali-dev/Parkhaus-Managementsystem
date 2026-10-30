import math

from .fahrzeug import Fahrzeug


class PKW(Fahrzeug):
    PREIS_PRO_STUNDE = 2.50

    def __init__(self, kennzeichen: str, parkdauer: int, ist_vip: bool = False):
        super().__init__(kennzeichen, parkdauer)
        self.ist_vip = ist_vip

    def berechne_gebuehr(self) -> float:
        stunden = math.ceil(self.parkdauer / 60)
        gebuehr = stunden * self.PREIS_PRO_STUNDE

        if self.ist_vip:
            gebuehr *= 0.8  # 20 % Rabatt

        return round(gebuehr, 2)


class ElektroPKW(PKW):

    def berechne_gebuehr(self) -> float:
        gebuehr = super().berechne_gebuehr()
        gebuehr -= 1.50

        return round(max(0.0, gebuehr), 2)