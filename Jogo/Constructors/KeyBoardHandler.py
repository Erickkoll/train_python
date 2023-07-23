from abc import ABC, abstractmethod
class KeyBoardHandler(ABC):

    @abstractmethod
    def keyboard_handler(self, keyboard_event):
        pass
