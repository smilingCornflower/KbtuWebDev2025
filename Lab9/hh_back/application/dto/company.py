from dataclasses import dataclass


@dataclass
class CompanyDTO:
    id: str
    name: str
    description: str
    city: str
    address: str
