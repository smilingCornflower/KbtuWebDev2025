from django.contrib import admin
from infrastructure.models.vacancy import Vacancy
from infrastructure.models.company import Company
from config.settings import MODE

if MODE == "DEV":
    from django_stubs_ext import monkeypatch

    monkeypatch()
    ModelAdminCompany = admin.ModelAdmin[Company]
    ModelAdminVacancy = admin.ModelAdmin[Vacancy]
else:
    ModelAdminCompany = ModelAdminVacancy = admin.ModelAdmin


@admin.register(Company)
class CompanyAdmin(ModelAdminCompany):
    pass


@admin.register(Vacancy)
class VacancyAdmin(ModelAdminVacancy):
    pass
