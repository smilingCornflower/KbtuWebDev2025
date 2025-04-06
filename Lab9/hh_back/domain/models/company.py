from dataclasses import dataclass

from domain.models.value_objects import CompanyId


@dataclass
class Company:
    id: CompanyId
    name: str
    description: str
    city: str
    address: str
