from abc import ABC, abstractmethod

class DexIntegration(ABC):

    @abstractmethod
    def get_data_about_tokens(self):
        pass
    
    @abstractmethod
    def get_data_about_single_token(self, token_id: str):
        pass


