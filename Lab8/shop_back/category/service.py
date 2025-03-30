from rest_framework.exceptions import NotFound

from django.db.models import QuerySet

from category.models import Category
from category.value_objects import CategoryQueryParamsVo


class CategoryService:
    @staticmethod
    def get(params: CategoryQueryParamsVo) -> list[Category] | Category:
        """
        :raises NotFound:
        """
        if params.id is None:
            return list(Category.objects.all())
        category: Category| None = Category.objects.filter(id=params.id).first()
        if category is not None:
            return category
        raise NotFound(f"Failed to found a category with id = {params.id}.")