from abc import ABC, abstractmethod

class ReadPublicContactInterface(ABC):
    @abstractmethod
    def readPublicContactInfo(viewinfo, information):
        pass