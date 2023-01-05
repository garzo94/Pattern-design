from abc import ABC, abstractmethod
#### PRODUCT ####
"""The drum is our product class"""
class Drum:
    def __init__(self) -> None:

        self.__snare = None
        self.__hihat = None
        self.__bass = None

    def set_snare(self,snare):
        self.__snare = snare

    def set_hihat(self,hihat):
        self.__hihat = hihat

    def set_bass(self,bass):
        self.__bass = bass

    def __str__(self) -> str:
        return f'Drum properties: Snare:{self.__snare.inches}, Hihat: {self.__hihat.brand}, Bass:{self.__bass.leather}'

#### PRODUCT COMPONENTS ###
class Snare:
    inches = None

class Hihat:
   brand = None

class Bass:
    leather = None


### BUILDER INTERFACE ###

"""We have an interface of the builder.
 Two concrete builders (workers) specialized in building different types of drums."""
class IBuilder(ABC):
    @abstractmethod
    def get_snare(self):
     #Assambly snare
     pass

    @abstractmethod
    def get_hihat(self):
     #Assambly snare
     pass

    @abstractmethod
    def get_bass(self):
     #Assambly snare
     pass


### CONCRETE BUILDER ###
class JazzDrumBuilder(IBuilder):
    def get_snare(self):
       snare = Snare()
       snare.inches = 10
       return snare

    def get_hihat(self):
       hihat = Hihat()
       hihat.brand = 'Zildjian'
       return hihat

    def get_bass(self):
       bass = Bass()
       bass.leather = "Soft"
       return bass

class MetalBuilder(IBuilder):

    def get_snare(self):
        snare = Snare()
        snare.inch = 14
        return snare

    def get_hihat(self):
        hihat = Hihat()
        hihat.brand = "Zildjian"
        return hihat

    def get_bass(self):
        bass = Bass()
        bass.leather = "Hard"
        return bass

# DIRECTOR

"""The director gets and appoints the appropriate builder according to the client’s order."""
class Director:
    __builder = None
    drum = Drum()
    def set_builder(self, builder):
       self.__builder = builder

    def get_drum(self):
        snare = self.__builder.get_snare()
        self.drum.set_snare(snare)

        hihat = self.__builder.get_hihat()
        self.drum.set_hihat(hihat)

        bass = self.__builder.get_bass()
        self.drum.set_bass(bass)

        return self.drum

director = Director()
jazzbuilder = JazzDrumBuilder()

director.set_builder(jazzbuilder)
print(director.get_drum())
# Drum properties: Snare:10, Hihat: Zildjian, Bass:Soft



# reference: https://python.plainenglish.io/design-patterns-in-python-builder-pattern-d921fbac7fb3






