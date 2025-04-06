from abc import ABC, abstractmethod

from domain.models.enums import SortDirection
from domain.models.vacancy import Vacancy
from domain.models.value_objects import VacancyId


class VacancyRepository(ABC):
    @abstractmethod
    def get_all(
            self, *,
            order_by: str | None = None,
            direction: SortDirection | None = None,
            limit: int | None = None
    ) -> list[Vacancy]:
        pass

    @abstractmethod
    def get_by_id(self, vacancy_id: VacancyId) -> Vacancy:
        pass
