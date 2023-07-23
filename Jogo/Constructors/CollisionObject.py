from abc import ABC, abstractmethod

class CollisionObject(ABC):

    @abstractmethod
    def onCollision(self, otherObject):
        pass
    @abstractmethod
    def getPos(self):
        pass
