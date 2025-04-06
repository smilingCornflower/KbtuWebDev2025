from abc import ABC, abstractmethod
from typing import TYPE_CHECKING
from uuid import UUID
from domain.models.company import Company
from domain.models.vacancy import Vacancy
from domain.models.value_objects import CompanyId


class CompanyRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[Company]:
        pass

    @abstractmethod
    def get_by_id(self, company_id: CompanyId) -> Company:
        pass

    @abstractmethod
    def get_vacancies(self, company_id: CompanyId) -> list[Vacancy]:
        pass
