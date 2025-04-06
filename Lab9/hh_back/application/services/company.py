from application.dto.company import CompanyDTO
from application.dto.vacancy import VacancyDTO
from domain.models.company import Company
from domain.models.vacancy import Vacancy
from domain.models.value_objects import CompanyId
from domain.repositories.company import CompanyRepository


class CompanyAppService:
    def __init__(self, repository: CompanyRepository):
        self.repository = repository

    def get_all_companies(self) -> list[CompanyDTO]:
        companies: list[Company] = self.repository.get_all()
        return [
            CompanyDTO(
                id=str(company.id),
                name=company.name,
                description=company.description,
                city=company.city,
                address=company.address
            ) for company in companies
        ]

    def get_company(self, company_id: CompanyId) -> CompanyDTO:
        company: Company = self.repository.get_by_id(company_id)
        return CompanyDTO(
            id=str(company.id),
            name=company.name,
            description=company.description,
            city=company.city,
            address=company.address
        )

    def get_company_vacancies(self, company_id: CompanyId) -> list[VacancyDTO]:
        vacancies: list[Vacancy] = self.repository.get_vacancies(company_id)
        return [
            VacancyDTO(
                id=str(vacancy.id),
                name=vacancy.name,
                description=vacancy.description,
                salary=vacancy.salary,
                company_id=str(vacancy.company_id)
            ) for vacancy in vacancies
        ]