from domain.models.enums import SortDirection
from domain.models.vacancy import Vacancy
from domain.models.value_objects import CompanyId, VacancyId
from domain.repositories.vacancy import VacancyRepository
from infrastructure.models.vacancy import Vacancy as VacancyModel
from infrastructure.services.sort_adapter import DjangoSortAdapter


class DjangoVacancyRepository(VacancyRepository):
    def get_by_id(self, vacancy_id: VacancyId) -> Vacancy:
        return VacancyModel.objects.filter(id=vacancy_id.value).first()

    def get_all(
            self, *,
            order_by: str | None = None,
            direction: SortDirection = SortDirection.ASCENDING,
            limit: int | None = None
    ) -> list[Vacancy]:
        queryset = VacancyModel.objects.all()

        if order_by:
            django_order_direction: str = DjangoSortAdapter.to_django(direction)
            order_param: str = django_order_direction + order_by
            queryset = queryset.order_by(order_param)

        if limit:
            queryset = queryset[:limit]
        return [Vacancy(
            id=VacancyId(vacancy.id),
            name=vacancy.name,
            description=vacancy.description,
            salary=vacancy.salary,
            company_id=CompanyId(vacancy.company.id),
        ) for vacancy in queryset]
