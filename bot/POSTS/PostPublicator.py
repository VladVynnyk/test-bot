from abc import ABC, abstractmethod

class PostPublicator(ABC):

    @abstractmethod
    def publicate_post(self):
        pass

