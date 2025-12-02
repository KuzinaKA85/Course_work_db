from abc import ABC, abstractmethod
from typing import Dict, List


class AbstractHHApi(ABC):
    @abstractmethod
    def get_employer(self, employer_id: str) -> Dict:
        pass

    @abstractmethod
    def get_vacancies(self, employer_id: str) -> List:
        pass
