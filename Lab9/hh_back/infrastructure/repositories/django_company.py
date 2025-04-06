from uuid import UUID

from domain.models.company import Company
from domain.models.vacancy import Vacancy
from domain.models.value_objects import CompanyId
from domain.repositories.company import CompanyRepository
from infrastructure.models.company import Company as CompanyModel
from infrastructure.models.vacancy import Vacancy as VacancyModel


class DjangoCompanyRepository(CompanyRepository):
    def get_all(self) -> list[Company]:
        return [Company(
            id=company.id,
            name=company.name,
            description=company.description,
            city=company.city,
            address=company.address,
        ) for company in CompanyModel.objects.all()]

    def get_by_id(self, company_id: CompanyId) -> Company:
        company = CompanyModel.objects.filter(id=company_id.value).first()
        return Company(
            id=CompanyId(company.id),
            name=company.name,
            description=company.description,
            city=company.city,
            address=company.address,
        )

    def get_vacancies(self, company_id: CompanyId) -> list[Vacancy]:
        vacancies = VacancyModel.objects.filter(company__id=company_id.value)
        return [
            Vacancy(
                id=vacancy.id,
                name=vacancy.name,
                description=vacancy.description,
                salary=vacancy.salary,
                company_id=vacancy.company_id
            )
            for vacancy in vacancies
        ]
