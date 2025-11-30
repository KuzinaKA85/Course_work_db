from abc import ABC, abstractmethod
from typing import Any, List, Dict


class AbstractHHApi(ABC):
    """Абстрактный класс для работы с API hh.ru"""

    @abstractmethod
    def get_vacancies(self, employers_ids: List[str]) -> List[Dict[str, Any]]:
        pass
