from abc import ABC, abstractmethod

class EditContactInfoInterface(ABC):
    @abstractmethod
    def editInfo(editContact):
        pass

    @abstractmethod
    def edit(contactInfo):
        pass

