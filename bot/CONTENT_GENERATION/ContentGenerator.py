from abc import ABC, abstractmethod

class ContentGenerator(ABC):

    @abstractmethod
    def generate_post(self):
        pass
    
    @abstractmethod
    def generate_meme(self, token_id: str):
        pass


