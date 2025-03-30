from django.http import QueryDict

from product.value_objects import ProductQueryParamsVo


def convert_product_query_params_to_vo(
        id_: int | None = None,
        category_id: int | None = None,
        query_params: QueryDict | None = None,
) -> ProductQueryParamsVo:
    return ProductQueryParamsVo(id=id_, category_id=category_id)

