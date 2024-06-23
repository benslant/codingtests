from abc import ABC, abstractmethod
from typing import List

class IPerson(ABC):

    @abstractmethod
    def first_name():
        pass

    @abstractmethod
    def last_name():
        pass

class ISoftwareEngineer(ABC):

    @abstractmethod
    def languages() -> List['str']:
        pass

class OfficeWorker(IPerson, ISoftwareEngineer):

    def __init__(self, first_name: str, last_name: str, languages: List[str]) -> None:
        super().__init__()
        self._first_name = first_name
        self._last_name = last_name
        self._languages = languages

    def __str__(self):
        return f"{self._first_name} {self._last_name}"

    def first_name(self):
        return self._first_name
    
    def last_name(self):
        return self._last_name
    
    def languages(self) -> List[str]:
        return self._languages
        
def display_worker_lanaguages(engineer: ISoftwareEngineer):
    print(engineer.languages())

def display_worker_name(engineer: IPerson):
    print(engineer)

person = OfficeWorker("ben", "caldwell", ["C#", "Python"])

display_worker_name(person)
display_worker_lanaguages(person)

    