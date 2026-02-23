from abc import ABC, abstractmethod  # For Abstraction
import datetime

class AbstractProduct(ABC):
    
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def apply_discount(self, percentage):
        pass

    @abstractmethod
    def get_category(self):
        pass

class AbstractUser(ABC):

    @abstractmethod
    def get_profile(self):
        pass

    @abstractmethod
    def get_role(self):
        pass