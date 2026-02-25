class AbstractProduct(ABC):

    @abstractmethod
    def get_details(self):
        pass


class AbstractUser(ABC):

    @abstractmethod
    def get_profile(self):
        pass
