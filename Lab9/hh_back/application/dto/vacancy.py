from dataclasses import dataclass


@dataclass
class VacancyDTO:
    id: str
    name: str
    description: str
    salary: float
    company_id: str

