from dataclasses import dataclass

from domain.models.value_objects import CompanyId, VacancyId

@dataclass
class Vacancy:
    id: VacancyId
    name: str
    description: str
    salary: float
    company_id: CompanyId
