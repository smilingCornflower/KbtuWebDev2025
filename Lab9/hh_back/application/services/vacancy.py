from application.dto.vacancy import VacancyDTO
from domain.models.enums import SortDirection
from domain.models.vacancy import Vacancy
from domain.models.value_objects import VacancyId
from domain.repositories.vacancy import VacancyRepository


class VacancyAppService:
    def __init__(self, repository: VacancyRepository):
        self.repository = repository

    def get_vacancy(self, vacancy_id: VacancyId) -> VacancyDTO:
        vacancy: Vacancy = self.repository.get_by_id(vacancy_id=vacancy_id)
        return VacancyDTO(
            id=str(vacancy.id),
            name=vacancy.name,
            description=vacancy.description,
            salary=vacancy.salary,
            company_id=str(vacancy.company_id),
        )

    def get_all_vacancies(self) -> list[VacancyDTO]:
        vacancies: list[Vacancy] = self.repository.get_all()
        return [
            VacancyDTO(
                id=str(vacancy.id),
                name=vacancy.name,
                description=vacancy.description,
                salary=vacancy.salary,
                company_id=str(vacancy.company_id),
            ) for vacancy in vacancies
        ]

    def get_vacancy(self, vacancy_id: VacancyId) -> VacancyDTO:
        vacancy: Vacancy = self.repository.get_by_id(vacancy_id=vacancy_id)
        return VacancyDTO(
            id=str(vacancy.id),
            name=vacancy.name,
            description=vacancy.description,
            salary=vacancy.salary,
            company_id=str(vacancy.company_id),
        )

    def get_top_ten_vacancies(self) -> list[VacancyDTO]:
        vacancies: list[Vacancy] = self.repository.get_all(order_by="salary",
                                                           direction=SortDirection.DESCENDING,
                                                           limit=10)
        return [
            VacancyDTO(
                id=str(vacancy.id),
                name=vacancy.name,
                description=vacancy.description,
                salary=vacancy.salary,
                company_id=str(vacancy.company_id),
            ) for vacancy in vacancies
        ]
