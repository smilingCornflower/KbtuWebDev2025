from django.urls import path

from infrastructure.api import views

urlpatterns = [
    path("companies/", views.CompanyListView.as_view()),
    path("companies/<str:company_id>", views.CompanyDetailView.as_view()),
    path("companies/<str:company_id>/vacancies/", views.CompanyVacanciesView.as_view()),
    path("vacancies/", views.VacanciesListView.as_view()),
    path("vacancies/top_ten/", views.TopTenVacanciesView.as_view()),
    path("vacancies/<str:vacancy_id>/", views.VacancyDetailView.as_view()),
]
