from rest_framework.exceptions import NotFound

from django.db.models import QuerySet

from product.models import Product
from product.value_objects import ProductQueryParamsVo


class ProductService:
    @staticmethod
    def get(params: ProductQueryParamsVo) -> list[Product] | Product:
        """
        :raises NotFound:
        """
        if params.id is not None:
            product = Product.objects.filter(id=params.id).first()
            if product is None:
                raise NotFound(f"Failed to find a product with id = {params.id}.")
            return product

        query = Product.objects.all()
        if params.category_id is not None:
            query = query.filter(category__id=params.category_id)
        return list(query)
