from src.parkhaus import Parkhaus
from src.pkw import PKW, ElektroPKW
from src.exceptions import (
    ParkhausVollError,
    FahrzeugNichtGefundenError
)

parkhaus = Parkhaus(kapazitaet=2)

p1 = PKW("M-AZ 100", 90, ist_vip=True)
e1 = ElektroPKW("B-EV 200", 61)
p2 = PKW("K-X 300", 30)

parkhaus.einfahrt(p1)
parkhaus.einfahrt(e1)

assert "M-AZ 100" in parkhaus
assert len(parkhaus) == 2

try:
    parkhaus.einfahrt(p2)
except ParkhausVollError as e:
    print(f"Erfolg: {e}")

gebuehr = parkhaus.ausfahrt("M-AZ 100")
print(
    f"Ausfahrtgebühr M-AZ 100: {gebuehr:.2f} €"
)

print("\nAktueller Bericht:")

for kennzeichen, gebuehr in parkhaus.bericht():
    print(f"{kennzeichen}: {gebuehr:.2f} €")

try:
    parkhaus.ausfahrt("XYZ-999")
except FahrzeugNichtGefundenError as e:
    print(f"Erfolg: {e}")