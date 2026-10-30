class ParkhausVollError(Exception):
    """Wird ausgelöst, wenn das Parkhaus voll ist."""
    pass


class FahrzeugNichtGefundenError(Exception):
    """Wird ausgelöst, wenn ein Fahrzeug nicht gefunden wird."""
    pass