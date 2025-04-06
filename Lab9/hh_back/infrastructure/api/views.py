from dataclasses import asdict

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from application.dto.company import CompanyDTO
from application.dto.vacancy import VacancyDTO
from application.services.company import CompanyAppService
from application.services.vacancy import VacancyAppService
from domain.models.value_objects import CompanyId, VacancyId
from infrastructure.repositories.django_company import DjangoCompanyRepository
from infrastructure.repositories.django_vacancies import DjangoVacancyRepository


class CompanyListView(APIView):
    @staticmethod
    def get(request: Request):
        service = CompanyAppService(DjangoCompanyRepository())
        companies: list[CompanyDTO] = service.get_all_companies()
        return Response(map(asdict, companies))


class CompanyDetailView(APIView):
    @staticmethod
    def get(request: Request, company_id: str):
        try:
            company_id = CompanyId.from_string(company_id)
        except ValueError as e:
            return Response({"error": "Invalid Company ID"}, status=400)
        service = CompanyAppService(DjangoCompanyRepository())
        company: CompanyDTO = service.get_company(company_id=company_id)
        return Response(asdict(company))


class CompanyVacanciesView(APIView):
    @staticmethod
    def get(request: Request, company_id: str):
        try:
            company_id = CompanyId.from_string(company_id)
        except ValueError as e:
            return Response({"error": "Invalid Company ID"}, status=400)
        service = CompanyAppService(DjangoCompanyRepository())
        vacancies: list[VacancyDTO] = service.get_company_vacancies(company_id=company_id)
        return Response(map(asdict, vacancies))


class VacanciesListView(APIView):
    @staticmethod
    def get(request: Request):
        service = VacancyAppService(DjangoVacancyRepository())
        vacancies: list[VacancyDTO] = service.get_all_vacancies()
        return Response(map(asdict, vacancies))


class VacancyDetailView(APIView):
    @staticmethod
    def get(request: Request, vacancy_id: str):
        try:
            vacancy_id = VacancyId.from_string(vacancy_id)
        except ValueError as e:
            return Response({"error": "Invalid Vacancy ID"}, status=400)
        service = VacancyAppService(DjangoVacancyRepository())
        vacancy: VacancyDTO = service.get_vacancy(vacancy_id=vacancy_id)
        return Response(asdict(vacancy))


class TopTenVacanciesView(APIView):
    @staticmethod
    def get(request: Request):
        service = VacancyAppService(DjangoVacancyRepository())
        vacancies: list[VacancyDTO] = service.get_top_ten_vacancies()
        return Response(map(asdict, vacancies))
