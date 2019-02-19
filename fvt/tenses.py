from enum import Enum
class Tenses(Enum):

    def __str__(self):
        return str(self.name)

    PRÉSENT = "présent"
    PASSÉ_COMPOSÉ = "passé composé"
    PASSÉ_SIMPLE = "passé simple"
    IMPARFAIT = "imparfait"
    PLUS_QUE_PARFAIT = "plus-que-parfait"
    FUTUR_COMPOSÉ = "futur composé"
    FUTUR_SIMPLE = "futur simple"
    FUTUR_ANTÉRIEUR = "futur antérieur"
